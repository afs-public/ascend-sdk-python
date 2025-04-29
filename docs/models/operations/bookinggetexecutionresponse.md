# BookingGetExecutionResponse


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `http_meta`                                                            | [components.HTTPMetadata](../../models/components/httpmetadata.md)     | :heavy_check_mark:                                                     | N/A                                                                    |
| `execution`                                                            | [Optional[components.Execution]](../../models/components/execution.md) | :heavy_minus_sign:                                                     | OK                                                                     |
| `status`                                                               | [Optional[components.Status]](../../models/components/status.md)       | :heavy_minus_sign:                                                     | INVALID_ARGUMENT: The request is not valid.                            |