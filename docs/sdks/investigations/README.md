# Investigations
(*investigations*)

## Overview

### Available Operations

* [get_investigation](#get_investigation) - Get Investigations
* [update_investigation](#update_investigation) - Update Investigation 
* [list_investigations](#list_investigations) - List Investigations
* [link_documents](#link_documents) - Link Documents
* [get_watchlist_item](#get_watchlist_item) - Get Watchlist Item
* [get_customer_identification](#get_customer_identification) - Get Identity Verification

## get_investigation

Use this endpoint to get the current state of an investigation by request reference UUID.

### Example Usage

<!-- UsageSnippet language="python" operationID="InvestigationService_GetInvestigation" method="get" path="/investigations/v1/investigations/{investigation_id}" -->
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

    res = sdk.investigations.get_investigation(investigation_id="01HEWVF4ZSNKYRP293J53ASJCJ")

    assert res.investigation is not None

    # Handle response
    print(res.investigation)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `investigation_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The investigation id.                                               | 01HEWVF4ZSNKYRP293J53ASJCJ                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.InvestigationServiceGetInvestigationResponse](../../models/operations/investigationservicegetinvestigationresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## update_investigation

Use this endpoint to update the details of an investigation by request reference UUID.

### Example Usage

<!-- UsageSnippet language="python" operationID="InvestigationService_UpdateInvestigation" method="patch" path="/investigations/v1/investigations/{investigation_id}" -->
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

    res = sdk.investigations.update_investigation(investigation_id="01HEWVF4ZSNKYRP293J53ASJCJ", investigation_update={}, update_mask="[object Object]")

    assert res.investigation is not None

    # Handle response
    print(res.investigation)

```

### Parameters

| Parameter                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `investigation_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                | The investigation id.                                                                                                                                                                                                             | 01HEWVF4ZSNKYRP293J53ASJCJ                                                                                                                                                                                                        |
| `investigation_update`                                                                                                                                                                                                            | [components.InvestigationUpdate](../../models/components/investigationupdate.md)                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `update_mask`                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                | The list of fields to update. Updatable Fields:<br/>  - identity_verification<br/>  - investigation_request_state<br/>  - watchlist_matches<br/>   - watchlist_id<br/>   - watchlist_item_id<br/>   - match_state<br/>   - exclude_from_screening<br/>  - comment | {<br/>"update_mask": "identity_verification"<br/>}                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                               |                                                                                                                                                                                                                                   |

### Response

**[operations.InvestigationServiceUpdateInvestigationResponse](../../models/operations/investigationserviceupdateinvestigationresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_investigations

Use this endpoint to retrieve a list of investigation summaries based on optional search parameters

### Example Usage

<!-- UsageSnippet language="python" operationID="InvestigationService_ListInvestigations" method="get" path="/investigations/v1/investigations" -->
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

    res = sdk.investigations.list_investigations(page_size=100, page_token="", filter_="person.given_name == 'Jane' && person.family_name == 'Dough'", order_by="person.given_name desc")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                          | The maximum number of records to return. Default is 50 The maximum is 200, values exceeding this will be set to 200                                                                                                                                                                                                                                                                         | 100                                                                                                                                                                                                                                                                                                                                                                                         |
| `page_token`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                          | The page token used to request a specific page of the search results                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                             |
| `filter_`                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                          | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:<br/> ListInvestigationStatesResponse.investigation_states                                                                                                                                      | person.given_name == 'Jane' && person.family_name == 'Dough'                                                                                                                                                                                                                                                                                                                                |
| `order_by`                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                          | The order in which investigations are listed. Only one field and direction can be specified. Supported fields (followed by 'asc' or 'desc'; 'asc' is default if left blank):<br/>  - investigation_request_state<br/>  - correspondent_id<br/>  - scope<br/>  - identity_verification<br/>  - watchlist_screen<br/>  - person.given_name<br/>  - person.family_name<br/>  - entity.legal_name<br/>  - created_at<br/>  - updated_at | person.given_name desc                                                                                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                             |

### Response

**[operations.InvestigationServiceListInvestigationsResponse](../../models/operations/investigationservicelistinvestigationsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## link_documents

Use this endpoint to update identity verification document IDs.

### Example Usage

<!-- UsageSnippet language="python" operationID="InvestigationService_LinkDocuments" method="post" path="/investigations/v1/investigations/{investigation_id}:linkDocuments" -->
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

    res = sdk.investigations.link_documents(investigation_id="01HEWVF4ZSNKYRP293J53ASJCJ", link_documents_request_create={
        "identity_verification_document_ids": [
            "0f01ae1f-d24c-4171-8f3f-c0b820bf3044",
        ],
    })

    assert res.link_documents_response is not None

    # Handle response
    print(res.link_documents_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    | Example                                                                                        |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `investigation_id`                                                                             | *str*                                                                                          | :heavy_check_mark:                                                                             | The investigation id.                                                                          | 01HEWVF4ZSNKYRP293J53ASJCJ                                                                     |
| `link_documents_request_create`                                                                | [components.LinkDocumentsRequestCreate](../../models/components/linkdocumentsrequestcreate.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |                                                                                                |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |                                                                                                |

### Response

**[operations.InvestigationServiceLinkDocumentsResponse](../../models/operations/investigationservicelinkdocumentsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_watchlist_item

Gets the details of an investigation by watchlist type and valid watchlist id

### Example Usage

<!-- UsageSnippet language="python" operationID="WatchlistService_GetWatchlistItem" method="get" path="/investigations/v1/watchlists/{watchlist_id}/items/{item_id}" -->
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

    res = sdk.investigations.get_watchlist_item(watchlist_id="DOWJONES", item_id="123456")

    assert res.watchlist_item is not None

    # Handle response
    print(res.watchlist_item)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `watchlist_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The watchlist id.                                                   | DOWJONES                                                            |
| `item_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The item id.                                                        | 123456                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.WatchlistServiceGetWatchlistItemResponse](../../models/operations/watchlistservicegetwatchlistitemresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_customer_identification

Gets a CustomerIdentification by CustomerIdentification ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="CustomerIdentificationResultService_GetCustomerIdentification" method="get" path="/cip/v1/correspondents/{correspondent_id}/customerIdentifications/{customerIdentification_id}" -->
```python
from ascend_sdk import SDK
from ascend_sdk.models import components, operations


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

    res = sdk.investigations.get_customer_identification(correspondent_id="01HPMZZM6RKMVZA1JQ63RQKJRP", customer_identification_id="01HEWVF4ZSNKYRP293J53ASJCJ", view=operations.CustomerIdentificationResultServiceGetCustomerIdentificationQueryParamView.BASIC)

    assert res.customer_identification is not None

    # Handle response
    print(res.customer_identification)

```

### Parameters

| Parameter                                                                                                                                                                                                | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              | Example                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `correspondent_id`                                                                                                                                                                                       | *str*                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                       | The correspondent id.                                                                                                                                                                                    | 01HPMZZM6RKMVZA1JQ63RQKJRP                                                                                                                                                                               |
| `customer_identification_id`                                                                                                                                                                             | *str*                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                       | The customerIdentification id.                                                                                                                                                                           | 01HEWVF4ZSNKYRP293J53ASJCJ                                                                                                                                                                               |
| `view`                                                                                                                                                                                                   | [Optional[operations.CustomerIdentificationResultServiceGetCustomerIdentificationQueryParamView]](../../models/operations/customeridentificationresultservicegetcustomeridentificationqueryparamview.md) | :heavy_minus_sign:                                                                                                                                                                                       | Optional. The view to return. Defaults to BASIC.                                                                                                                                                         | BASIC                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                      |                                                                                                                                                                                                          |

### Response

**[operations.CustomerIdentificationResultServiceGetCustomerIdentificationResponse](../../models/operations/customeridentificationresultservicegetcustomeridentificationresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |