# EntityDueDiligenceUpdate

Due Diligence for Legal Entities required when a Legal Entity is the Primary Owner on an Account.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `entity_issues_bearer_shares`                                                            | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Indicates whether the entity issues bearer shares                                        | false                                                                                    |
| `negative_news`                                                                          | [Optional[components.NegativeNewsUpdate]](../../models/components/negativenewsupdate.md) | :heavy_minus_sign:                                                                       | Negative News detail.                                                                    |                                                                                          |