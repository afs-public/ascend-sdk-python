# AlternativeOrders
(*alternative_orders*)

## Overview

### Available Operations

* [create_alternative_order](#create_alternative_order) - Create Alternative Order
* [list_alternative_orders](#list_alternative_orders) - List Alternative Orders
* [get_alternative_order](#get_alternative_order) - Get Alternative Order
* [retrieve_pending_investor_actions](#retrieve_pending_investor_actions) - Get Pending Investor Actions
* [settle_alternative_order](#settle_alternative_order) - Simulate Alternative Order Booking

## create_alternative_order

Creates an order for an alternative investment asset.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlternativeOrders_CreateAlternativeOrder" method="post" path="/trading/v1/accounts/{account_id}/alternativeOrders" -->
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

    res = sdk.alternative_orders.create_alternative_order(account_id="01JR8YQT40WAQT8S95ZQGS1QN0", alternative_order_create=components.AlternativeOrderCreate(
        client_order_id="f5074670-1b25-439f-9b5c-702027660800",
        identifier="8395",
        identifier_type=components.AlternativeOrderCreateIdentifierType.ASSET_ID,
        side=components.AlternativeOrderCreateSide.BUY,
    ))

    assert res.alternative_order is not None

    # Handle response
    print(res.alternative_order)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `account_id`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | The account id.                                                                        | 01JR8YQT40WAQT8S95ZQGS1QN0                                                             |
| `alternative_order_create`                                                             | [components.AlternativeOrderCreate](../../models/components/alternativeordercreate.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |                                                                                        |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[operations.AlternativeOrdersCreateAlternativeOrderResponse](../../models/operations/alternativeorderscreatealternativeorderresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.Status           | 400, 401, 403, 404, 409 | application/json        |
| errors.Status           | 500                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_alternative_orders

Retrieves a list of alternative investment orders for the specified account.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlternativeOrders_ListAlternativeOrders" method="get" path="/trading/v1/accounts/{account_id}/alternativeOrders" -->
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

    res = sdk.alternative_orders.list_alternative_orders(account_id="01JR8YQT40WAQT8S95ZQGS1QN0", page_size=100, page_token="cGFnZV90b2tlbgo=", filter_="side == 'BUY' && order_status == 'FILLED'")

    assert res.list_alternative_orders_response is not None

    # Handle response
    print(res.list_alternative_orders_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                        | Example                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                 | The account id.                                                                                                                                                                                                                                                                    | 01JR8YQT40WAQT8S95ZQGS1QN0                                                                                                                                                                                                                                                         |
| `page_size`                                                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | The maximum number of orders to return. - Max value = 100 - Values above 100 will be coerced to 100. - If the specified value is greater than the number of orders, the service will return fewer than the specified value. - If unspecified, at most 100 orders will be returned. | 100                                                                                                                                                                                                                                                                                |
| `page_token`                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | For pagination, provide the page token, received from a previous `ListAlternativeOrders` call, to retrieve the subsequent page. All other parameters provided to `ListAlternativeOrders` must match the request that provided the page token.                                      | cGFnZV90b2tlbgo=                                                                                                                                                                                                                                                                   |
| `filter_`                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | A CEL string to filter results. All fields from the response can be used as filters.<br/><br/> See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) guide for syntax details and examples.                                              | side == 'BUY' && order_status == 'FILLED'                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                    |

### Response

**[operations.AlternativeOrdersListAlternativeOrdersResponse](../../models/operations/alternativeorderslistalternativeordersresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_alternative_order

Retrieves the details for the specified alternative investment order.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlternativeOrders_GetAlternativeOrder" method="get" path="/trading/v1/accounts/{account_id}/alternativeOrders/{alternativeOrder_id}" -->
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

    res = sdk.alternative_orders.get_alternative_order(account_id="01JR8YQT40WAQT8S95ZQGS1QN0", alternative_order_id="01H5TSDAD9MQ98B8KF36J3Q8P9")

    assert res.alternative_order is not None

    # Handle response
    print(res.alternative_order)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01JR8YQT40WAQT8S95ZQGS1QN0                                          |
| `alternative_order_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The alternativeOrder id.                                            | 01H5TSDAD9MQ98B8KF36J3Q8P9                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AlternativeOrdersGetAlternativeOrderResponse](../../models/operations/alternativeordersgetalternativeorderresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## retrieve_pending_investor_actions

Retrieves the links for any order documents that are awaiting signature and the `party_id` of the party responsible for signing them.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlternativeOrders_RetrievePendingInvestorActions" method="get" path="/trading/v1/accounts/{account_id}/alternativeOrders/{alternativeOrder_id}:retrievePendingInvestorActions" -->
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

    res = sdk.alternative_orders.retrieve_pending_investor_actions(account_id="01JR8YQT40WAQT8S95ZQGS1QN0", alternative_order_id="01H5TSDAD9MQ98B8KF36J3Q8P9")

    assert res.retrieve_pending_investor_actions_response is not None

    # Handle response
    print(res.retrieve_pending_investor_actions_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01JR8YQT40WAQT8S95ZQGS1QN0                                          |
| `alternative_order_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The alternativeOrder id.                                            | 01H5TSDAD9MQ98B8KF36J3Q8P9                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AlternativeOrdersRetrievePendingInvestorActionsResponse](../../models/operations/alternativeordersretrievependinginvestoractionsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## settle_alternative_order

Simulates settlement process for an alternative order. For use in UAT environment only.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlternativeOrders_SettleAlternativeOrder" method="post" path="/trading/v1/accounts/{account_id}/alternativeOrders/{alternativeOrder_id}:settle" -->
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

    res = sdk.alternative_orders.settle_alternative_order(account_id="01JR8YQT40WAQT8S95ZQGS1QN0", alternative_order_id="01H5TSDAD9MQ98B8KF36J3Q8P9", settle_alternative_order_request_create={
        "name": "accounts/01JR8YQT40WAQT8S95ZQGS1QN0/alternativeOrders/01H5TSDAD9MQ98B8KF36J3Q8P9",
    })

    assert res.alternative_order is not None

    # Handle response
    print(res.alternative_order)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The account id.                                                                                                  | 01JR8YQT40WAQT8S95ZQGS1QN0                                                                                       |
| `alternative_order_id`                                                                                           | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The alternativeOrder id.                                                                                         | 01H5TSDAD9MQ98B8KF36J3Q8P9                                                                                       |
| `settle_alternative_order_request_create`                                                                        | [components.SettleAlternativeOrderRequestCreate](../../models/components/settlealternativeorderrequestcreate.md) | :heavy_check_mark:                                                                                               | N/A                                                                                                              |                                                                                                                  |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[operations.AlternativeOrdersSettleAlternativeOrderResponse](../../models/operations/alternativeorderssettlealternativeorderresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |