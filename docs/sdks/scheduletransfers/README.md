# ScheduleTransfers
(*schedule_transfers*)

## Overview

### Available Operations

* [list_schedule_summaries](#list_schedule_summaries) - List Schedule Summaries
* [create_ach_deposit_schedule](#create_ach_deposit_schedule) - Create ACH Deposit Schedule
* [list_ach_deposit_schedules](#list_ach_deposit_schedules) - List ACH Deposit Schedules
* [get_ach_deposit_schedule](#get_ach_deposit_schedule) - Get ACH Deposit Schedule
* [update_ach_deposit_schedule](#update_ach_deposit_schedule) - Update ACH Deposit Schedules
* [cancel_ach_deposit_schedule](#cancel_ach_deposit_schedule) - Cancel ACH Deposit Schedule
* [create_ach_withdrawal_schedule](#create_ach_withdrawal_schedule) - Create ACH Withdrawal Schedule
* [list_ach_withdrawal_schedules](#list_ach_withdrawal_schedules) - List ACH Withdrawal Schedules
* [get_ach_withdrawal_schedule](#get_ach_withdrawal_schedule) - Get ACH Withdrawal Schedule
* [update_ach_withdrawal_schedule](#update_ach_withdrawal_schedule) - Update ACH Withdrawal Schedule
* [cancel_ach_withdrawal_schedule](#cancel_ach_withdrawal_schedule) - Cancel ACH Withdrawal Schedule
* [create_wire_withdrawal_schedule](#create_wire_withdrawal_schedule) - Create Wire Withdrawal Schedule
* [list_wire_withdrawal_schedules](#list_wire_withdrawal_schedules) - List Wire Withdrawal Schedules
* [get_wire_withdrawal_schedule](#get_wire_withdrawal_schedule) - Get Wire Withdrawal Schedule
* [update_wire_withdrawal_schedule](#update_wire_withdrawal_schedule) - Update Wire Withdrawal Schedule
* [cancel_wire_withdrawal_schedule](#cancel_wire_withdrawal_schedule) - Cancel Wire Withdrawal Schedule

## list_schedule_summaries

Lists transfer schedule summaries that match the filter in the request

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

res = s.schedule_transfers.list_schedule_summaries()

if res.list_schedule_summaries_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_`                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                   | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:<br/> `account`<br/> `mechanism`<br/> `direction`<br/> `state`<br/> `start_date`<br/> `end_date` | mechanism == 'ACH' && direction == DEPOSIT && state == 'ACTIVE' && start_date > '2024-04-05' && end_date < '2024-08-10'                                                                                                                                              |
| `page_size`                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                   | The maximum number of schedules to return. The service may return fewer than this value. If unspecified, at most 25 schedules will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.                                                | 100                                                                                                                                                                                                                                                                  |
| `page_token`                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                   | The page token to request                                                                                                                                                                                                                                            | 4ZHd3wAaMD1IQ0ZKS2BKV0FSRVdLW4VLWkY1R1B3MU4                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                      |

### Response

**[operations.TransferScheduleSummariesListScheduleSummariesResponse](../../models/operations/transferschedulesummarieslistschedulesummariesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## create_ach_deposit_schedule

Creates an ACH deposit transfer schedule

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

res = s.schedule_transfers.create_ach_deposit_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_schedule_create={
    "bank_relationship": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/bankRelationships/651ef9de0dee00240813e60e",
    "schedule_details": {
        "amount": {},
        "client_schedule_id": "ABC-123",
        "schedule_properties": {
            "start_date": {},
            "time_unit": components.TimeUnit.MONTH,
            "unit_multiplier": 1,
        },
    },
})

if res.ach_deposit_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `account_id`                                                                               | *str*                                                                                      | :heavy_check_mark:                                                                         | The account id.                                                                            | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                 |
| `ach_deposit_schedule_create`                                                              | [components.AchDepositScheduleCreate](../../models/components/achdepositschedulecreate.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |                                                                                            |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |                                                                                            |

### Response

**[operations.AchDepositSchedulesCreateAchDepositScheduleResponse](../../models/operations/achdepositschedulescreateachdepositscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_ach_deposit_schedules

Return a list of ACH deposit schedules for the specified account and filter params

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

res = s.schedule_transfers.list_ach_deposit_schedules(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y")

if res.list_ach_deposit_schedules_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                              | The account id.                                                                                                                                                                                                                 | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                                                                                                                      |
| `filter_`                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:<br/> `state`<br/> `start_date`<br/> `end_date` | state == 'ACTIVE' && start_date > '2024-04-05' && end_date < '2024-08-10'                                                                                                                                                       |
| `page_size`                                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | The maximum number of schedules to return. The service may return fewer than this value. If unspecified, at most 25 schedules will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.           | 100                                                                                                                                                                                                                             |
| `page_token`                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | The page token to request                                                                                                                                                                                                       | 4ZHd3wAaMD1IQ0ZKS2BKV0FSRVdLW4VLWkY1R1B3MU4                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                             |                                                                                                                                                                                                                                 |

### Response

**[operations.AchDepositSchedulesListAchDepositSchedulesResponse](../../models/operations/achdepositscheduleslistachdepositschedulesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_ach_deposit_schedule

Gets an ACH deposit transfer schedule

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

res = s.schedule_transfers.get_ach_deposit_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_schedule_id="40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1")

if res.ach_deposit_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `ach_deposit_schedule_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | The achDepositSchedule id.                                          | 40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AchDepositSchedulesGetAchDepositScheduleResponse](../../models/operations/achdepositschedulesgetachdepositscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## update_ach_deposit_schedule

Updates the amount of an ACH deposit transfer schedule

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

res = s.schedule_transfers.update_ach_deposit_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_schedule_id="40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1", ach_deposit_schedule_update={})

if res.ach_deposit_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               | Example                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                              | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The account id.                                                                                                           | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                |
| `ach_deposit_schedule_id`                                                                                                 | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The achDepositSchedule id.                                                                                                | 40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1                                                                                      |
| `ach_deposit_schedule_update`                                                                                             | [components.AchDepositScheduleUpdate](../../models/components/achdepositscheduleupdate.md)                                | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |                                                                                                                           |
| `update_mask`                                                                                                             | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | A field mask representing the update. Note: only the 'schedule_details.amount' field of a schedule is currently updatable |                                                                                                                           |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |                                                                                                                           |

### Response

**[operations.AchDepositSchedulesUpdateAchDepositScheduleResponse](../../models/operations/achdepositschedulesupdateachdepositscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_ach_deposit_schedule

Cancels an ACH deposit transfer schedule

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

res = s.schedule_transfers.cancel_ach_deposit_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_deposit_schedule_id="40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1", cancel_ach_deposit_schedule_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achDepositSchedules/40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1",
})

if res.ach_deposit_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                         | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The account id.                                                                                                      | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                           |
| `ach_deposit_schedule_id`                                                                                            | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The achDepositSchedule id.                                                                                           | 40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1                                                                                 |
| `cancel_ach_deposit_schedule_request_create`                                                                         | [components.CancelAchDepositScheduleRequestCreate](../../models/components/cancelachdepositschedulerequestcreate.md) | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |                                                                                                                      |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |                                                                                                                      |

### Response

**[operations.AchDepositSchedulesCancelAchDepositScheduleResponse](../../models/operations/achdepositschedulescancelachdepositscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## create_ach_withdrawal_schedule

Creates an ACH withdrawal transfer schedule

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

res = s.schedule_transfers.create_ach_withdrawal_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_schedule_create={
    "bank_relationship": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/bankRelationships/651ef9de0dee00240813e60e",
    "schedule_details": {
        "client_schedule_id": "ABC-123",
        "schedule_properties": {
            "start_date": {},
            "time_unit": components.TimeUnit.MONTH,
            "unit_multiplier": 1,
        },
    },
})

if res.ach_withdrawal_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                     | *str*                                                                                            | :heavy_check_mark:                                                                               | The account id.                                                                                  | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                       |
| `ach_withdrawal_schedule_create`                                                                 | [components.AchWithdrawalScheduleCreate](../../models/components/achwithdrawalschedulecreate.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |                                                                                                  |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |                                                                                                  |

### Response

**[operations.AchWithdrawalSchedulesCreateAchWithdrawalScheduleResponse](../../models/operations/achwithdrawalschedulescreateachwithdrawalscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_ach_withdrawal_schedules

Return a list of ACH withdrawal schedules for the specified account and filter params

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

res = s.schedule_transfers.list_ach_withdrawal_schedules(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y")

if res.list_ach_withdrawal_schedules_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                              | The account id.                                                                                                                                                                                                                 | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                                                                                                                      |
| `filter_`                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:<br/> `state`<br/> `start_date`<br/> `end_date` | state == 'ACTIVE' && start_date > '2024-04-05' && end_date < '2024-08-10'                                                                                                                                                       |
| `page_size`                                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | The maximum number of schedules to return. The service may return fewer than this value. If unspecified, at most 25 schedules will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.           | 100                                                                                                                                                                                                                             |
| `page_token`                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | The page token to request                                                                                                                                                                                                       | 4ZHd3wAaMD1IQ0ZKS2BKV0FSRVdLW4VLWkY1R1B3MU4                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                             |                                                                                                                                                                                                                                 |

### Response

**[operations.AchWithdrawalSchedulesListAchWithdrawalSchedulesResponse](../../models/operations/achwithdrawalscheduleslistachwithdrawalschedulesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_ach_withdrawal_schedule

Gets an ACH withdrawal transfer schedule

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

res = s.schedule_transfers.get_ach_withdrawal_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_schedule_id="40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1")

if res.ach_withdrawal_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `ach_withdrawal_schedule_id`                                        | *str*                                                               | :heavy_check_mark:                                                  | The achWithdrawalSchedule id.                                       | 40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AchWithdrawalSchedulesGetAchWithdrawalScheduleResponse](../../models/operations/achwithdrawalschedulesgetachwithdrawalscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## update_ach_withdrawal_schedule

Updates the amount of an ACH withdrawal transfer schedule

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

res = s.schedule_transfers.update_ach_withdrawal_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_schedule_id="40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1", ach_withdrawal_schedule_update={})

if res.ach_withdrawal_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               | Example                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                              | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The account id.                                                                                                           | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                |
| `ach_withdrawal_schedule_id`                                                                                              | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The achWithdrawalSchedule id.                                                                                             | 40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1                                                                                      |
| `ach_withdrawal_schedule_update`                                                                                          | [components.AchWithdrawalScheduleUpdate](../../models/components/achwithdrawalscheduleupdate.md)                          | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |                                                                                                                           |
| `update_mask`                                                                                                             | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | A field mask representing the update. Note: only the 'schedule_details.amount' field of a schedule is currently updatable |                                                                                                                           |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |                                                                                                                           |

### Response

**[operations.AchWithdrawalSchedulesUpdateAchWithdrawalScheduleResponse](../../models/operations/achwithdrawalschedulesupdateachwithdrawalscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_ach_withdrawal_schedule

Cancels an ACH withdrawal transfer schedule

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

res = s.schedule_transfers.cancel_ach_withdrawal_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", ach_withdrawal_schedule_id="40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1", cancel_ach_withdrawal_schedule_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achWithdrawalSchedules/40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1",
})

if res.ach_withdrawal_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                | Example                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | The account id.                                                                                                            | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                 |
| `ach_withdrawal_schedule_id`                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | The achWithdrawalSchedule id.                                                                                              | 40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1                                                                                       |
| `cancel_ach_withdrawal_schedule_request_create`                                                                            | [components.CancelAchWithdrawalScheduleRequestCreate](../../models/components/cancelachwithdrawalschedulerequestcreate.md) | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |                                                                                                                            |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |                                                                                                                            |

### Response

**[operations.AchWithdrawalSchedulesCancelAchWithdrawalScheduleResponse](../../models/operations/achwithdrawalschedulescancelachwithdrawalscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## create_wire_withdrawal_schedule

Creates a Wire withdrawal transfer schedule

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

res = s.schedule_transfers.create_wire_withdrawal_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", wire_withdrawal_schedule_create={
    "beneficiary": {
        "account": "73849218650987",
    },
    "recipient_bank": {
        "bank_id": {
            "id": "ABNANL2AXXX",
            "type": components.RecipientBankBankIDCreateType.BIC,
        },
    },
    "schedule_details": {
        "client_schedule_id": "ABC-123",
        "schedule_properties": {
            "start_date": {},
            "time_unit": components.TimeUnit.MONTH,
            "unit_multiplier": 1,
        },
    },
})

if res.wire_withdrawal_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                       | *str*                                                                                              | :heavy_check_mark:                                                                                 | The account id.                                                                                    | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                         |
| `wire_withdrawal_schedule_create`                                                                  | [components.WireWithdrawalScheduleCreate](../../models/components/wirewithdrawalschedulecreate.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |                                                                                                    |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |                                                                                                    |

### Response

**[operations.WireWithdrawalSchedulesCreateWireWithdrawalScheduleResponse](../../models/operations/wirewithdrawalschedulescreatewirewithdrawalscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_wire_withdrawal_schedules

Return a list of Wire withdrawal schedules for the specified account and filter params

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

res = s.schedule_transfers.list_wire_withdrawal_schedules(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y")

if res.list_wire_withdrawal_schedules_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                              | The account id.                                                                                                                                                                                                                 | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                                                                                                                      |
| `filter_`                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:<br/> `state`<br/> `start_date`<br/> `end_date` | state == 'ACTIVE' && start_date > '2024-04-05' && end_date < '2024-08-10'                                                                                                                                                       |
| `page_size`                                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | The maximum number of schedules to return. The service may return fewer than this value. If unspecified, at most 25 schedules will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.           | 100                                                                                                                                                                                                                             |
| `page_token`                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                              | The page token to request                                                                                                                                                                                                       | 4ZHd3wAaMD1IQ0ZKS2BKV0FSRVdLW4VLWkY1R1B3MU4                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                             |                                                                                                                                                                                                                                 |

### Response

**[operations.WireWithdrawalSchedulesListWireWithdrawalSchedulesResponse](../../models/operations/wirewithdrawalscheduleslistwirewithdrawalschedulesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_wire_withdrawal_schedule

Gets a Wire withdrawal transfer schedule

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

res = s.schedule_transfers.get_wire_withdrawal_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", wire_withdrawal_schedule_id="40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1")

if res.wire_withdrawal_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `wire_withdrawal_schedule_id`                                       | *str*                                                               | :heavy_check_mark:                                                  | The wireWithdrawalSchedule id.                                      | 40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.WireWithdrawalSchedulesGetWireWithdrawalScheduleResponse](../../models/operations/wirewithdrawalschedulesgetwirewithdrawalscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## update_wire_withdrawal_schedule

Updates the amount of a Wire withdrawal transfer schedule

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

res = s.schedule_transfers.update_wire_withdrawal_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", wire_withdrawal_schedule_id="40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1", wire_withdrawal_schedule_update={})

if res.wire_withdrawal_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               | Example                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                              | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The account id.                                                                                                           | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                |
| `wire_withdrawal_schedule_id`                                                                                             | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The wireWithdrawalSchedule id.                                                                                            | 40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1                                                                                      |
| `wire_withdrawal_schedule_update`                                                                                         | [components.WireWithdrawalScheduleUpdate](../../models/components/wirewithdrawalscheduleupdate.md)                        | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |                                                                                                                           |
| `update_mask`                                                                                                             | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | A field mask representing the update. Note: only the 'schedule_details.amount' field of a schedule is currently updatable | {<br/>"update_mask": "schedule_details.amount"<br/>}                                                                      |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |                                                                                                                           |

### Response

**[operations.WireWithdrawalSchedulesUpdateWireWithdrawalScheduleResponse](../../models/operations/wirewithdrawalschedulesupdatewirewithdrawalscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## cancel_wire_withdrawal_schedule

Cancels a Wire withdrawal transfer schedule

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

res = s.schedule_transfers.cancel_wire_withdrawal_schedule(account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", wire_withdrawal_schedule_id="40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1", cancel_wire_withdrawal_schedule_request_create={
    "name": "accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/wireWithdrawalSchedules/40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1",
})

if res.wire_withdrawal_schedule is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  | Example                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                 | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | The account id.                                                                                                              | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                   |
| `wire_withdrawal_schedule_id`                                                                                                | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | The wireWithdrawalSchedule id.                                                                                               | 40eb6b6f-76ff-4dc9-b8a0-b65a7658f8b1                                                                                         |
| `cancel_wire_withdrawal_schedule_request_create`                                                                             | [components.CancelWireWithdrawalScheduleRequestCreate](../../models/components/cancelwirewithdrawalschedulerequestcreate.md) | :heavy_check_mark:                                                                                                           | N/A                                                                                                                          |                                                                                                                              |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |                                                                                                                              |

### Response

**[operations.WireWithdrawalSchedulesCancelWireWithdrawalScheduleResponse](../../models/operations/wirewithdrawalschedulescancelwirewithdrawalscheduleresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |