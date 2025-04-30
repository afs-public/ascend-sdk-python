# BondYield

A percentage yield


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `percent`                                                                                | [OptionalNullable[components.Percent]](../../models/components/percent.md)               | :heavy_minus_sign:                                                                       | The percentage yield.                                                                    | {<br/>"value": "25.00"<br/>}                                                             |
| `yield_type`                                                                             | [Optional[components.BondYieldYieldType]](../../models/components/bondyieldyieldtype.md) | :heavy_minus_sign:                                                                       | The type of yield.                                                                       | YIELD_TO_MATURITY                                                                        |