# LinkDocumentsResponse

Custom response - returns identity verification documentIds added to investigation request


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `identity_verification_document_ids`                                                 | List[*str*]                                                                          | :heavy_minus_sign:                                                                   | Document IDs from identity verification result object                                | 0f01ae1f-d24c-4171-8f3f-c0b820bf3044                                                 |
| `name`                                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Required: The ID of the investigation The format is "investigations/{investigation}" | investigations/01HEWVF4ZSNKYRP293J53ASJCJ                                            |