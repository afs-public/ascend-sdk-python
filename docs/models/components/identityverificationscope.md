# IdentityVerificationScope

Used to determine who is responsible for running identity verification checks, one of:
- `IDENTITY_VERIFICATION_SCOPE_UNSPECIFIED` - Default/Null value.
- `PERFORMED_BY_APEX` - Run CIP and CDD checks.
- `PROVIDED_BY_CLIENT` - Run CDD checks with CIP provided in request.


## Values

| Name                                      | Value                                     |
| ----------------------------------------- | ----------------------------------------- |
| `IDENTITY_VERIFICATION_SCOPE_UNSPECIFIED` | IDENTITY_VERIFICATION_SCOPE_UNSPECIFIED   |
| `PERFORMED_BY_APEX`                       | PERFORMED_BY_APEX                         |
| `PROVIDED_BY_CLIENT`                      | PROVIDED_BY_CLIENT                        |