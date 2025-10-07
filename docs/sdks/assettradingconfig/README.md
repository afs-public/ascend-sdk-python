# AssetTradingConfig
(*asset_trading_config*)

## Overview

### Available Operations

* [get_asset_trading_config](#get_asset_trading_config) - Get Asset Trading Config
* [list_asset_trading_configs](#list_asset_trading_configs) - List Asset Trading Configs

## get_asset_trading_config

Gets an asset trading config by asset_id `/assettradingconfig/v1/correspondents/{correspondent_id}/assets/{asset_id}/tradingConfig`

### Example Usage

<!-- UsageSnippet language="python" operationID="AssetTradingConfigService_GetAssetTradingConfig" method="get" path="/assettradingconfig/v1/correspondents/{correspondent_id}/assets/{asset_id}/tradingConfig" -->
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

    res = sdk.asset_trading_config.get_asset_trading_config(correspondent_id="01HBRQ5BW6ZAY4BNWP4GWRD80X", asset_id="612")

    assert res.asset_trading_config is not None

    # Handle response
    print(res.asset_trading_config)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `correspondent_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The correspondent id.                                               | 01HBRQ5BW6ZAY4BNWP4GWRD80X                                          |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The asset id.                                                       | 612                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.AssetTradingConfigServiceGetAssetTradingConfigResponse](../../models/operations/assettradingconfigservicegetassettradingconfigresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.Status      | 400, 401, 403, 404 | application/json   |
| errors.Status      | 500, 503           | application/json   |
| errors.SDKError    | 4XX, 5XX           | \*/\*              |

## list_asset_trading_configs

Retrieve a list of asset trading configs `/assettradingconfig/v1/correspondents/{correspondent_id}/assets/-/tradingConfigs`

### Example Usage

<!-- UsageSnippet language="python" operationID="AssetTradingConfigService_ListAssetTradingConfigs" method="get" path="/assettradingconfig/v1/correspondents/{correspondent_id}/assets/{asset_id}/tradingConfigs" -->
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

    res = sdk.asset_trading_config.list_asset_trading_configs(request={
        "correspondent_id": "01HBRQ5BW6ZAY4BNWP4GWRD80X",
        "asset_id": "",
        "page_size": 100,
        "page_token": "Mv-BAwEBCVBhZ2VUb2tlbgH_ggABAgEPUmVxdWVzdENoZWNrc3VtAQYAAQJJZAEMAAAAD_-CAfzrRtzkAQQ1MDA3AA==",
        "filter_": "symbol == 'SBUX' && asset_type == 'EQUITY'",
    })

    assert res.list_asset_trading_configs_response is not None

    # Handle response
    print(res.list_asset_trading_configs_response)

```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.AssetTradingConfigServiceListAssetTradingConfigsRequest](../../models/operations/assettradingconfigservicelistassettradingconfigsrequest.md) | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |
| `retries`                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                         | :heavy_minus_sign:                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                      |

### Response

**[operations.AssetTradingConfigServiceListAssetTradingConfigsResponse](../../models/operations/assettradingconfigservicelistassettradingconfigsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Status    | 400, 401, 403    | application/json |
| errors.Status    | 500, 503, 504    | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |