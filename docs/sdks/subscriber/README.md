# Subscriber
(*subscriber*)

## Overview

### Available Operations

* [create_push_subscription](#create_push_subscription) - Create Push Subscription
* [list_push_subscriptions](#list_push_subscriptions) - List Push Subscriptions
* [get_push_subscription](#get_push_subscription) - Get Push Subscription
* [update_push_subscription](#update_push_subscription) - Update Subscription
* [delete_push_subscription](#delete_push_subscription) - Delete Subscription
* [get_push_subscription_delivery](#get_push_subscription_delivery) - Get Subscription Event Delivery
* [list_push_subscription_deliveries](#list_push_subscription_deliveries) - List Push Subscription Event Deliveries

## create_push_subscription

Creates a new push subscription for event notifications.

### Example Usage

<!-- UsageSnippet language="python" operationID="Subscriber_CreatePushSubscription" method="post" path="/events/v1/subscriptions" -->
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

    res = sdk.subscriber.create_push_subscription(request={
        "display_name": "This is an example HTTP configuration.",
        "event_types": [
            "position.v1.updated",
        ],
    })

    assert res.push_subscription is not None

    # Handle response
    print(res.push_subscription)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.PushSubscriptionCreate](../../models/components/pushsubscriptioncreate.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.SubscriberCreatePushSubscriptionResponse](../../models/operations/subscribercreatepushsubscriptionresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 409 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## list_push_subscriptions

Gets a list of push subscriptions.

### Example Usage

<!-- UsageSnippet language="python" operationID="Subscriber_ListPushSubscriptions" method="get" path="/events/v1/subscriptions" -->
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

    res = sdk.subscriber.list_push_subscriptions(filter_="correspondent_id==\"01H8MCDXH4HYJJAV921BDKCC83\"", page_size=50, page_token="ZXhhbXBsZQo")

    assert res.list_push_subscriptions_response is not None

    # Handle response
    print(res.list_push_subscriptions_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `filter_`                                                                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                   | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; If empty, all subscriptions the user has permission to view will be returned; Filter options include:<br/> `name`<br/> `subscription_id`<br/> `client_id`<br/> `correspondent_id`<br/> `display_name`<br/> `event_types`<br/> `state`<br/> `http_callback.url`<br/> `http_callback.timeout_seconds` | correspondent_id=="01H8MCDXH4HYJJAV921BDKCC83"                                                                                                                                                                                                                                                                                                                                                                                       |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                   | The number of entries to return in a single page; Default = 100; Maximum = 1000                                                                                                                                                                                                                                                                                                                                                      | 50                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `page_token`                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                   | Page token used for pagination; Supplying a page token returns the next page of results                                                                                                                                                                                                                                                                                                                                              | ZXhhbXBsZQo                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Response

**[operations.SubscriberListPushSubscriptionsResponse](../../models/operations/subscriberlistpushsubscriptionsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_push_subscription

Gets the details of a specific push subscription.

### Example Usage

<!-- UsageSnippet language="python" operationID="Subscriber_GetPushSubscription" method="get" path="/events/v1/subscriptions/{subscription_id}" -->
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

    res = sdk.subscriber.get_push_subscription(subscription_id="01H8MCDXH4JVH7KVNB2YY42907")

    assert res.push_subscription is not None

    # Handle response
    print(res.push_subscription)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscription_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The subscription id.                                                | 01H8MCDXH4JVH7KVNB2YY42907                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.SubscriberGetPushSubscriptionResponse](../../models/operations/subscribergetpushsubscriptionresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## update_push_subscription

Updates the details of a push subscription.

### Example Usage

<!-- UsageSnippet language="python" operationID="Subscriber_UpdatePushSubscription" method="patch" path="/events/v1/subscriptions/{subscription_id}" -->
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

    res = sdk.subscriber.update_push_subscription(subscription_id="01H8MCDXH4JVH7KVNB2YY42907", push_subscription_update={})

    assert res.push_subscription is not None

    # Handle response
    print(res.push_subscription)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `subscription_id`                                                                      | *str*                                                                                  | :heavy_check_mark:                                                                     | The subscription id.                                                                   | 01H8MCDXH4JVH7KVNB2YY42907                                                             |
| `push_subscription_update`                                                             | [components.PushSubscriptionUpdate](../../models/components/pushsubscriptionupdate.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |                                                                                        |
| `update_mask`                                                                          | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The fields to update in subscription                                                   |                                                                                        |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[operations.SubscriberUpdatePushSubscriptionResponse](../../models/operations/subscriberupdatepushsubscriptionresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## delete_push_subscription

Stops receiving events from a push subscription, and then deletes it.

### Example Usage

<!-- UsageSnippet language="python" operationID="Subscriber_DeletePushSubscription" method="delete" path="/events/v1/subscriptions/{subscription_id}" -->
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

    res = sdk.subscriber.delete_push_subscription(subscription_id="01H8MCDXH4JVH7KVNB2YY42907")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscription_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The subscription id.                                                | 01H8MCDXH4JVH7KVNB2YY42907                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.SubscriberDeletePushSubscriptionResponse](../../models/operations/subscriberdeletepushsubscriptionresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_push_subscription_delivery

Gets the details of a specific push subscription delivery.

### Example Usage

<!-- UsageSnippet language="python" operationID="Subscriber_GetPushSubscriptionDelivery" method="get" path="/events/v1/subscriptions/{subscription_id}/deliveries/{delivery_id}" -->
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

    res = sdk.subscriber.get_push_subscription_delivery(subscription_id="01H8MCDXH4JVH7KVNB2YY42907", delivery_id="01H8MCDXH415BJ962YDN4B02JK")

    assert res.push_subscription_delivery is not None

    # Handle response
    print(res.push_subscription_delivery)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscription_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The subscription id.                                                | 01H8MCDXH4JVH7KVNB2YY42907                                          |
| `delivery_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The delivery id.                                                    | 01H8MCDXH415BJ962YDN4B02JK                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.SubscriberGetPushSubscriptionDeliveryResponse](../../models/operations/subscribergetpushsubscriptiondeliveryresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## list_push_subscription_deliveries

Gets a list of a push subscription's event deliveries.

### Example Usage

<!-- UsageSnippet language="python" operationID="Subscriber_ListPushSubscriptionDeliveries" method="get" path="/events/v1/subscriptions/{subscription_id}/deliveries" -->
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

    res = sdk.subscriber.list_push_subscription_deliveries(subscription_id="01H8MCDXH4JVH7KVNB2YY42907", filter_="event_publish_time==timestamp(\"2023-06-13T23:48:58.343Z\")", page_size=50, page_token="ZXhhbXBsZQo")

    assert res.list_push_subscription_deliveries_response is not None

    # Handle response
    print(res.list_push_subscription_deliveries_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subscription_id`                                                                                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                      | The subscription id.                                                                                                                                                                                                                                                                                                                                                                    | 01H8MCDXH4JVH7KVNB2YY42907                                                                                                                                                                                                                                                                                                                                                              |
| `filter_`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                      | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; If left empty, all deliveries the user has permission to view are returned; Filter options include:<br/> `name`<br/> `delivery_id`<br/> `event`<br/> `event_publish_time`<br/> `result`<br/> `last_response`<br/> `last_send_time`<br/> `duration` | event_publish_time==timestamp("2023-06-13T23:48:58.343Z")                                                                                                                                                                                                                                                                                                                               |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                      | The number of entries to return in a single page; Default = 100; Maximum = 1000                                                                                                                                                                                                                                                                                                         | 50                                                                                                                                                                                                                                                                                                                                                                                      |
| `page_token`                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                      | Page token used for pagination; Supplying a page token returns the next page of results                                                                                                                                                                                                                                                                                                 | ZXhhbXBsZQo                                                                                                                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                         |

### Response

**[operations.SubscriberListPushSubscriptionDeliveriesResponse](../../models/operations/subscriberlistpushsubscriptiondeliveriesresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |