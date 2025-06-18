# ExemptCustomerReason

**Field Dependencies:**

Exempt entities must set `exempt_verifying_beneficial_owners` to `true` and provide an `exempt_customer_reason` on the owner record.

Required if `exempt_verifying_beneficial_owners` is `true`.

Otherwise, must be empty.


## Values

| Name                                                       | Value                                                      |
| ---------------------------------------------------------- | ---------------------------------------------------------- |
| `EXEMPT_REASON_UNSPECIFIED`                                | EXEMPT_REASON_UNSPECIFIED                                  |
| `REGULATED_FINANCIAL_INSTITUTION`                          | REGULATED_FINANCIAL_INSTITUTION                            |
| `DEPARTMENT_OR_AGENCY_OF_FEDERAL_STATE_OR_SUBDIVISION`     | DEPARTMENT_OR_AGENCY_OF_FEDERAL_STATE_OR_SUBDIVISION       |
| `NON_BANK_LISTED_ENTITY`                                   | NON_BANK_LISTED_ENTITY                                     |
| `SECTION_12_SECURITIES_EXCHANGE_ACT_1934_OR_15_D`          | SECTION_12_SECURITIES_EXCHANGE_ACT_1934_OR_15D             |
| `SECTION_3_INVESTMENT_COMPANY_ACT_1940`                    | SECTION_3_INVESTMENT_COMPANY_ACT_1940                      |
| `SECTION_202_A_INVESTMENT_ADVISORS_ACT_1940`               | SECTION_202A_INVESTMENT_ADVISORS_ACT_1940                  |
| `SECTION_3_SECURITIES_EXCHANGE_ACT_1934_SECTION_6_OR_17_A` | SECTION_3_SECURITIES_EXCHANGE_ACT_1934_SECTION_6_OR_17A    |
| `ANY_OTHER_SECURITIES_EXCHANGE_ACT_1934`                   | ANY_OTHER_SECURITIES_EXCHANGE_ACT_1934                     |
| `COMMODITY_FUTURES_TRADING_COMMISSION_REGISTERED`          | COMMODITY_FUTURES_TRADING_COMMISSION_REGISTERED            |
| `PUBLIC_ACCOUNTING_FIRM_SECTION_102_SARBANES_OXLEY`        | PUBLIC_ACCOUNTING_FIRM_SECTION_102_SARBANES_OXLEY          |
| `STATE_REGULATED_INSURANCE_COMPANY`                        | STATE_REGULATED_INSURANCE_COMPANY                          |