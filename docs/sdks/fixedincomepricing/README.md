# FixedIncomePricing
(*fixed_income_pricing*)

## Overview

### Available Operations

* [preview_order_cost](#preview_order_cost) - Preview Order Cost
* [retrieve_quote](#retrieve_quote) - Retrieve Quote
* [retrieve_fixed_income_marks](#retrieve_fixed_income_marks) - Retrieve Fixed Income Marks

## preview_order_cost

Returns a calculation estimating the costs involved in ordering a given quantity of a Fixed Income asset at a specified limit price.

### Example Usage

<!-- UsageSnippet language="python" operationID="OrderPriceService_PreviewOrderCost" method="post" path="/trading/v1/accounts/{account_id}/orders:previewOrderCost" -->
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

    res = sdk.fixed_income_pricing.preview_order_cost(account_id="<id>", order_cost_preview_request_create=components.OrderCostPreviewRequestCreate(
        asset_type=components.OrderCostPreviewRequestCreateAssetType.FIXED_INCOME,
        identifier="37833100",
        identifier_type=components.OrderCostPreviewRequestCreateIdentifierType.CUSIP,
        limit_price=components.LimitPriceCreate(
            price=components.DecimalCreate(),
            type=components.LimitPriceCreateType.PRICE_PER_UNIT,
        ),
        parent="<value>",
        quantity=components.DecimalCreate(),
    ))

    assert res.order_cost_preview_response is not None

    # Handle response
    print(res.order_cost_preview_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | The account id.                                                                                      |
| `order_cost_preview_request_create`                                                                  | [components.OrderCostPreviewRequestCreate](../../models/components/ordercostpreviewrequestcreate.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.OrderPriceServicePreviewOrderCostResponse](../../models/operations/orderpriceservicepreviewordercostresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## retrieve_quote

Returns quote information containing the best bid/ask for the given Fixed Income asset.

### Example Usage

<!-- UsageSnippet language="python" operationID="OrderPriceService_RetrieveQuote" method="post" path="/trading/v1/accounts/{account_id}/orders:retrieveAssetQuote" -->
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

    res = sdk.fixed_income_pricing.retrieve_quote(account_id="<id>", retrieve_quote_request_create={
        "asset_type": components.RetrieveQuoteRequestCreateAssetType.FIXED_INCOME,
        "identifier": "37833100",
        "identifier_type": components.RetrieveQuoteRequestCreateIdentifierType.CUSIP,
        "parent": "<value>",
    })

    assert res.retrieve_quote_response is not None

    # Handle response
    print(res.retrieve_quote_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `account_id`                                                                                   | *str*                                                                                          | :heavy_check_mark:                                                                             | The account id.                                                                                |
| `retrieve_quote_request_create`                                                                | [components.RetrieveQuoteRequestCreate](../../models/components/retrievequoterequestcreate.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.OrderPriceServiceRetrieveQuoteResponse](../../models/operations/orderpriceserviceretrievequoteresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## retrieve_fixed_income_marks

Returns marks for a specified set of Fixed Income assets (up to 100 per request)

### Example Usage

<!-- UsageSnippet language="python" operationID="OrderPriceService_RetrieveFixedIncomeMarks" method="post" path="/trading/v1/correspondents/{correspondent_id}/prices:retrieveFixedIncomeMarks" -->
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

    res = sdk.fixed_income_pricing.retrieve_fixed_income_marks(correspondent_id="<id>", retrieve_fixed_income_marks_request_create={
        "parent": "<value>",
        "security_identifiers": [
            {
                "identifier": "US0378331005",
                "identifier_type": components.RetrieveFixedIncomeMarksRequestSecurityIdentifiersCreateIdentifierType.ISIN,
            },
            {
                "identifier": "38259P508",
                "identifier_type": components.RetrieveFixedIncomeMarksRequestSecurityIdentifiersCreateIdentifierType.CUSIP,
            },
        ],
    })

    assert res.retrieve_fixed_income_marks_response is not None

    # Handle response
    print(res.retrieve_fixed_income_marks_response)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `correspondent_id`                                                                                                   | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The correspondent id.                                                                                                |
| `retrieve_fixed_income_marks_request_create`                                                                         | [components.RetrieveFixedIncomeMarksRequestCreate](../../models/components/retrievefixedincomemarksrequestcreate.md) | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.OrderPriceServiceRetrieveFixedIncomeMarksResponse](../../models/operations/orderpriceserviceretrievefixedincomemarksresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |