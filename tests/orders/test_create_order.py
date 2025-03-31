import time

from ascend_sdk.models import components


def test_create_order_orders_create_order_create_order1(
    create_order_id,
):
    assert create_order_id is not None


def test_create_order_orders_get_order_get_order1(
    create_sdk, enrolled_account_id, create_order_id
):
    s = create_sdk

    assert s is not None

    res = s.create_order.get_order(
        account_id=enrolled_account_id, order_id=create_order_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_create_order_orders_cancel_order_cancel_order1(
    create_sdk, enrolled_account_id, create_order_id
):
    time.sleep(10)
    s = create_sdk

    assert s is not None

    # Cancel Order
    request = components.CancelOrderRequestCreate(
        name="accounts/" + enrolled_account_id + "/orders/" + create_order_id,
    )

    res = s.create_order.cancel_order(
        account_id=enrolled_account_id,
        order_id=create_order_id,
        cancel_order_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
