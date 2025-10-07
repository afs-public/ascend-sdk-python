from ascend_sdk.models import components
import time


def test_person_management_accounts_create_legal_natural_person_create_legal_natural_person1(
    create_legal_natural_person_id,
):
    assert create_legal_natural_person_id is not None


def test_person_management_accounts_get_legal_natural_person_get_legal_natural_person1(
    create_sdk,
    create_legal_natural_person_id,
):
    s = create_sdk

    assert s is not None
    res = s.person_management.get_legal_natural_person(
        legal_natural_person_id=create_legal_natural_person_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_person_management_accounts_update_legal_natural_person_update_legal_natural_person1(
    create_sdk,
    create_legal_natural_person_id,
):
    s = create_sdk

    assert s is not None

    legal_natural_person_request = components.LegalNaturalPersonUpdate(
        marital_status=components.LegalNaturalPersonUpdateMaritalStatus.MARRIED,
    )

    res = s.person_management.update_legal_natural_person(
        legal_natural_person_id=create_legal_natural_person_id,
        legal_natural_person_update=legal_natural_person_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_person_management_accounts_assign_large_trader_assign_large_trader1(
    assign_large_trader_id,
):
    assert assign_large_trader_id is not None


def test_person_management_accounts_end_large_trader_end_large_trader1(
    create_sdk,
    create_legal_natural_person_id,
):
    s = create_sdk

    assert s is not None
    end_large_trader_request = components.EndLargeTraderRequestCreate(
        end_reason=components.EndReason.EVENT_REASON_CREATED,
    )
    res = s.person_management.end_large_trader_legal_natural_person(
        legal_natural_person_id=create_legal_natural_person_id,
        end_large_trader_request_create=end_large_trader_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_person_management_accounts_create_legal_entity_create_legal_entity1(
    create_legal_entity_id,
):
    assert create_legal_entity_id is not None


def test_person_management_accounts_get_legal_entity_get_legal_entity1(
    create_sdk,
    create_legal_entity_id,
):
    s = create_sdk

    assert s is not None

    res = s.person_management.get_legal_entity(legal_entity_id=create_legal_entity_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_person_management_accounts_update_legal_entity_update_legal_entity1(
    create_sdk,
    create_legal_entity_id,
):
    s = create_sdk

    assert s is not None

    legal_entity_request = components.LegalEntityUpdate(
        entity_name="John Doe",
    )

    res = s.person_management.update_legal_entity(
        legal_entity_id=create_legal_entity_id, legal_entity_update=legal_entity_request
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_person_management_accounts_assign_large_trader_legal_entity_assign_large_trader_legal_entity1(
    create_sdk, create_legal_entity_id, assign_large_trader_id
):
    s = create_sdk

    assert s is not None

    large_trader_request = components.AssignLargeTraderRequestCreate(
        large_trader_id=assign_large_trader_id,
    )

    res = s.person_management.assign_large_trader_legal_entity(
        legal_entity_id=create_legal_entity_id,
        assign_large_trader_request_create=large_trader_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_person_management_accounts_end_large_trader_legal_entity_end_large_trader_legal_entity1(
    create_sdk,
    create_legal_entity_id,
):
    s = create_sdk

    assert s is not None

    end_large_trader_request = components.EndLargeTraderRequestCreate(
        end_reason=components.EndReason.EVENT_REASON_CREATED,
    )

    res = s.person_management.end_large_trader(
        legal_entity_id=create_legal_entity_id,
        end_large_trader_request_create=end_large_trader_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
