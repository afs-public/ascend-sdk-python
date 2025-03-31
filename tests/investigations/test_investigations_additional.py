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

    assert (
        len(identity_verification_results) > 0
    ), "No identity verification results found"

    identity_verification_result = identity_verification_results[0]

    assert identity_verification_result.customer_identification_id is not None

    res = s.investigations.get_customer_identification(
        correspondent_id=correspondent_id,
        customer_identification_id=identity_verification_result.customer_identification_id,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
