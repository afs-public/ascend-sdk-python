import os
import time
import uuid

from ascend_sdk.models import components
from ascend_sdk.models import operations

from tests.conftest import create_enrolled_account, retry_on_transient_error


def test_account_transfers_account_transfers_create_transfer_create_transfer1(
    create_account_transfer_id,
):
    assert create_account_transfer_id is not None


def test_account_transfers_account_transfers_list_transfers_list_transfers1(
    create_sdk,
    enrolled_account_id,
):
    s = create_sdk

    assert s is not None

    request = operations.AccountTransfersListTransfersRequest(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        account_id=enrolled_account_id,
    )

    res = s.account_transfers.list_transfers(
        request=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_transfers_account_transfers_reject_transfer_reject_transfer1(
    create_sdk, enrolled_account_id, create_account_transfer_id
):
    s = create_sdk

    assert s is not None

    request = components.RejectTransferRequestCreate(
        name="correspondents/"
        + os.getenv("CORRESPONDENT_ID")
        + "/accounts/"
        + enrolled_account_id
        + "/transfers/"
        + create_account_transfer_id,
    )

    res = s.account_transfers.reject_transfer(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        account_id=enrolled_account_id,
        transfer_id=create_account_transfer_id,
        reject_transfer_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_transfers_account_transfers_accept_transfer_accept_transfer1(
    create_sdk,
    withdrawal_account_id,
):
    s = create_sdk

    assert s is not None

    # Use a dedicated account: rejecting the earlier transfer restricts its
    # deliverer account (ACAT_PARTIAL_OUTBOUND entitlement) for an unbounded
    # window, so a second transfer on the same account is rejected as
    # "Account not entitled".
    accept_account_id = create_enrolled_account(s)
    account = s.account_creation.get_account(account_id=accept_account_id)
    accept_account_number = account.account.account_number

    s.fees_and_credits.create_credit(
        account_id=accept_account_id,
        transfers_credit_create=components.TransfersCreditCreate(
            amount=components.DecimalCreate(value="1000.00"),
            client_transfer_id=str(uuid.uuid4()),
            description="Credit given as promotion",
            type=components.TransfersCreditCreateType.PROMOTIONAL,
        ),
    )

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
                account_number=accept_account_number,
                participant_number="158",
            ),
        ),
    )
    # The funding credit from the create_account_transfer_id fixture posts
    # asynchronously; until it lands the API rejects the transfer for
    # insufficient cash.
    accept_transfer = retry_on_transient_error(
        lambda: s.account_transfers.create_transfer(
            correspondent_id=os.getenv("CORRESPONDENT_ID"),
            account_id=withdrawal_account_id,
            transfer_create=request,
        )
    )

    assert accept_transfer is not None
    accept_transfer_id = accept_transfer.acats_transfer.name.split("/")[-1]

    request = components.AcceptTransferRequestCreate(
        name="correspondents/"
        + os.getenv("CORRESPONDENT_ID")
        + "/accounts/"
        + accept_account_id
        + "/transfers/"
        + accept_transfer_id,
    )

    res = s.account_transfers.accept_transfer(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        account_id=accept_account_id,
        transfer_id=accept_transfer_id,
        accept_transfer_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_transfers_account_transfers_get_transfer_get_transfer1(
    create_sdk,
    enrolled_account_id,
    create_account_transfer_id,
):
    s = create_sdk

    assert s is not None
    res = s.account_transfers.get_transfer(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        account_id=enrolled_account_id,
        transfer_id=create_account_transfer_id,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
