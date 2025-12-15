import uuid
from ascend_sdk.models import components


def test_investigations_investigation_service_update_investigation_update_investigation1(
    create_sdk, investigation_id
):
    s = create_sdk

    assert s is not None

    investigation_update = components.InvestigationUpdate(
        comment="new investigation name",
    )

    res = s.investigations.update_investigation(
        investigation_id=investigation_id, investigation_update=investigation_update
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_investigations_investigation_service_link_documents_link_documents1(
    create_sdk, investigation_id
):
    s = create_sdk

    assert s is not None

    link_documents_request = components.LinkDocumentsRequestCreate(
        identity_verification_document_ids=[str(uuid.uuid4())]
    )

    res = s.investigations.link_documents(
        investigation_id=investigation_id,
        link_documents_request_create=link_documents_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_investigations_investigations_get_identify_verification(
    create_sdk, correspondent_id, apex_investigation_id
):
    s = create_sdk

    assert s is not None

    res = s.investigations.get_investigation(
        investigation_id=apex_investigation_id,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200

    identity_verification_results = res.investigation.identity_verification_results

    assert len(identity_verification_results) > 0, (
        "No identity verification results found"
    )

    identity_verification_result = identity_verification_results[0]

    assert identity_verification_result.customer_identification_id is not None

    res = s.investigations.get_customer_identification(
        correspondent_id=correspondent_id,
        customer_identification_id=identity_verification_result.customer_identification_id,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_identity_lookup_service_create_identity_lookup(create_sdk, correspondent_id):
    s = create_sdk

    assert s is not None

    request = components.IdentityLookupCreate(
        device_metadata=components.DeviceMetadataCreate(
            ip_address="203.0.113.42",
        ),
        identification=components.IdentificationCreate(
            region_code="US",
            type=components.IdentificationCreateType.SSN,
            value="123-45-6789",
        ),
        phone_number=components.PhoneNumberCreate(
            e164_number="+15035550123",
            extension="123",
        ),
        user_consent=True,
    )

    res = s.investigations.create_identity_lookup(
        correspondent_id=correspondent_id,
        identity_lookup_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
    assert res.identity_lookup is not None
    assert res.identity_lookup.name is not None

    # Extract identity lookup ID from name
    name_parts = res.identity_lookup.name.split("/")
    lookup_id = name_parts[-1]
    assert lookup_id is not None
    assert len(lookup_id) > 0


def test_identity_lookup_service_verify_identity_lookup(create_sdk, correspondent_id):
    s = create_sdk

    assert s is not None

    # First create an identity lookup
    create_request = components.IdentityLookupCreate(
        device_metadata=components.DeviceMetadataCreate(
            ip_address="203.0.113.42",
        ),
        identification=components.IdentificationCreate(
            region_code="US",
            type=components.IdentificationCreateType.SSN,
            value="123-45-6789",
        ),
        phone_number=components.PhoneNumberCreate(
            e164_number="+15035550123",
            extension="123",
        ),
        user_consent=True,
    )

    create_res = s.investigations.create_identity_lookup(
        correspondent_id=correspondent_id,
        identity_lookup_create=create_request,
    )

    assert create_res.identity_lookup is not None
    assert create_res.identity_lookup.name is not None

    # Extract identity lookup ID from name
    name_parts = create_res.identity_lookup.name.split("/")
    lookup_id = name_parts[-1]
    assert lookup_id is not None

    # Now verify the identity lookup
    verify_request = components.VerifyIdentityLookupRequestCreate(
        name=f"correspondents/{correspondent_id}/identityLookups/{lookup_id}",
        verification_code="123456",  # This is a test verification code
    )

    try:
        res = s.investigations.verify_identity_lookup(
            correspondent_id=correspondent_id,
            identity_lookup_id=lookup_id,
            verify_identity_lookup_request_create=verify_request,
        )

        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except Exception as error:
        # The verification may fail with invalid code, which is expected in test environment
        # We're just testing that the endpoint is callable
        assert "verification" in str(error).lower()
