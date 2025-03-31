# AvailableRestriction

Available Restriction on an Account.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `description`                                                                  | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The description of the restriction.                                            | A full outbound transfer of assets was initiated through ACATS or other means. |
| `display_name`                                                                 | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The human readable representation of the restriction code.                     | Account Transfer Request Received - Full Outbound                              |
| `restriction_code`                                                             | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The restriction code.                                                          | ACAT_FULL_OUTBOUND                                                             |