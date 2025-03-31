from ascend_sdk.models import components


def test_schedule_transfers_transfers_list_schedule_summaries_list_schedule_summaries1(
    create_sdk,
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.list_schedule_summaries()
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_create_ach_deposit_schedule_create_ach_deposit_schedule1(
    create_ach_deposit_schedule_id,
):
    assert create_ach_deposit_schedule_id is not None


def test_schedule_transfers_transfers_list_ach_deposit_schedules_list_ach_deposit_schedules1(
    create_sdk, enrolled_account_id
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.list_ach_deposit_schedules(
        account_id=enrolled_account_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_get_ach_deposit_schedule_get_ach_deposit_schedule1(
    create_sdk, enrolled_account_id, create_ach_deposit_schedule_id
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.get_ach_deposit_schedule(
        account_id=enrolled_account_id,
        ach_deposit_schedule_id=create_ach_deposit_schedule_id,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_update_ach_deposit_schedule_update_ach_deposit_schedule1(
    create_sdk, enrolled_account_id, create_ach_deposit_schedule_id
):
    s = create_sdk

    assert s is not None

    ach_deposit_schedule_request = components.AchDepositScheduleUpdate(
        schedule_details=components.DepositScheduleDetailsUpdate(
            amount=components.DecimalUpdate(
                value="100",
            ),
        )
    )

    res = s.schedule_transfers.update_ach_deposit_schedule(
        account_id=enrolled_account_id,
        ach_deposit_schedule_id=create_ach_deposit_schedule_id,
        ach_deposit_schedule_update=ach_deposit_schedule_request,
        update_mask="schedule_details.amount",
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_cancel_ach_deposit_schedule_cancel_ach_deposit_schedule1(
    create_sdk, enrolled_account_id, create_ach_deposit_schedule_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelAchDepositScheduleRequestCreate(
        name="accounts/"
        + enrolled_account_id
        + "/scheduleTransfers/"
        + create_ach_deposit_schedule_id,
    )

    res = s.schedule_transfers.cancel_ach_deposit_schedule(
        account_id=enrolled_account_id,
        ach_deposit_schedule_id=create_ach_deposit_schedule_id,
        cancel_ach_deposit_schedule_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_create_ach_withdrawal_schedule_create_ach_deposit_withdrawal1(
    create_ach_withdrawal_schedule_id,
):
    assert create_ach_withdrawal_schedule_id is not None


def test_schedule_transfers_transfers_list_ach_withdrawal_schedules_list_ach_withdrawal_schedules1(
    create_sdk, enrolled_account_id
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.list_ach_withdrawal_schedules(
        account_id=enrolled_account_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_get_ach_withdrawal_schedule_get_ach_withdrawal_schedule1(
    create_sdk, enrolled_account_id, create_ach_withdrawal_schedule_id
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.get_ach_withdrawal_schedule(
        account_id=enrolled_account_id,
        ach_withdrawal_schedule_id=create_ach_withdrawal_schedule_id,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_update_ach_withdrawal_schedule_update_ach_withdrawal_schedule1(
    create_sdk, enrolled_account_id, create_ach_withdrawal_schedule_id
):
    s = create_sdk

    assert s is not None

    ach_withdrawal_schedule_request = components.AchWithdrawalScheduleUpdate(
        schedule_details=components.WithdrawalScheduleDetailsUpdate(
            amount=components.DecimalUpdate(
                value="100",
            ),
        )
    )

    res = s.schedule_transfers.update_ach_withdrawal_schedule(
        account_id=enrolled_account_id,
        ach_withdrawal_schedule_id=create_ach_withdrawal_schedule_id,
        ach_withdrawal_schedule_update=ach_withdrawal_schedule_request,
        update_mask="schedule_details.amount",
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_cancel_ach_withdrawal_schedule_cancel_ach_withdrawal_schedule1(
    create_sdk, enrolled_account_id, create_ach_withdrawal_schedule_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelAchWithdrawalScheduleRequestCreate(
        name="accounts/"
        + enrolled_account_id
        + "/scheduleTransfers/"
        + create_ach_withdrawal_schedule_id,
    )

    res = s.schedule_transfers.cancel_ach_withdrawal_schedule(
        account_id=enrolled_account_id,
        ach_withdrawal_schedule_id=create_ach_withdrawal_schedule_id,
        cancel_ach_withdrawal_schedule_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_create_wire_withdrawal_schedule_create_wire_withdrawal_schedule1(
    create_wire_withdrawal_schedule_id,
):
    assert create_wire_withdrawal_schedule_id is not None


def test_schedule_transfers_transfers_list_wire_withdrawal_schedules_list_wire_withdrawal_schedules1(
    create_sdk,
    enrolled_account_id,
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.list_wire_withdrawal_schedules(
        account_id=enrolled_account_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_get_wire_withdrawal_schedule_get_wire_withdrawal_schedule1(
    create_sdk,
    enrolled_account_id,
    create_wire_withdrawal_schedule_id,
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.get_wire_withdrawal_schedule(
        account_id=enrolled_account_id,
        wire_withdrawal_schedule_id=create_wire_withdrawal_schedule_id,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_update_wire_withdrawal_schedule_update_wire_withdrawal_schedule1(
    create_sdk,
    enrolled_account_id,
    create_wire_withdrawal_schedule_id,
):
    s = create_sdk

    assert s is not None

    wire_withdrawal_schedule_request = components.WireWithdrawalScheduleUpdate(
        schedule_details=components.WithdrawalScheduleDetailsUpdate(
            amount=components.DecimalUpdate(
                value="100",
            ),
        )
    )

    res = s.schedule_transfers.update_wire_withdrawal_schedule(
        account_id=enrolled_account_id,
        wire_withdrawal_schedule_id=create_wire_withdrawal_schedule_id,
        wire_withdrawal_schedule_update=wire_withdrawal_schedule_request,
        update_mask="schedule_details.amount",
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_schedule_transfers_transfers_cancel_wire_withdrawal_schedule_cancel_wire_withdrawal_schedule1(
    create_sdk,
    enrolled_account_id,
    create_wire_withdrawal_schedule_id,
):
    s = create_sdk

    assert s is not None

    request = components.CancelWireWithdrawalScheduleRequestCreate(
        name="accounts/"
        + enrolled_account_id
        + "/scheduleTransfers/"
        + create_wire_withdrawal_schedule_id,
    )

    res = s.schedule_transfers.cancel_wire_withdrawal_schedule(
        account_id=enrolled_account_id,
        wire_withdrawal_schedule_id=create_wire_withdrawal_schedule_id,
        cancel_wire_withdrawal_schedule_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
