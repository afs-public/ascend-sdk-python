# Fee


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `amount`                                                                 | [OptionalNullable[components.Amount]](../../models/components/amount.md) | :heavy_minus_sign:                                                       | Monetary amount associated with the fee                                  | {<br/>"value": "0.25"<br/>}                                              |
| `type`                                                                   | [Optional[components.FeeType]](../../models/components/feetype.md)       | :heavy_minus_sign:                                                       | The type of fee being assessed                                           | LIQUIDITY                                                                |