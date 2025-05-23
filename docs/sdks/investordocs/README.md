# InvestorDocs
(*investor_docs*)

## Overview

### Available Operations

* [batch_create_upload_links](#batch_create_upload_links) - Batch Create Upload Links
* [list_documents](#list_documents) - List Documents

## batch_create_upload_links

Create a batch of signed links that can be used to upload files.

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

res = s.investor_docs.batch_create_upload_links(request={})

if res.batch_create_upload_links_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [components.BatchCreateUploadLinksRequestCreate](../../models/components/batchcreateuploadlinksrequestcreate.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.InvestorCommunicationServiceBatchCreateUploadLinksResponse](../../models/operations/investorcommunicationservicebatchcreateuploadlinksresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 500 | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## list_documents

List documents that match search parameters.

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

res = s.investor_docs.list_documents()

if res.list_documents_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_size`                                                                                                                                           | *Optional[int]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | The maximum number of items to return; The service may return fewer than this value                                                                   |
| `page_token`                                                                                                                                          | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Token used to get a specific page of results                                                                                                          |
| `filter_`                                                                                                                                             | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | CEL filter to be applied against the documents; Providing a correspondent to search for is required; Only one correspondent can be searched at a time |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[operations.InvestorCommunicationServiceListDocumentsResponse](../../models/operations/investorcommunicationservicelistdocumentsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 500 | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |