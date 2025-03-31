# AssetCreate

The asset being transferred If cash, the asset_id is the currency code (e.g. USD) and the position is the amount


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `identifier`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | The asset identifier                                                     | US37733W2044                                                             |
| `position`                                                               | [components.PositionCreate](../../models/components/positioncreate.md)   | :heavy_check_mark:                                                       | The position or amount of the asset                                      |                                                                          |
| `type`                                                                   | [components.AssetCreateType](../../models/components/assetcreatetype.md) | :heavy_check_mark:                                                       | The asset identifier type                                                | CUSIP                                                                    |