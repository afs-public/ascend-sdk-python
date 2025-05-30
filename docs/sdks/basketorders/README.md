# BasketOrders
(*basket_orders*)

## Overview

### Available Operations

* [create_basket](#create_basket) - Create Basket
* [add_orders](#add_orders) - Add Orders
* [get_basket](#get_basket) - Get Basket
* [submit_basket](#submit_basket) - Submit Basket
* [list_basket_orders](#list_basket_orders) - List Basket Orders
* [list_compressed_orders](#list_compressed_orders) - List Compressed Orders

## create_basket

Creates an empty basket

 Upon successful submission, if the request is a duplicate, returns the existing basket in its current state in the system. If the request is not a duplicate, returns the summary of the newly created basket.

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

res = s.basket_orders.create_basket(correspondent_id="01HPMZZM6RKMVZA1JQ63RQKJRP", basket_create={
    "client_basket_id": "39347a0d-860b-48e8-a04d-511133f057e3",
    "correspondent_id": "01HPMZZM6RKMVZA1JQ63RQKJRP",
})

if res.basket is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `correspondent_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The correspondent id.                                               | 01HPMZZM6RKMVZA1JQ63RQKJRP                                          |
| `basket_create`                                                     | [components.BasketCreate](../../models/components/basketcreate.md)  | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.BasketOrdersServiceCreateBasketResponse](../../models/operations/basketordersservicecreatebasketresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.Status                | 400, 401, 403, 409, 500, 503 | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## add_orders

Adds a list of basket orders to a basket

 Upon successful submission, returns the basket with a new total count of orders within the basket

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

res = s.basket_orders.add_orders(correspondent_id="01HPMZZM6RKMVZA1JQ63RQKJRP", basket_id="fffd326-72fa-4d2b-bd1f-45384fe5d521", add_orders_request_create={
    "basket_orders": [
        {
            "account_id": "01HBRQ5BW6ZAY4BNWP4GWRD80X",
            "asset_type": components.BasketOrderCreateAssetType.EQUITY,
            "client_order_id": "a6d5258b-6b23-478a-8145-98e79d60427a",
            "identifier": "SBUX",
            "identifier_type": components.BasketOrderCreateIdentifierType.SYMBOL,
            "order_type": components.BasketOrderCreateOrderType.MARKET,
            "side": components.BasketOrderCreateSide.BUY,
            "time_in_force": components.BasketOrderCreateTimeInForce.DAY,
        },
        {
            "account_id": "01HBRQ5BW6ZAY4BNWP4GWRD80X",
            "asset_type": components.BasketOrderCreateAssetType.EQUITY,
            "client_order_id": "a6d5258b-6b23-478a-8145-98e79d60427a",
            "identifier": "SBUX",
            "identifier_type": components.BasketOrderCreateIdentifierType.SYMBOL,
            "order_type": components.BasketOrderCreateOrderType.MARKET,
            "side": components.BasketOrderCreateSide.BUY,
            "time_in_force": components.BasketOrderCreateTimeInForce.DAY,
        },
    ],
    "name": "correspondents/01HPMZZM6RKMVZA1JQ63RQKJRP/baskets/fffd326-72fa-4d2b-bd1f-45384fe5d521",
})

if res.basket is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `correspondent_id`                                                                     | *str*                                                                                  | :heavy_check_mark:                                                                     | The correspondent id.                                                                  | 01HPMZZM6RKMVZA1JQ63RQKJRP                                                             |
| `basket_id`                                                                            | *str*                                                                                  | :heavy_check_mark:                                                                     | The basket id.                                                                         | fffd326-72fa-4d2b-bd1f-45384fe5d521                                                    |
| `add_orders_request_create`                                                            | [components.AddOrdersRequestCreate](../../models/components/addordersrequestcreate.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |                                                                                        |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[operations.BasketOrdersServiceAddOrdersResponse](../../models/operations/basketordersserviceaddordersresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.Status                     | 400, 401, 403, 404, 409, 500, 503 | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## get_basket

Gets a basket by basket ID.

 Upon successful submission, returns the details of the queried basket

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

res = s.basket_orders.get_basket(correspondent_id="01HPMZZM6RKMVZA1JQ63RQKJRP", basket_id="fffd326-72fa-4d2b-bd1f-45384fe5d521")

if res.basket is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `correspondent_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The correspondent id.                                               | 01HPMZZM6RKMVZA1JQ63RQKJRP                                          |
| `basket_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The basket id.                                                      | fffd326-72fa-4d2b-bd1f-45384fe5d521                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.BasketOrdersServiceGetBasketResponse](../../models/operations/basketordersservicegetbasketresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.Status                | 400, 401, 403, 404, 500, 503 | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## submit_basket

Submits a basket for execution in the market

 Upon successful submission, if the request is a duplicate, returns the existing basket in its current state in the system. If the request is not a duplicate, returns the summary of the newly submitted basket in a SUBMITTED state

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

res = s.basket_orders.submit_basket(correspondent_id="01HPMZZM6RKMVZA1JQ63RQKJRP", basket_id="fffd326-72fa-4d2b-bd1f-45384fe5d521", submit_basket_request_create={
    "name": "correspondents/01HPMZZM6RKMVZA1JQ63RQKJRP/baskets/fffd326-72fa-4d2b-bd1f-45384fe5d521",
})

if res.basket is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `correspondent_id`                                                                           | *str*                                                                                        | :heavy_check_mark:                                                                           | The correspondent id.                                                                        | 01HPMZZM6RKMVZA1JQ63RQKJRP                                                                   |
| `basket_id`                                                                                  | *str*                                                                                        | :heavy_check_mark:                                                                           | The basket id.                                                                               | fffd326-72fa-4d2b-bd1f-45384fe5d521                                                          |
| `submit_basket_request_create`                                                               | [components.SubmitBasketRequestCreate](../../models/components/submitbasketrequestcreate.md) | :heavy_check_mark:                                                                           | N/A                                                                                          |                                                                                              |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |                                                                                              |

### Response

**[operations.BasketOrdersServiceSubmitBasketResponse](../../models/operations/basketordersservicesubmitbasketresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.Status                | 400, 401, 403, 404, 500, 503 | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list_basket_orders

Gets a list of basket orders within a basket.

 Upon successful submission, returns a list of basket orders for the basket. If the list of basket orders becomes too large, a token is returned to retrieve the next page of basket orders.

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

res = s.basket_orders.list_basket_orders(correspondent_id="01HPMZZM6RKMVZA1JQ63RQKJRP", basket_id="fffd326-72fa-4d2b-bd1f-45384fe5d521")

if res.list_basket_orders_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `correspondent_id`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                   | The correspondent id.                                                                                                                                                                                                                | 01HPMZZM6RKMVZA1JQ63RQKJRP                                                                                                                                                                                                           |
| `basket_id`                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                   | The basket id.                                                                                                                                                                                                                       | fffd326-72fa-4d2b-bd1f-45384fe5d521                                                                                                                                                                                                  |
| `page_size`                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                   | The maximum number of basket orders to return. The service may return fewer than this value. If unspecified, at most 1000 basket orders will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.      | 25                                                                                                                                                                                                                                   |
| `page_token`                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                   | A page token, received from a previous `ListBasketOrders` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListBasketOrders` must match the call that provided the page token. | AbTYnwAkMjIyZDNjYTAtZmVjZS00N2Q5LTgyMDctNzI3MDdkMjFiZj3h                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                  |                                                                                                                                                                                                                                      |

### Response

**[operations.BasketOrdersServiceListBasketOrdersResponse](../../models/operations/basketordersservicelistbasketordersresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.Status                | 400, 401, 403, 404, 500, 503 | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list_compressed_orders

Gets a list of compressed orders within a basket.

 Upon successful submission, returns a list of compressed orders for the basket. If the basket has not been submitted yet, this list will be empty. If the list of compressed orders becomes too large, a token is returned to retrieve the next page of compressed orders.

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

res = s.basket_orders.list_compressed_orders(correspondent_id="01HPMZZM6RKMVZA1JQ63RQKJRP", basket_id="fffd326-72fa-4d2b-bd1f-45384fe5d521")

if res.list_compressed_orders_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `correspondent_id`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | The correspondent id.                                                                                                                                                                                                                        | 01HPMZZM6RKMVZA1JQ63RQKJRP                                                                                                                                                                                                                   |
| `basket_id`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                           | The basket id.                                                                                                                                                                                                                               | fffd326-72fa-4d2b-bd1f-45384fe5d521                                                                                                                                                                                                          |
| `page_size`                                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | The maximum number of compressed orders to return. The service may return fewer than this value. If unspecified, at most 1000 compressed orders will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.      | 25                                                                                                                                                                                                                                           |
| `page_token`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                           | A page token, received from a previous `ListCompressedOrders` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListCompressedOrders` must match the call that provided the page token. | AbTYnwAkMjIyZDNjYTAtZmVjZS00N2Q5LTgyMDctNzI3MDdkMjFiZj3h                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                          |                                                                                                                                                                                                                                              |

### Response

**[operations.BasketOrdersServiceListCompressedOrdersResponse](../../models/operations/basketordersservicelistcompressedordersresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.Status                | 400, 401, 403, 404, 500, 503 | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |