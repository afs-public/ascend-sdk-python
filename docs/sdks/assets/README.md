# Assets
(*assets*)

## Overview

### Available Operations

* [list_assets](#list_assets) - List Assets
* [get_asset](#get_asset) - Get Asset
* [list_assets_correspondent](#list_assets_correspondent) - List Assets (By Correspondent)
* [get_asset_correspondent](#get_asset_correspondent) - Get Asset (By Correspondent)

## list_assets

Lists assets

### Example Usage

<!-- UsageSnippet language="python" operationID="Assets_ListAssets_1" method="get" path="/assets/v1/assets" -->
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

    res = sdk.assets.list_assets(parent="correspondents/1234", page_size=100, page_token="Mv-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAD_-CAfzrRtzkAQQ1MDA3AA==", filter_="(symbol == 'IBM' && usable) || symbol == 'USD'")

    assert res.list_assets_response is not None

    # Handle response
    print(res.list_assets_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `parent`                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | The parent resource name, which is the correspondent ID.                                                                                                                                                                                                          | correspondents/1234                                                                                                                                                                                                                                               |
| `page_size`                                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | The maximum number of assets to return. The service may return fewer than this value. Default is 100 (subject to change) The maximum is 1000, values exceeding this will be set to 1000 (subject to change)                                                       | 100                                                                                                                                                                                                                                                               |
| `page_token`                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | A page token, received from a previous `ListAssets` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAssets` must match the call that provided the page token in order to maintain a stable result set. | Mv-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAD_-CAfzrRtzkAQQ1MDA3AA==                                                                                                                                                                      |
| `filter_`                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information;                                                                                              | (symbol == 'IBM' && usable) \|\| symbol == 'USD'                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                               |                                                                                                                                                                                                                                                                   |

### Response

**[operations.AssetsListAssets1Response](../../models/operations/assetslistassets1response.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_asset

Gets assets

### Example Usage

<!-- UsageSnippet language="python" operationID="Assets_GetAsset" method="get" path="/assets/v1/assets/{asset_id}" -->
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

    res = sdk.assets.get_asset(asset_id="8395")

    assert res.asset is not None

    # Handle response
    print(res.asset)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The asset id.                                                       | 8395                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AssetsGetAssetResponse](../../models/operations/assetsgetassetresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## list_assets_correspondent

Lists assets

### Example Usage

<!-- UsageSnippet language="python" operationID="Assets_ListAssets_Correspondent" method="get" path="/assets/v1/correspondents/{correspondent_id}/assets" -->
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

    res = sdk.assets.list_assets_correspondent(correspondent_id="1234", page_size=100, page_token="Mv-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAD_-CAfzrRtzkAQQ1MDA3AA==", filter_="(symbol == 'IBM' && usable) || symbol == 'USD'")

    assert res.list_assets_response is not None

    # Handle response
    print(res.list_assets_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `correspondent_id`                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                | The correspondent id.                                                                                                                                                                                                                                             | 1234                                                                                                                                                                                                                                                              |
| `page_size`                                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | The maximum number of assets to return. The service may return fewer than this value. Default is 100 (subject to change) The maximum is 1000, values exceeding this will be set to 1000 (subject to change)                                                       | 100                                                                                                                                                                                                                                                               |
| `page_token`                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | A page token, received from a previous `ListAssets` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAssets` must match the call that provided the page token in order to maintain a stable result set. | Mv-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAD_-CAfzrRtzkAQQ1MDA3AA==                                                                                                                                                                      |
| `filter_`                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information;                                                                                              | (symbol == 'IBM' && usable) \|\| symbol == 'USD'                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                               |                                                                                                                                                                                                                                                                   |

### Response

**[operations.AssetsListAssetsCorrespondentResponse](../../models/operations/assetslistassetscorrespondentresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |

## get_asset_correspondent

Gets assets

### Example Usage

<!-- UsageSnippet language="python" operationID="Assets_GetAsset_Correspondent" method="get" path="/assets/v1/correspondents/{correspondent_id}/assets/{asset_id}" -->
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

    res = sdk.assets.get_asset_correspondent(correspondent_id="8395", asset_id="<id>")

    assert res.asset is not None

    # Handle response
    print(res.asset)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `correspondent_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The correspondent id.                                               | 8395                                                                |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The asset id.                                                       |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AssetsGetAssetCorrespondentResponse](../../models/operations/assetsgetassetcorrespondentresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 403, 404    | application/json |
| errors.Status    | 500, 503         | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |