# Orders
(*orders*)

## Overview

### Available Operations

* [create_order](#create_order) - Create Order
* [get_order](#get_order) - Get Order
* [cancel_order](#cancel_order) - Cancel Order
* [set_extra_reporting_data](#set_extra_reporting_data) - Set Extra Reporting Data
* [list_correspondent_orders](#list_correspondent_orders) - List Correspondent Orders

## create_order

Creates a new order for equity or fixed income securities.

 Equity quantities may be for fractional shares, whole shares, or notional dollar amounts. Fixed income orders may be specified in face value currency amounts, with prices expressed in conventional "percentage of par" values.

 Upon successful submission, if the request is a duplicate, returns the existing order in its current state in the system. If the request is not a duplicate, returns the summary of the newly submitted order.

### Example Usage

<!-- UsageSnippet language="python" operationID="OrderService_CreateOrder" method="post" path="/trading/v1/accounts/{account_id}/orders" -->
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

    res = sdk.orders.create_order(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", order_create=components.OrderCreate(
        asset_type=components.AssetType.EQUITY,
        client_order_id="a6d5258b-6b23-478a-8145-98e79d60427a",
        identifier="SBUX",
        identifier_type=components.IdentifierType.SYMBOL,
        order_date=components.DateCreate(),
        order_type=components.OrderType.MARKET,
        side=components.Side.BUY,
        time_in_force=components.TimeInForce.DAY,
    ))

    assert res.order is not None

    # Handle response
    print(res.order)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01HBRQ5BW6ZAY4BNWP4GWRD80X                                          |
| `order_create`                                                      | [components.OrderCreate](../../models/components/ordercreate.md)    | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.OrderServiceCreateOrderResponse](../../models/operations/orderservicecreateorderresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 409 | application/json   |
| errors.Status      | 500, 503           | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_order

Gets an order by order ID.

 Upon successful submission, returns the details of the queried order.

### Example Usage

<!-- UsageSnippet language="python" operationID="OrderService_GetOrder" method="get" path="/trading/v1/accounts/{account_id}/orders/{order_id}" -->
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

    res = sdk.orders.get_order(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", order_id="ebb0c9b5-2c74-45c9-a4ab-40596b778706")

    assert res.order is not None

    # Handle response
    print(res.order)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01HBRQ5BW6ZAY4BNWP4GWRD80X                                          |
| `order_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The order id.                                                       | ebb0c9b5-2c74-45c9-a4ab-40596b778706                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.OrderServiceGetOrderResponse](../../models/operations/orderservicegetorderresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500, 503           | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## cancel_order

Submits an order cancellation request by order ID. Confirmation of order cancellation requests are provided through asynchronous events.

 Upon successful submission, returns the details of the order pending cancellation.

### Example Usage

<!-- UsageSnippet language="python" operationID="OrderService_CancelOrder" method="post" path="/trading/v1/accounts/{account_id}/orders/{order_id}:cancel" -->
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

    res = sdk.orders.cancel_order(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", order_id="ebb0c9b5-2c74-45c9-a4ab-40596b778706", cancel_order_request_create={
        "name": "accounts/01HBRQ5BW6ZAY4BNWP4GWRD80X/orders/ebb0c9b5-2c74-45c9-a4ab-40596b778706",
    })

    assert res.order is not None

    # Handle response
    print(res.order)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `account_id`                                                                               | *str*                                                                                      | :heavy_check_mark:                                                                         | The account id.                                                                            | 01HBRQ5BW6ZAY4BNWP4GWRD80X                                                                 |
| `order_id`                                                                                 | *str*                                                                                      | :heavy_check_mark:                                                                         | The order id.                                                                              | ebb0c9b5-2c74-45c9-a4ab-40596b778706                                                       |
| `cancel_order_request_create`                                                              | [components.CancelOrderRequestCreate](../../models/components/cancelorderrequestcreate.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |                                                                                            |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |                                                                                            |

### Response

**[operations.OrderServiceCancelOrderResponse](../../models/operations/orderservicecancelorderresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500, 503           | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## set_extra_reporting_data

Sets extra reporting data to an existing order. Any SetExtraReportingDataRequest must include the name of the order and the cancel_confirmed_time

### Example Usage

<!-- UsageSnippet language="python" operationID="OrderService_SetExtraReportingData" method="post" path="/trading/v1/accounts/{account_id}/orders/{order_id}:setExtraReportingData" -->
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

    res = sdk.orders.set_extra_reporting_data(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", order_id="ebb0c9b5-2c74-45c9-a4ab-40596b778706", set_extra_reporting_data_request_create={
        "cancel_confirmed_time": parse_datetime("2025-12-13T15:28:17.262732Z"),
        "name": "accounts/01HBRQ5BW6ZAY4BNWP4GWRD80X/orders/ebb0c9b5-2c74-45c9-a4ab-40596b778706",
    })

    assert res.order is not None

    # Handle response
    print(res.order)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                   | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The account id.                                                                                                | 01HBRQ5BW6ZAY4BNWP4GWRD80X                                                                                     |
| `order_id`                                                                                                     | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The order id.                                                                                                  | ebb0c9b5-2c74-45c9-a4ab-40596b778706                                                                           |
| `set_extra_reporting_data_request_create`                                                                      | [components.SetExtraReportingDataRequestCreate](../../models/components/setextrareportingdatarequestcreate.md) | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |                                                                                                                |

### Response

**[operations.OrderServiceSetExtraReportingDataResponse](../../models/operations/orderservicesetextrareportingdataresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500, 503           | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## list_correspondent_orders

Lists orders matching the specified filter criteria. Results are paginated and sorted in the reverse order of their creation.

### Example Usage

<!-- UsageSnippet language="python" operationID="OrderService_ListCorrespondentOrders" method="get" path="/trading/v1/correspondents/{correspondent_id}/orders" -->
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

    res = sdk.orders.list_correspondent_orders(correspondent_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", filter_="open && order_date >= date('2025-05-10')", page_size=50, page_token="CiAKGjBpNDd2Nmp2Zml2cXRwYjBpOXA")

    assert res.list_correspondent_orders_response is not None

    # Handle response
    print(res.list_correspondent_orders_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `correspondent_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | The correspondent id.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 01HBRQ5BW6ZAY4BNWP4GWRD80X                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `filter_`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | CEL filter string expressing what orders should be listed. The only properties available for filtering are the boolean `open` and `order_date`. Each of these represent fields on the Orders object, and more details about each can be found attached to the properties.<br/><br/> If `open` is not provided, both "open" and "not open" orders will be returned. All `order_date` searches are limited to orders within the most recent 365 days. If no `order_date` is specified, the default will search between now and 365 days ago. | open && order_date >= date('2025-05-10')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | The number of records to return in a single page. The maximum page size is 100. If a value is not provided, the default of 100 will be used. If a value less than one, or greater than the maximum, is provided, the default value will be used.                                                                                                                                                                                                                                                                                   | 50                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `page_token`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | The token for the next page of content to fetch. When paginating, all other parameters provided to `ListOrders` must match the call that provided the page token.                                                                                                                                                                                                                                                                                                                                                                  | CiAKGjBpNDd2Nmp2Zml2cXRwYjBpOXA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### Response

**[operations.OrderServiceListCorrespondentOrdersResponse](../../models/operations/orderservicelistcorrespondentordersresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |