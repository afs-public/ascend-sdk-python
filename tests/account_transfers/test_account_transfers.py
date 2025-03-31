import os
import time


def test_account_transfers_account_transfers_create_transfer_create_transfer1(
    create_account_transfer_id,
):
    assert create_account_transfer_id is not None


def test_account_transfers_account_transfers_get_transfer_get_transfer1(
    create_sdk,
    enrolled_account_id,
    create_account_transfer_id,
):
    time.sleep(5)
    s = create_sdk

    assert s is not None
    res = s.account_transfers.get_transfer(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        account_id=enrolled_account_id,
        transfer_id=create_account_transfer_id,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
