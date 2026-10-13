# AcatsPreviewTransferExternalAccount

The contra-broker account the holdings are transferring from, ready to use as the delivering party of a transfer.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `account_number`                                                      | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | The account identifier The account number for external communications | 1234567890                                                            |
| `account_title`                                                       | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Account owner title                                                   | John Doe & Jane Doe JTWROS                                            |
| `participant_number`                                                  | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | The NSCC brokerage / clearing house identifier                        | 987                                                                   |