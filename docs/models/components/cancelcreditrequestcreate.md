# CancelCreditRequestCreate

Request to cancel an existing credit


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | The name of the credit to cancel                           | accounts/01H8FB90ZRRFWXB4XC2JPJ1D4Y/credits/20230823123456 |
| `reason`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | The optional reason about why the credit is being canceled | Reverse previous credit                                    |