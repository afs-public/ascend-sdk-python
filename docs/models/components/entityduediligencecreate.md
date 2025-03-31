# EntityDueDiligenceCreate

Due Diligence for Legal Entities required when a Legal Entity is the Primary Owner on an Account.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `entity_issues_bearer_shares`                                                  | *bool*                                                                         | :heavy_check_mark:                                                             | Indicates whether the entity issues bearer shares                              | false                                                                          |
| `negative_news`                                                                | [components.NegativeNewsCreate](../../models/components/negativenewscreate.md) | :heavy_check_mark:                                                             | Negative News detail.                                                          |                                                                                |