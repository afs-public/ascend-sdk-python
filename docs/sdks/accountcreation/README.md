# AccountCreation
(*account_creation*)

## Overview

### Available Operations

* [create_account](#create_account) - Create Account
* [get_account](#get_account) - Get Account

## create_account

CREATE Creates an account.

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

res = s.account_creation.create_account(request={
    "account_group_id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",
    "correspondent_id": "01HPMZZM6RKMVZA1JQ63RQKJRP",
    "parties": [
        {
            "email_address": "example@domain.com",
            "mailing_address": {},
            "phone_number": {},
            "relation_type": components.RelationType.PRIMARY_OWNER,
        },
    ],
})

if res.account is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.AccountRequestCreate](../../models/components/accountrequestcreate.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.AccountsCreateAccountResponse](../../models/operations/accountscreateaccountresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 403, 500, 503 | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## get_account

READ Get Account

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

res = s.account_creation.get_account(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK")

if res.account is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `account_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | The account id.                                                                  | 01HC3MAQ4DR9QN1V8MJ4CN1HMK                                                       |
| `view`                                                                           | [Optional[operations.QueryParamView]](../../models/operations/queryparamview.md) | :heavy_minus_sign:                                                               | The view to return. Defaults to `FULL`.                                          | FULL                                                                             |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[operations.AccountsGetAccountResponse](../../models/operations/accountsgetaccountresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.Status           | 400, 403, 404, 500, 503 | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |