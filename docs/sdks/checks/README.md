# Checks
(*checks*)

## Overview

### Available Operations

* [get_check_deposit](#get_check_deposit) - Get Check Deposit

## get_check_deposit

Gets an existing check deposit.

### Example Usage

<!-- UsageSnippet language="python" operationID="CheckDeposits_GetCheckDeposit" method="get" path="/transfers/v1/accounts/{account_id}/checkDeposits/{checkDeposit_id}" -->
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

    res = sdk.checks.get_check_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", check_deposit_id="20230817000319")

    assert res.check_deposit is not None

    # Handle response
    print(res.check_deposit)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `check_deposit_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The checkDeposit id.                                                | 20230817000319                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.CheckDepositsGetCheckDepositResponse](../../models/operations/checkdepositsgetcheckdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |