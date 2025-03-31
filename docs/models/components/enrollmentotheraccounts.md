# EnrollmentOtherAccounts

A customer-disclosed list of other Apex-held accounts owned by the Entity applicant at the time of this account's application; expressed as zero, one, or many account numbers


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `account_names`                      | List[*str*]                          | :heavy_minus_sign:                   | Other account names held at Apex     |                                      |
| `account_numbers`                    | List[*str*]                          | :heavy_minus_sign:                   | Other account numbers held at Apex   |                                      |
| `owner_has_other_accounts_at_apex`   | *Optional[bool]*                     | :heavy_minus_sign:                   | The owner has other accounts at Apex | true                                 |