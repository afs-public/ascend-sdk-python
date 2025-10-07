import os
import time
import uuid

import pytest

from datetime import date

from ascend_sdk.models import components


@pytest.fixture(scope="module")
def basket_order_to_remove():
    return str(uuid.uuid4())


@pytest.fixture(scope="module")
def create_basket_id(create_sdk):
    s = create_sdk

    # Create Basket
    basket_request = components.BasketCreate(
        client_basket_id=str(uuid.uuid4()),
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
    )

    res = s.basket_orders.create_basket(
        correspondent_id=os.getenv("CORRESPONDENT_ID"), basket_create=basket_request
    )

    if res.http_meta.response.status_code == 200:
        return res.basket.basket_id
    else:
        return None


@pytest.fixture(scope="module")
def create_order_id(create_sdk, enrolled_account_id):
    s = create_sdk

    # Fund Account with Credit
    transfers_credit_create = components.TransfersCreditCreate(
        amount=components.DecimalCreate(value="10000.00"),
        client_transfer_id=str(uuid.uuid4()),
        description="Credit given as promotion",
        type=components.TransfersCreditCreateType.PROMOTIONAL,
    )

    s.fees_and_credits.create_credit(
        account_id=enrolled_account_id, transfers_credit_create=transfers_credit_create
    )

    # Create Order
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%-m")
    day = today.strftime("%-d")
    order_request = components.OrderCreate(
        asset_type=components.AssetType.EQUITY,
        client_order_id=str(uuid.uuid4()),
        order_date=components.DateCreate(
            year=year,
            month=month,
            day=day,
        ),
        identifier="SBUX",
        identifier_type=components.IdentifierType.SYMBOL,
        quantity=components.DecimalCreate(value="1"),
        order_type=components.OrderType.LIMIT,
        limit_price=components.LimitPriceCreate(
            price=components.DecimalCreate(value="5.00"),
            type=components.LimitPriceCreateType.PRICE_PER_UNIT,
        ),
        side=components.Side.BUY,
        time_in_force=components.TimeInForce.DAY,
    )

    res = s.create_order.create_order(
        account_id=enrolled_account_id, order_create=order_request
    )

    if res.http_meta.response.status_code == 200:
        return res.order.order_id
    else:
        return None


@pytest.fixture(scope="module")
def identifier_cusp():
    return "912810SX7"
