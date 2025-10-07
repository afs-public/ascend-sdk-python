import time


def test_cash_balances_transfers_get_cash_balance_get_cash_balance(
    create_sdk,
    create_account_id,
):
    s = create_sdk

    assert s is not None
    res = s.cash_balances.calculate_cash_balance(account_id=create_account_id)

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
