# CreateOrder
(*create_order*)

## Overview

### Available Operations

* [create_order](#create_order) - Create Order
* [get_order](#get_order) - Get Order
* [cancel_order](#cancel_order) - Cancel Order

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

    res = sdk.create_order.create_order(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", order_create=components.OrderCreate(
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

    res = sdk.create_order.get_order(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", order_id="ebb0c9b5-2c74-45c9-a4ab-40596b778706")

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

    res = sdk.create_order.cancel_order(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", order_id="ebb0c9b5-2c74-45c9-a4ab-40596b778706", cancel_order_request_create={
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