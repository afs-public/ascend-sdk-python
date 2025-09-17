# BankRelationships
(*bank_relationships*)

## Overview

### Available Operations

* [create_bank_relationship](#create_bank_relationship) - Create Bank Relationship
* [list_bank_relationships](#list_bank_relationships) - List Bank Relationships
* [get_bank_relationship](#get_bank_relationship) - Get Bank Relationship
* [update_bank_relationship](#update_bank_relationship) - Update Bank Relationship
* [cancel_bank_relationship](#cancel_bank_relationship) - Cancel Bank Relationship
* [verify_micro_deposits](#verify_micro_deposits) - Verify Micro Deposits
* [reissue_micro_deposits](#reissue_micro_deposits) - Reissue Micro Deposits
* [reuse_bank_relationship](#reuse_bank_relationship) - Reuse Bank Relationship

## create_bank_relationship

Creates a bank relationship.

### Example Usage

<!-- UsageSnippet language="python" operationID="BankRelationships_CreateBankRelationship" method="post" path="/transfers/v1/accounts/{account_id}/bankRelationships" -->
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

    res = sdk.bank_relationships.create_bank_relationship(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", bank_relationship_create={
        "nickname": "My Primary Bank",
        "verification_method": components.VerificationMethod.MICRO_DEPOSIT,
    })

    assert res.bank_relationship is not None

    # Handle response
    print(res.bank_relationship)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `account_id`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | The account id.                                                                        | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                             |
| `bank_relationship_create`                                                             | [components.BankRelationshipCreate](../../models/components/bankrelationshipcreate.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |                                                                                        |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[operations.BankRelationshipsCreateBankRelationshipResponse](../../models/operations/bankrelationshipscreatebankrelationshipresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_bank_relationships

Lists bank relationships for an account.

### Example Usage

<!-- UsageSnippet language="python" operationID="BankRelationships_ListBankRelationships" method="get" path="/transfers/v1/accounts/{account_id}/bankRelationships" -->
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

    res = sdk.bank_relationships.list_bank_relationships(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", page_size=100, page_token="CMFRGgYQup3BhQgaCSkAQCKS7AAAAA==", state=operations.State.APPROVED)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                             | The account id.                                                                                                                                                                                                                                | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                                                                                                                                     |
| `page_size`                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | The maximum number of bank relationships to return. The service may return fewer than this value. If unspecified, at most 50 bank relationships will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.        | 100                                                                                                                                                                                                                                            |
| `page_token`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                             | A page token, received from a previous `ListBankRelationships` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListBankRelationships` must match the call that provided the page token. | CMFRGgYQup3BhQgaCSkAQCKS7AAAAA==                                                                                                                                                                                                               |
| `state`                                                                                                                                                                                                                                        | [Optional[operations.State]](../../models/operations/state.md)                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                             | The state of bank relationships to filter by. Unspecified returns relationships of all states.                                                                                                                                                 | APPROVED                                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                            |                                                                                                                                                                                                                                                |

### Response

**[operations.BankRelationshipsListBankRelationshipsResponse](../../models/operations/bankrelationshipslistbankrelationshipsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_bank_relationship

Gets an existing bank relationship.

### Example Usage

<!-- UsageSnippet language="python" operationID="BankRelationships_GetBankRelationship" method="get" path="/transfers/v1/accounts/{account_id}/bankRelationships/{bankRelationship_id}" -->
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

    res = sdk.bank_relationships.get_bank_relationship(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", bank_relationship_id="651ef9de0dee00240813e60e")

    assert res.bank_relationship is not None

    # Handle response
    print(res.bank_relationship)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `bank_relationship_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The bankRelationship id.                                            | 651ef9de0dee00240813e60e                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.BankRelationshipsGetBankRelationshipResponse](../../models/operations/bankrelationshipsgetbankrelationshipresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## update_bank_relationship

Updates an existing bank relationship.

### Example Usage

<!-- UsageSnippet language="python" operationID="BankRelationships_UpdateBankRelationship" method="patch" path="/transfers/v1/accounts/{account_id}/bankRelationships/{bankRelationship_id}" -->
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

    res = sdk.bank_relationships.update_bank_relationship(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", bank_relationship_id="651ef9de0dee00240813e60e", bank_relationship_update={}, update_mask="[object Object]")

    assert res.bank_relationship is not None

    # Handle response
    print(res.bank_relationship)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `account_id`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | The account id.                                                                        | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                             |
| `bank_relationship_id`                                                                 | *str*                                                                                  | :heavy_check_mark:                                                                     | The bankRelationship id.                                                               | 651ef9de0dee00240813e60e                                                               |
| `bank_relationship_update`                                                             | [components.BankRelationshipUpdate](../../models/components/bankrelationshipupdate.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |                                                                                        |
| `update_mask`                                                                          | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The field of the bank relationship to update. Only `nickname` is supported.            | {<br/>"update_mask": {<br/>"paths": [<br/>"nickname"<br/>]<br/>}<br/>}                 |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[operations.BankRelationshipsUpdateBankRelationshipResponse](../../models/operations/bankrelationshipsupdatebankrelationshipresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_bank_relationship

Cancels an existing bank relationship.

### Example Usage

<!-- UsageSnippet language="python" operationID="BankRelationships_CancelBankRelationship" method="post" path="/transfers/v1/accounts/{account_id}/bankRelationships/{bankRelationship_id}:cancel" -->
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

    res = sdk.bank_relationships.cancel_bank_relationship(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", bank_relationship_id="651ef9de0dee00240813e60e", cancel_bank_relationship_request_create={
        "comment": "User Request",
        "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/bankRelationships/651ef9de0dee00240813e60e",
    })

    assert res.bank_relationship is not None

    # Handle response
    print(res.bank_relationship)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The account id.                                                                                                  | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                       |
| `bank_relationship_id`                                                                                           | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The bankRelationship id.                                                                                         | 651ef9de0dee00240813e60e                                                                                         |
| `cancel_bank_relationship_request_create`                                                                        | [components.CancelBankRelationshipRequestCreate](../../models/components/cancelbankrelationshiprequestcreate.md) | :heavy_check_mark:                                                                                               | N/A                                                                                                              |                                                                                                                  |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[operations.BankRelationshipsCancelBankRelationshipResponse](../../models/operations/bankrelationshipscancelbankrelationshipresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## verify_micro_deposits

Verifies a pending bank relationship with the `MICRO_DEPOSIT` verification method. Successful verification of the micro deposit amounts will result in the relationship moving to the `APPROVED` state. The micro deposits will be taken back from the bank account.

### Example Usage

<!-- UsageSnippet language="python" operationID="BankRelationships_VerifyMicroDeposits" method="post" path="/transfers/v1/accounts/{account_id}/bankRelationships/{bankRelationship_id}:verifyMicroDeposits" -->
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

    res = sdk.bank_relationships.verify_micro_deposits(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", bank_relationship_id="651ef9de0dee00240813e60e", verify_micro_deposits_request_create=components.VerifyMicroDepositsRequestCreate(
        amounts=components.MicroDepositAmountsCreate(
            amount1=components.DecimalCreate(),
            amount2=components.DecimalCreate(),
        ),
        name="accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/bankRelationships/651ef9de0dee00240813e60e",
    ))

    assert res.bank_relationship is not None

    # Handle response
    print(res.bank_relationship)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                               | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The account id.                                                                                            | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                 |
| `bank_relationship_id`                                                                                     | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The bankRelationship id.                                                                                   | 651ef9de0dee00240813e60e                                                                                   |
| `verify_micro_deposits_request_create`                                                                     | [components.VerifyMicroDepositsRequestCreate](../../models/components/verifymicrodepositsrequestcreate.md) | :heavy_check_mark:                                                                                         | N/A                                                                                                        |                                                                                                            |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |                                                                                                            |

### Response

**[operations.BankRelationshipsVerifyMicroDepositsResponse](../../models/operations/bankrelationshipsverifymicrodepositsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## reissue_micro_deposits

Reissues micro deposits after micro deposit verification has failed. The user should have received a message that new micro deposits should be reissued.

### Example Usage

<!-- UsageSnippet language="python" operationID="BankRelationships_ReissueMicroDeposits" method="post" path="/transfers/v1/accounts/{account_id}/bankRelationships/{bankRelationship_id}:reissue" -->
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

    res = sdk.bank_relationships.reissue_micro_deposits(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", bank_relationship_id="651ef9de0dee00240813e60e", reissue_micro_deposits_request_create={
        "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/bankRelationships/651ef9de0dee00240813e60e",
    })

    assert res.bank_relationship is not None

    # Handle response
    print(res.bank_relationship)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  | Example                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                 | *str*                                                                                                        | :heavy_check_mark:                                                                                           | The account id.                                                                                              | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                   |
| `bank_relationship_id`                                                                                       | *str*                                                                                                        | :heavy_check_mark:                                                                                           | The bankRelationship id.                                                                                     | 651ef9de0dee00240813e60e                                                                                     |
| `reissue_micro_deposits_request_create`                                                                      | [components.ReissueMicroDepositsRequestCreate](../../models/components/reissuemicrodepositsrequestcreate.md) | :heavy_check_mark:                                                                                           | N/A                                                                                                          |                                                                                                              |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |                                                                                                              |

### Response

**[operations.BankRelationshipsReissueMicroDepositsResponse](../../models/operations/bankrelationshipsreissuemicrodepositsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## reuse_bank_relationship

Reuses an existing bank relationship for a new account. The source bank relationship must be approved. The new account must be related to the parent account of the `source_bank_relationship`. The new relationship will be created with the `USE_EXISTING` verification method in place of the source bank relationship's verification method.

### Example Usage

<!-- UsageSnippet language="python" operationID="BankRelationships_ReuseBankRelationship" method="post" path="/transfers/v1/accounts/{account_id}/bankRelationships:reuse" -->
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

    res = sdk.bank_relationships.reuse_bank_relationship(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Z", reuse_bank_relationship_request_create={
        "parent": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Z",
        "source_bank_relationship": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/bankRelationships/651ef9de0dee00240813e60e",
    })

    assert res.bank_relationship is not None

    # Handle response
    print(res.bank_relationship)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                   | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The account id.                                                                                                | 01H8FB90ZRRFWXB4XC2JPJ1D4Z                                                                                     |
| `reuse_bank_relationship_request_create`                                                                       | [components.ReuseBankRelationshipRequestCreate](../../models/components/reusebankrelationshiprequestcreate.md) | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |                                                                                                                |

### Response

**[operations.BankRelationshipsReuseBankRelationshipResponse](../../models/operations/bankrelationshipsreusebankrelationshipresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |