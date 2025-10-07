import time

from ascend_sdk.models import components


def test_journals_transfers_create_cash_journal_create_cash_journal1(
    create_cash_journal_id,
):
    assert create_cash_journal_id is not None


def test_journals_transfers_get_cash_journal_get_cash_journal1(
    create_sdk, create_cash_journal_id
):
    s = create_sdk

    assert s is not None

    res = s.journals.get_cash_journal(cash_journal_id=create_cash_journal_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_journals_transfers_cancel_cash_journal_cancel_cash_journal1(
    create_sdk, create_cash_journal_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelCashJournalRequestCreate(
        name="cashJournals/" + create_cash_journal_id,
        reason="Test cancel cash journal",
    )

    res = s.journals.cancel_cash_journal(
        cash_journal_id=create_cash_journal_id,
        cancel_cash_journal_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_journals_transfers_retrieve_cash_journal_constraints_retrieve_cash_journal_constraints1(
    create_sdk, deceased_account_id, withdrawal_account_id
):
    s = create_sdk
    assert s is not None

    request = components.RetrieveCashJournalConstraintsRequestCreate(
        destination_account="accounts/" + deceased_account_id,
        source_account="accounts/" + withdrawal_account_id,
    )

    res = s.journals.retrieve_cash_journal_constraints(request=request)

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_journals_transfers_retrieve_cash_journal_party_retrieve_cash_journal_party1(
    create_sdk, deceased_account_id, withdrawal_account_id
):
    s = create_sdk
    assert s is not None

    request = components.CheckPartyTypeRequestCreate(
        destination_account="accounts/" + deceased_account_id,
        source_account="accounts/" + withdrawal_account_id,
    )

    res = s.journals.check_party_type(request=request)

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
