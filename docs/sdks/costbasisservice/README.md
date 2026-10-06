# CostBasisService
(*cost_basis_service*)

## Overview

### Available Operations

* [search_closed_lots](#search_closed_lots) - Search Closed Lots
* [search_open_lots](#search_open_lots) - Search Open Lots

## search_closed_lots

SearchClosedLots returns a list of closed lots for a given account and date range. Please note that if no trade date ranges are provided, all the closed lots using the MTD range will be returned.

### Example Usage

<!-- UsageSnippet language="python" operationID="CostBasisService_SearchClosedLots" method="post" path="/costbasis/v1/accounts/{account_id}/closedLots:search" -->
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

    res = sdk.cost_basis_service.search_closed_lots(account_id="01J71HKJ1K1GX5C0EWZ4BCPACB", search_closed_lots_request_create=components.SearchClosedLotsRequestCreate(
        parent="accounts/01J71HKJ1K1GX5C0EWZ4BCPACB",
    ))

    assert res.search_closed_lots_response is not None

    # Handle response
    print(res.search_closed_lots_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | The account id.                                                                                      | 01J71HKJ1K1GX5C0EWZ4BCPACB                                                                           |
| `search_closed_lots_request_create`                                                                  | [components.SearchClosedLotsRequestCreate](../../models/components/searchclosedlotsrequestcreate.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |                                                                                                      |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |                                                                                                      |

### Response

**[operations.CostBasisServiceSearchClosedLotsResponse](../../models/operations/costbasisservicesearchclosedlotsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## search_open_lots

SearchOpenLots returns a list of open lots for a given account

### Example Usage

<!-- UsageSnippet language="python" operationID="CostBasisService_SearchOpenLots" method="post" path="/costbasis/v1/accounts/{account_id}/openLots:search" -->
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

    res = sdk.cost_basis_service.search_open_lots(account_id="01J71HKJ1K1GX5C0EWZ4BCPACB", search_open_lots_request_create={
        "parent": "accounts/01J71HKJ1K1GX5C0EWZ4BCPACB",
    })

    assert res.search_open_lots_response is not None

    # Handle response
    print(res.search_open_lots_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                     | *str*                                                                                            | :heavy_check_mark:                                                                               | The account id.                                                                                  | 01J71HKJ1K1GX5C0EWZ4BCPACB                                                                       |
| `search_open_lots_request_create`                                                                | [components.SearchOpenLotsRequestCreate](../../models/components/searchopenlotsrequestcreate.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |                                                                                                  |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |                                                                                                  |

### Response

**[operations.CostBasisServiceSearchOpenLotsResponse](../../models/operations/costbasisservicesearchopenlotsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |