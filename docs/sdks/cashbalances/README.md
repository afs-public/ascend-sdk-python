# CashBalances
(*cash_balances*)

## Overview

### Available Operations

* [calculate_cash_balance](#calculate_cash_balance) - Get Cash Balance

## calculate_cash_balance

Calculates the cash balance for an account.

### Example Usage

<!-- UsageSnippet language="python" operationID="CashBalances_CalculateCashBalance" method="get" path="/transfers/v1/accounts/{account_id}:calculateCashBalance" -->
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

    res = sdk.cash_balances.calculate_cash_balance(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", mechanism=operations.Mechanism.ACH)

    assert res.calculate_cash_balance_response is not None

    # Handle response
    print(res.calculate_cash_balance_response)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  | Example                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                 | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | The account id.                                                                                                              | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                   |
| `mechanism`                                                                                                                  | [Optional[operations.Mechanism]](../../models/operations/mechanism.md)                                                       | :heavy_minus_sign:                                                                                                           | The withdraw mechanism to calculate the balance for. The mechanism determines what account activity will affect the balance. | ACH                                                                                                                          |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |                                                                                                                              |

### Response

**[operations.CashBalancesCalculateCashBalanceResponse](../../models/operations/cashbalancescalculatecashbalanceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |