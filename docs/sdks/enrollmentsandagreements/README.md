# EnrollmentsAndAgreements
(*enrollments_and_agreements*)

## Overview

### Available Operations

* [enroll_account](#enroll_account) - Enroll Account
* [list_available_enrollments](#list_available_enrollments) - List Available Enrollments
* [accounts_list_available_enrollments_by_account_group](#accounts_list_available_enrollments_by_account_group) - List Available Enrollments (by Account Group)
* [deactivate_enrollment](#deactivate_enrollment) - Deactivate Enrollment
* [list_enrollments](#list_enrollments) - List Account Enrollments
* [affirm_agreements](#affirm_agreements) - Affirm Agreements
* [list_agreements](#list_agreements) - List Account Agreements
* [list_entitlements](#list_entitlements) - List Account Entitlements

## enroll_account

Adds an Enrollment to an Account.

### Example Usage

<!-- UsageSnippet language="python" operationID="Accounts_EnrollAccount" method="post" path="/accounts/v1/accounts/{account_id}:enroll" -->
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

    res = sdk.enrollments_and_agreements.enroll_account(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", enroll_account_request_create=components.EnrollAccountRequestCreate(
        enrollment=components.EnrollmentCreate(
            principal_approver_id="02HB7N66WW02WL3B6B9W29K0HW",
            type=components.EnrollmentCreateType.REGISTRATION_INDIVIDUAL,
        ),
    ))

    assert res.enroll_account_response is not None

    # Handle response
    print(res.enroll_account_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    | Example                                                                                        |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `account_id`                                                                                   | *str*                                                                                          | :heavy_check_mark:                                                                             | The account id.                                                                                | 01HC3MAQ4DR9QN1V8MJ4CN1HMK                                                                     |
| `enroll_account_request_create`                                                                | [components.EnrollAccountRequestCreate](../../models/components/enrollaccountrequestcreate.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |                                                                                                |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |                                                                                                |

### Response

**[operations.AccountsEnrollAccountResponse](../../models/operations/accountsenrollaccountresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_available_enrollments

Get a list of Enrollments available for an Account.

### Example Usage

<!-- UsageSnippet language="python" operationID="Accounts_ListAvailableEnrollments" method="get" path="/accounts/v1/accounts/{account_id}/availableEnrollments" -->
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

    res = sdk.enrollments_and_agreements.list_available_enrollments(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", page_size=25, page_token="AbTYnwAkMjIyZDNjYTAtZmVjZS00N2Q5LTgyMDctNzI3MDdkMjFiZj3h", filter_="enrollment_type == \"REGISTRATION_INDIVIDUAL\"")

    assert res.list_available_enrollments_response is not None

    # Handle response
    print(res.list_available_enrollments_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | The account id.                                                                                                                                                                                                                                        | 01HC3MAQ4DR9QN1V8MJ4CN1HMK                                                                                                                                                                                                                             |
| `page_size`                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | The maximum number of available enrollments to return. The service may return fewer than this value. The maximum value is 100; values above 100 will be coerced to 100.                                                                                | 25                                                                                                                                                                                                                                                     |
| `page_token`                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | A page token, received from a previous `ListAvailableEnrollments` call. Provide this to retrieve the subsequent page.<br/><br/> When paginating, all other parameters provided to `ListAvailableEnrollments` must match the call that provided the page token. | AbTYnwAkMjIyZDNjYTAtZmVjZS00N2Q5LTgyMDctNzI3MDdkMjFiZj3h                                                                                                                                                                                               |
| `filter_`                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:<br/> `enrollment_type`                                    | enrollment_type == "REGISTRATION_INDIVIDUAL"                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |

### Response

**[operations.AccountsListAvailableEnrollmentsResponse](../../models/operations/accountslistavailableenrollmentsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## accounts_list_available_enrollments_by_account_group

Get a list of Enrollments available for an Account.

### Example Usage

<!-- UsageSnippet language="python" operationID="Accounts_ListAvailableEnrollments_1" method="get" path="/accounts/v1/accountGroups/{accountGroup_id}/availableEnrollments" -->
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

    res = sdk.enrollments_and_agreements.accounts_list_available_enrollments_by_account_group(account_group_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", page_size=25, page_token="AbTYnwAkMjIyZDNjYTAtZmVjZS00N2Q5LTgyMDctNzI3MDdkMjFiZj3h", filter_="enrollment_type == \"REGISTRATION_INDIVIDUAL\"")

    assert res.list_available_enrollments_response is not None

    # Handle response
    print(res.list_available_enrollments_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `account_group_id`                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | The accountGroup id.                                                                                                                                                                                                                                   | 01HC3MAQ4DR9QN1V8MJ4CN1HMK                                                                                                                                                                                                                             |
| `page_size`                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | The maximum number of available enrollments to return. The service may return fewer than this value. The maximum value is 100; values above 100 will be coerced to 100.                                                                                | 25                                                                                                                                                                                                                                                     |
| `page_token`                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | A page token, received from a previous `ListAvailableEnrollments` call. Provide this to retrieve the subsequent page.<br/><br/> When paginating, all other parameters provided to `ListAvailableEnrollments` must match the call that provided the page token. | AbTYnwAkMjIyZDNjYTAtZmVjZS00N2Q5LTgyMDctNzI3MDdkMjFiZj3h                                                                                                                                                                                               |
| `filter_`                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:<br/> `enrollment_type`                                    | enrollment_type == "REGISTRATION_INDIVIDUAL"                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |

### Response

**[operations.AccountsListAvailableEnrollments1Response](../../models/operations/accountslistavailableenrollments1response.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## deactivate_enrollment

Deactivates an Account Enrollment.

### Example Usage

<!-- UsageSnippet language="python" operationID="Accounts_DeactivateEnrollment" method="post" path="/accounts/v1/accounts/{account_id}/enrollments:deactivate" -->
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

    res = sdk.enrollments_and_agreements.deactivate_enrollment(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", deactivate_enrollment_request_create={})

    assert res.enrollment is not None

    # Handle response
    print(res.enrollment)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  | Example                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                 | *str*                                                                                                        | :heavy_check_mark:                                                                                           | The account id.                                                                                              | 01HC3MAQ4DR9QN1V8MJ4CN1HMK                                                                                   |
| `deactivate_enrollment_request_create`                                                                       | [components.DeactivateEnrollmentRequestCreate](../../models/components/deactivateenrollmentrequestcreate.md) | :heavy_check_mark:                                                                                           | N/A                                                                                                          |                                                                                                              |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |                                                                                                              |

### Response

**[operations.AccountsDeactivateEnrollmentResponse](../../models/operations/accountsdeactivateenrollmentresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_enrollments

Gets a list of Enrollments for an Account.

### Example Usage

<!-- UsageSnippet language="python" operationID="Accounts_ListEnrollments" method="get" path="/accounts/v1/accounts/{account_id}/enrollments" -->
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

    res = sdk.enrollments_and_agreements.list_enrollments(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", page_size=5, page_token="4ZHd3wAaMD1IQ0ZKS2BKV0FSRVdLW4VLWkY1R1B3MU4")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                   | The account id.                                                                                                                                                                                                                      | 01HC3MAQ4DR9QN1V8MJ4CN1HMK                                                                                                                                                                                                           |
| `page_size`                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                   | The maximum number of enrollments to return.                                                                                                                                                                                         | 5                                                                                                                                                                                                                                    |
| `page_token`                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                   | A page token, received from a previous `ListEnrollments` call. Provide this to retrieve the subsequent page.<br/><br/> When paginating, all other parameters provided to `ListEnrollments` must match the call that provided the page token. | 4ZHd3wAaMD1IQ0ZKS2BKV0FSRVdLW4VLWkY1R1B3MU4                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                  |                                                                                                                                                                                                                                      |

### Response

**[operations.AccountsListEnrollmentsResponse](../../models/operations/accountslistenrollmentsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## affirm_agreements

Affirm Agreements for an Account.

### Example Usage

<!-- UsageSnippet language="python" operationID="Accounts_AffirmAgreements" method="post" path="/accounts/v1/accounts/{account_id}/agreements:affirm" -->
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

    res = sdk.enrollments_and_agreements.affirm_agreements(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", affirm_agreements_request_create={
        "account_agreement_ids": [
            "fa2f181c-f2fb-4bc2-b75a-79302c634ae5",
        ],
    })

    assert res.affirm_agreements_response is not None

    # Handle response
    print(res.affirm_agreements_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | The account id.                                                                                      | 01HC3MAQ4DR9QN1V8MJ4CN1HMK                                                                           |
| `affirm_agreements_request_create`                                                                   | [components.AffirmAgreementsRequestCreate](../../models/components/affirmagreementsrequestcreate.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |                                                                                                      |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |                                                                                                      |

### Response

**[operations.AccountsAffirmAgreementsResponse](../../models/operations/accountsaffirmagreementsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_agreements

Gets a list of Agreements on an Account.

### Example Usage

<!-- UsageSnippet language="python" operationID="Accounts_ListAgreements" method="get" path="/accounts/v1/accounts/{account_id}/agreements" -->
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

    res = sdk.enrollments_and_agreements.list_agreements(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", page_size=5, page_token="4ZHd3wAaMD1IQ0ZKS2BKV0FSRVdLW4VLWkY1R1B3MU4")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                        | Example                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                 | The account id.                                                                                                                                                                                                                    | 01HC3MAQ4DR9QN1V8MJ4CN1HMK                                                                                                                                                                                                         |
| `page_size`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                 | The maximum number of agreements to return.                                                                                                                                                                                        | 5                                                                                                                                                                                                                                  |
| `page_token`                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                 | A page token, received from a previous `ListAgreements` call. Provide this to retrieve the subsequent page.<br/><br/> When paginating, all other parameters provided to `ListAgreements` must match the call that provided the page token. | 4ZHd3wAaMD1IQ0ZKS2BKV0FSRVdLW4VLWkY1R1B3MU4                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                |                                                                                                                                                                                                                                    |

### Response

**[operations.AccountsListAgreementsResponse](../../models/operations/accountslistagreementsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_entitlements

Gets a list of Entitlements for an Account.

### Example Usage

<!-- UsageSnippet language="python" operationID="Accounts_ListEntitlements" method="get" path="/accounts/v1/accounts/{account_id}/entitlements" -->
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

    res = sdk.enrollments_and_agreements.list_entitlements(account_id="01HC3MAQ4DR9QN1V8MJ4CN1HMK", page_size=5, page_token="4ZHd3wAaMD1IQ0ZKS2BKV0FSRVdLW4VLWkY1R1B3MU4")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                     | The account id.                                                                                                                                                                                                                        | 01HC3MAQ4DR9QN1V8MJ4CN1HMK                                                                                                                                                                                                             |
| `page_size`                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                     | The maximum number of entitlements to return.                                                                                                                                                                                          | 5                                                                                                                                                                                                                                      |
| `page_token`                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                     | A page token, received from a previous `ListEntitlements` call. Provide this to retrieve the subsequent page.<br/><br/> When paginating, all other parameters provided to `ListEntitlements` must match the call that provided the page token. | 4ZHd3wAaMD1IQ0ZKS2BKV0FSRVdLW4VLWkY1R1B3MU4                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                    |                                                                                                                                                                                                                                        |

### Response

**[operations.AccountsListEntitlementsResponse](../../models/operations/accountslistentitlementsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |