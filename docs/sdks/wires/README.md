# Wires
(*wires*)

## Overview

### Available Operations

* [get_wire_deposit](#get_wire_deposit) - Get Wire Deposit
* [create_wire_withdrawal](#create_wire_withdrawal) - Create Wire Withdrawal
* [get_wire_withdrawal](#get_wire_withdrawal) - Get Wire Withdrawal
* [cancel_wire_withdrawal](#cancel_wire_withdrawal) - Cancel Wire Withdrawal

## get_wire_deposit

Gets an existing wire deposit

### Example Usage

<!-- UsageSnippet language="python" operationID="WireDeposits_GetWireDeposit" method="get" path="/transfers/v1/accounts/{account_id}/wireDeposits/{wireDeposit_id}" -->
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

    res = sdk.wires.get_wire_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", wire_deposit_id="20230817000319")

    assert res.wire_deposit is not None

    # Handle response
    print(res.wire_deposit)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `wire_deposit_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The wireDeposit id.                                                 | 20230817000319                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.WireDepositsGetWireDepositResponse](../../models/operations/wiredepositsgetwiredepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## create_wire_withdrawal

Creates a wire withdrawal

### Example Usage

<!-- UsageSnippet language="python" operationID="WireWithdrawals_CreateWireWithdrawal" method="post" path="/transfers/v1/accounts/{account_id}/wireWithdrawals" -->
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

    res = sdk.wires.create_wire_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", wire_withdrawal_create=components.WireWithdrawalCreate(
        beneficiary=components.WireWithdrawalBeneficiaryCreate(
            account="73849218650987",
        ),
        client_transfer_id="ABC-123",
        recipient_bank=components.WireWithdrawalRecipientBankCreate(
            bank_id=components.RecipientBankBankIDCreate(
                id="ABNANL2AXXX",
                type=components.RecipientBankBankIDCreateType.BIC,
            ),
        ),
    ))

    assert res.wire_withdrawal is not None

    # Handle response
    print(res.wire_withdrawal)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `account_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | The account id.                                                                    | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                         |
| `wire_withdrawal_create`                                                           | [components.WireWithdrawalCreate](../../models/components/wirewithdrawalcreate.md) | :heavy_check_mark:                                                                 | N/A                                                                                |                                                                                    |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |                                                                                    |

### Response

**[operations.WireWithdrawalsCreateWireWithdrawalResponse](../../models/operations/wirewithdrawalscreatewirewithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_wire_withdrawal

Gets an existing wire withdrawal

### Example Usage

<!-- UsageSnippet language="python" operationID="WireWithdrawals_GetWireWithdrawal" method="get" path="/transfers/v1/accounts/{account_id}/wireWithdrawals/{wireWithdrawal_id}" -->
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

    res = sdk.wires.get_wire_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", wire_withdrawal_id="20230817000319")

    assert res.wire_withdrawal is not None

    # Handle response
    print(res.wire_withdrawal)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `wire_withdrawal_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The wireWithdrawal id.                                              | 20230817000319                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.WireWithdrawalsGetWireWithdrawalResponse](../../models/operations/wirewithdrawalsgetwirewithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_wire_withdrawal

Cancels an existing wire withdrawal

### Example Usage

<!-- UsageSnippet language="python" operationID="WireWithdrawals_CancelWireWithdrawal" method="post" path="/transfers/v1/accounts/{account_id}/wireWithdrawals/{wireWithdrawal_id}:cancel" -->
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

    res = sdk.wires.cancel_wire_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", wire_withdrawal_id="20230817000319", cancel_wire_withdrawal_request_create={
        "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/wireWithdrawals/20230817000319",
    })

    assert res.wire_withdrawal is not None

    # Handle response
    print(res.wire_withdrawal)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  | Example                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                 | *str*                                                                                                        | :heavy_check_mark:                                                                                           | The account id.                                                                                              | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                   |
| `wire_withdrawal_id`                                                                                         | *str*                                                                                                        | :heavy_check_mark:                                                                                           | The wireWithdrawal id.                                                                                       | 20230817000319                                                                                               |
| `cancel_wire_withdrawal_request_create`                                                                      | [components.CancelWireWithdrawalRequestCreate](../../models/components/cancelwirewithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                           | N/A                                                                                                          |                                                                                                              |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |                                                                                                              |

### Response

**[operations.WireWithdrawalsCancelWireWithdrawalResponse](../../models/operations/wirewithdrawalscancelwirewithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |