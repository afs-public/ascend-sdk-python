# MicroDepositAmounts

The micro deposits sent to verify a pending bank relationship. FOR TESTING ONLY!


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `amount1`                                                                  | [OptionalNullable[components.Amount1]](../../models/components/amount1.md) | :heavy_minus_sign:                                                         | The amount of one of the micro deposits.                                   | {<br/>"value": "0.03"<br/>}                                                |
| `amount2`                                                                  | [OptionalNullable[components.Amount2]](../../models/components/amount2.md) | :heavy_minus_sign:                                                         | The amount of the other micro deposit.                                     | {<br/>"value": "0.67"<br/>}                                                |