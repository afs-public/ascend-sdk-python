# AssetTradability

Indicators to determine what types of orders allowed to be traded


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `close_fractional_quantity_enabled`                              | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Indicates whether fractional quantities are allowed to be closed | true                                                             |
| `close_notional_quantity_enabled`                                | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Indicates whether notional quantities are allowed to be closed   | true                                                             |
| `close_whole_quantity_enabled`                                   | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Indicates whether whole quantities are allowed to be closed      | true                                                             |
| `open_fractional_quantity_enabled`                               | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Indicates whether fractional quantities are allowed to be opened | true                                                             |
| `open_notional_quantity_enabled`                                 | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Indicates whether notional quantities are allowed to be opened   | true                                                             |
| `open_whole_quantity_enabled`                                    | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Indicates whether whole quantities are allowed to be opened      | true                                                             |