# DataRetrieval
(*data_retrieval*)

## Overview

### Available Operations

* [list_snapshots](#list_snapshots) - List Snapshots

## list_snapshots

Returns details of a list of snapshots.

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

res = s.data_retrieval.list_snapshots()

if res.list_snapshots_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                     | Type                                                                                                                                                                          | Required                                                                                                                                                                      | Description                                                                                                                                                                   | Example                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_`                                                                                                                                                                     | *Optional[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                            | A CEL string to filter snapshot results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; | snapshot_type=="daily_accounts"&&process_date==date("2023-09-30")                                                                                                             |
| `page_size`                                                                                                                                                                   | *Optional[int]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                            | The number of snapshots to be returned per page. Defaults to 500. Maximum is 1000.                                                                                            | 500                                                                                                                                                                           |
| `page_token`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                            | The token for retrieving the next page of snapshots, the value of which will have been returned in a previous response.                                                       | M_-BAwEBCVBhZ2VUb2tlbgH_ggABAgEMUnVubmluZ1RvdGFsAQQAAQZGaWx0ZXIBDAAAAAX_ggEyAA==                                                                                              |
| `retries`                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                           |                                                                                                                                                                               |

### Response

**[operations.SnapshotsListSnapshotsResponse](../../models/operations/snapshotslistsnapshotsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 500    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |