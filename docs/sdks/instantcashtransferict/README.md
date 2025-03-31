# InstantCashTransferICT
(*instant_cash_transfer_ict*)

## Overview

### Available Operations

* [create_ict_deposit](#create_ict_deposit) - Create ICT Deposit
* [get_ict_deposit](#get_ict_deposit) - Get ICT Deposit
* [cancel_ict_deposit](#cancel_ict_deposit) - Cancel ICT Deposit
* [create_ict_withdrawal](#create_ict_withdrawal) - Create ICT Withdrawal
* [get_ict_withdrawal](#get_ict_withdrawal) - Get ICT Withdrawal
* [cancel_ict_withdrawal](#cancel_ict_withdrawal) - Cancel ICT Withdrawal
* [locate_ict_report](#locate_ict_report) - Locate ICT Report

## create_ict_deposit

Creates an ICT deposit

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

res = s.instant_cash_transfer_ict.create_ict_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ict_deposit_create={
    "amount": {},
    "client_transfer_id": "ABC-123",
    "program": components.Program.DEPOSIT_ONLY,
    "travel_rule": {
        "originating_institution": {
            "account_id": "<id>",
            "title": "<value>",
        },
    },
})

if res.ict_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `account_id`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | The account id.                                                            | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                 |
| `ict_deposit_create`                                                       | [components.IctDepositCreate](../../models/components/ictdepositcreate.md) | :heavy_check_mark:                                                         | N/A                                                                        |                                                                            |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |                                                                            |

### Response

**[operations.IctDepositsCreateIctDepositResponse](../../models/operations/ictdepositscreateictdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_ict_deposit

Gets an existing ICT deposit

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

res = s.instant_cash_transfer_ict.get_ict_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ict_deposit_id="20240321000472")

if res.ict_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `ict_deposit_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ictDeposit id.                                                  | 20240321000472                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.IctDepositsGetIctDepositResponse](../../models/operations/ictdepositsgetictdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_ict_deposit

Cancels an existing ICT deposit

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

res = s.instant_cash_transfer_ict.cancel_ict_deposit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ict_deposit_id="20240321000472", cancel_ict_deposit_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/ictDeposits/20240321000472",
})

if res.ict_deposit is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | The account id.                                                                                      | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                           |
| `ict_deposit_id`                                                                                     | *str*                                                                                                | :heavy_check_mark:                                                                                   | The ictDeposit id.                                                                                   | 20240321000472                                                                                       |
| `cancel_ict_deposit_request_create`                                                                  | [components.CancelIctDepositRequestCreate](../../models/components/cancelictdepositrequestcreate.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |                                                                                                      |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |                                                                                                      |

### Response

**[operations.IctDepositsCancelIctDepositResponse](../../models/operations/ictdepositscancelictdepositresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## create_ict_withdrawal

Creates an ICT withdrawal

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

res = s.instant_cash_transfer_ict.create_ict_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ict_withdrawal_create={
    "client_transfer_id": "20230817000319",
    "program": components.IctWithdrawalCreateProgram.BROKER_PARTNER,
    "travel_rule": {
        "recipient_institution": {
            "account_id": "<id>",
            "title": "<value>",
        },
    },
})

if res.ict_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `account_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | The account id.                                                                  | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                       |
| `ict_withdrawal_create`                                                          | [components.IctWithdrawalCreate](../../models/components/ictwithdrawalcreate.md) | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[operations.IctWithdrawalsCreateIctWithdrawalResponse](../../models/operations/ictwithdrawalscreateictwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_ict_withdrawal

Gets an existing ICT withdrawal

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

res = s.instant_cash_transfer_ict.get_ict_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ict_withdrawal_id="20240321000472")

if res.ict_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `ict_withdrawal_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ictWithdrawal id.                                               | 20240321000472                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.IctWithdrawalsGetIctWithdrawalResponse](../../models/operations/ictwithdrawalsgetictwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_ict_withdrawal

Cancels an existing ICT withdrawal

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

res = s.instant_cash_transfer_ict.cancel_ict_withdrawal(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ict_withdrawal_id="20240321000472", cancel_ict_withdrawal_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/ictWithdrawals/20240321000472",
})

if res.ict_withdrawal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                               | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The account id.                                                                                            | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                 |
| `ict_withdrawal_id`                                                                                        | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The ictWithdrawal id.                                                                                      | 20240321000472                                                                                             |
| `cancel_ict_withdrawal_request_create`                                                                     | [components.CancelIctWithdrawalRequestCreate](../../models/components/cancelictwithdrawalrequestcreate.md) | :heavy_check_mark:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |                                                                                                            |

### Response

**[operations.IctWithdrawalsCancelIctWithdrawalResponse](../../models/operations/ictwithdrawalscancelictwithdrawalresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## locate_ict_report

Returns a signed link pointing to a recon report file for a specific ICT batch.

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

res = s.instant_cash_transfer_ict.locate_ict_report(correspondent_id="01H8MCDXH4HYJJAV921BDKCC83")

if res.locate_ict_report_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `correspondent_id`                                                                                   | *str*                                                                                                | :heavy_check_mark:                                                                                   | The correspondent id.                                                                                | 01H8MCDXH4HYJJAV921BDKCC83                                                                           |
| `batch_id`                                                                                           | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | The id of the ICT batch for which to locate the report.                                              | 24114.108.2b2c1.001                                                                                  |
| `program_date_filter_program`                                                                        | [Optional[operations.ProgramDateFilterProgram]](../../models/operations/programdatefilterprogram.md) | :heavy_minus_sign:                                                                                   | The ICT program for which to locate the report.                                                      | BROKER_PARTNER                                                                                       |
| `program_date_filter_process_date`                                                                   | [Optional[components.DateCreate]](../../models/components/datecreate.md)                             | :heavy_minus_sign:                                                                                   | The process date for which to locate the report.                                                     | {<br/>"process_date": {<br/>"day": 30,<br/>"month": 9,<br/>"year": 2023<br/>}<br/>}                  |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |                                                                                                      |

### Response

**[operations.IctReconReportsLocateIctReportResponse](../../models/operations/ictreconreportslocateictreportresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |