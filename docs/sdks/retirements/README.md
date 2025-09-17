# Retirements
(*retirements*)

## Overview

### Available Operations

* [list_contribution_summaries](#list_contribution_summaries) - List Contribution Summaries
* [retrieve_contribution_constraints](#retrieve_contribution_constraints) - Retrieve Contribution Constraints
* [list_distribution_summaries](#list_distribution_summaries) - List Distribution Summaries
* [retrieve_distribution_constraints](#retrieve_distribution_constraints) - Retrieve Distribution Constraints

## list_contribution_summaries

Lists the aggregated retirement contribution summaries by tax year

### Example Usage

<!-- UsageSnippet language="python" operationID="RetirementConstraints_ListContributionSummaries" method="get" path="/transfers/v1/accounts/{account_id}/contributionSummaries" -->
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

    res = sdk.retirements.list_contribution_summaries(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", page_size=2, page_token="AbTYnwAkMjIyZDNjYTAtZmVjZS00N2Q5LTgyMDctNzI3MDdkMjFiZ3hh")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               | Example                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                              | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The account id.                                                                                                           | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                |
| `page_size`                                                                                                               | *Optional[int]*                                                                                                           | :heavy_minus_sign:                                                                                                        | Number of contribution summaries to get (partitioned by tax year) Default = 2 (current year and prior year), maximum = 10 | 2                                                                                                                         |
| `page_token`                                                                                                              | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | When paginating, this is used to retrieve a specific page from the overall response                                       | AbTYnwAkMjIyZDNjYTAtZmVjZS00N2Q5LTgyMDctNzI3MDdkMjFiZ3hh                                                                  |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |                                                                                                                           |

### Response

**[operations.RetirementConstraintsListContributionSummariesResponse](../../models/operations/retirementconstraintslistcontributionsummariesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## retrieve_contribution_constraints

Retrieves retirement contribution constraints for an account

### Example Usage

<!-- UsageSnippet language="python" operationID="RetirementConstraints_RetrieveContributionConstraints" method="post" path="/transfers/v1/accounts/{account_id}:retrieveContributionConstraints" -->
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

    res = sdk.retirements.retrieve_contribution_constraints(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", retrieve_contribution_constraints_request_create={
        "mechanism": components.Mechanism.ACH,
        "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y",
    })

    assert res.contribution_constraints is not None

    # Handle response
    print(res.contribution_constraints)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        | Example                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                       | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | The account id.                                                                                                                    | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                         |
| `retrieve_contribution_constraints_request_create`                                                                                 | [components.RetrieveContributionConstraintsRequestCreate](../../models/components/retrievecontributionconstraintsrequestcreate.md) | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |                                                                                                                                    |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |                                                                                                                                    |

### Response

**[operations.RetirementConstraintsRetrieveContributionConstraintsResponse](../../models/operations/retirementconstraintsretrievecontributionconstraintsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_distribution_summaries

Lists the aggregated retirement distribution summaries by tax year

### Example Usage

<!-- UsageSnippet language="python" operationID="RetirementConstraints_ListDistributionSummaries" method="get" path="/transfers/v1/accounts/{account_id}/distributionSummaries" -->
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

    res = sdk.retirements.list_distribution_summaries(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", page_size=2, page_token="AbTYnwAkMjIyZDNjYTAtZmVjZS00N2Q5LTgyMDctNzI3MDdkMjFiZ3hh")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               | Example                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                              | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The account id.                                                                                                           | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                |
| `page_size`                                                                                                               | *Optional[int]*                                                                                                           | :heavy_minus_sign:                                                                                                        | Number of distribution summaries to get (partitioned by tax year) Default = 2 (current year and prior year), maximum = 10 | 2                                                                                                                         |
| `page_token`                                                                                                              | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | When paginating, this is used to retrieve a specific page from the overall response                                       | AbTYnwAkMjIyZDNjYTAtZmVjZS00N2Q5LTgyMDctNzI3MDdkMjFiZ3hh                                                                  |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |                                                                                                                           |

### Response

**[operations.RetirementConstraintsListDistributionSummariesResponse](../../models/operations/retirementconstraintslistdistributionsummariesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## retrieve_distribution_constraints

Retrieves retirement distribution constraints for an account

### Example Usage

<!-- UsageSnippet language="python" operationID="RetirementConstraints_RetrieveDistributionConstraints" method="post" path="/transfers/v1/accounts/{account_id}:retrieveDistributionConstraints" -->
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

    res = sdk.retirements.retrieve_distribution_constraints(account_id="01H8FM6EXVH77SAW3TC8KAWMES", retrieve_distribution_constraints_request_create={
        "mechanism": components.RetrieveDistributionConstraintsRequestCreateMechanism.ACH,
        "name": "accounts/01H8FM6EXVH77SAW3TC8KAWMES",
    })

    assert res.distribution_constraints is not None

    # Handle response
    print(res.distribution_constraints)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        | Example                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                       | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | The account id.                                                                                                                    | 01H8FM6EXVH77SAW3TC8KAWMES                                                                                                         |
| `retrieve_distribution_constraints_request_create`                                                                                 | [components.RetrieveDistributionConstraintsRequestCreate](../../models/components/retrievedistributionconstraintsrequestcreate.md) | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |                                                                                                                                    |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |                                                                                                                                    |

### Response

**[operations.RetirementConstraintsRetrieveDistributionConstraintsResponse](../../models/operations/retirementconstraintsretrievedistributionconstraintsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |