# TestSimulation
(*test_simulation*)

## Overview

### Available Operations

* [force_approve_ach_deposit](#force_approve_ach_deposit) - ACH Deposit Approval
* [force_noc_ach_deposit](#force_noc_ach_deposit) - NOC for a Deposit
* [force_reject_ach_deposit](#force_reject_ach_deposit) - ACH Deposit Rejection
* [force_return_ach_deposit](#force_return_ach_deposit) - ACH Deposit Return
* [force_approve_ach_withdrawal](#force_approve_ach_withdrawal) - ACH Withdrawal Approval
* [force_noc_ach_withdrawal](#force_noc_ach_withdrawal) - ACH Withdrawal NOC
* [force_reject_ach_withdrawal](#force_reject_ach_withdrawal) - ACH Withdrawal Rejection
* [force_return_ach_withdrawal](#force_return_ach_withdrawal) - ACH Withdrawal Return
* [get_micro_deposit_amounts](#get_micro_deposit_amounts) - Get Relationship Micro Deposit Verification
* [force_approve_ict_deposit](#force_approve_ict_deposit) - Force Approve ICT Deposit
* [force_reject_ict_deposit](#force_reject_ict_deposit) - Force Reject ICT Deposit
* [force_approve_ict_withdrawal](#force_approve_ict_withdrawal) - Force Approve ICT Withdrawal
* [force_reject_ict_withdrawal](#force_reject_ict_withdrawal) - Force Reject ICT Withdrawal
* [force_approve_wire_withdrawal](#force_approve_wire_withdrawal) - Force Approve Wire Withdrawal
* [force_reject_wire_withdrawal](#force_reject_wire_withdrawal) - Force Reject Wire Withdrawal
* [force_approve_cash_journal](#force_approve_cash_journal) - Force Approve Cash Journal
* [force_reject_cash_journal](#force_reject_cash_journal) - Force Reject Cash Journal

## force_approve_ach_deposit

Forces approval of an existing ACH deposit that is pending review. FOR TESTING ONLY!

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

res = s.test_simulation.force_approve_ach_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_id="20230817000319", force_approve_ach_deposit_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achDeposits/20230817000319",
})

if res.ach_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The account id.                                                                                                  | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                       |
| `ach_deposit_id`                                                                                                 | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The achDeposit id.                                                                                               | 20230817000319                                                                                                   |
| `force_approve_ach_deposit_request_create`                                                                       | [components.ForceApproveAchDepositRequestCreate](../../models/components/forceapproveachdepositrequestcreate.md) | :heavy_check_mark:                                                                                               | N/A                                                                                                              |                                                                                                                  |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[operations.AchDepositsForceApproveAchDepositResponse](../../models/operations/achdepositsforceapproveachdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_noc_ach_deposit

Forces a Nacha notice of change (NOC) on a completed ACH deposit. FOR TESTING ONLY!

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

res = s.test_simulation.force_noc_ach_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_id="20230817000319", force_noc_ach_deposit_request_create={
    "nacha_noc": {
        "code": components.Code.C01,
    },
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achDeposits/20230817000319",
})

if res.ach_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              | Example                                                                                                  |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                             | *str*                                                                                                    | :heavy_check_mark:                                                                                       | The account id.                                                                                          | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                               |
| `ach_deposit_id`                                                                                         | *str*                                                                                                    | :heavy_check_mark:                                                                                       | The achDeposit id.                                                                                       | 20230817000319                                                                                           |
| `force_noc_ach_deposit_request_create`                                                                   | [components.ForceNocAchDepositRequestCreate](../../models/components/forcenocachdepositrequestcreate.md) | :heavy_check_mark:                                                                                       | N/A                                                                                                      |                                                                                                          |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |                                                                                                          |

### Response

**[operations.AchDepositsForceNocAchDepositResponse](../../models/operations/achdepositsforcenocachdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_reject_ach_deposit

Forces rejection of an existing ACH deposit that is pending review. FOR TESTING ONLY!

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

res = s.test_simulation.force_reject_ach_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_id="20230817000319", force_reject_ach_deposit_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achDeposits/20230817000319",
})

if res.ach_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                   | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The account id.                                                                                                | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                     |
| `ach_deposit_id`                                                                                               | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The achDeposit id.                                                                                             | 20230817000319                                                                                                 |
| `force_reject_ach_deposit_request_create`                                                                      | [components.ForceRejectAchDepositRequestCreate](../../models/components/forcerejectachdepositrequestcreate.md) | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |                                                                                                                |

### Response

**[operations.AchDepositsForceRejectAchDepositResponse](../../models/operations/achdepositsforcerejectachdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_return_ach_deposit

Forces a Nacha return on a completed ACH deposit. FOR TESTING ONLY!

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

res = s.test_simulation.force_return_ach_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_id="20230817000319", force_return_ach_deposit_request_create={
    "nacha_return": {
        "code": components.NachaReturnCreateCode.R34,
    },
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achDeposits/20230817000319",
})

if res.ach_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                   | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The account id.                                                                                                | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                     |
| `ach_deposit_id`                                                                                               | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The achDeposit id.                                                                                             | 20230817000319                                                                                                 |
| `force_return_ach_deposit_request_create`                                                                      | [components.ForceReturnAchDepositRequestCreate](../../models/components/forcereturnachdepositrequestcreate.md) | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |                                                                                                                |

### Response

**[operations.AchDepositsForceReturnAchDepositResponse](../../models/operations/achdepositsforcereturnachdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_approve_ach_withdrawal

Forces approval of an existing ACH withdrawal that is pending review. FOR TESTING ONLY!

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

res = s.test_simulation.force_approve_ach_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_id="20230620500726", force_approve_ach_withdrawal_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achWithdrawals/20230620500726",
})

if res.ach_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            | Example                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                           | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | The account id.                                                                                                        | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                             |
| `ach_withdrawal_id`                                                                                                    | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | The achWithdrawal id.                                                                                                  | 20230620500726                                                                                                         |
| `force_approve_ach_withdrawal_request_create`                                                                          | [components.ForceApproveAchWithdrawalRequestCreate](../../models/components/forceapproveachwithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    |                                                                                                                        |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |                                                                                                                        |

### Response

**[operations.AchWithdrawalsForceApproveAchWithdrawalResponse](../../models/operations/achwithdrawalsforceapproveachwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_noc_ach_withdrawal

Forces a Nacha notice of change (NOC) on a completed ACH withdrawal. FOR TESTING ONLY!

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

res = s.test_simulation.force_noc_ach_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_id="20230620500726", force_noc_ach_withdrawal_request_create={
    "nacha_noc": {
        "code": components.Code.C01,
    },
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achWithdrawals/20230620500726",
})

if res.ach_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                   | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The account id.                                                                                                | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                     |
| `ach_withdrawal_id`                                                                                            | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The achWithdrawal id.                                                                                          | 20230620500726                                                                                                 |
| `force_noc_ach_withdrawal_request_create`                                                                      | [components.ForceNocAchWithdrawalRequestCreate](../../models/components/forcenocachwithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |                                                                                                                |

### Response

**[operations.AchWithdrawalsForceNocAchWithdrawalResponse](../../models/operations/achwithdrawalsforcenocachwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_reject_ach_withdrawal

Forces rejection of an existing ACH withdrawal that is pending review. FOR TESTING ONLY!

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

res = s.test_simulation.force_reject_ach_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_id="20230620500726", force_reject_ach_withdrawal_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achWithdrawals/20230620500726",
})

if res.ach_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                         | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The account id.                                                                                                      | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                           |
| `ach_withdrawal_id`                                                                                                  | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The achWithdrawal id.                                                                                                | 20230620500726                                                                                                       |
| `force_reject_ach_withdrawal_request_create`                                                                         | [components.ForceRejectAchWithdrawalRequestCreate](../../models/components/forcerejectachwithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |                                                                                                                      |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |                                                                                                                      |

### Response

**[operations.AchWithdrawalsForceRejectAchWithdrawalResponse](../../models/operations/achwithdrawalsforcerejectachwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_return_ach_withdrawal

Forces a Nacha return on a completed ACH withdrawal. FOR TESTING ONLY!

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

res = s.test_simulation.force_return_ach_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_id="20230620500726", force_return_ach_withdrawal_request_create={
    "nacha_return": {
        "code": components.NachaReturnCreateCode.R28,
    },
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achWithdrawals/20230620500726",
})

if res.ach_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                         | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The account id.                                                                                                      | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                           |
| `ach_withdrawal_id`                                                                                                  | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The achWithdrawal id.                                                                                                | 20230620500726                                                                                                       |
| `force_return_ach_withdrawal_request_create`                                                                         | [components.ForceReturnAchWithdrawalRequestCreate](../../models/components/forcereturnachwithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |                                                                                                                      |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |                                                                                                                      |

### Response

**[operations.AchWithdrawalsForceReturnAchWithdrawalResponse](../../models/operations/achwithdrawalsforcereturnachwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_micro_deposit_amounts

Gets micro deposit amounts for bank relationships with the `MICRO_DEPOSIT` verification method. FOR TESTING ONLY!

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

res = s.test_simulation.get_micro_deposit_amounts(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", bank_relationship_id="651ef9de0dee00240813e60e")

if res.micro_deposit_amounts is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `bank_relationship_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The bankRelationship id.                                            | 651ef9de0dee00240813e60e                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.BankRelationshipsGetMicroDepositAmountsResponse](../../models/operations/bankrelationshipsgetmicrodepositamountsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_approve_ict_deposit

Forces an approval on an existing ICT deposit pending review - FOR TESTING

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

res = s.test_simulation.force_approve_ict_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ict_deposit_id="20240321000472", force_approve_ict_deposit_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/ictDeposits/20240321000472",
})

if res.ict_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The account id.                                                                                                  | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                       |
| `ict_deposit_id`                                                                                                 | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The ictDeposit id.                                                                                               | 20240321000472                                                                                                   |
| `force_approve_ict_deposit_request_create`                                                                       | [components.ForceApproveIctDepositRequestCreate](../../models/components/forceapproveictdepositrequestcreate.md) | :heavy_check_mark:                                                                                               | N/A                                                                                                              |                                                                                                                  |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[operations.IctDepositsForceApproveIctDepositResponse](../../models/operations/ictdepositsforceapproveictdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_reject_ict_deposit

Forces a rejection on an existing ICT deposit pending review - FOR TESTING

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

res = s.test_simulation.force_reject_ict_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ict_deposit_id="20240321000472", force_reject_ict_deposit_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/ictDeposits/20240321000472",
})

if res.ict_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                   | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The account id.                                                                                                | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                     |
| `ict_deposit_id`                                                                                               | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The ictDeposit id.                                                                                             | 20240321000472                                                                                                 |
| `force_reject_ict_deposit_request_create`                                                                      | [components.ForceRejectIctDepositRequestCreate](../../models/components/forcerejectictdepositrequestcreate.md) | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |                                                                                                                |

### Response

**[operations.IctDepositsForceRejectIctDepositResponse](../../models/operations/ictdepositsforcerejectictdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_approve_ict_withdrawal

Forces an approval on an existing ICT withdrawal pending review - FOR TESTING

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

res = s.test_simulation.force_approve_ict_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ict_withdrawal_id="20240321000472", force_approve_ict_withdrawal_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/ictWithdrawals/20240321000472",
})

if res.ict_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            | Example                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                           | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | The account id.                                                                                                        | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                             |
| `ict_withdrawal_id`                                                                                                    | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | The ictWithdrawal id.                                                                                                  | 20240321000472                                                                                                         |
| `force_approve_ict_withdrawal_request_create`                                                                          | [components.ForceApproveIctWithdrawalRequestCreate](../../models/components/forceapproveictwithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    |                                                                                                                        |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |                                                                                                                        |

### Response

**[operations.IctWithdrawalsForceApproveIctWithdrawalResponse](../../models/operations/ictwithdrawalsforceapproveictwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_reject_ict_withdrawal

Forces a rejection on an existing ICT withdrawal pending review - FOR TESTING

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

res = s.test_simulation.force_reject_ict_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ict_withdrawal_id="20240321000472", force_reject_ict_withdrawal_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/ictWithdrawals/20240321000472",
})

if res.ict_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                         | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The account id.                                                                                                      | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                           |
| `ict_withdrawal_id`                                                                                                  | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The ictWithdrawal id.                                                                                                | 20240321000472                                                                                                       |
| `force_reject_ict_withdrawal_request_create`                                                                         | [components.ForceRejectIctWithdrawalRequestCreate](../../models/components/forcerejectictwithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |                                                                                                                      |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |                                                                                                                      |

### Response

**[operations.IctWithdrawalsForceRejectIctWithdrawalResponse](../../models/operations/ictwithdrawalsforcerejectictwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_approve_wire_withdrawal

Forces an approval on an existing wire withdrawal pending review - FOR TESTING

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

res = s.test_simulation.force_approve_wire_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", wire_withdrawal_id="20230817000319", force_approve_wire_withdrawal_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/wireWithdrawals/20230817000319",
})

if res.wire_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              | Example                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                             | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The account id.                                                                                                          | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                               |
| `wire_withdrawal_id`                                                                                                     | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The wireWithdrawal id.                                                                                                   | 20230817000319                                                                                                           |
| `force_approve_wire_withdrawal_request_create`                                                                           | [components.ForceApproveWireWithdrawalRequestCreate](../../models/components/forceapprovewirewithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |                                                                                                                          |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |                                                                                                                          |

### Response

**[operations.WireWithdrawalsForceApproveWireWithdrawalResponse](../../models/operations/wirewithdrawalsforceapprovewirewithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_reject_wire_withdrawal

Forces a rejection on an existing wire withdrawal pending review - FOR TESTING

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

res = s.test_simulation.force_reject_wire_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", wire_withdrawal_id="20230817000319", force_reject_wire_withdrawal_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/wireWithdrawals/20230817000319",
})

if res.wire_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            | Example                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                           | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | The account id.                                                                                                        | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                             |
| `wire_withdrawal_id`                                                                                                   | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | The wireWithdrawal id.                                                                                                 | 20230817000319                                                                                                         |
| `force_reject_wire_withdrawal_request_create`                                                                          | [components.ForceRejectWireWithdrawalRequestCreate](../../models/components/forcerejectwirewithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    |                                                                                                                        |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |                                                                                                                        |

### Response

**[operations.WireWithdrawalsForceRejectWireWithdrawalResponse](../../models/operations/wirewithdrawalsforcerejectwirewithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_approve_cash_journal

Forces approval of an existing cash journal that is pending review FOR TESTING ONLY!

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

res = s.test_simulation.force_approve_cash_journal(cash_journal_id="20230817000319", force_approve_cash_journal_request_create={
    "name": "cashJournals/20230817000319",
})

if res.cash_journal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        | Example                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `cash_journal_id`                                                                                                  | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | The cashJournal id.                                                                                                | 20230817000319                                                                                                     |
| `force_approve_cash_journal_request_create`                                                                        | [components.ForceApproveCashJournalRequestCreate](../../models/components/forceapprovecashjournalrequestcreate.md) | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |                                                                                                                    |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |                                                                                                                    |

### Response

**[operations.CashJournalsForceApproveCashJournalResponse](../../models/operations/cashjournalsforceapprovecashjournalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## force_reject_cash_journal

Forces rejection of an existing cash journal that is pending review FOR TESTING ONLY!

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

res = s.test_simulation.force_reject_cash_journal(cash_journal_id="20230817000319", force_reject_cash_journal_request_create={
    "name": "cashJournals/20230817000319",
})

if res.cash_journal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `cash_journal_id`                                                                                                | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The cashJournal id.                                                                                              | 20230817000319                                                                                                   |
| `force_reject_cash_journal_request_create`                                                                       | [components.ForceRejectCashJournalRequestCreate](../../models/components/forcerejectcashjournalrequestcreate.md) | :heavy_check_mark:                                                                                               | N/A                                                                                                              |                                                                                                                  |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[operations.CashJournalsForceRejectCashJournalResponse](../../models/operations/cashjournalsforcerejectcashjournalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |