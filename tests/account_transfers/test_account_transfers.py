import os
import time

from ascend_sdk.models import components
from ascend_sdk.models import operations


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
    account_number,
    enrolled_account_id,
    withdrawal_account_id,
):
    s = create_sdk

    assert s is not None

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
    accept_transfer = s.account_transfers.create_transfer(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        account_id=withdrawal_account_id,
        transfer_create=request,
    )

    assert accept_transfer is not None
    accept_transfer_id = accept_transfer.acats_transfer.name.split("/")[-1]

    request = components.AcceptTransferRequestCreate(
        name="correspondents/"
        + os.getenv("CORRESPONDENT_ID")
        + "/accounts/"
        + enrolled_account_id
        + "/transfers/"
        + accept_transfer_id,
    )

    res = s.account_transfers.accept_transfer(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        account_id=enrolled_account_id,
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
