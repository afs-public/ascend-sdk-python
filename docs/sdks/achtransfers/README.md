# ACHTransfers
(*ach_transfers*)

## Overview

### Available Operations

* [create_ach_deposit](#create_ach_deposit) - Create ACH Deposit
* [get_ach_deposit](#get_ach_deposit) - Get ACH Deposit
* [cancel_ach_deposit](#cancel_ach_deposit) - Cancel ACH Deposit
* [create_ach_withdrawal](#create_ach_withdrawal) - Create ACH Withdrawal
* [get_ach_withdrawal](#get_ach_withdrawal) - Get ACH Withdrawal
* [cancel_ach_withdrawal](#cancel_ach_withdrawal) - Cancel ACH Withdrawal

## create_ach_deposit

Creates an ACH deposit.

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

res = s.ach_transfers.create_ach_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_create={
    "amount": {},
    "bank_relationship": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/bankRelationships/651ef9de0dee00240813e60e",
    "client_transfer_id": "179dcd33-49f8-4615-989c-560fb387c4fd",
})

if res.ach_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `account_id`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | The account id.                                                            | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                 |
| `ach_deposit_create`                                                       | [components.AchDepositCreate](../../models/components/achdepositcreate.md) | :heavy_check_mark:                                                         | N/A                                                                        |                                                                            |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |                                                                            |

### Response

**[operations.AchDepositsCreateAchDepositResponse](../../models/operations/achdepositscreateachdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_ach_deposit

Gets an existing ACH deposit.

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

res = s.ach_transfers.get_ach_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_id="20230817000319")

if res.ach_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `ach_deposit_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The achDeposit id.                                                  | 20230817000319                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AchDepositsGetAchDepositResponse](../../models/operations/achdepositsgetachdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_ach_deposit

Cancels an existing ACH deposit.

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

res = s.ach_transfers.cancel_ach_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_id="20230817000319", cancel_ach_deposit_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achDeposits/20230817000319",
})

if res.ach_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | The account id.                                                                                      | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                           |
| `ach_deposit_id`                                                                                     | *str*                                                                                                | :heavy_check_mark:                                                                                   | The achDeposit id.                                                                                   | 20230817000319                                                                                       |
| `cancel_ach_deposit_request_create`                                                                  | [components.CancelAchDepositRequestCreate](../../models/components/cancelachdepositrequestcreate.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |                                                                                                      |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |                                                                                                      |

### Response

**[operations.AchDepositsCancelAchDepositResponse](../../models/operations/achdepositscancelachdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## create_ach_withdrawal

Creates an ACH withdrawal.

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

res = s.ach_transfers.create_ach_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_create={
    "bank_relationship": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/bankRelationships/651ef9de0dee00240813e60e",
    "client_transfer_id": "179dcd33-49f8-4615-989c-560fb387c4fd",
})

if res.ach_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `account_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | The account id.                                                                  | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                       |
| `ach_withdrawal_create`                                                          | [components.AchWithdrawalCreate](../../models/components/achwithdrawalcreate.md) | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[operations.AchWithdrawalsCreateAchWithdrawalResponse](../../models/operations/achwithdrawalscreateachwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_ach_withdrawal

Gets an existing ACH withdrawal.

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

res = s.ach_transfers.get_ach_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_id="20230620500726")

if res.ach_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `ach_withdrawal_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The achWithdrawal id.                                               | 20230620500726                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AchWithdrawalsGetAchWithdrawalResponse](../../models/operations/achwithdrawalsgetachwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_ach_withdrawal

Cancels an existing ACH withdrawal.

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

res = s.ach_transfers.cancel_ach_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_id="20230620500726", cancel_ach_withdrawal_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achWithdrawals/20230620500726",
})

if res.ach_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                               | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The account id.                                                                                            | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                 |
| `ach_withdrawal_id`                                                                                        | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The achWithdrawal id.                                                                                      | 20230620500726                                                                                             |
| `cancel_ach_withdrawal_request_create`                                                                     | [components.CancelAchWithdrawalRequestCreate](../../models/components/cancelachwithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |                                                                                                            |

### Response

**[operations.AchWithdrawalsCancelAchWithdrawalResponse](../../models/operations/achwithdrawalscancelachwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |