# AlternativeInvestments
(*alternative_investments*)

## Overview

### Available Operations

* [list_alternative_investments](#list_alternative_investments) - List Alternative Investment Assets
* [get_alternative_investment](#get_alternative_investment) - Get Alternative Investment Asset

## list_alternative_investments

Retrieves a list of available alternative investment assets and their details.  Replace `{asset_id}` in the endpoint path with a dash to act as a wild card.  Ex:`/trading/v1/assets/-/alternativeInvestments`

### Example Usage

<!-- UsageSnippet language="python" operationID="AlternativeInvestments_ListAlternativeInvestments" method="get" path="/trading/v1/assets/{asset_id}/alternativeInvestments" -->
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

    res = sdk.alternative_investments.list_alternative_investments(asset_id="-", page_size=50, page_token="eyJzaXplIjoxMCwib2Zmc2V0IjoxMDAsInBhcmVudElkIjoicGFyZW50SWQifQ==", filter_="state == 'OPEN' && type == 'PRIVATE_EQUITY_FUND'")

    assert res.list_alternative_investments_response is not None

    # Handle response
    print(res.list_alternative_investments_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                           | Example                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_id`                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                    | The asset id.                                                                                                                                                                                                                                                                         | -                                                                                                                                                                                                                                                                                     |
| `page_size`                                                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | The maximum number of orders to return.  - Max value =100  - Values above 100 will be coerced to 100.  - If the specified value is greater than the number of orders, the service will return fewer than the specified value.  - If unspecified, at most 100 orders will be returned. | 50                                                                                                                                                                                                                                                                                    |
| `page_token`                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | For pagination, provide the page token, received from a previous `ListAlternativeInvestments` call, to retrieve the subsequent page.  All other parameters provided to `ListAlternativeInvestments` must match the request that provided the page token.                              | eyJzaXplIjoxMCwib2Zmc2V0IjoxMDAsInBhcmVudElkIjoicGFyZW50SWQifQ==                                                                                                                                                                                                                      |
| `filter_`                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | A CEL string to filter results. All fields from the response can be used as filters.<br/><br/> See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) guide for syntax details and examples.                                                 | state == 'OPEN' && type == 'PRIVATE_EQUITY_FUND'                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                       |

### Response

**[operations.AlternativeInvestmentsListAlternativeInvestmentsResponse](../../models/operations/alternativeinvestmentslistalternativeinvestmentsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_alternative_investment

Retrieves the specified alternative investment asset details.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlternativeInvestments_GetAlternativeInvestment" method="get" path="/trading/v1/assets/{asset_id}/alternativeInvestment" -->
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

    res = sdk.alternative_investments.get_alternative_investment(asset_id="123")

    assert res.alternative_investment is not None

    # Handle response
    print(res.alternative_investment)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The asset id.                                                       | 123                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AlternativeInvestmentsGetAlternativeInvestmentResponse](../../models/operations/alternativeinvestmentsgetalternativeinvestmentresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |