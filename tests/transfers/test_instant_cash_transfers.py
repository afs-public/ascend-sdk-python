import os
import time

from ascend_sdk.models import components, operations


def test_instant_cash_transfer_transfers_create_ict_deposit_create_ict_deposit1(
    create_ict_deposit_id,
):
    assert create_ict_deposit_id is not None


def test_instant_cash_transfer_transfers_get_ict_deposit_get_ict_deposit1(
    create_sdk, enrolled_account_id, create_ict_deposit_id
):
    s = create_sdk

    assert s is not None
    res = s.instant_cash_transfer_ict.get_ict_deposit(
        account_id=enrolled_account_id, ict_deposit_id=create_ict_deposit_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_instant_cash_transfer_transfers_cancel_ict_deposit_cancel_ict_deposit1(
    create_sdk, enrolled_account_id, create_ict_deposit_id
):
    s = create_sdk

    assert s is not None

    cancel_ict_deposit_request = components.CancelIctDepositRequestCreate(
        name="accounts/"
        + enrolled_account_id
        + "ictDeposits/"
        + create_ict_deposit_id
        + ":cancel",
        reason="User requested",
    )

    res = s.instant_cash_transfer_ict.cancel_ict_deposit(
        account_id=enrolled_account_id,
        ict_deposit_id=create_ict_deposit_id,
        cancel_ict_deposit_request_create=cancel_ict_deposit_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_instant_cash_transfer_transfers_create_ict_withdrawal_create_ict_withdrawal1(
    create_ict_withdrawal_id,
):
    assert create_ict_withdrawal_id is not None


def test_instant_cash_transfer_transfers_get_ict_withdrawal_get_ict_withdrawal1(
    create_sdk, enrolled_account_id, create_ict_withdrawal_id
):
    s = create_sdk

    assert s is not None
    res = s.instant_cash_transfer_ict.get_ict_withdrawal(
        account_id=enrolled_account_id, ict_withdrawal_id=create_ict_withdrawal_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_instant_cash_transfer_transfers_cancel_ict_withdrawal_cancel_ict_withdrawal1(
    create_sdk, enrolled_account_id, create_ict_withdrawal_id
):
    s = create_sdk

    assert s is not None

    cancel_ict_withdrawal_request_create = components.CancelIctWithdrawalRequestCreate(
        name="accounts/"
        + enrolled_account_id
        + "/ictWithdrawals/"
        + create_ict_withdrawal_id
        + ":cancel",
        reason="User requested",
    )

    res = s.instant_cash_transfer_ict.cancel_ict_withdrawal(
        account_id=enrolled_account_id,
        ict_withdrawal_id=create_ict_withdrawal_id,
        cancel_ict_withdrawal_request_create=cancel_ict_withdrawal_request_create,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_instant_cash_transfer_transfers_locate_ict_report_locate_ict_report1(
    create_sdk,
):
    s = create_sdk

    assert s is not None

    request = operations.IctReconReportsLocateIctReportRequest(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        program_date_filter_program=operations.ProgramDateFilterProgram.BROKER_PARTNER,
        program_date_filter_process_date_year=2025,
        program_date_filter_process_date_month=5,
        program_date_filter_process_date_day=28,
    )

    res = s.instant_cash_transfer_ict.locate_ict_report(
        request=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
