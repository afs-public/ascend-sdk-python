# TradeAllocation
(*trade_allocation*)

## Overview

### Available Operations

* [create_trade_allocation](#create_trade_allocation) - Create Trade Allocation
* [get_trade_allocation](#get_trade_allocation) - Get Trade Allocation
* [cancel_trade_allocation](#cancel_trade_allocation) - Cancel Trade Allocation
* [rebook_trade_allocation](#rebook_trade_allocation) - Rebook Trade Allocation

## create_trade_allocation

Creates a new trade allocation. These are used to allocate or distribute positions between Apex accounts.

 Upon success, returns the created trade allocation and its enriched details.

### Example Usage

```python
from ascend_sdk import SDK
from ascend_sdk.models import components
import dateutil.parser

s = SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
)

res = s.trade_allocation.create_trade_allocation(account_id="01FAKEACCOUNT1TYKWEYRH8S2K", trade_allocation_create={
    "broker_capacity": components.TradeAllocationCreateBrokerCapacity.AGENCY,
    "execution_time": dateutil.parser.isoparse("2024-07-17T12:00:00Z"),
    "from_account_id": "01HASWB2DTMRT3DAM45P56J2H3",
    "identifier": "AAPL",
    "identifier_type": components.TradeAllocationCreateIdentifierType.SYMBOL,
    "price": {},
    "quantity": {},
    "source_application": "Trading-App",
    "to_account_id": "02HASWB2DTMRT3DAM45P56J2T2",
    "to_side": components.ToSide.BUY,
})

if res.trade_allocation is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | The account id.                                                                                                             | 01FAKEACCOUNT1TYKWEYRH8S2K                                                                                                  |
| `trade_allocation_create`                                                                                                   | [components.TradeAllocationCreate](../../models/components/tradeallocationcreate.md)                                        | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |                                                                                                                             |
| `request_id`                                                                                                                | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | A globally unique UUID that is specific to the request. This id is used to prevent duplicate requests from being processed. | 8a0d35c0-428c-439e-9b03-b611530fe06f                                                                                        |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[operations.BookingCreateTradeAllocationResponse](../../models/operations/bookingcreatetradeallocationresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.Status                     | 400, 403, 404, 409, 500, 503, 504 | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## get_trade_allocation

Retrieves a trade allocation and its details.

 Upon successful submission, returns the trade allocation details.

### Example Usage

```python
from ascend_sdk import SDK
from ascend_sdk.models import components

s = SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
)

res = s.trade_allocation.get_trade_allocation(account_id="02HASWB2DTMRT3DAM45P56J2T2", trade_allocation_id="01J0XX2KDN3M9QKFKRE2HYSCQM")

if res.trade_allocation is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 02HASWB2DTMRT3DAM45P56J2T2                                          |
| `trade_allocation_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The tradeAllocation id.                                             | 01J0XX2KDN3M9QKFKRE2HYSCQM                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.BookingGetTradeAllocationResponse](../../models/operations/bookinggettradeallocationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.Status                | 400, 403, 404, 500, 503, 504 | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## cancel_trade_allocation

Cancel a trade allocation using the original trade_allocation_id.

 Upon successful submission, returns an empty response. CancelTradeAllocation will either cancel everything, or nothing at all if a failure occurs.

### Example Usage

```python
from ascend_sdk import SDK
from ascend_sdk.models import components

s = SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
)

res = s.trade_allocation.cancel_trade_allocation(account_id="02HASWB2DTMRT3DAM45P56J2T2", trade_allocation_id="01J0XX2KDN3M9QKFKRE2HYSCQM", cancel_trade_allocation_request_create={
    "name": "accounts/02HASWB2DTMRT3DAM45P56J2T2/tradeAllocations/01J0XX2KDN3M9QKFKRE2HYSCQM",
})

if res.cancel_trade_allocation_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                   | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The account id.                                                                                                | 02HASWB2DTMRT3DAM45P56J2T2                                                                                     |
| `trade_allocation_id`                                                                                          | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The tradeAllocation id.                                                                                        | 01J0XX2KDN3M9QKFKRE2HYSCQM                                                                                     |
| `cancel_trade_allocation_request_create`                                                                       | [components.CancelTradeAllocationRequestCreate](../../models/components/canceltradeallocationrequestcreate.md) | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |                                                                                                                |

### Response

**[operations.BookingCancelTradeAllocationResponse](../../models/operations/bookingcanceltradeallocationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.Status                | 400, 403, 404, 500, 503, 504 | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## rebook_trade_allocation

Rebook a trade allocation by the original trade_allocation_id. The allocation is rebooked by canceling the original allocation and creating a new one with the provided details.

 Upon successful submission, returns both the original and new allocation, as separate resources.

### Example Usage

```python
from ascend_sdk import SDK
from ascend_sdk.models import components
import dateutil.parser

s = SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
)

res = s.trade_allocation.rebook_trade_allocation(account_id="02HASWB2DTMRT3DAM45P56J2T2", trade_allocation_id="01J0XX2KDN3M9QKFKRE2HYSCQM", rebook_trade_allocation_request_create={
    "name": "accounts/02HASWB2DTMRT3DAM45P56J2T2/tradeAllocations/01J0XX2KDN3M9QKFKRE2HYSCQM",
    "request_id": "8a0d35c0-428c-439e-9b03-b611530fe06f",
    "trade_allocation": {
        "broker_capacity": components.TradeAllocationCreateBrokerCapacity.AGENCY,
        "execution_time": dateutil.parser.isoparse("2024-07-17T12:00:00Z"),
        "from_account_id": "01HASWB2DTMRT3DAM45P56J2H3",
        "identifier": "AAPL",
        "identifier_type": components.TradeAllocationCreateIdentifierType.SYMBOL,
        "price": {},
        "quantity": {},
        "source_application": "Trading-App",
        "to_account_id": "02HASWB2DTMRT3DAM45P56J2T2",
        "to_side": components.ToSide.BUY,
    },
})

if res.rebook_trade_allocation_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                   | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The account id.                                                                                                | 02HASWB2DTMRT3DAM45P56J2T2                                                                                     |
| `trade_allocation_id`                                                                                          | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The tradeAllocation id.                                                                                        | 01J0XX2KDN3M9QKFKRE2HYSCQM                                                                                     |
| `rebook_trade_allocation_request_create`                                                                       | [components.RebookTradeAllocationRequestCreate](../../models/components/rebooktradeallocationrequestcreate.md) | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |                                                                                                                |

### Response

**[operations.BookingRebookTradeAllocationResponse](../../models/operations/bookingrebooktradeallocationresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.Status                | 400, 403, 404, 500, 503, 504 | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |