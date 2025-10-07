import time


def test_account_creation_accounts_create_account_create_account1(
    create_account_id,
):
    assert create_account_id is not None


def test_account_creation_accounts_get_account_get_account1(
    create_sdk,
    create_account_id,
):
    s = create_sdk

    assert s is not None
    res = s.account_creation.get_account(account_id=create_account_id)

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
