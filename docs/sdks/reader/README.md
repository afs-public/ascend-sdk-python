# Reader
(*reader*)

## Overview

### Available Operations

* [list_event_messages](#list_event_messages) - List Event Messages
* [get_event_message](#get_event_message) - Get Event Message

## list_event_messages

Gets a list of events.

### Example Usage

<!-- UsageSnippet language="python" operationID="Reader_ListEventMessages" method="get" path="/events/v1/messages" -->
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

    res = sdk.reader.list_event_messages(filter_="publish_time==timestamp(\"2023-06-13T23:48:58.343Z\")", page_size=50, page_token="ZXhhbXBsZQo")

    assert res.list_event_messages_response is not None

    # Handle response
    print(res.list_event_messages_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; If left empty, all events the user has permission to view are returned; Filter options include:<br/> `name`<br/> `message_id`<br/> `event_type`<br/> `publish_time`<br/> `partition_key`<br/> `client_id`<br/> `correspondent_id`<br/> `account_id` | publish_time==timestamp("2023-06-13T23:48:58.343Z")                                                                                                                                                                                                                                                                                                                                      |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | The number of entries to return in a single page; Default = 100; Maximum = 1000                                                                                                                                                                                                                                                                                                          | 50                                                                                                                                                                                                                                                                                                                                                                                       |
| `page_token`                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Page token used for pagination; Supplying a page token returns the next page of results                                                                                                                                                                                                                                                                                                  | ZXhhbXBsZQo                                                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                          |

### Response

**[operations.ReaderListEventMessagesResponse](../../models/operations/readerlisteventmessagesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_event_message

Gets the details of a specific event.

### Example Usage

<!-- UsageSnippet language="python" operationID="Reader_GetEventMessage" method="get" path="/events/v1/messages/{message_id}" -->
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

    res = sdk.reader.get_event_message(message_id="01H8MCDXH3ZXXMAA3918GRCFVE")

    assert res.event_message is not None

    # Handle response
    print(res.event_message)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `message_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The message id.                                                     | 01H8MCDXH3ZXXMAA3918GRCFVE                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ReaderGetEventMessageResponse](../../models/operations/readergeteventmessageresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |