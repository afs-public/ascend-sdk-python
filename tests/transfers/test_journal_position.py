import uuid
from ascend_sdk.models import components
from ascend_sdk.models import errors


def tests_positions_journal_create(
    create_sdk,
    enrolled_account_id,
    withdrawal_account_id,
):
    s = create_sdk

    assert s is not None

    position_journal_request = components.PositionJournalCreate(
        client_transfer_id=str(uuid.uuid4()),
        destination_account=f"accounts/{enrolled_account_id}",
        identifier="AAPL",
        identifier_type=components.IdentifierType.SYMBOL,
        quantity=components.DecimalCreate(value="1.0"),
        source_account=f"accounts/{withdrawal_account_id}",
        type=components.PositionJournalCreateType.REWARD,
        fair_market_value=components.DecimalCreate(value="150.00"),
        description="Stock reward for testing",
    )

    res = s.position_journals.create_position_journal(request=position_journal_request)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
    assert res.position_journal is not None
    assert res.position_journal.name is not None


def tests_positions_journal_get(
    create_sdk,
    create_position_journal_id,
):
    s = create_sdk

    assert s is not None

    res = s.position_journals.get_position_journal(
        position_journal_id=create_position_journal_id,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
    assert res.position_journal is not None


def tests_positions_journal_cancel(
    create_sdk,
    create_position_journal_id,
):
    s = create_sdk

    assert s is not None

    request = components.CancelPositionJournalRequestCreate(
        name=f"positionJournals/{create_position_journal_id}",
        reason="Cancel position journal for testing",
    )

    res = s.position_journals.cancel_position_journal(
        position_journal_id=create_position_journal_id,
        cancel_position_journal_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def tests_positions_journal_force_approve(
    create_sdk,
    pending_position_journal_id,
):
    s = create_sdk

    assert s is not None

    request = components.ForceApprovePositionJournalRequestCreate(
        name=f"positionJournals/{pending_position_journal_id}",
    )

    try:
        res = s.test_simulation.force_approve_position_journal(
            position_journal_id=pending_position_journal_id,
            force_approve_position_journal_request_create=request,
        )
        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "that does not need review" in status.data.message.lower()


def tests_positions_journal_force_reject(
    create_sdk,
    pending_position_journal_id,
):
    s = create_sdk

    assert s is not None

    request = components.ForceRejectPositionJournalRequestCreate(
        name=f"positionJournals/{pending_position_journal_id}",
        reason="Force reject for testing",
    )

    try:
        res = s.test_simulation.force_reject_position_journal(
            position_journal_id=pending_position_journal_id,
            force_reject_position_journal_request_create=request,
        )
        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "that does not need review" in status.data.message.lower()
