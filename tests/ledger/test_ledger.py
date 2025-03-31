def test_ledger_ledger_list_entries_ledger_list_entries1(entity_id):
    assert entity_id is not None


def test_ledger_ledger_list_activities_ledger_list_activities1(activity_id):
    assert activity_id is not None


def test_ledger_ledger_list_positions_ledger_list_positions1(
    create_sdk, withdrawal_account_id
):
    s = create_sdk

    assert s is not None

    res = s.ledger.list_positions(account_id=withdrawal_account_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_ledger_ledger_get_activity_ledger_get_activity1(
    create_sdk, withdrawal_account_id, activity_id
):
    s = create_sdk

    assert s is not None

    res = s.ledger.get_activity(
        account_id=withdrawal_account_id, activity_id=activity_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_ledger_ledger_get_entry_ledger_get_entry1(
    create_sdk, withdrawal_account_id, entity_id
):
    s = create_sdk

    assert s is not None

    res = s.ledger.get_entry(
        account_id=withdrawal_account_id,
        entry_id=entity_id,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
