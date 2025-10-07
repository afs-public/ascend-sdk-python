import time

from ascend_sdk.models import components


def test_ach_transfers_transfers_create_ach_deposit_create_ach_deposit1(
    create_ach_deposit_id,
):
    assert create_ach_deposit_id is not None


def test_ach_transfers_transfers_get_ach_deposit_get_ach_deposit1(
    create_sdk,
    enrolled_account_id,
    create_ach_deposit_id,
):
    s = create_sdk

    assert s is not None
    res = s.ach_transfers.get_ach_deposit(
        account_id=enrolled_account_id, ach_deposit_id=create_ach_deposit_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_ach_transfers_transfers_cancel_ach_deposit_cancel_ach_deposit1(
    create_sdk,
    enrolled_account_id,
    create_ach_deposit_id,
):
    s = create_sdk

    assert s is not None

    request = components.CancelAchDepositRequestCreate(
        name="accounts/"
        + enrolled_account_id
        + "/achTransfers/"
        + create_ach_deposit_id,
    )

    res = s.ach_transfers.cancel_ach_deposit(
        account_id=enrolled_account_id,
        ach_deposit_id=create_ach_deposit_id,
        cancel_ach_deposit_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_ach_transfers_transfers_create_ach_withdrawal_create_ach_withdrawal1(
    create_ach_withdrawal_id,
):
    assert create_ach_withdrawal_id is not None


def test_ach_transfers_transfers_get_ach_withdrawal_get_ach_withdrawal1(
    create_sdk,
    enrolled_account_id,
    create_ach_withdrawal_id,
):
    s = create_sdk

    assert s is not None
    res = s.ach_transfers.get_ach_withdrawal(
        account_id=enrolled_account_id, ach_withdrawal_id=create_ach_withdrawal_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_ach_transfers_transfers_cancel_ach_withdrawal_cancel_ach_withdrawal1(
    create_sdk,
    enrolled_account_id,
    create_ach_withdrawal_id,
):
    s = create_sdk

    assert s is not None

    request = components.CancelAchWithdrawalRequestCreate(
        name="accounts/"
        + enrolled_account_id
        + "/achTransfers/"
        + create_ach_withdrawal_id,
    )

    res = s.ach_transfers.cancel_ach_withdrawal(
        account_id=enrolled_account_id,
        ach_withdrawal_id=create_ach_withdrawal_id,
        cancel_ach_withdrawal_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
