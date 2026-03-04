# OptionOrders
(*option_orders*)

## Overview

### Available Operations

* [create_option_order](#create_option_order) - Create Option Order
* [get_option_order](#get_option_order) - Get Option Order
* [cancel_option_order](#cancel_option_order) - Cancel Option Order

## create_option_order

Creates a new option order.

 Currently only single-leg option orders are supported, but the data structures will support multi-leg orders in the future. The single-leg constraint will be repeated in this documentation, but validation rules related to the initial (future) multi-leg support are also documented.

 Upon successful submission, if the request is a duplicate, returns the existing order in its current state in the system. If the request is not a duplicate, returns the summary of the newly submitted order.

### Example Usage

<!-- UsageSnippet language="python" operationID="OptionOrderService_CreateOptionOrder" method="post" path="/trading/v1/accounts/{account_id}/optionOrders" -->
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

    res = sdk.option_orders.create_option_order(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", option_order_create=components.OptionOrderCreate(
        broker_capacity=components.OptionOrderCreateBrokerCapacity.AGENCY,
        client_order_id="a6d5258b-6b23-478a-8145-98e79d60427a",
        currency_code="USD",
        legs=[],
        limit_price=components.DecimalCreate(),
        order_date=components.DateCreate(),
        order_type=components.OptionOrderCreateOrderType.LIMIT,
        price_direction=components.PriceDirection.CREDIT,
        quantity=components.DecimalCreate(),
        time_in_force=components.OptionOrderCreateTimeInForce.DAY,
    ))

    assert res.option_order is not None

    # Handle response
    print(res.option_order)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `account_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | The account id.                                                              | 01HBRQ5BW6ZAY4BNWP4GWRD80X                                                   |
| `option_order_create`                                                        | [components.OptionOrderCreate](../../models/components/optionordercreate.md) | :heavy_check_mark:                                                           | N/A                                                                          |                                                                              |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[operations.OptionOrderServiceCreateOptionOrderResponse](../../models/operations/optionorderservicecreateoptionorderresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 409 | application/json   |
| errors.Status      | 500, 503           | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_option_order

Gets an option order by option order ID.

 Upon successful submission, returns the details of the queried order.

### Example Usage

<!-- UsageSnippet language="python" operationID="OptionOrderService_GetOptionOrder" method="get" path="/trading/v1/accounts/{account_id}/optionOrders/{optionOrder_id}" -->
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

    res = sdk.option_orders.get_option_order(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", option_order_id="ebb0c9b5-2c74-45c9-a4ab-40596b778706")

    assert res.option_order is not None

    # Handle response
    print(res.option_order)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01HBRQ5BW6ZAY4BNWP4GWRD80X                                          |
| `option_order_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The optionOrder id.                                                 | ebb0c9b5-2c74-45c9-a4ab-40596b778706                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.OptionOrderServiceGetOptionOrderResponse](../../models/operations/optionorderservicegetoptionorderresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500, 503           | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## cancel_option_order

Submits an order cancellation request by option order ID. Confirmation of order cancellation requests are provided through asynchronous events.

 Upon successful submission, returns the details of the order pending cancellation.

### Example Usage

<!-- UsageSnippet language="python" operationID="OptionOrderService_CancelOptionOrder" method="post" path="/trading/v1/accounts/{account_id}/optionOrders/{optionOrder_id}:cancel" -->
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

    res = sdk.option_orders.cancel_option_order(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", option_order_id="ebb0c9b5-2c74-45c9-a4ab-40596b778706", cancel_option_order_request_create={
        "name": "accounts/01HBRQ5BW6ZAY4BNWP4GWRD80X/optionOrders/ebb0c9b5-2c74-45c9-a4ab-40596b778706",
    })

    assert res.option_order is not None

    # Handle response
    print(res.option_order)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            | Example                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                           | *str*                                                                                                  | :heavy_check_mark:                                                                                     | The account id.                                                                                        | 01HBRQ5BW6ZAY4BNWP4GWRD80X                                                                             |
| `option_order_id`                                                                                      | *str*                                                                                                  | :heavy_check_mark:                                                                                     | The optionOrder id.                                                                                    | ebb0c9b5-2c74-45c9-a4ab-40596b778706                                                                   |
| `cancel_option_order_request_create`                                                                   | [components.CancelOptionOrderRequestCreate](../../models/components/canceloptionorderrequestcreate.md) | :heavy_check_mark:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |                                                                                                        |

### Response

**[operations.OptionOrderServiceCancelOptionOrderResponse](../../models/operations/optionorderservicecanceloptionorderresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500, 503           | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |