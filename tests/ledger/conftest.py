import pytest


@pytest.fixture(scope="module")
def entity_id(create_sdk, withdrawal_account_id):
    s = create_sdk

    res = s.ledger.list_entries(account_id=withdrawal_account_id)

    if res.http_meta.response.status_code == 200:
        return res.list_entries_response.entries[0].entry_id
    else:
        return None


@pytest.fixture(scope="module")
def activity_id(create_sdk, withdrawal_account_id):
    s = create_sdk

    res = s.ledger.list_activities(account_id=withdrawal_account_id)

    if res.http_meta.response.status_code == 200:
        return res.list_activities_response.activities[0].activity_id
    else:
        return None
