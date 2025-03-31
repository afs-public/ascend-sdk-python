# ActivityRoundingAdjustment

Used to record rounding adjustments when the sum(price x quantity) of all entries for a given activity do not equal the price x quantity of the fully formed activity record


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `rounding_reason`                                  | *Optional[str]*                                    | :heavy_minus_sign:                                 | Free form text field providing reason for rounding | Trade Rounding                                     |