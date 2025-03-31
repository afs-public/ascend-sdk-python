# ForceReturnAchDepositRequestCreate

Request to force a Nacha return on a completed ACH deposit. FOR TESTING ONLY!


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `nacha_return`                                                               | [components.NachaReturnCreate](../../models/components/nachareturncreate.md) | :heavy_check_mark:                                                           | A return on an ACH transfer from the Nacha network.                          |                                                                              |
| `name`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | The name of the ACH deposit to force a Nacha return on.                      | accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/achDeposits/20230817000319               |