# Margins
(*margins*)

## Overview

### Available Operations

* [get_buying_power](#get_buying_power) - Get Buying Power

## get_buying_power

Gets the buying power for an account

### Example Usage

<!-- UsageSnippet language="python" operationID="MarginsRealTime_GetBuyingPower" method="get" path="/buyingpower/v1/accounts/{account_id}/buyingPower" -->
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

    res = sdk.margins.get_buying_power(account_id="01HMS9S15AKBHBD8GPW33P2PMH")

    assert res.buying_power is not None

    # Handle response
    print(res.buying_power)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01HMS9S15AKBHBD8GPW33P2PMH                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.MarginsRealTimeGetBuyingPowerResponse](../../models/operations/marginsrealtimegetbuyingpowerresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |