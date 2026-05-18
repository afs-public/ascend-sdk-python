# AvailableEnrollment

Available Enrollment on an Account.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `agreements`                                                                     | List[[components.LegalAgreement](../../models/components/legalagreement.md)]     | :heavy_minus_sign:                                                               | A list of legal agreements associated with the enrollment.                       |                                                                                  |
| `enrollment_type`                                                                | [Optional[components.EnrollmentType]](../../models/components/enrollmenttype.md) | :heavy_minus_sign:                                                               | The enrollment type.                                                             | REGISTRATION_INDIVIDUAL                                                          |