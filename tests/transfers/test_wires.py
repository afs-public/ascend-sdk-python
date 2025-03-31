import time
import datetime
import pytest
from ascend_sdk.models import components


def test_wires_transfers_get_wire_deposit_get_wire_deposit1(
    create_sdk, withdrawal_account_id, wire_deposit_id
):
    s = create_sdk

    assert s is not None

    res = s.wires.get_wire_deposit(
        account_id=withdrawal_account_id, wire_deposit_id=wire_deposit_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


@pytest.mark.skip(
    reason="Skipping Endpoint Test: Endpoint is not ready for testing in the test environment"
)
def test_wires_transfers_get_wire_deposit_fee_summary_get_wire_deposit_fee_summary1(
    create_sdk, withdrawal_account_id, wire_deposit_id
):
    s = create_sdk

    assert s is not None

    res = s.wires.get_wire_deposits_fee_summary(
        account_id=withdrawal_account_id, wire_deposit_id=wire_deposit_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_wires_transfers_create_wire_withdrawal_create_wire_withdrawal1(
    create_wire_withdrawal_id,
):
    assert create_wire_withdrawal_id is not None


def test_wires_transfers_get_wire_withdrawal_get_wire_withdrawal1(
    create_sdk, withdrawal_account_id, create_wire_withdrawal_id
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    res = s.wires.get_wire_withdrawal(
        account_id=withdrawal_account_id, wire_withdrawal_id=create_wire_withdrawal_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


@pytest.mark.skip(
    reason="Skipping Endpoint Test: Endpoint is not ready for testing in the test environment"
)
def test_wires_transfers_get_wire_withdrawal_fee_summary_get_wire_withdrawal_fee_summary1(
    create_sdk, withdrawal_account_id, create_wire_withdrawal_id, current_time
):
    if not (datetime.time(6, 0) <= current_time.time() <= datetime.time(15, 0)):
        pytest.skip("Skipping Endpoint Test: Get Wire Withdrawal Fee Summary")
    time.sleep(5)
    s = create_sdk

    assert s is not None

    request = components.ForceApproveWireWithdrawalRequestCreate(
        name=f"accounts/{withdrawal_account_id}/wireWithdrawals/{create_wire_withdrawal_id}",
    )

    s.test_simulation.force_approve_wire_withdrawal(
        account_id=withdrawal_account_id,
        wire_withdrawal_id=create_wire_withdrawal_id,
        force_approve_wire_withdrawal_request_create=request,
    )

    res = s.wires.get_wire_withdrawals_fee_summary(
        account_id=withdrawal_account_id, wire_withdrawal_id=create_wire_withdrawal_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_wires_transfers_cancel_wire_withdrawal_cancel_wire_withdrawal1(
    create_sdk, withdrawal_account_id, create_wire_withdrawal_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelWireWithdrawalRequestCreate(
        name="accounts/"
        + withdrawal_account_id
        + "/wireWithdrawals/"
        + create_wire_withdrawal_id,
        reason="User Request",
    )

    res = s.wires.cancel_wire_withdrawal(
        account_id=withdrawal_account_id,
        wire_withdrawal_id=create_wire_withdrawal_id,
        cancel_wire_withdrawal_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
