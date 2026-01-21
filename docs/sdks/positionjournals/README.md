# PositionJournals
(*position_journals*)

## Overview

### Available Operations

* [create_position_journal](#create_position_journal) - Create Position Journal
* [get_position_journal](#get_position_journal) - Get Position Journal
* [cancel_position_journal](#cancel_position_journal) - Cancel Position Journal

## create_position_journal

Creates a position journal

### Example Usage

<!-- UsageSnippet language="python" operationID="PositionJournals_CreatePositionJournal" method="post" path="/transfers/v1/positionJournals" -->
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

    res = sdk.position_journals.create_position_journal(request=components.PositionJournalCreate(
        client_transfer_id="113bw03-49f8-4525-934c-560fb39dg2kd",
        destination_account="accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y",
        identifier="AAPL",
        identifier_type=components.IdentifierType.SYMBOL,
        quantity=components.DecimalCreate(),
        source_account="accounts/01H8FM6EXVH77SAW3TC8KAWMES",
        type=components.PositionJournalCreateType.REWARD,
    ))

    assert res.position_journal is not None

    # Handle response
    print(res.position_journal)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.PositionJournalCreate](../../models/components/positionjournalcreate.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PositionJournalsCreatePositionJournalResponse](../../models/operations/positionjournalscreatepositionjournalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_position_journal

Gets an existing position journal

### Example Usage

<!-- UsageSnippet language="python" operationID="PositionJournals_GetPositionJournal" method="get" path="/transfers/v1/positionJournals/{positionJournal_id}" -->
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

    res = sdk.position_journals.get_position_journal(position_journal_id="20230817000319")

    assert res.position_journal is not None

    # Handle response
    print(res.position_journal)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `position_journal_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The positionJournal id.                                             | 20230817000319                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.PositionJournalsGetPositionJournalResponse](../../models/operations/positionjournalsgetpositionjournalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_position_journal

Cancels an existing position journal

### Example Usage

<!-- UsageSnippet language="python" operationID="PositionJournals_CancelPositionJournal" method="post" path="/transfers/v1/positionJournals/{positionJournal_id}:cancel" -->
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

    res = sdk.position_journals.cancel_position_journal(position_journal_id="20240717000319", cancel_position_journal_request_create={
        "name": "positionJournals/20240717000319",
    })

    assert res.position_journal is not None

    # Handle response
    print(res.position_journal)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `position_journal_id`                                                                                          | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The positionJournal id.                                                                                        | 20240717000319                                                                                                 |
| `cancel_position_journal_request_create`                                                                       | [components.CancelPositionJournalRequestCreate](../../models/components/cancelpositionjournalrequestcreate.md) | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |                                                                                                                |

### Response

**[operations.PositionJournalsCancelPositionJournalResponse](../../models/operations/positionjournalscancelpositionjournalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |