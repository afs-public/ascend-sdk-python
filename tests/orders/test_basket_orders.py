import os
import time
import uuid

from ascend_sdk.models import components
from ascend_sdk.models import operations


def test_basket_orders_orders_create_basket_create_basket1(
    create_basket_id,
):
    assert create_basket_id is not None


def test_basket_orders_orders_add_orders_add_orders1(
    create_sdk, create_basket_id, withdrawal_account_id, basket_order_to_remove
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    # Add Orders
    request = components.AddOrdersRequestCreate(
        name="correspondents/"
        + os.getenv("CORRESPONDENT_ID")
        + "/baskets/"
        + create_basket_id,
        basket_orders=[
            components.BasketOrderCreate(
                account_id=withdrawal_account_id,
                asset_type=components.BasketOrderCreateAssetType.EQUITY,
                client_order_id=str(uuid.uuid4()),
                identifier="SBUX",
                identifier_type=components.BasketOrderCreateIdentifierType.SYMBOL,
                order_type=components.BasketOrderCreateOrderType.MARKET,
                quantity=components.DecimalCreate(value="1"),
                side=components.BasketOrderCreateSide.BUY,
                time_in_force=components.BasketOrderCreateTimeInForce.DAY,
            ),
            components.BasketOrderCreate(
                account_id=withdrawal_account_id,
                asset_type=components.BasketOrderCreateAssetType.EQUITY,
                client_order_id=basket_order_to_remove,
                identifier="SBUX",
                identifier_type=components.BasketOrderCreateIdentifierType.SYMBOL,
                order_type=components.BasketOrderCreateOrderType.MARKET,
                quantity=components.DecimalCreate(value="1"),
                side=components.BasketOrderCreateSide.BUY,
                time_in_force=components.BasketOrderCreateTimeInForce.DAY,
            ),
        ],
    )

    res = s.basket_orders.add_orders(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        basket_id=create_basket_id,
        add_orders_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_basket_orders_orders_get_basket_get_basket1(create_sdk, create_basket_id):
    s = create_sdk

    assert s is not None

    res = s.basket_orders.get_basket(
        correspondent_id=os.getenv("CORRESPONDENT_ID"), basket_id=create_basket_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_basket_orders_orders_remove_basket_remove_basket1(
    create_sdk, create_basket_id, basket_order_to_remove
):
    s = create_sdk

    assert s is not None

    request = components.RemoveOrdersRequestCreate(
        name="correspondents/"
        + os.getenv("CORRESPONDENT_ID")
        + "/baskets/"
        + create_basket_id,
        client_order_ids=[basket_order_to_remove],
    )

    res = s.basket_orders.remove_orders(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        basket_id=create_basket_id,
        remove_orders_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_basket_orders_orders_submit_basket_submit_basket1(
    create_sdk, create_basket_id
):
    s = create_sdk

    assert s is not None

    request = components.SubmitBasketRequestCreate(
        name="correspondents/"
        + os.getenv("CORRESPONDENT_ID")
        + "/baskets/"
        + create_basket_id
    )

    res = s.basket_orders.submit_basket(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        basket_id=create_basket_id,
        submit_basket_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_basket_orders_orders_list_basket_orders_list_basket_orders1(
    create_sdk, create_basket_id
):
    s = create_sdk

    assert s is not None

    request = operations.BasketOrdersServiceListBasketOrdersRequest(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        basket_id=create_basket_id,
    )

    res = s.basket_orders.list_basket_orders(request=request)

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_basket_orders_orders_list_compressed_orders_list_compressed_orders1(
    create_sdk, create_basket_id
):
    s = create_sdk

    assert s is not None

    res = s.basket_orders.list_compressed_orders(
        correspondent_id=os.getenv("CORRESPONDENT_ID"), basket_id=create_basket_id
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
