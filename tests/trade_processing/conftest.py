import uuid
from datetime import datetime, timezone
from ascend_sdk.models import components
import pytest


def create_execution_request():
    """Helper function to create an execution request object."""
    return components.ExecutionCreate(
        execution_time=str(datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")),
        external_id=str(uuid.uuid4()),
        price=components.DecimalCreate(value="5"),
        quantity=components.DecimalCreate(value="1"),
    )


def create_trade_allocation_request(from_account_id, to_account_id):
    """Helper function to create a trade allocation request object."""
    return components.TradeAllocationCreate(
        broker_capacity=components.TradeAllocationCreateBrokerCapacity.PRINCIPAL,
        execution_time=str(datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")),
        from_account_id=from_account_id,
        identifier="SBUX",
        identifier_type=components.TradeAllocationCreateIdentifierType.SYMBOL,
        asset_type=components.TradeAllocationCreateAssetType.EQUITY,
        price=components.DecimalCreate(value="5"),
        quantity=components.DecimalCreate(value="1"),
        source_application="Trading-App",
        to_account_id=to_account_id,
        to_side=components.TradeAllocationToSide.BUY,
    )


@pytest.fixture(scope="module")
def deceased_account_id():
    return "01JHK07CRQ9X8P5XE9JWG4PFSP"


@pytest.fixture(scope="module")
def create_booking_id(create_sdk, withdrawal_account_id):
    s = create_sdk

    # Create Booking
    booking_request = components.TradeCreate(
        account_id=withdrawal_account_id,
        broker_capacity=components.TradeCreateBrokerCapacity.PRINCIPAL,
        client_order_id=str(uuid.uuid4()),
        executions=[create_execution_request()],
        identifier="SBUX",
        identifier_type=components.TradeCreateIdentifierType.SYMBOL,
        route_type=components.RouteType.QUIK,
        side=components.TradeCreateSide.BUY,
        source_application="Trading-App",
        asset_type=components.TradeCreateAssetType.EQUITY,
        open=True,
    )

    res = s.trade_booking.create_trade(
        account_id=withdrawal_account_id, trade_create=booking_request
    )
    if res.http_meta.response.status_code == 200:
        return [res.booking_trade.trade_id, res.booking_trade.client_order_id]
    else:
        return None


def create_execution_fixture(sdk, account_id, trade_id):
    """Helper function to create execution and return its ID."""
    execution_request = create_execution_request()

    res = sdk.trade_booking.create_execution(
        account_id=account_id, execution_create=execution_request, trade_id=trade_id
    )
    if res.http_meta.response.status_code == 200:
        return res.execution.execution_id
    else:
        return None


@pytest.fixture(scope="module")
def create_execution_id(create_sdk, withdrawal_account_id, create_booking_id):
    return create_execution_fixture(
        create_sdk, withdrawal_account_id, create_booking_id[0]
    )


@pytest.fixture(scope="module")
def create_rebook_execution_id(create_sdk, withdrawal_account_id, create_booking_id):
    return create_execution_fixture(
        create_sdk, withdrawal_account_id, create_booking_id[0]
    )


def create_trade_allocation_fixture(
    sdk, from_account_id, to_account_id, withdrawal_account_id
):
    """Helper function to create a trade allocation and return its ID."""
    allocation_request = create_trade_allocation_request(from_account_id, to_account_id)
    request_id = str(uuid.uuid4())

    res = sdk.trade_allocation.create_trade_allocation(
        account_id=withdrawal_account_id,
        trade_allocation_create=allocation_request,
        request_id=request_id,
    )

    if res.http_meta.response.status_code == 200:
        return res.trade_allocation.trade_allocation_id
    else:
        return None


@pytest.fixture(scope="module")
def create_trade_allocation_id(create_sdk, withdrawal_account_id, deceased_account_id):
    return create_trade_allocation_fixture(
        create_sdk, deceased_account_id, withdrawal_account_id, withdrawal_account_id
    )


@pytest.fixture(scope="module")
def create_rebook_trade_allocation_id(
    create_sdk, withdrawal_account_id, deceased_account_id
):
    return create_trade_allocation_fixture(
        create_sdk, deceased_account_id, withdrawal_account_id, withdrawal_account_id
    )
