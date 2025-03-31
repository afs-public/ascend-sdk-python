# Credit

Used to disburse funds into a customer's account, typically for purposes such as refunds, interest payments, or rewards from enrolled programs and details related to the credit


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `additional_instructions`                                                 | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Free form text field providing additional information about a transaction | FDIC sweep interest payment                                               |
| `credit_type`                                                             | [Optional[components.CreditType]](../../models/components/credittype.md)  | :heavy_minus_sign:                                                        | Provides more details on the type of credit                               | WRITE_OFF                                                                 |
| `taxable`                                                                 | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Indicates whether the credit is taxable                                   | false                                                                     |