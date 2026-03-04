from ascend_sdk.models import components


def test_check_withdrawal_schedules_create_check_withdrawal_schedule(
    create_check_withdrawal_schedule_id,
):
    assert create_check_withdrawal_schedule_id is not None


def test_check_withdrawal_schedules_list_check_withdrawal_schedules(
    create_sdk, enrolled_account_id, create_check_withdrawal_schedule_id
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.list_check_withdrawal_schedules(
        account_id=enrolled_account_id,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_check_withdrawal_schedules_get_check_withdrawal_schedule(
    create_sdk, enrolled_account_id, create_check_withdrawal_schedule_id
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.get_check_withdrawal_schedule(
        account_id=enrolled_account_id,
        check_withdrawal_schedule_id=create_check_withdrawal_schedule_id,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_check_withdrawal_schedules_update_check_withdrawal_schedule(
    create_sdk, enrolled_account_id, create_check_withdrawal_schedule_id
):
    s = create_sdk

    assert s is not None

    check_withdrawal_schedule_update = components.CheckWithdrawalScheduleUpdate(
        schedule_details=components.WithdrawalScheduleDetailsUpdate(
            amount=components.DecimalUpdate(value="20.00"),
        ),
    )

    res = s.schedule_transfers.update_check_withdrawal_schedule(
        account_id=enrolled_account_id,
        check_withdrawal_schedule_id=create_check_withdrawal_schedule_id,
        check_withdrawal_schedule_update=check_withdrawal_schedule_update,
        update_mask="schedule_details.amount",
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_check_withdrawal_schedules_cancel_check_withdrawal_schedule(
    create_sdk, enrolled_account_id, create_check_withdrawal_schedule_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelCheckWithdrawalScheduleRequestCreate(
        name=f"accounts/{enrolled_account_id}/checkWithdrawalSchedules/{create_check_withdrawal_schedule_id}",
        comment="canceled due to test",
    )

    res = s.schedule_transfers.cancel_check_withdrawal_schedule(
        account_id=enrolled_account_id,
        check_withdrawal_schedule_id=create_check_withdrawal_schedule_id,
        cancel_check_withdrawal_schedule_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
