import uuid
from datetime import date

from ascend_sdk.models import components


def test_option_orders_create_option_order(create_option_order_id):
    assert create_option_order_id is not None
    assert create_option_order_id["option_order_id"] is not None


def test_option_orders_get_option_order(
    create_sdk, enrolled_account_id, create_option_order_id
):
    s = create_sdk

    assert s is not None

    res = s.option_orders.get_option_order(
        account_id=enrolled_account_id,
        option_order_id=create_option_order_id["option_order_id"],
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_option_orders_cancel_option_order(
    create_sdk, enrolled_account_id, create_option_order_id
):
    s = create_sdk

    assert s is not None

    option_order_id = create_option_order_id["option_order_id"]

    # Check if order is in a cancelable state
    get_res = s.option_orders.get_option_order(
        account_id=enrolled_account_id,
        option_order_id=option_order_id,
    )

    status = get_res.option_order.order_status
    if status in (
        components.OptionOrderOrderStatus.REJECTED,
        components.OptionOrderOrderStatus.FILLED,
        components.OptionOrderOrderStatus.CANCELED,
    ):
        import pytest

        pytest.skip(f"Skipping: option order is already in terminal status {status}")

    request = components.CancelOptionOrderRequestCreate(
        name=f"accounts/{enrolled_account_id}/optionOrders/{option_order_id}",
    )

    res = s.option_orders.cancel_option_order(
        account_id=enrolled_account_id,
        option_order_id=option_order_id,
        cancel_option_order_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
