# SanctionsListDetail

Sanctions list detail used for Dow Jones Profile details


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `end_day`                                                | *Optional[str]*                                          | :heavy_minus_sign:                                       | Dow Jones day persons will be taken off sanctions list   | 1                                                        |
| `end_month`                                              | *Optional[str]*                                          | :heavy_minus_sign:                                       | Dow Jones month persons will be taken off sanctions list | June                                                     |
| `end_year`                                               | *Optional[str]*                                          | :heavy_minus_sign:                                       | Dow Jones year persons will be taken off sanctions list  | 2025                                                     |
| `sanctions_reference_description`                        | *Optional[str]*                                          | :heavy_minus_sign:                                       | Dow Jones persons sanctions ref id                       | OFAC - Specially Designated National List                |
| `start_day`                                              | *Optional[str]*                                          | :heavy_minus_sign:                                       | Dow Jones day persons were added to the sanctions list   | 1                                                        |
| `start_month`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | Dow Jones month persons were added to the sanctions list | June                                                     |
| `start_year`                                             | *Optional[str]*                                          | :heavy_minus_sign:                                       | Dow Jones year persons were added to the sanctions list  | 2020                                                     |