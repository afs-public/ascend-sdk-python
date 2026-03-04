# OptionInstructions
(*option_instructions*)

## Overview

### Available Operations

* [create_option_instruction](#create_option_instruction) - Create Option Instruction
* [list_option_instructions](#list_option_instructions) - List Option Instructions
* [get_option_instruction](#get_option_instruction) - Get Option Instruction
* [cancel_option_instruction](#cancel_option_instruction) - Cancel Option Instruction

## create_option_instruction

CreateOptionInstruction creates a new option instruction for trading actions

### Example Usage

<!-- UsageSnippet language="python" operationID="ExerciseService_CreateOptionInstruction" method="post" path="/options/v1/accounts/{account_id}/assets/{asset_id}/instructions" -->
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

    res = sdk.option_instructions.create_option_instruction(account_id="ACC123456", asset_id="12345", option_instruction_create={
        "account_id": "01JTNGZM8PWRR6MHBCC6TEG9HE",
        "identifier": "AAPL250620P00090000",
        "identifier_type": components.OptionInstructionCreateIdentifierType.OSI,
        "quantity": {},
        "type": components.OptionInstructionCreateType.DO_NOT_EXERCISE,
    })

    assert res.option_instruction is not None

    # Handle response
    print(res.option_instruction)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `account_id`                                                                             | *str*                                                                                    | :heavy_check_mark:                                                                       | The account id.                                                                          | ACC123456                                                                                |
| `asset_id`                                                                               | *str*                                                                                    | :heavy_check_mark:                                                                       | The asset id.                                                                            | 12345                                                                                    |
| `option_instruction_create`                                                              | [components.OptionInstructionCreate](../../models/components/optioninstructioncreate.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |                                                                                          |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |                                                                                          |

### Response

**[operations.ExerciseServiceCreateOptionInstructionResponse](../../models/operations/exerciseservicecreateoptioninstructionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_option_instructions

ListOptionInstructions lists option instructions with optional filtering and pagination

### Example Usage

<!-- UsageSnippet language="python" operationID="ExerciseService_ListOptionInstructions" method="get" path="/options/v1/accounts/{account_id}/assets/{asset_id}/instructions" -->
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

    res = sdk.option_instructions.list_option_instructions(request={
        "account_id": "ACC123456",
        "asset_id": "12345",
        "page_size": 50,
        "page_token": "eyJvZmZzZXQiOjUwfQ==",
        "filter_": "type == 'DO_NOT_EXERCISE' && account_id == '12345'",
    })

    assert res.list_option_instructions_response is not None

    # Handle response
    print(res.list_option_instructions_response)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.ExerciseServiceListOptionInstructionsRequest](../../models/operations/exerciseservicelistoptioninstructionsrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |

### Response

**[operations.ExerciseServiceListOptionInstructionsResponse](../../models/operations/exerciseservicelistoptioninstructionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_option_instruction

GetOptionInstruction retrieves an existing instruction by name

### Example Usage

<!-- UsageSnippet language="python" operationID="ExerciseService_GetOptionInstruction" method="get" path="/options/v1/accounts/{account_id}/assets/{asset_id}/instructions/{instruction_id}" -->
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

    res = sdk.option_instructions.get_option_instruction(account_id="ACC123456", asset_id="12345", instruction_id="abc12345")

    assert res.option_instruction is not None

    # Handle response
    print(res.option_instruction)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | ACC123456                                                           |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The asset id.                                                       | 12345                                                               |
| `instruction_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The instruction id.                                                 | abc12345                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ExerciseServiceGetOptionInstructionResponse](../../models/operations/exerciseservicegetoptioninstructionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## cancel_option_instruction

CancelOptionInstruction cancels an existing instruction by name

### Example Usage

<!-- UsageSnippet language="python" operationID="ExerciseService_CancelOptionInstruction" method="post" path="/options/v1/accounts/{account_id}/assets/{asset_id}/instructions/{instruction_id}:cancel" -->
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

    res = sdk.option_instructions.cancel_option_instruction(account_id="ACC123456", asset_id="12345", instruction_id="abc12345", cancel_option_instruction_request_create={
        "name": "accounts/ACC123456/assets/12345/instructions/abc12345",
    })

    assert res.option_instruction is not None

    # Handle response
    print(res.option_instruction)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        | Example                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                       | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | The account id.                                                                                                    | ACC123456                                                                                                          |
| `asset_id`                                                                                                         | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | The asset id.                                                                                                      | 12345                                                                                                              |
| `instruction_id`                                                                                                   | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | The instruction id.                                                                                                | abc12345                                                                                                           |
| `cancel_option_instruction_request_create`                                                                         | [components.CancelOptionInstructionRequestCreate](../../models/components/canceloptioninstructionrequestcreate.md) | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |                                                                                                                    |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |                                                                                                                    |

### Response

**[operations.ExerciseServiceCancelOptionInstructionResponse](../../models/operations/exerciseservicecanceloptioninstructionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |