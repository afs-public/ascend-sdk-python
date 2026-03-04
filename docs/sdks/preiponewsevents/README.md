# PreIPONewsEvents
(*pre_ipo_news_events*)

## Overview

### Available Operations

* [list_pre_ipo_company_news_events](#list_pre_ipo_company_news_events) - List Pre IPO Company News Events

## list_pre_ipo_company_news_events

Lists Pre IPO Company News Events.

### Example Usage

<!-- UsageSnippet language="python" operationID="PreIpoCompanyNewsEvents_ListPreIpoCompanyNewsEvents" method="get" path="/trading/v1/preIpoCompanies/{preIpoCompany_id}/newsEvents" -->
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

    res = sdk.pre_ipo_news_events.list_pre_ipo_company_news_events(pre_ipo_company_id="3fa85f64-5717-4562-b3fc-2c963f66afa6", page_size=50, page_token="eyJzaXplIjoxMCwib2Zmc2V0IjoxMDAsInBhcmVudElkIjoicGFyZW50SWQifQ==")

    assert res.list_pre_ipo_company_news_events_response is not None

    # Handle response
    print(res.list_pre_ipo_company_news_events_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `pre_ipo_company_id`                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                       | The preIpoCompany id.                                                                                                                                                                                                                                                    | 3fa85f64-5717-4562-b3fc-2c963f66afa6                                                                                                                                                                                                                                     |
| `page_size`                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                       | The maximum number of Pre IPO Company News Events to return. The service may return fewer than this value. If unspecified, at most 100 Pre IPO Company News Events will be returned. The maximum value is 100; values above 100 will be coerced to 100.                  | 50                                                                                                                                                                                                                                                                       |
| `page_token`                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                       | A page token, received from a previous `ListPreIpoCompanyNewsEventsRequest` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListPreIpoCompanyNewsEventsRequest` must match the call that provided the page token. | eyJzaXplIjoxMCwib2Zmc2V0IjoxMDAsInBhcmVudElkIjoicGFyZW50SWQifQ==                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                          |

### Response

**[operations.PreIpoCompanyNewsEventsListPreIpoCompanyNewsEventsResponse](../../models/operations/preipocompanynewseventslistpreipocompanynewseventsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |