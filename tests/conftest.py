import datetime
import os
import random
import time
from typing import Optional
import pytest

import pytz
from typing import Optional
from ascend_sdk import SDK
from ascend_sdk.models import components

from ascend_sdk import SDK
from ascend_sdk.models import components


@pytest.fixture
def current_time():
    ct_timezone = pytz.timezone("America/Chicago")
    return datetime.datetime.now(ct_timezone)


@pytest.fixture(scope="module")
def create_sdk():
    return SDK(
        server_url="https://uat.apexapis.com",
        security=components.Security(
            api_key=os.getenv("API_KEY", ""),
            service_account_creds=components.ServiceAccountCreds(
                private_key=os.getenv("SERVICE_ACCOUNT_CREDS_PRIVATE_KEY", ""),
                name=os.getenv("SERVICE_ACCOUNT_CREDS_NAME", ""),
                organization=os.getenv("SERVICE_ACCOUNT_CREDS_ORGANIZATION", ""),
                type="serviceAccount",
            ),
        ),
    )


@pytest.fixture(scope="module")
def withdrawal_account_id():
    return "01JHGTEPC6ZTAHCFRH2MD3VJJT"


@pytest.fixture(scope="module")
def correspondent_id() -> Optional[str]:
    return os.getenv("CORRESPONDENT_ID")


@pytest.fixture(scope="module")
def create_legal_natural_person_id(create_sdk):
    s = create_sdk
    legal_natural_person_request = components.LegalNaturalPersonCreate(
        birth_date=components.DateCreate(
            year="1981",
            month="3",
            day="13",
        ),
        citizenship_countries=["US"],
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        family_name="Jacob",
        given_name="Bob",
        personal_address=components.PostalAddressCreate(
            locality="Portland",
            region_code="US",
            postal_code="97035",
            administrative_area="OR",
            address_lines=["19409 Sherilyn Courts"],
        ),
        politically_exposed_immediate_family_names=[],
        tax_id="874-45-6789",
        tax_id_type=components.TaxIDType.TAX_ID_TYPE_SSN,
        custodian_employee=False,
        tax_profile=components.TaxProfileCreate(
            federal_tax_classification=components.FederalTaxClassification.INDIV_SOLEPROP_OR_SINGLEMEMBERLLC,
            us_tin_status=components.UsTinStatus.PASSING,
            irs_form_type=components.IrsFormType.W_9,
            legal_tax_region_code="US",
        ),
        employment=components.EmploymentCreate(
            occupation="fisherman",
            employment_status=components.EmploymentStatus.EMPLOYED,
            employer_address=components.PostalAddressCreate(
                administrative_area="OR",
                region_code="US",
                postal_code="97209",
                locality="Portland",
                address_lines=["123 Street"],
            ),
        ),
        identity_verification_result=components.IdentityVerificationResultCreate(
            address_verified=True,
            birth_date_verified=True,
            execution_date=components.DateCreate(
                year="2021",
                month="3",
                day="13",
            ),
            name_verified=True,
            tax_id_verified=True,
            external_case_id="6526280",
            vendor="Super Security Service",
            raw_vendor_data_document_id="04eb923b-793d-481d-98c4-bb16f17378ea",
        ),
    )
    res = s.person_management.create_legal_natural_person(
        request=legal_natural_person_request
    )
    if res.http_meta.response.status_code == 200:
        return res.legal_natural_person.legal_natural_person_id
    else:
        return None


@pytest.fixture(scope="module")
def account_group_id() -> Optional[str]:
    return os.getenv("ACCOUNT_GROUP_ID")


