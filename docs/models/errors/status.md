# Status

The status message serves as the general-purpose service error message. Each status message includes a gRPC error code, error message, and error details.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The code field contains an enum value of google.rpc.Code.           |
| `details`                                                           | List[[components.AnyT](../../models/components/anyt.md)]            | :heavy_minus_sign:                                                  | The details field contains one or more technical error details.     |
| `message`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The message field contains human-friendly messages about the error. |