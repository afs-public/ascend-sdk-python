from ascend_sdk.models import components


def test_fees_and_credits_transfers_create_fee_create_fee1(
    create_fee_id,
):
    assert create_fee_id is not None


def test_fees_and_credits_transfers_get_fee_get_fee1(
    create_sdk, enrolled_account_id, create_fee_id
):
    s = create_sdk

    assert s is not None
    res = s.fees_and_credits.get_fee(
        account_id=enrolled_account_id, fee_id=create_fee_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_fees_and_credits_transfers_cancel_fee_cancel_fee1(
    create_sdk, enrolled_account_id, create_fee_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelFeeRequestCreate(
        name="accounts/" + enrolled_account_id + "/feesAndCredits/" + create_fee_id,
    )

    res = s.fees_and_credits.cancel_fee(
        account_id=enrolled_account_id,
        fee_id=create_fee_id,
        cancel_fee_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_fees_and_credits_transfers_create_credit_create_credit1(
    create_credit_id,
):
    assert create_credit_id is not None


def test_fees_and_credits_transfers_get_credit_get_credit1(
    create_sdk, enrolled_account_id, create_credit_id
):
    s = create_sdk

    assert s is not None
    res = s.fees_and_credits.get_credit(
        account_id=enrolled_account_id, credit_id=create_credit_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_fees_and_credits_transfers_cancel_credit_cancel_credit1(
    create_sdk, enrolled_account_id, create_credit_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelCreditRequestCreate(
        name="accounts/" + enrolled_account_id + "/feesAndCredits/" + create_credit_id,
    )

    res = s.fees_and_credits.cancel_credit(
        account_id=enrolled_account_id,
        credit_id=create_credit_id,
        cancel_credit_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