@pytest.fixture(scope="module")
def create_account_id(create_sdk, create_legal_natural_person_id):
    s = create_sdk

    request = components.AccountRequestCreate(
        account_group_id=os.getenv("ACCOUNT_GROUP_ID"),
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        parties=[
            components.PartyRequestCreate(
                legal_natural_person_id=create_legal_natural_person_id,
                relation_type=components.RelationType.PRIMARY_OWNER,
                email_address="mail@example.com",
                phone_number=components.PhoneNumberCreate(
                    e164_number="+14155552671",
                    extension="123",
                ),
                mailing_address=components.PostalAddressCreate(
                    address_lines=["1 Main Street"],
                    region_code="US",
                    postal_code="12345",
                    administrative_area="NY",
                    locality="New York",
                ),
            )
        ],
    )

    res = s.account_creation.create_account(request=request)
    if res.http_meta.response.status_code == 200:
        return res.account.account_id
    else:
        return None


@pytest.fixture(scope="module")
def enroll_account_ids(create_sdk, create_account_id):
    s = create_sdk

    enroll_account_request = components.EnrollAccountRequestCreate(
        enrollment=components.EnrollmentCreate(
            principal_approver_id="01HMESE8WMDNTTWJ2BAEG3TZWA",
            type=components.EnrollmentType.REGISTRATION_INDIVIDUAL,
            individual_enrollment_metadata=components.IndividualEnrollmentMetadataCreate(
                fdic_cash_sweep=components.FdicCashSweep.FDIC_CASH_SWEEP_DECLINE,
            ),
        ),
    )

    res = s.enrollments_and_agreements.enroll_account(
        account_id=create_account_id,
        enroll_account_request_create=enroll_account_request,
    )
    if res.http_meta.response.status_code == 200:
        return (
            res.enroll_account_response.agreements[0].agreement_id,
            res.enroll_account_response.agreements[1].agreement_id,
        )


@pytest.fixture(scope="module")
def enrolled_account_id(create_sdk, create_account_id, enroll_account_ids):
    s = create_sdk

    affirm_agreements_request = components.AffirmAgreementsRequestCreate(
        account_agreement_ids=enroll_account_ids
    )

    res = s.enrollments_and_agreements.affirm_agreements(
        account_id=create_account_id,
        affirm_agreements_request_create=affirm_agreements_request,
    )
    if res.http_meta.response.status_code == 200:
        return create_account_id
    else:
        return None


@pytest.fixture(scope="module")
def create_bank_relationship_id(create_sdk, enrolled_account_id):
    s = create_sdk

    bank_relationship_request = components.BankRelationshipCreate(
        bank_account=components.BankAccountCreate(
            account_number=str(random.randint(10000000, 99999999)),
            owner="TEST123",
            routing_number="112203216",
            type=components.BankAccountCreateType.SAVINGS,
        ),
        nickname="ACH TEST",
        verification_method=components.VerificationMethod.MICRO_DEPOSIT,
    )

    res = s.bank_relationships.create_bank_relationship(
        account_id=enrolled_account_id,
        bank_relationship_create=bank_relationship_request,
    )
    if res.http_meta.response.status_code == 200:
        return res.bank_relationship.name.split("/")[3]
    else:
        return None


@pytest.fixture(scope="module")
def verified_bank_relationship_id(
    create_sdk, enrolled_account_id, create_bank_relationship_id
):
    s = create_sdk

    res = s.test_simulation.get_micro_deposit_amounts(
        account_id=enrolled_account_id, bank_relationship_id=create_bank_relationship_id
    )

    micro_deposits_request = components.VerifyMicroDepositsRequestCreate(
        amounts=components.MicroDepositAmountsCreate(
            amount1=components.DecimalCreate(
                value=res.micro_deposit_amounts.amount1.value
            ),
            amount2=components.DecimalCreate(
                value=res.micro_deposit_amounts.amount2.value
            ),
        ),
        name=f"accounts/{enrolled_account_id}/bankRelationships/{create_bank_relationship_id}",
    )

    res = s.bank_relationships.verify_micro_deposits(
        account_id=enrolled_account_id,
        bank_relationship_id=create_bank_relationship_id,
        verify_micro_deposits_request_create=micro_deposits_request,
    )
    if res.http_meta.response.status_code == 200:
        return create_bank_relationship_id
    else:
        return False
