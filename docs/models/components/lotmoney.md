# LotMoney

Object containing currency/ price information for the trade lot


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `currency_code`                                                              | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Currency code of the price                                                   | USD                                                                          |
| `price`                                                                      | [OptionalNullable[components.LotPrice]](../../models/components/lotprice.md) | :heavy_minus_sign:                                                           | Price of the trade lot                                                       | {<br/>"value": "0.25"<br/>}                                                  |