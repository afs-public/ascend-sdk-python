# ReaderGetEventMessageResponse


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `http_meta`                                                                  | [components.HTTPMetadata](../../models/components/httpmetadata.md)           | :heavy_check_mark:                                                           | N/A                                                                          |
| `event_message`                                                              | [Optional[components.EventMessage]](../../models/components/eventmessage.md) | :heavy_minus_sign:                                                           | OK                                                                           |
| `status`                                                                     | [Optional[components.Status]](../../models/components/status.md)             | :heavy_minus_sign:                                                           | INVALID_ARGUMENT: The request was not well formed.                           |