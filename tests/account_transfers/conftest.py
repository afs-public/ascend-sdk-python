import time

from ascend_sdk.models import components
import pytest
import os
import uuid


@pytest.fixture(scope="module")
def account_number(create_sdk, enrolled_account_id):
    time.sleep(5)
    s = create_sdk
    account = s.account_creation.get_account(account_id=enrolled_account_id)
    return account.account.account_number


@pytest.fixture(scope="module")
def create_account_transfer_id(
    create_sdk, enrolled_account_id, account_number, withdrawal_account_id
):
    time.sleep(5)
    s = create_sdk

    # Fund Account
    funding_request = components.TransfersCreditCreate(
        amount=components.DecimalCreate(value="1000.00"),
        client_transfer_id=str(uuid.uuid4()),
        description="Credit given as promotion",
        type=components.TransfersCreditCreateType.PROMOTIONAL,
    )

    s.fees_and_credits.create_credit(
        account_id=enrolled_account_id, transfers_credit_create=funding_request
    )

    time.sleep(5)

    request = components.TransferCreate(
        assets=[
            components.AssetCreate(
                identifier="USD",
                position=components.PositionCreate(
                    quantity=components.DecimalCreate(value="1.00"),
                ),
                type=components.AssetCreateType.CURRENCY_CODE,
            ),
        ],
        deliverer=components.TransferAccountCreate(
            external_account=components.ExternalAccountCreate(
                account_number=account_number,
                participant_number="158",
            ),
        ),
    )
    res = s.account_transfers.create_transfer(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        account_id=withdrawal_account_id,
        transfer_create=request,
    )
    if res.http_meta.response.status_code == 200:
        return res.acats_transfer.name.split("/")[-1]
    else:
        return None
