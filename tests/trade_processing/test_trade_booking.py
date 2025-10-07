import time
import uuid
from datetime import datetime, timezone
from ascend_sdk.models import components


def test_trade_booking_trade_processing_create_trade_create_trade1(create_booking_id):
    assert create_booking_id is not None


def test_trade_booking_trade_processing_get_trade_get_trade1(
    create_sdk, create_booking_id, withdrawal_account_id
):
    s = create_sdk

    assert s is not None

    res = s.trade_booking.get_trade(
        account_id=withdrawal_account_id, trade_id=create_booking_id[0]
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_trade_booking_trade_processing_create_execution_create_execution1(
    create_execution_id, create_rebook_execution_id
):
    assert create_execution_id is not None
    assert create_rebook_execution_id is not None


def test_trade_booking_trade_processing_get_execution_get_execution1(
    create_sdk, create_booking_id, withdrawal_account_id, create_execution_id
):
    s = create_sdk

    assert s is not None

    res = s.trade_booking.get_execution(
        account_id=withdrawal_account_id,
        trade_id=create_booking_id[0],
        execution_id=create_execution_id,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_trade_booking_trade_processing_complete_trade_complete_trade1(
    create_sdk, create_booking_id, withdrawal_account_id
):
    s = create_sdk

    assert s is not None

    request = components.CompleteTradeRequestCreate(
        name="accounts/" + withdrawal_account_id + "/trades/" + create_booking_id[0],
    )

    res = s.trade_booking.complete_trade(
        account_id=withdrawal_account_id,
        trade_id=create_booking_id[0],
        complete_trade_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_trade_booking_trade_processing_rebook_execution_rebook_execution1(
    create_sdk, create_booking_id, withdrawal_account_id, create_rebook_execution_id
):
    s = create_sdk

    assert s is not None

    request = components.RebookExecutionRequestCreate(
        name="accounts/"
        + withdrawal_account_id
        + "/trades/"
        + create_booking_id[0]
        + "/executions/"
        + create_rebook_execution_id,
        execution=components.ExecutionCreate(
            execution_time=str(
                datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            ),
            external_id=str(uuid.uuid4()),
            price=components.DecimalCreate(value="5"),
            quantity=components.DecimalCreate(value="1"),
        ),
    )

    res = s.trade_booking.rebook_execution(
        account_id=withdrawal_account_id,
        trade_id=create_booking_id[0],
        execution_id=create_rebook_execution_id,
        rebook_execution_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_trade_booking_trade_processing_cancel_execution_cancel_execution1(
    create_sdk, create_booking_id, withdrawal_account_id, create_execution_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelExecutionRequestCreate(
        name="accounts/"
        + withdrawal_account_id
        + "/trades/"
        + create_booking_id[0]
        + "/executions/"
        + create_execution_id
    )

    res = s.trade_booking.cancel_execution(
        account_id=withdrawal_account_id,
        trade_id=create_booking_id[0],
        execution_id=create_execution_id,
        cancel_execution_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_trade_booking_trade_processing_rebook_trade_rebook_trade1(
    create_sdk, create_booking_id, withdrawal_account_id
):
    s = create_sdk

    assert s is not None

    request = components.RebookTradeRequestCreate(
        name="accounts/" + withdrawal_account_id + "/trades/" + create_booking_id[0],
        trade=components.TradeCreate(
            account_id=withdrawal_account_id,
            broker_capacity=components.TradeCreateBrokerCapacity.PRINCIPAL,
            client_order_id=create_booking_id[1],
            executions=[
                components.ExecutionCreate(
                    execution_time=str(
                        datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                    ),
                    external_id=str(uuid.uuid4()),
                    price=components.DecimalCreate(value="5"),
                    quantity=components.DecimalCreate(value="1"),
                )
            ],
            identifier="SBUX",
            identifier_type=components.TradeCreateIdentifierType.SYMBOL,
            route_type=components.RouteType.QUIK,
            side=components.TradeCreateSide.BUY,
            source_application="Trading-App",
            asset_type=components.TradeCreateAssetType.EQUITY,
        ),
    )

    res = s.trade_booking.rebook_trade(
        account_id=withdrawal_account_id,
        trade_id=create_booking_id[0],
        rebook_trade_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_trade_booking_trade_processing_cancel_trade_cancel_trade1(
    create_sdk, create_booking_id, withdrawal_account_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelTradeRequestCreate(
        name="accounts/" + withdrawal_account_id + "/trades/" + create_booking_id[0]
    )

    res = s.trade_booking.cancel_trade(
        account_id=withdrawal_account_id,
        trade_id=create_booking_id[0],
        cancel_trade_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
