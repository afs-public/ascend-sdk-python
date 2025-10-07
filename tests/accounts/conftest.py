import time

from ascend_sdk.models import components
import pytest
import os


@pytest.fixture(scope="module")
def large_trader_id():
    return "123456789100"


@pytest.fixture(scope="module")
def assign_large_trader_id(create_sdk, create_legal_natural_person_id, large_trader_id):
    s = create_sdk

    large_trader_request = components.AssignLargeTraderRequestCreate(
        large_trader_id=large_trader_id,
    )
    res = s.person_management.assign_large_trader(
        legal_natural_person_id=create_legal_natural_person_id,
        assign_large_trader_request_create=large_trader_request,
    )
    if res.http_meta.response.status_code == 200:
        return res.large_trader.large_trader_id
    else:
        return None


@pytest.fixture(scope="module")
def create_legal_entity_id(create_sdk):
    s = create_sdk

    legal_entity_request = components.LegalEntityCreate(
        accredited_investor=False,
        adviser=False,
        brokerDealer=False,
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        entity_name="AcmeInc",
        entity_type=components.EntityType.ESTATE,
        exempt_verifying_beneficial_owners=False,
        foreign_financial_institution=False,
        legal_address=components.PostalAddressCreate(
            address_lines=["19409 Sherilyn Courts"],
            administrative_area="OR",
            locality="Portland",
            postal_code="97035",
            region_code="US",
        ),
        lei_code="12340012345678911000",
        operating_regions=["US"],
        registration_region="US",
        tax_id="987-65-4321",
        tax_id_type=components.LegalEntityCreateTaxIDType.TAX_ID_TYPE_ITIN,
        tax_profile=components.TaxProfileCreate(
            federal_tax_classification=components.FederalTaxClassification.TRUST_ESTATE,
            us_tin_status=components.UsTinStatus.PASSING,
            irs_form_type=components.IrsFormType.W_9,
            legal_tax_region_code="US",
        ),
    )
    res = s.person_management.create_legal_entity(request=legal_entity_request)
    if res.http_meta.response.status_code == 200:
        return res.legal_entity.legal_entity_id
    else:
        return None


@pytest.fixture(scope="module")
def add_party_id(create_sdk, create_account_id, create_legal_entity_id):
    s = create_sdk

    party_request = components.AddPartyRequestCreate(
        authorized_by_party_ids=[
            "8096110d-fb55-4f9d-b883-b84f0b70d3ea",
            "8096110d-fb55-4f9d-b883-b84f0b70d3rb",
        ],
        parent=f"accounts/{create_account_id}",
        party=components.PartyRequestCreate(
            email_address="example@domain.com",
            mailing_address=components.PostalAddressCreate(
                address_lines=["123 Main St"],
                administrative_area="CA",
                locality="San Francisco",
                postal_code="12345",
                region_code="US",
            ),
            phone_number=components.PhoneNumberCreate(
                e164_number="+14155552671",
            ),
            legal_entity_id=create_legal_entity_id,
            relation_type=components.RelationType.PRIMARY_OWNER,
        ),
    )

    res = s.account_management.add_party(
        account_id=create_account_id, add_party_request_create=party_request
    )
    if res.http_meta.response.status_code == 200:
        return res.party.party_id
    else:
        return None


@pytest.fixture(scope="module")
def get_enrollment_to_deactivate(create_sdk, create_account_id):
    s = create_sdk

    res = s.enrollments_and_agreements.list_enrollments(account_id=create_account_id)

    enrollments = res.list_enrollments_response.enrollments
    if enrollments:
        for enrollment in enrollments:
            if enrollment.type == "DIVIDEND_REINVESTMENT_PLAN":
                return enrollment.enrollment_id
    return None


@pytest.fixture(scope="module")
def replace_party_id(
    create_sdk, create_account_id, create_legal_natural_person_id, add_party_id
):
    s = create_sdk

    party_request = components.ReplacePartyRequestCreate(
        authorized_by_party_ids=[
            "8096110d-fb55-4f9d-b883-b84f0b70d3ea",
            "8096110d-fb55-4f9d-b883-b84f0b70d3rb",
        ],
        name=f"accounts/{create_account_id}/parties/{add_party_id}",
        party=components.PartyRequestCreate(
            email_address="example@domain.com",
            mailing_address=components.PostalAddressCreate(
                address_lines=["123 Main St"],
                administrative_area="CA",
                locality="San Francisco",
                postal_code="12345",
                region_code="US",
            ),
            phone_number=components.PhoneNumberCreate(
                e164_number="+14155552671",
            ),
            legal_natural_person_id=create_legal_natural_person_id,
            relation_type=components.RelationType.PRIMARY_OWNER,
        ),
    )

    res = s.account_management.replace_party(
        account_id=create_account_id,
        party_id=add_party_id,
        replace_party_request_create=party_request,
    )
    if res.http_meta.response.status_code == 200:
        return res.party.party_id
    else:
        return None


@pytest.fixture(scope="module")
def create_trusted_contact_id(create_sdk, create_account_id):
    s = create_sdk

    trusted_contact_request = components.TrustedContactCreate(
        email_address="example@email.com",
        family_name="Doe",
        given_name="John",
        middle_names="Larry",
        phone_number=components.PhoneNumberCreate(
            e164_number="+14155552671",
        ),
    )

    res = s.account_management.create_trusted_contact(
        account_id=create_account_id, trusted_contact_create=trusted_contact_request
    )
    if res.http_meta.response.status_code == 200:
        return res.trusted_contact.trusted_contact_id
    else:
        return None


@pytest.fixture(scope="module")
def create_interested_party_id(create_sdk, create_account_id):
    s = create_sdk

    interested_party_request = components.InterestedPartyCreate(
        mailing_address=components.PostalAddressCreate(
            address_lines=["123 Main St"],
            administrative_area="CA",
            locality="San Francisco",
            postal_code="12345",
            region_code="US",
        ),
        recipient="John Dough",
    )

    res = s.account_management.create_interested_party(
        account_id=create_account_id, interested_party_create=interested_party_request
    )
    if res.http_meta.response.status_code == 200:
        return res.interested_party.interested_party_id
    else:
        return None


@pytest.fixture(scope="module")
def create_restriction_code(create_sdk, create_account_id):
    s = create_sdk

    restriction_request = components.RestrictionCreate(
        create_reason="Some reason for creating",
        ended_reason="Some reason for removing",
        restriction_code="TRADING_LIQUIDATION_ONLY_BY_CORRESPONDENT",
    )

    res = s.account_management.create_restriction(
        account_id=create_account_id, restriction_create=restriction_request
    )
    if res.http_meta.response.status_code == 200:
        return res.restriction.restriction_code
    else:
        return None
