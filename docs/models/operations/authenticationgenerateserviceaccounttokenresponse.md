# AuthenticationGenerateServiceAccountTokenResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `http_meta`                                                        | [components.HTTPMetadata](../../models/components/httpmetadata.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `token`                                                            | [Optional[components.Token]](../../models/components/token.md)     | :heavy_minus_sign:                                                 | OK                                                                 |
| `status`                                                           | [Optional[components.Status]](../../models/components/status.md)   | :heavy_minus_sign:                                                 | INVALID_ARGUMENT: The request was not well formed.                 |