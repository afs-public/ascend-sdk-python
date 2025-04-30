# RebookTradeResponse

A response for the rebook trade method.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `new_trade`                                                                            | [OptionalNullable[components.NewTrade]](../../models/components/newtrade.md)           | :heavy_minus_sign:                                                                     | The new trade that is booked.                                                          |
| `original_trade`                                                                       | [OptionalNullable[components.OriginalTrade]](../../models/components/originaltrade.md) | :heavy_minus_sign:                                                                     | The original trade that was rebooked.                                                  |