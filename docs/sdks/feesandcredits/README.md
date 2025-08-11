# FeesAndCredits
(*fees_and_credits*)

## Overview

### Available Operations

* [create_fee](#create_fee) - Create Fee
* [get_fee](#get_fee) - Get Fee
* [cancel_fee](#cancel_fee) - Cancel Fee
* [create_credit](#create_credit) - Create Credit
* [get_credit](#get_credit) - Get Credit
* [cancel_credit](#cancel_credit) - Cancel Credit

## create_fee

Create a fee

### Example Usage

<!-- UsageSnippet language="python" operationID="Fees_CreateFee" method="post" path="/transfers/v1/accounts/{account_id}/fees" -->
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

    res = sdk.fees_and_credits.create_fee(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", transfers_fee_create={
        "amount": {},
        "client_transfer_id": "179dcd33-49f8-4615-989c-560fb387c4fd",
        "type": components.TransfersFeeCreateType.PLATFORM,
    })

    assert res.transfers_fee is not None

    # Handle response
    print(res.transfers_fee)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `account_id`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | The account id.                                                                | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                     |
| `transfers_fee_create`                                                         | [components.TransfersFeeCreate](../../models/components/transfersfeecreate.md) | :heavy_check_mark:                                                             | N/A                                                                            |                                                                                |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |                                                                                |

### Response

**[operations.FeesCreateFeeResponse](../../models/operations/feescreatefeeresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_fee

Retrieve an existing fee

### Example Usage

<!-- UsageSnippet language="python" operationID="Fees_GetFee" method="get" path="/transfers/v1/accounts/{account_id}/fees/{fee_id}" -->
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

    res = sdk.fees_and_credits.get_fee(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", fee_id="20230823123456")

    assert res.transfers_fee is not None

    # Handle response
    print(res.transfers_fee)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `fee_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The fee id.                                                         | 20230823123456                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.FeesGetFeeResponse](../../models/operations/feesgetfeeresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_fee

Cancel an existing fee

### Example Usage

<!-- UsageSnippet language="python" operationID="Fees_CancelFee" method="post" path="/transfers/v1/accounts/{account_id}/fees/{fee_id}:cancel" -->
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

    res = sdk.fees_and_credits.cancel_fee(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", fee_id="20230823123456", cancel_fee_request_create={
        "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/fees/20230823123456",
    })

    assert res.transfers_fee is not None

    # Handle response
    print(res.transfers_fee)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `account_id`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | The account id.                                                                        | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                             |
| `fee_id`                                                                               | *str*                                                                                  | :heavy_check_mark:                                                                     | The fee id.                                                                            | 20230823123456                                                                         |
| `cancel_fee_request_create`                                                            | [components.CancelFeeRequestCreate](../../models/components/cancelfeerequestcreate.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |                                                                                        |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[operations.FeesCancelFeeResponse](../../models/operations/feescancelfeeresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## create_credit

Create a credit

### Example Usage

<!-- UsageSnippet language="python" operationID="Credits_CreateCredit" method="post" path="/transfers/v1/accounts/{account_id}/credits" -->
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

    res = sdk.fees_and_credits.create_credit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", transfers_credit_create={
        "amount": {},
        "client_transfer_id": "179dcd33-49f8-4615-989c-560fb387c4fd",
        "type": components.TransfersCreditCreateType.PROMOTIONAL,
    })

    assert res.transfers_credit is not None

    # Handle response
    print(res.transfers_credit)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `account_id`                                                                         | *str*                                                                                | :heavy_check_mark:                                                                   | The account id.                                                                      | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                           |
| `transfers_credit_create`                                                            | [components.TransfersCreditCreate](../../models/components/transferscreditcreate.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |                                                                                      |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |                                                                                      |

### Response

**[operations.CreditsCreateCreditResponse](../../models/operations/creditscreatecreditresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_credit

Retrieve an existing credit

### Example Usage

<!-- UsageSnippet language="python" operationID="Credits_GetCredit" method="get" path="/transfers/v1/accounts/{account_id}/credits/{credit_id}" -->
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

    res = sdk.fees_and_credits.get_credit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", credit_id="20230823123456")

    assert res.transfers_credit is not None

    # Handle response
    print(res.transfers_credit)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `credit_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The credit id.                                                      | 20230823123456                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.CreditsGetCreditResponse](../../models/operations/creditsgetcreditresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_credit

Cancel an existing credit

### Example Usage

<!-- UsageSnippet language="python" operationID="Credits_CancelCredit" method="post" path="/transfers/v1/accounts/{account_id}/credits/{credit_id}:cancel" -->
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

    res = sdk.fees_and_credits.cancel_credit(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", credit_id="20230823123456", cancel_credit_request_create={
        "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/credits/20230823123456",
    })

    assert res.transfers_credit is not None

    # Handle response
    print(res.transfers_credit)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `account_id`                                                                                 | *str*                                                                                        | :heavy_check_mark:                                                                           | The account id.                                                                              | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                   |
| `credit_id`                                                                                  | *str*                                                                                        | :heavy_check_mark:                                                                           | The credit id.                                                                               | 20230823123456                                                                               |
| `cancel_credit_request_create`                                                               | [components.CancelCreditRequestCreate](../../models/components/cancelcreditrequestcreate.md) | :heavy_check_mark:                                                                           | N/A                                                                                          |                                                                                              |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |                                                                                              |

### Response

**[operations.CreditsCancelCreditResponse](../../models/operations/creditscancelcreditresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |