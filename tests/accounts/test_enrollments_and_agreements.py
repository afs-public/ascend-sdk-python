import time
from pytest import fail
from ascend_sdk.models import components


def test_enrollments_and_agreements_accounts_enroll_account_enroll_account1(
    enroll_account_ids,
):
    assert enroll_account_ids is not None


def test_enrollments_and_agreements_list_available_enrollments_list_available_enrollments1(
    create_sdk,
    create_account_id,
):
    s = create_sdk

    assert s is not None
    res = s.enrollments_and_agreements.list_available_enrollments(
        account_id=create_account_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_enrollments_and_agreements_list_enrollments_list_enrollments1(
    create_sdk,
    create_account_id,
):
    s = create_sdk

    assert s is not None
    res = s.enrollments_and_agreements.list_enrollments(account_id=create_account_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_enrollments_and_agreements_affirm_agreements_affirm_agreements1(
    create_sdk, create_account_id, enroll_account_ids
):
    s = create_sdk

    assert s is not None

    affirm_agreements_request = components.AffirmAgreementsRequestCreate(
        account_agreement_ids=enroll_account_ids
    )

    res = s.enrollments_and_agreements.affirm_agreements(
        account_id=create_account_id,
        affirm_agreements_request_create=affirm_agreements_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_enrollments_and_agreements_list_agreements_list_agreements1(
    create_sdk,
    create_account_id,
):
    s = create_sdk

    assert s is not None
    res = s.enrollments_and_agreements.list_agreements(account_id=create_account_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_enrollments_and_agreements_list_entitlements_list_entitlements1(
    create_sdk,
    create_account_id,
):
    s = create_sdk

    assert s is not None
    res = s.enrollments_and_agreements.list_entitlements(account_id=create_account_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_enrollments_and_agreements_deactivate_enrollment_deactivate_enrollment1(
    create_sdk,
    create_account_id,
    get_enrollment_to_deactivate,
):
    s = create_sdk

    assert s is not None

    deactivate_enrollment_request = components.DeactivateEnrollmentRequestCreate(
        enrollment_id=get_enrollment_to_deactivate,
    )

    res = s.enrollments_and_agreements.deactivate_enrollment(
        account_id=create_account_id,
        deactivate_enrollment_request_create=deactivate_enrollment_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_enrollments_and_agreements_accounts__list_available_enrollments_by_account_group_accounts__list_available_enrollments_by_account_group1(
    create_sdk, account_group_id
):
    s = create_sdk

    assert s is not None

    if not account_group_id:
        fail("Account group ID is required")

    res = s.enrollments_and_agreements.accounts_list_available_enrollments_by_account_group(
        account_group_id=account_group_id
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
