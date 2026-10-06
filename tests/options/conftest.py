import datetime
import os
import uuid

import pytest
import pytz

from ascend_sdk.models import components


def _outside_exercise_submission_window():
    """DO_NOT_EXERCISE (and other exercise instructions) are only accepted
    between 3:00:00 PM and 4:19:59 PM Central Time -- the real-world options
    exercise cutoff window near market close. Outside that window every
    attempt 400s with "outside allowed time window" regardless of which
    contract or expiration date is used.
    """
    now_ct = datetime.datetime.now(pytz.timezone("America/Chicago")).time()
    return not (datetime.time(15, 0) <= now_ct <= datetime.time(16, 19, 59))


def _find_option_expiring_today(s):
    """Find a usable equity option contract expiring today.

    DO_NOT_EXERCISE instructions can only be submitted on an option's expiration
    date, so a fixed/hardcoded asset_id only works on the one calendar day it
    happens to expire. Looking one up dynamically each run stays valid
    indefinitely instead of breaking again the day after whatever asset was
    hardcoded. Restricted to EQUITY options -- 0DTE index options (XSP,
    APXSIM, etc.) expire daily but don't support exercise instructions at all
    ("exercise instructions are not supported for index options"). Equity
    options only expire on specific days (weekly/monthly), so none may be
    expiring today; the caller should skip in that case rather than treat it
    as a failure.
    """
    # "Today" must match the America/Chicago submission window this test is
    # gated on -- system-local dates diverge from it on machines east of UTC.
    today = datetime.datetime.now(pytz.timezone("America/Chicago")).date()
    # Filter server-side: without the expiration/usable constraints this
    # walks the entire option universe page by page on no-match days.
    filter_ = (
        f'type == "OPTION" && usable'
        f' && option.expiration_date == date("{today.isoformat()}")'
    )
    page_token = ""
    while True:
        res = s.assets.list_assets(
            filter_=filter_, page_size=200, page_token=page_token
        )
        lr = res.list_assets_response
        for asset in lr.assets:
            option = asset.option
            if option and option.option_type == "EQUITY":
                return asset.asset_id
        page_token = lr.next_page_token
        if not page_token:
            return None


@pytest.fixture(scope="module")
def create_option_instruction_id(create_sdk, enrolled_account_id):
    s = create_sdk

    if _outside_exercise_submission_window():
        pytest.skip(
            "Exercise instructions are only accepted 3:00-4:19:59 PM Central Time"
        )

    # Fund Account with Credit
    transfers_credit_create = components.TransfersCreditCreate(
        amount=components.DecimalCreate(value="1000000.00"),
        client_transfer_id=str(uuid.uuid4()),
        description="Credit given as promotion",
        type=components.TransfersCreditCreateType.PROMOTIONAL,
    )

    s.fees_and_credits.create_credit(
        account_id=enrolled_account_id, transfers_credit_create=transfers_credit_create
    )

    asset_id = _find_option_expiring_today(s)
    if asset_id is None:
        pytest.skip("No option contract expiring today was found")

    option_instruction_create = components.OptionInstructionCreate(
        account_id=enrolled_account_id,
        identifier=asset_id,
        identifier_type=components.OptionInstructionCreateIdentifierType.ASSET_ID,
        quantity=components.DecimalCreate(value="1"),
        type=components.OptionInstructionCreateType.DO_NOT_EXERCISE,
    )

    res = s.option_instructions.create_option_instruction(
        account_id=enrolled_account_id,
        asset_id=asset_id,
        option_instruction_create=option_instruction_create,
    )

    if res.http_meta.response.status_code == 200:
        return {
            "instruction_id": res.option_instruction.instruction_id,
            "asset_id": asset_id,
        }
    else:
        return None
