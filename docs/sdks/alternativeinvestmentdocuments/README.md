# AlternativeInvestmentDocuments
(*alternative_investment_documents*)

## Overview

### Available Operations

* [list_alternative_investment_documents](#list_alternative_investment_documents) - List Alternative Investment Documents
* [get_alternative_investment_document](#get_alternative_investment_document) - Get Alternative Investment Document
* [download_alternative_investment_document](#download_alternative_investment_document) - Download Alternative Investment Documents

## list_alternative_investment_documents

Retrieves a list of all investment document details for the specified asset.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlternativeInvestmentDocuments_ListAlternativeInvestmentDocuments" method="get" path="/trading/v1/assets/{asset_id}/alternativeInvestmentDocuments" -->
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

    res = sdk.alternative_investment_documents.list_alternative_investment_documents(asset_id="123", page_size=10, page_token="next-page-token-example", filter_="type == 'OFFERING_DOCUMENT'")

    assert res.list_alternative_investment_documents_response is not None

    # Handle response
    print(res.list_alternative_investment_documents_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                           | Example                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_id`                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                    | The asset id.                                                                                                                                                                                                                                                                         | 123                                                                                                                                                                                                                                                                                   |
| `page_size`                                                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | The maximum number of orders to return. - Max value = 100  - Values above 100 will be coerced to 100.  - If the specified value is greater than the number of orders, the service will return fewer than the specified value.  - If unspecified, at most 100 orders will be returned. | 10                                                                                                                                                                                                                                                                                    |
| `page_token`                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | For pagination, provide the page token, received from a previous `ListInvestmentDocuments` call, to retrieve the subsequent page.  All other parameters provided to `ListInvestmentDocuments` must match the request that provided the page token.                                    | next-page-token-example                                                                                                                                                                                                                                                               |
| `filter_`                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | A CEL string to filter results. All fields from the response can be used as filters.<br/><br/> See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) guide for syntax details and examples.                                                 | type == 'OFFERING_DOCUMENT'                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                       |

### Response

**[operations.AlternativeInvestmentDocumentsListAlternativeInvestmentDocumentsResponse](../../models/operations/alternativeinvestmentdocumentslistalternativeinvestmentdocumentsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_alternative_investment_document

Retrieves a specific investment document for the specified asset.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlternativeInvestmentDocuments_GetAlternativeInvestmentDocument" method="get" path="/trading/v1/assets/{asset_id}/alternativeInvestmentDocuments/{alternativeInvestmentDocument_id}" -->
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

    res = sdk.alternative_investment_documents.get_alternative_investment_document(asset_id="123", alternative_investment_document_id="01H7YH8QKZJ8V4Q2X8F4G6JQ2B")

    assert res.alternative_investment_document is not None

    # Handle response
    print(res.alternative_investment_document)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The asset id.                                                       | 123                                                                 |
| `alternative_investment_document_id`                                | *str*                                                               | :heavy_check_mark:                                                  | The alternativeInvestmentDocument id.                               | 01H7YH8QKZJ8V4Q2X8F4G6JQ2B                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AlternativeInvestmentDocumentsGetAlternativeInvestmentDocumentResponse](../../models/operations/alternativeinvestmentdocumentsgetalternativeinvestmentdocumentresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## download_alternative_investment_document

Returns a URI to download the specified investment document.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlternativeInvestmentDocuments_DownloadAlternativeInvestmentDocument" method="get" path="/trading/v1/assets/{asset_id}/alternativeInvestmentDocuments/{alternativeInvestmentDocument_id}:download" -->
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

    res = sdk.alternative_investment_documents.download_alternative_investment_document(asset_id="123", alternative_investment_document_id="01H7YH8QKZJ8V4Q2X8F4G6JQ2B")

    assert res.download_alternative_investment_document_response is not None

    # Handle response
    print(res.download_alternative_investment_document_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The asset id.                                                       | 123                                                                 |
| `alternative_investment_document_id`                                | *str*                                                               | :heavy_check_mark:                                                  | The alternativeInvestmentDocument id.                               | 01H7YH8QKZJ8V4Q2X8F4G6JQ2B                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AlternativeInvestmentDocumentsDownloadAlternativeInvestmentDocumentResponse](../../models/operations/alternativeinvestmentdocumentsdownloadalternativeinvestmentdocumentresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |