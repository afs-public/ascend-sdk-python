# PreIPOFundingRounds
(*pre_ipo_funding_rounds*)

## Overview

### Available Operations

* [list_pre_ipo_company_funding_rounds](#list_pre_ipo_company_funding_rounds) - List Pre IPO Company Funding Rounds
* [get_pre_ipo_company_funding_round](#get_pre_ipo_company_funding_round) - Get Pre IPO Company Funding Round

## list_pre_ipo_company_funding_rounds

Lists Pre IPO Company Funding Rounds.

### Example Usage

<!-- UsageSnippet language="python" operationID="PreIpoCompanyFundingRounds_ListPreIpoCompanyFundingRounds" method="get" path="/trading/v1/preIpoCompanies/{preIpoCompany_id}/fundingRounds" -->
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

    res = sdk.pre_ipo_funding_rounds.list_pre_ipo_company_funding_rounds(pre_ipo_company_id="3fa85f64-5717-4562-b3fc-2c963f66afa6", page_size=50, page_token="eyJzaXplIjoxMCwib2Zmc2V0IjoxMDAsInBhcmVudElkIjoicGFyZW50SWQifQ==")

    assert res.list_pre_ipo_company_funding_rounds_response is not None

    # Handle response
    print(res.list_pre_ipo_company_funding_rounds_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `pre_ipo_company_id`                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                             | The preIpoCompany id.                                                                                                                                                                                                                                                          | 3fa85f64-5717-4562-b3fc-2c963f66afa6                                                                                                                                                                                                                                           |
| `page_size`                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                             | The maximum number of Pre IPO Company Funding Rounds to return. The service may return fewer than this value. If unspecified, at most 100 Pre IPO Company Funding Rounds will be returned. The maximum value is 100; values above 100 will be coerced to 100.                  | 50                                                                                                                                                                                                                                                                             |
| `page_token`                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                             | A page token, received from a previous `ListPreIpoCompanyFundingRoundsRequest` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListPreIpoCompanyFundingRoundsRequest` must match the call that provided the page token. | eyJzaXplIjoxMCwib2Zmc2V0IjoxMDAsInBhcmVudElkIjoicGFyZW50SWQifQ==                                                                                                                                                                                                               |
| `retries`                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                |

### Response

**[operations.PreIpoCompanyFundingRoundsListPreIpoCompanyFundingRoundsResponse](../../models/operations/preipocompanyfundingroundslistpreipocompanyfundingroundsresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_pre_ipo_company_funding_round

Gets a Pre IPO Company Funding Round.

### Example Usage

<!-- UsageSnippet language="python" operationID="PreIpoCompanyFundingRounds_GetPreIpoCompanyFundingRound" method="get" path="/trading/v1/preIpoCompanies/{preIpoCompany_id}/fundingRounds/{fundingRound_id}" -->
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

    res = sdk.pre_ipo_funding_rounds.get_pre_ipo_company_funding_round(pre_ipo_company_id="3fa85f64-5717-4562-b3fc-2c963f66afa6", funding_round_id="5f29def7-445a-46e1-b0af-e475c5481820")

    assert res.pre_ipo_company_funding_round is not None

    # Handle response
    print(res.pre_ipo_company_funding_round)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `pre_ipo_company_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The preIpoCompany id.                                               | 3fa85f64-5717-4562-b3fc-2c963f66afa6                                |
| `funding_round_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The fundingRound id.                                                | 5f29def7-445a-46e1-b0af-e475c5481820                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.PreIpoCompanyFundingRoundsGetPreIpoCompanyFundingRoundResponse](../../models/operations/preipocompanyfundingroundsgetpreipocompanyfundingroundresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |