# IctWithdrawalsGetIctWithdrawalResponse


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `http_meta`                                                                    | [components.HTTPMetadata](../../models/components/httpmetadata.md)             | :heavy_check_mark:                                                             | N/A                                                                            |
| `ict_withdrawal`                                                               | [Optional[components.IctWithdrawal]](../../models/components/ictwithdrawal.md) | :heavy_minus_sign:                                                             | OK                                                                             |
| `status`                                                                       | [Optional[components.Status]](../../models/components/status.md)               | :heavy_minus_sign:                                                             | INVALID_ARGUMENT: The request has an invalid argument.                         |