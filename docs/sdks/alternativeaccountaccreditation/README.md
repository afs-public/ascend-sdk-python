# AlternativeAccountAccreditation
(*alternative_account_accreditation*)

## Overview

### Available Operations

* [get_account_accreditation](#get_account_accreditation) - Get Account Accreditation
* [set_account_accreditation_type](#set_account_accreditation_type) - Set Account Accreditation

## get_account_accreditation

Gets the accreditation properties for the specified account.

### Example Usage

<!-- UsageSnippet language="python" operationID="AccountAccreditationService_GetAccountAccreditation" method="get" path="/trading/v1/accounts/{account_id}/accreditation" -->
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

    res = sdk.alternative_account_accreditation.get_account_accreditation(account_id="01JR8YQT40WAQT8S95ZQGS1QN0")

    assert res.account_accreditation is not None

    # Handle response
    print(res.account_accreditation)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01JR8YQT40WAQT8S95ZQGS1QN0                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AccountAccreditationServiceGetAccountAccreditationResponse](../../models/operations/accountaccreditationservicegetaccountaccreditationresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## set_account_accreditation_type

Sets the accreditation type for an account. Accounts must be accredited to participate in alternative investment orders.

### Example Usage

<!-- UsageSnippet language="python" operationID="AccountAccreditationService_SetAccountAccreditationType" method="post" path="/trading/v1/accounts/{account_id}/accreditation:setType" -->
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

    res = sdk.alternative_account_accreditation.set_account_accreditation_type(account_id="01JR8YQT40WAQT8S95ZQGS1QN0", set_account_accreditation_type_request_create={
        "accreditation_type": components.SetAccountAccreditationTypeRequestCreateAccreditationType.NET_WORTH_GT_1_M,
        "name": "accounts/01JR8YQT40WAQT8S95ZQGS1QN0/accreditation",
    })

    assert res.account_accreditation is not None

    # Handle response
    print(res.account_accreditation)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                | Example                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | The account id.                                                                                                            | 01JR8YQT40WAQT8S95ZQGS1QN0                                                                                                 |
| `set_account_accreditation_type_request_create`                                                                            | [components.SetAccountAccreditationTypeRequestCreate](../../models/components/setaccountaccreditationtyperequestcreate.md) | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |                                                                                                                            |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |                                                                                                                            |

### Response

**[operations.AccountAccreditationServiceSetAccountAccreditationTypeResponse](../../models/operations/accountaccreditationservicesetaccountaccreditationtyperesponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500                | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |