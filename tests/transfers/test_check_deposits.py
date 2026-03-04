import pytest

from ascend_sdk.models import components, errors


def test_check_deposits_simulate_create_check_deposit(
    create_sdk, withdrawal_account_id
):
    s = create_sdk

    assert s is not None

    res = s.test_simulation.simulate_create_check_deposit(
        account_id=withdrawal_account_id,
        simulate_create_check_deposit_request_create={
            "amount": {"value": "100"},
            "parent": withdrawal_account_id,
        },
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
    assert res.check_deposit is not None
    assert res.check_deposit.name is not None


def test_check_deposits_get_check_deposit(create_sdk, withdrawal_account_id):
    s = create_sdk

    assert s is not None

    # Create a check deposit first to get a valid ID
    create_res = s.test_simulation.simulate_create_check_deposit(
        account_id=withdrawal_account_id,
        simulate_create_check_deposit_request_create={
            "amount": {"value": "100"},
            "parent": withdrawal_account_id,
        },
    )
    assert create_res.check_deposit is not None

    check_deposit_id = create_res.check_deposit.name.split("/")[-1]

    res = s.checks.get_check_deposit(
        account_id=withdrawal_account_id,
        check_deposit_id=check_deposit_id,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_check_deposits_force_approve_check_deposit(create_sdk, withdrawal_account_id):
    s = create_sdk

    assert s is not None

    # Create a check deposit first
    create_res = s.test_simulation.simulate_create_check_deposit(
        account_id=withdrawal_account_id,
        simulate_create_check_deposit_request_create={
            "amount": {"value": "100"},
            "parent": withdrawal_account_id,
        },
    )
    assert create_res.check_deposit is not None

    check_deposit_id = create_res.check_deposit.name.split("/")[-1]

    request = components.ForceApproveCheckDepositRequestCreate(
        name=f"accounts/{withdrawal_account_id}/checkDeposits/{check_deposit_id}",
    )

    try:
        res = s.test_simulation.force_approve_check_deposit(
            account_id=withdrawal_account_id,
            check_deposit_id=check_deposit_id,
            force_approve_check_deposit_request_create=request,
        )
        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "does not need review" in status.data.message.lower()
