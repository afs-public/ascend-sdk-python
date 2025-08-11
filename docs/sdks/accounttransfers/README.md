# AccountTransfers
(*account_transfers*)

## Overview

### Available Operations

* [create_transfer](#create_transfer) - Create Transfer
* [list_transfers](#list_transfers) - List Transfers
* [accept_transfer](#accept_transfer) - Accept Transfer
* [reject_transfer](#reject_transfer) - Reject Transfer
* [get_transfer](#get_transfer) - Get Transfer

## create_transfer

Creates a transfer

### Example Usage

<!-- UsageSnippet language="python" operationID="AccountTransfers_CreateTransfer" method="post" path="/acats/v1/correspondents/{correspondent_id}/accounts/{account_id}/transfers" -->
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

    res = sdk.account_transfers.create_transfer(correspondent_id="00000000-0000-0000-0000-000000000002", account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", transfer_create={
        "deliverer": {},
    }, request_id="ABC-123")

    assert res.acats_transfer is not None

    # Handle response
    print(res.acats_transfer)

```

### Parameters

| Parameter                                                                                                                                                                                                  | Type                                                                                                                                                                                                       | Required                                                                                                                                                                                                   | Description                                                                                                                                                                                                | Example                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `correspondent_id`                                                                                                                                                                                         | *str*                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                         | The correspondent id.                                                                                                                                                                                      | 00000000-0000-0000-0000-000000000002                                                                                                                                                                       |
| `account_id`                                                                                                                                                                                               | *str*                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                         | The account id.                                                                                                                                                                                            | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                                                                                                                                 |
| `transfer_create`                                                                                                                                                                                          | [components.TransferCreate](../../models/components/transfercreate.md)                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                         | N/A                                                                                                                                                                                                        |                                                                                                                                                                                                            |
| `request_id`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                         | A client-specified ID for the account transfer; no specific pattern is imposed. This field is used for idempotency to ensure that repeated requests with the same ID do not result in duplicate transfers. | ABC-123                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                        |                                                                                                                                                                                                            |

### Response

**[operations.AccountTransfersCreateTransferResponse](../../models/operations/accounttransferscreatetransferresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 409    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_transfers

Lists existing transfers using a CEL filter.

### Example Usage

<!-- UsageSnippet language="python" operationID="AccountTransfers_ListTransfers" method="get" path="/acats/v1/correspondents/{correspondent_id}/accounts/{account_id}/transfers" -->
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

    res = sdk.account_transfers.list_transfers(request={
        "correspondent_id": "00000000-0000-0000-0000-000000000002",
        "account_id": "01FAKEACCOUNT",
        "page_size": 25,
        "page_token": "CgwI5uHttgYQyJXO2wESJDAxOTFjOTMxLTA3YjMtYzU0ZC0yMDNmLWU1M2U0OTBkY2FhZRoicmVjZWl2ZXIuYWNjb3VudF9pZCBpbiBbJzEwMDAwQUEnXQ",
        "filter_": "deliverer.account_number == \"R9AHY8P\"",
    })

    assert res.list_transfers_response is not None

    # Handle response
    print(res.list_transfers_response)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.AccountTransfersListTransfersRequest](../../models/operations/accounttransferslisttransfersrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.AccountTransfersListTransfersResponse](../../models/operations/accounttransferslisttransfersresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## accept_transfer

Accept one side (incoming/outgoing) of an internal Ascend transfer. When both the incoming side and outgoing side of the transfer have been accepted then bookkeeping is done immediately. If neither, or only one side of a transfer is accepted, then both sides of the internal perform bookkeeping one full settlement day after they went into the bookkeeping queue.

### Example Usage

<!-- UsageSnippet language="python" operationID="AccountTransfers_AcceptTransfer" method="post" path="/acats/v1/correspondents/{correspondent_id}/accounts/{account_id}/transfers/{transfer_id}:accept" -->
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

    res = sdk.account_transfers.accept_transfer(correspondent_id="00000000-0000-0000-0000-000000000002", account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", transfer_id="00000000-0000-0000-0000-000000000000", accept_transfer_request_create={
        "name": "correspondents/00000000-0000-0000-0000-000000000002/accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/transfers/00000000-0000-0000-0000-000000000000",
    })

    assert res.accept_transfer_response is not None

    # Handle response
    print(res.accept_transfer_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `correspondent_id`                                                                               | *str*                                                                                            | :heavy_check_mark:                                                                               | The correspondent id.                                                                            | 00000000-0000-0000-0000-000000000002                                                             |
| `account_id`                                                                                     | *str*                                                                                            | :heavy_check_mark:                                                                               | The account id.                                                                                  | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                       |
| `transfer_id`                                                                                    | *str*                                                                                            | :heavy_check_mark:                                                                               | The transfer id.                                                                                 | 00000000-0000-0000-0000-000000000000                                                             |
| `accept_transfer_request_create`                                                                 | [components.AcceptTransferRequestCreate](../../models/components/accepttransferrequestcreate.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |                                                                                                  |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |                                                                                                  |

### Response

**[operations.AccountTransfersAcceptTransferResponse](../../models/operations/accounttransfersaccepttransferresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## reject_transfer

Reject one side (incoming/outgoing) of an internal Ascend transfer. Rejecting one side automatically moves the contra side of the transfer to be rejected as well.

### Example Usage

<!-- UsageSnippet language="python" operationID="AccountTransfers_RejectTransfer" method="post" path="/acats/v1/correspondents/{correspondent_id}/accounts/{account_id}/transfers/{transfer_id}:reject" -->
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

    res = sdk.account_transfers.reject_transfer(correspondent_id="00000000-0000-0000-0000-000000000002", account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", transfer_id="00000000-0000-0000-0000-000000000000", reject_transfer_request_create={
        "name": "correspondents/00000000-0000-0000-0000-000000000002/accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/transfers/00000000-0000-0000-0000-000000000000",
    })

    assert res.reject_transfer_response is not None

    # Handle response
    print(res.reject_transfer_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `correspondent_id`                                                                               | *str*                                                                                            | :heavy_check_mark:                                                                               | The correspondent id.                                                                            | 00000000-0000-0000-0000-000000000002                                                             |
| `account_id`                                                                                     | *str*                                                                                            | :heavy_check_mark:                                                                               | The account id.                                                                                  | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                                                       |
| `transfer_id`                                                                                    | *str*                                                                                            | :heavy_check_mark:                                                                               | The transfer id.                                                                                 | 00000000-0000-0000-0000-000000000000                                                             |
| `reject_transfer_request_create`                                                                 | [components.RejectTransferRequestCreate](../../models/components/rejecttransferrequestcreate.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |                                                                                                  |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |                                                                                                  |

### Response

**[operations.AccountTransfersRejectTransferResponse](../../models/operations/accounttransfersrejecttransferresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403         | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_transfer

Gets an existing transfer

### Example Usage

<!-- UsageSnippet language="python" operationID="AccountTransfers_GetTransfer" method="get" path="/acats/v1/correspondents/{correspondent_id}/accounts/{account_id}/transfers/{transfer_id}" -->
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

    res = sdk.account_transfers.get_transfer(correspondent_id="00000000-0000-0000-0000-000000000002", account_id="01H8FB90ZRRFWXB4XC2JPJ1D4Y", transfer_id="00000000-0000-0000-0000-000000000000")

    assert res.acats_transfer is not None

    # Handle response
    print(res.acats_transfer)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `correspondent_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The correspondent id.                                               | 00000000-0000-0000-0000-000000000002                                |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account id.                                                     | 01H8FB90ZRRFWXB4XC2JPJ1D4Y                                          |
| `transfer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The transfer id.                                                    | 00000000-0000-0000-0000-000000000000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AccountTransfersGetTransferResponse](../../models/operations/accounttransfersgettransferresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |