# TradeBooking
(*trade_booking*)

## Overview

### Available Operations

* [create_trade](#create_trade) - Create Trade
* [get_trade](#get_trade) - Get Trade
* [complete_trade](#complete_trade) - Complete Trade
* [cancel_trade](#cancel_trade) - Cancel Trade
* [rebook_trade](#rebook_trade) - Rebook Trade
* [create_execution](#create_execution) - Create Execution
* [get_execution](#get_execution) - Get Execution
* [cancel_execution](#cancel_execution) - Cancel Execution
* [rebook_execution](#rebook_execution) - Rebook Execution

## create_trade

Creates a trade with one or more executions. Combination of (account_id, client_order_id, and the process_date (determined by Booking service)) determines the uniqueness of the trade.

 Upon successful submission, returns the created trade and its details including Booking service enriched details.

### Example Usage

<!-- UsageSnippet language="python" operationID="Booking_CreateTrade" method="post" path="/booking/v1/accounts/{account_id}/trades" -->
```python
from ascend_sdk import SDK
from ascend_sdk.models import components
from ascend_sdk.utils import parse_datetime


with SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.trade_booking.create_trade(account_id="01FAKEACCOUNT1TYKWEYRH8S2K", trade_create=components.TradeCreate(
        account_id="02HASWB2DTMRT3DAM45P56J2T2",
        asset_type=components.TradeCreateAssetType.EQUITY,
        broker_capacity=components.TradeCreateBrokerCapacity.AGENCY,
        client_order_id="00be5285-0623-4560-8c58-f05af2c56ba0",
        executions=[
            components.ExecutionCreate(
                execution_time=parse_datetime("2024-07-17T12:00:00Z"),
                external_id="0H06HAP3A3Y",
                price=components.DecimalCreate(),
                quantity=components.DecimalCreate(),
            ),
        ],
        identifier="AAPL",
        identifier_type=components.TradeCreateIdentifierType.SYMBOL,
        route_type=components.RouteType.MNGD,
        side=components.TradeCreateSide.BUY,
        source_application="Trading-App",
    ))

    assert res.booking_trade is not None

    # Handle response
    print(res.booking_trade)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01FAKEACCOUNT1TYKWEYRH8S2K                                          |
| `trade_create`                                                      | [components.TradeCreate](../../models/components/tradecreate.md)    | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.BookingCreateTradeResponse](../../models/operations/bookingcreatetraderesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_trade

Gets a trade and all executions by trade_id.

 Upon successful submission, returns the trade details and all the execution by trade_id.

### Example Usage

<!-- UsageSnippet language="python" operationID="Booking_GetTrade" method="get" path="/booking/v1/accounts/{account_id}/trades/{trade_id}" -->
```python
from ascend_sdk import SDK
from ascend_sdk.models import components


with SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.trade_booking.get_trade(account_id="01FAKEACCOUNT1TYKWEYRH8S2K", trade_id="01FAKETRADEIDPROVIDEDFROMCREATETRADE")

    assert res.booking_trade is not None

    # Handle response
    print(res.booking_trade)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01FAKEACCOUNT1TYKWEYRH8S2K                                          |
| `trade_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The trade id.                                                       | 01FAKETRADEIDPROVIDEDFROMCREATETRADE                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.BookingGetTradeResponse](../../models/operations/bookinggettraderesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## complete_trade

Complete a Trade by closing and generating any fees and withholdings if necessary. Once this endpoint returns an OK, the combination of details that generated the Trade (account_id, client_order_id, and the process_date) cannot be reused.

 Upon successful submission, returns completed trade details and all the executions. Trades that are left open will be automatically closed nightly before Ledger's EOD.

### Example Usage

<!-- UsageSnippet language="python" operationID="Booking_CompleteTrade" method="post" path="/booking/v1/accounts/{account_id}/trades/{trade_id}:complete" -->
```python
from ascend_sdk import SDK
from ascend_sdk.models import components


with SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.trade_booking.complete_trade(account_id="02HASWB2DTMRT3DAM45P56J2T2", trade_id="01J0XX2KDN3M9QKFKRE2HYSCQM", complete_trade_request_create={
        "name": "accounts/02HASWB2DTMRT3DAM45P56J2T2/trades/01J0XX2KDN3M9QKFKRE2HYSCQM",
    })

    assert res.complete_trade_response is not None

    # Handle response
    print(res.complete_trade_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    | Example                                                                                        |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `account_id`                                                                                   | *str*                                                                                          | :heavy_check_mark:                                                                             | The account id.                                                                                | 02HASWB2DTMRT3DAM45P56J2T2                                                                     |
| `trade_id`                                                                                     | *str*                                                                                          | :heavy_check_mark:                                                                             | The trade id.                                                                                  | 01J0XX2KDN3M9QKFKRE2HYSCQM                                                                     |
| `complete_trade_request_create`                                                                | [components.CompleteTradeRequestCreate](../../models/components/completetraderequestcreate.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |                                                                                                |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |                                                                                                |

### Response

**[operations.BookingCompleteTradeResponse](../../models/operations/bookingcompletetraderesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_trade

Cancel a trade and all the executions using the original trade_id. CancelTrade will either cancel everything, or nothing at all if a failure occurs.

 Upon successful submission, returns an empty response.

### Example Usage

<!-- UsageSnippet language="python" operationID="Booking_CancelTrade" method="post" path="/booking/v1/accounts/{account_id}/trades/{trade_id}:cancel" -->
```python
from ascend_sdk import SDK
from ascend_sdk.models import components


with SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.trade_booking.cancel_trade(account_id="01FAKEACCOUNT1TYKWEYRH8S2K", trade_id="01FAKETRADEIDPROVIDEDFROMCREATETRADE", cancel_trade_request_create={
        "name": "accounts/01FAKEACCOUNT1TYKWEYRH8S2K/trades/01FAKETRADEIDPROVIDEDFROMCREATETRADE",
    })

    assert res.cancel_trade_response is not None

    # Handle response
    print(res.cancel_trade_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `account_id`                                                                               | *str*                                                                                      | :heavy_check_mark:                                                                         | The account id.                                                                            | 01FAKEACCOUNT1TYKWEYRH8S2K                                                                 |
| `trade_id`                                                                                 | *str*                                                                                      | :heavy_check_mark:                                                                         | The trade id.                                                                              | 01FAKETRADEIDPROVIDEDFROMCREATETRADE                                                       |
| `cancel_trade_request_create`                                                              | [components.CancelTradeRequestCreate](../../models/components/canceltraderequestcreate.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |                                                                                            |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |                                                                                            |

### Response

**[operations.BookingCancelTradeResponse](../../models/operations/bookingcanceltraderesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## rebook_trade

Rebook a trade by the original trade_id. The entire original trade's executions are rebooked using the executions provided in the request. If applicable, fees and backup withholdings will be re-calculated.

 Upon successful submission, returns the rebooked trade details and all the executions.

### Example Usage

<!-- UsageSnippet language="python" operationID="Booking_RebookTrade" method="post" path="/booking/v1/accounts/{account_id}/trades/{trade_id}:rebook" -->
```python
from ascend_sdk import SDK
from ascend_sdk.models import components


with SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.trade_booking.rebook_trade(account_id="02HASWB2DTMRT3DAM45P56J2T2", trade_id="01J0XX2KDN3M9QKFKRE2HYSCQM", rebook_trade_request_create=components.RebookTradeRequestCreate(
        name="accounts/02HASWB2DTMRT3DAM45P56J2T2/trades/01J0XX2KDN3M9QKFKRE2HYSCQM",
        trade=components.TradeCreate(
            account_id="02HASWB2DTMRT3DAM45P56J2T2",
            asset_type=components.TradeCreateAssetType.EQUITY,
            broker_capacity=components.TradeCreateBrokerCapacity.AGENCY,
            client_order_id="00be5285-0623-4560-8c58-f05af2c56ba0",
            executions=[],
            identifier="AAPL",
            identifier_type=components.TradeCreateIdentifierType.SYMBOL,
            route_type=components.RouteType.MNGD,
            side=components.TradeCreateSide.BUY,
            source_application="Trading-App",
        ),
    ))

    assert res.rebook_trade_response is not None

    # Handle response
    print(res.rebook_trade_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `account_id`                                                                               | *str*                                                                                      | :heavy_check_mark:                                                                         | The account id.                                                                            | 02HASWB2DTMRT3DAM45P56J2T2                                                                 |
| `trade_id`                                                                                 | *str*                                                                                      | :heavy_check_mark:                                                                         | The trade id.                                                                              | 01J0XX2KDN3M9QKFKRE2HYSCQM                                                                 |
| `rebook_trade_request_create`                                                              | [components.RebookTradeRequestCreate](../../models/components/rebooktraderequestcreate.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |                                                                                            |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |                                                                                            |

### Response

**[operations.BookingRebookTradeResponse](../../models/operations/bookingrebooktraderesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## create_execution

Create a new execution under an existing trade that is open.

 Upon successful submission, returns the created execution and its details.

### Example Usage

<!-- UsageSnippet language="python" operationID="Booking_CreateExecution" method="post" path="/booking/v1/accounts/{account_id}/trades/{trade_id}/executions" -->
```python
from ascend_sdk import SDK
from ascend_sdk.models import components
from ascend_sdk.utils import parse_datetime


with SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.trade_booking.create_execution(account_id="01FAKEACCOUNT1TYKWEYRH8S2K", trade_id="01FAKETRADEIDPROVIDEDFROMCREATETRADE", execution_create=components.ExecutionCreate(
        execution_time=parse_datetime("2024-07-17T12:00:00Z"),
        external_id="0H06HAP3A3Y",
        price=components.DecimalCreate(),
        quantity=components.DecimalCreate(),
    ))

    assert res.execution is not None

    # Handle response
    print(res.execution)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `account_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | The account id.                                                          | 01FAKEACCOUNT1TYKWEYRH8S2K                                               |
| `trade_id`                                                               | *str*                                                                    | :heavy_check_mark:                                                       | The trade id.                                                            | 01FAKETRADEIDPROVIDEDFROMCREATETRADE                                     |
| `execution_create`                                                       | [components.ExecutionCreate](../../models/components/executioncreate.md) | :heavy_check_mark:                                                       | N/A                                                                      |                                                                          |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |                                                                          |

### Response

**[operations.BookingCreateExecutionResponse](../../models/operations/bookingcreateexecutionresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_execution

Gets an execution by execution_id.

 Upon successful submission, returns the execution details by execution_id.

### Example Usage

<!-- UsageSnippet language="python" operationID="Booking_GetExecution" method="get" path="/booking/v1/accounts/{account_id}/trades/{trade_id}/executions/{execution_id}" -->
```python
from ascend_sdk import SDK
from ascend_sdk.models import components


with SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.trade_booking.get_execution(account_id="01FAKEACCOUNT1TYKWEYRH8S2K", trade_id="01FAKETRADEIDPROVIDEDFROMCREATETRADE", execution_id="01FAKEEXECUTONIDPROVIDEDFROMBOOKINGAPI")

    assert res.execution is not None

    # Handle response
    print(res.execution)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01FAKEACCOUNT1TYKWEYRH8S2K                                          |
| `trade_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The trade id.                                                       | 01FAKETRADEIDPROVIDEDFROMCREATETRADE                                |
| `execution_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The execution id.                                                   | 01FAKEEXECUTONIDPROVIDEDFROMBOOKINGAPI                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.BookingGetExecutionResponse](../../models/operations/bookinggetexecutionresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_execution

Cancel an execution using the original execution_id. If applicable, fees and backup withholdings will be re-calculated.

 Upon successful submission, returns the execution that was canceled.

### Example Usage

<!-- UsageSnippet language="python" operationID="Booking_CancelExecution" method="post" path="/booking/v1/accounts/{account_id}/trades/{trade_id}/executions/{execution_id}:cancel" -->
```python
from ascend_sdk import SDK
from ascend_sdk.models import components


with SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.trade_booking.cancel_execution(account_id="02HASWB2DTMRT3DAM45P56J2T2", trade_id="01J0XX2KDN3M9QKFKRE2HYSCQM", execution_id="02G0XX2KDN3M9QKFKRE2HYSCMY", cancel_execution_request_create={
        "name": "accounts/02HASWB2DTMRT3DAM45P56J2T2/trades/01J0XX2KDN3M9QKFKRE2HYSCQM/executions/02G0XX2KDN3M9QKFKRE2HYSCMY",
    })

    assert res.cancel_execution_response is not None

    # Handle response
    print(res.cancel_execution_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                       | *str*                                                                                              | :heavy_check_mark:                                                                                 | The account id.                                                                                    | 02HASWB2DTMRT3DAM45P56J2T2                                                                         |
| `trade_id`                                                                                         | *str*                                                                                              | :heavy_check_mark:                                                                                 | The trade id.                                                                                      | 01J0XX2KDN3M9QKFKRE2HYSCQM                                                                         |
| `execution_id`                                                                                     | *str*                                                                                              | :heavy_check_mark:                                                                                 | The execution id.                                                                                  | 02G0XX2KDN3M9QKFKRE2HYSCMY                                                                         |
| `cancel_execution_request_create`                                                                  | [components.CancelExecutionRequestCreate](../../models/components/cancelexecutionrequestcreate.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |                                                                                                    |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |                                                                                                    |

### Response

**[operations.BookingCancelExecutionResponse](../../models/operations/bookingcancelexecutionresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## rebook_execution

Rebook an execution by the original execution_id. If applicable, fees and backup withholdings will be re-calculated.

 Upon successful submission, returns the rebooked execution details.

### Example Usage

<!-- UsageSnippet language="python" operationID="Booking_RebookExecution" method="post" path="/booking/v1/accounts/{account_id}/trades/{trade_id}/executions/{execution_id}:rebook" -->
```python
from ascend_sdk import SDK
from ascend_sdk.models import components
from ascend_sdk.utils import parse_datetime


with SDK(
    security=components.Security(
        api_key="ABCDEFGHIJ0123456789abcdefghij0123456789",
        service_account_creds=components.ServiceAccountCreds(
            private_key="-----BEGIN PRIVATE KEY--{OMITTED FOR BREVITY}",
            name="FinFirm",
            organization="correspondents/00000000-0000-0000-0000-000000000000",
            type="serviceAccount",
        ),
    ),
) as sdk:

    res = sdk.trade_booking.rebook_execution(account_id="02HASWB2DTMRT3DAM45P56J2T2", trade_id="01J0XX2KDN3M9QKFKRE2HYSCQM", execution_id="02G0XX2KDN3M9QKFKRE2HYSCMY", rebook_execution_request_create=components.RebookExecutionRequestCreate(
        execution=components.ExecutionCreate(
            execution_time=parse_datetime("2024-07-17T12:00:00Z"),
            external_id="0H06HAP3A3Y",
            price=components.DecimalCreate(),
            quantity=components.DecimalCreate(),
        ),
        name="accounts/02HASWB2DTMRT3DAM45P56J2T2/trades/01J0XX2KDN3M9QKFKRE2HYSCQM/executions/02G0XX2KDN3M9QKFKRE2HYSCMY",
    ))

    assert res.rebook_execution_response is not None

    # Handle response
    print(res.rebook_execution_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                       | *str*                                                                                              | :heavy_check_mark:                                                                                 | The account id.                                                                                    | 02HASWB2DTMRT3DAM45P56J2T2                                                                         |
| `trade_id`                                                                                         | *str*                                                                                              | :heavy_check_mark:                                                                                 | The trade id.                                                                                      | 01J0XX2KDN3M9QKFKRE2HYSCQM                                                                         |
| `execution_id`                                                                                     | *str*                                                                                              | :heavy_check_mark:                                                                                 | The execution id.                                                                                  | 02G0XX2KDN3M9QKFKRE2HYSCMY                                                                         |
| `rebook_execution_request_create`                                                                  | [components.RebookExecutionRequestCreate](../../models/components/rebookexecutionrequestcreate.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |                                                                                                    |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |                                                                                                    |

### Response

**[operations.BookingRebookExecutionResponse](../../models/operations/bookingrebookexecutionresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |