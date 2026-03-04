# PreIPOResearchDocuments
(*pre_ipo_research_documents*)

## Overview

### Available Operations

* [list_pre_ipo_company_research_documents](#list_pre_ipo_company_research_documents) - List Pre IPO Company Research Documents

## list_pre_ipo_company_research_documents

Lists Pre IPO Company Research Documents.

### Example Usage

<!-- UsageSnippet language="python" operationID="PreIpoCompanyResearchDocuments_ListPreIpoCompanyResearchDocuments" method="get" path="/trading/v1/preIpoCompanies/{preIpoCompany_id}/researchDocuments" -->
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

    res = sdk.pre_ipo_research_documents.list_pre_ipo_company_research_documents(pre_ipo_company_id="3fa85f64-5717-4562-b3fc-2c963f66afa6", page_size=50, page_token="eyJzaXplIjoxMCwib2Zmc2V0IjoxMDAsInBhcmVudElkIjoicGFyZW50SWQifQ==", filter_="type == 'MARKET' && relation == 'SUBJECT'")

    assert res.list_pre_ipo_company_research_documents_response is not None

    # Handle response
    print(res.list_pre_ipo_company_research_documents_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pre_ipo_company_id`                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                     | The preIpoCompany id.                                                                                                                                                                                                                                                                  | 3fa85f64-5717-4562-b3fc-2c963f66afa6                                                                                                                                                                                                                                                   |
| `page_size`                                                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | The maximum number of Pre IPO Company Research Documents to return. The service may return fewer than this value. If unspecified, at most 100 Pre IPO Company Research Documents will be returned. The maximum value is 100; values above 100 will be coerced to 100.                  | 50                                                                                                                                                                                                                                                                                     |
| `page_token`                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | A page token, received from a previous `ListPreIpoCompanyResearchDocumentsRequest` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListPreIpoCompanyResearchDocumentsRequest` must match the call that provided the page token. | eyJzaXplIjoxMCwib2Zmc2V0IjoxMDAsInBhcmVudElkIjoicGFyZW50SWQifQ==                                                                                                                                                                                                                       |
| `filter_`                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | A CEL string to filter results. Filterable fields:<br/> - type<br/> - relation<br/> Only `&&` and `==` operators are allowed.<br/> See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search)<br/> page in Guides for more information;           | type == 'MARKET' && relation == 'SUBJECT'                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                        |

### Response

**[operations.PreIpoCompanyResearchDocumentsListPreIpoCompanyResearchDocumentsResponse](../../models/operations/preipocompanyresearchdocumentslistpreipocompanyresearchdocumentsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |