import time

from ascend_sdk.models import components


def test_retirements_transfers_list_contribution_summaries_list_contribution_summaries1(
    create_sdk,
    create_account_id,
):
    time.sleep(5)
    s = create_sdk

    assert s is not None
    res = s.retirements.list_contribution_summaries(account_id=create_account_id)

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_retirements_transfers_retrieve_contribution_constraints_retrieve_contribution_constraints1(
    create_sdk,
    create_account_id,
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    request = components.RetrieveContributionConstraintsRequestCreate(
        mechanism=components.Mechanism.ACH, name="accounts/" + create_account_id
    )
    res = s.retirements.retrieve_contribution_constraints(
        account_id=create_account_id,
        retrieve_contribution_constraints_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_retirements_transfers_retrieve_distribution_constraints_retrieve_distribution_constraints1(
    create_sdk,
    create_account_id,
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    request = components.RetrieveDistributionConstraintsRequestCreate(
        mechanism=components.Mechanism.ACH, name="accounts/" + create_account_id
    )
    res = s.retirements.retrieve_distribution_constraints(
        account_id=create_account_id,
        retrieve_distribution_constraints_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_retirements_transfers_list_distribution_summaries_list_distribution_summaries1(
    create_sdk,
    create_account_id,
):
    s = create_sdk
    assert s is not None
    res = s.retirements.list_distribution_summaries(
        account_id=create_account_id,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
