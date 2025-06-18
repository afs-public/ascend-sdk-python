# ~~BookingLotMoney~~

Deprecated; use the price field instead

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `currency_code`                                                                                      | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  | USD                                                                                                  |
| `price`                                                                                              | [OptionalNullable[components.BookingLotMoneyPrice]](../../models/components/bookinglotmoneyprice.md) | :heavy_minus_sign:                                                                                   | N/A                                                                                                  | {<br/>"value": "2.50"<br/>}                                                                          |