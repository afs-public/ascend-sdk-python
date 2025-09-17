# Ledger
(*ledger*)

## Overview

### Available Operations

* [list_entries](#list_entries) - List Entries
* [list_activities](#list_activities) - List Activities
* [list_positions](#list_positions) - List Positions
* [get_activity](#get_activity) - Get Activity
* [get_entry](#get_entry) - Get Entry

## list_entries

List all Entries based on a filter

### Example Usage

<!-- UsageSnippet language="python" operationID="Ledger_ListEntries" method="get" path="/ledger/v1/accounts/{account_id}/entries" -->
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

    res = sdk.ledger.list_entries(account_id="01FAKEACCOUNT1TYKWEYRH8S2K", page_size=0, page_token="v-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAOv-CAfzbNG7ZAS8xZWYyMmM3ZS01NjdmLTBhYzgtYjZmZi1kNzYwNDI3YmI3N2Q6MjAyNC0wNi0wMgA=", filter_="process_date == date('2024-05-11') && account_id == '01HBRQ5BW6ZAY4BNWP4GWRD80X'")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                | The account id.                                                                                                                                                                                                                                                   | 01FAKEACCOUNT1TYKWEYRH8S2K                                                                                                                                                                                                                                        |
| `page_size`                                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | The maximum number of entries to return. The service may return fewer than this value Default is 100 (subject to change) The maximum is 1000, values exceeding this will be set to 1000 (subject to change)                                                       | 0                                                                                                                                                                                                                                                                 |
| `page_token`                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | A page token, received from a previous `ListEntries` call. Provide this to retrieve the subsequent page When paginating, all other parameters provided to `ListEntries` must match the call that provided the page token in order to maintain a stable result set | v-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAOv-CAfzbNG7ZAS8xZWYyMmM3ZS01NjdmLTBhYzgtYjZmZi1kNzYwNDI3YmI3N2Q6MjAyNC0wNi0wMgA=                                                                                                               |
| `filter_`                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information;                                                                                              | process_date == date('2024-05-11') && account_id == '01HBRQ5BW6ZAY4BNWP4GWRD80X'                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                               |                                                                                                                                                                                                                                                                   |

### Response

**[operations.LedgerListEntriesResponse](../../models/operations/ledgerlistentriesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_activities

List all Completed Activities based on a filter

### Example Usage

<!-- UsageSnippet language="python" operationID="Ledger_ListActivities" method="get" path="/ledger/v1/accounts/{account_id}/activities" -->
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

    res = sdk.ledger.list_activities(account_id="01FAKEACCOUNT1TYKWEYRH8S2K", page_size=100, page_token="Mv-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAI_-CAfwVsHF9ARgyMDI0LTA2LTA0OjFGQTA1MDExOjUwMDEA", filter_="subtype_category == 'TRADE' && process_date >= date('2023-07-31') && settle_date >= date('2023-08-18') && side == 'BUY' &&  activity_date >= date('2023-09-15') && asset_id == 8395")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                  | The account id.                                                                                                                                                                                                                                                     | 01FAKEACCOUNT1TYKWEYRH8S2K                                                                                                                                                                                                                                          |
| `page_size`                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                  | The maximum number of activities to return. The service may return fewer than this value Default is 100 (subject to change) The maximum is 1000, values exceeding this will be set to 1000 (subject to change)                                                      | 100                                                                                                                                                                                                                                                                 |
| `page_token`                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                  | A page token, received from a previous `ListActivity` call. Provide this to retrieve the subsequent page When paginating, all other parameters provided to `ListActivity` must match the call that provided the page token in order to maintain a stable result set | Mv-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAI_-CAfwVsHF9ARgyMDI0LTA2LTA0OjFGQTA1MDExOjUwMDEA                                                                                                                                                |
| `filter_`                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                  | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information;                                                                                                | subtype_category == 'TRADE' && process_date >= date('2023-07-31') && settle_date >= date('2023-08-18') && side == 'BUY' &&  activity_date >= date('2023-09-15') && asset_id == 8395                                                                                 |
| `retries`                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                     |

### Response

**[operations.LedgerListActivitiesResponse](../../models/operations/ledgerlistactivitiesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_positions

List positions based on a filter

### Example Usage

<!-- UsageSnippet language="python" operationID="Ledger_ListPositions" method="get" path="/ledger/v1/accounts/{account_id}/positions" -->
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

    res = sdk.ledger.list_positions(account_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", page_size=20, page_token="Mv-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAOv-CAfwFIZG3AS8xZWYyMmM4Ny0zNDI5LTAyYzItODRjNC03ODdmNTJlNDY1MTE6MjAyNC0wNi0wMgA=", filter_="date >= date('2023-08-31') && asset_id == 8395")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                   | The account id.                                                                                                                                                                                                                                                      | 01HBRQ5BW6ZAY4BNWP4GWRD80X                                                                                                                                                                                                                                           |
| `page_size`                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                   | The maximum number of positions to return. The service may return fewer than this value Default is 100 (subject to change) The maximum is 1000, values exceeding this will be set to 1000 (subject to change)                                                        | 20                                                                                                                                                                                                                                                                   |
| `page_token`                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                   | This page token comes from a previous `ListPositions` call; provide this token to retrieve the subsequent page When paginating, all other parameters you include in `ListPositions` must match the call that includes the page token to maintain a stable result set | Mv-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAOv-CAfwFIZG3AS8xZWYyMmM4Ny0zNDI5LTAyYzItODRjNC03ODdmNTJlNDY1MTE6MjAyNC0wNi0wMgA=                                                                                                                 |
| `filter_`                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                   | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information;                                                                                                 | date >= date('2023-08-31') && asset_id == 8395                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                      |

### Response

**[operations.LedgerListPositionsResponse](../../models/operations/ledgerlistpositionsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_activity

Get an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="Ledger_GetActivity" method="get" path="/ledger/v1/accounts/{account_id}/activities/{activity_id}" -->
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

    res = sdk.ledger.get_activity(account_id="01FAKEACCOUNT1TYKWEYRH8S2K", activity_id="FAKEACTIVITYID")

    assert res.activity is not None

    # Handle response
    print(res.activity)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01FAKEACCOUNT1TYKWEYRH8S2K                                          |
| `activity_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The activity id.                                                    | FAKEACTIVITYID                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.LedgerGetActivityResponse](../../models/operations/ledgergetactivityresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_entry

Get an entry

### Example Usage

<!-- UsageSnippet language="python" operationID="Ledger_GetEntry" method="get" path="/ledger/v1/accounts/{account_id}/entries/{entry_id}" -->
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

    res = sdk.ledger.get_entry(account_id="[object Object]", entry_id="[object Object]")

    assert res.entry is not None

    # Handle response
    print(res.entry)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | {<br/>"account_id": ""<br/>}                                        |
| `entry_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The entry id.                                                       | {<br/>"entry_id": ""<br/>}                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.LedgerGetEntryResponse](../../models/operations/ledgergetentryresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |