from ascend_sdk.models import components, operations


def test_cash_journal_schedules_create_cash_journal_schedule(
    create_cash_journal_schedule_id,
):
    assert create_cash_journal_schedule_id is not None


def test_cash_journal_schedules_get_cash_journal_schedule(
    create_sdk, create_cash_journal_schedule_id
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.get_cash_journal_schedule(
        cash_journal_schedule_id=create_cash_journal_schedule_id,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_cash_journal_schedules_search_cash_journal_schedules(
    create_sdk, withdrawal_account_id, create_cash_journal_schedule_id
):
    s = create_sdk

    assert s is not None

    res = s.schedule_transfers.search_cash_journal_schedules(
        request=operations.CashJournalSchedulesSearchCashJournalSchedulesRequest(
            source_account=withdrawal_account_id,
        ),
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_cash_journal_schedules_update_cash_journal_schedule(
    create_sdk, create_cash_journal_schedule_id
):
    s = create_sdk

    assert s is not None

    cash_journal_schedule_update = components.CashJournalScheduleUpdate(
        schedule_details=components.WithdrawalScheduleDetailsUpdate(
            amount=components.DecimalUpdate(value="20.00"),
        ),
    )

    res = s.schedule_transfers.update_cash_journal_schedule(
        cash_journal_schedule_id=create_cash_journal_schedule_id,
        cash_journal_schedule_update=cash_journal_schedule_update,
        update_mask="schedule_details.amount",
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_cash_journal_schedules_cancel_cash_journal_schedule(
    create_sdk, create_cash_journal_schedule_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelCashJournalScheduleRequestCreate(
        name=f"cashJournalSchedules/{create_cash_journal_schedule_id}",
        comment="canceled due to test",
    )

    res = s.schedule_transfers.cancel_cash_journal_schedule(
        cash_journal_schedule_id=create_cash_journal_schedule_id,
        cancel_cash_journal_schedule_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
