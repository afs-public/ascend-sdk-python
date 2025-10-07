import time
import uuid
from datetime import datetime, timezone
from ascend_sdk.models import components


def test_trade_allocation_trade_processing_create_trade_allocation_create_trade_allocation1(
    create_trade_allocation_id, create_rebook_trade_allocation_id
):
    assert create_trade_allocation_id is not None
    assert create_rebook_trade_allocation_id is not None


def test_trade_allocation_trade_processing_get_trade_allocation_get_trade_allocation1(
    create_sdk, create_trade_allocation_id, withdrawal_account_id
):
    s = create_sdk

    assert s is not None

    res = s.trade_allocation.get_trade_allocation(
        account_id=withdrawal_account_id, trade_allocation_id=create_trade_allocation_id
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_trade_allocation_trade_processing_rebook_trade_allocation_rebook_trade_allocation1(
    create_sdk,
    create_rebook_trade_allocation_id,
    withdrawal_account_id,
    deceased_account_id,
):
    s = create_sdk

    assert s is not None

    request = components.RebookTradeAllocationRequestCreate(
        name="accounts/"
        + withdrawal_account_id
        + "/tradeAllocations/"
        + create_rebook_trade_allocation_id,
        request_id=str(uuid.uuid4()),
        trade_allocation=components.TradeAllocationCreate(
            broker_capacity=components.TradeAllocationCreateBrokerCapacity.PRINCIPAL,
            execution_time=str(
                datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            ),
            from_account_id=deceased_account_id,
            identifier="SBUX",
            identifier_type=components.TradeAllocationCreateIdentifierType.SYMBOL,
            asset_type=components.TradeAllocationCreateAssetType.EQUITY,
            price=components.DecimalCreate(value="5"),
            quantity=components.DecimalCreate(value="1"),
            source_application="Trading-App",
            to_account_id=withdrawal_account_id,
            to_side=components.TradeAllocationToSide.BUY,
        ),
    )

    res = s.trade_allocation.rebook_trade_allocation(
        account_id=withdrawal_account_id,
        trade_allocation_id=create_rebook_trade_allocation_id,
        rebook_trade_allocation_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_trade_allocation_trade_processing_cancel_trade_allocation_cancel_trade_allocation1(
    create_sdk, create_trade_allocation_id, withdrawal_account_id
):
    s = create_sdk

    assert s is not None

    request = components.CancelTradeAllocationRequestCreate(
        name="accounts/"
        + withdrawal_account_id
        + "/tradeAllocations/"
        + create_trade_allocation_id,
    )

    res = s.trade_allocation.cancel_trade_allocation(
        account_id=withdrawal_account_id,
        trade_allocation_id=create_trade_allocation_id,
        cancel_trade_allocation_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
