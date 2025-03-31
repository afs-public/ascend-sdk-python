import time

from ascend_sdk.models import components, errors


def test_bank_relationships_transfers_create_bank_relationship_create_bank_relationship1(
    create_bank_relationship_id,
):
    assert create_bank_relationship_id is not None


def test_bank_relationships_transfers_list_bank_relationships_list_bank_relationships(
    create_sdk,
    enrolled_account_id,
):
    s = create_sdk

    assert s is not None
    res = s.bank_relationships.list_bank_relationships(account_id=enrolled_account_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_bank_relationships_transfers_get_bank_relationship_get_bank_relationship1(
    create_sdk,
    enrolled_account_id,
    create_bank_relationship_id,
):
    s = create_sdk

    assert s is not None
    res = s.bank_relationships.get_bank_relationship(
        account_id=enrolled_account_id, bank_relationship_id=create_bank_relationship_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_bank_relationships_transfers_update_bank_relationship_update_bank_relationship1(
    create_sdk,
    enrolled_account_id,
    create_bank_relationship_id,
):
    s = create_sdk

    assert s is not None

    bank_relationship_request = components.BankRelationshipUpdate(
        nickname="My Primary Bank",
    )

    res = s.bank_relationships.update_bank_relationship(
        account_id=enrolled_account_id,
        bank_relationship_id=create_bank_relationship_id,
        bank_relationship_update=bank_relationship_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_bank_relationships_transfers_reissue_micro_deposits_reissue_micro_deposits1(
    create_sdk,
    enrolled_account_id,
    create_bank_relationship_id,
    get_failed_micro_deposit_amounts,
):
    s = create_sdk

    assert s is not None

    # Fail verify micro deposits
    request = components.VerifyMicroDepositsRequestCreate(
        amounts=components.MicroDepositAmountsCreate(
            amount1=components.DecimalCreate(
                value="{:.2f}".format(float(get_failed_micro_deposit_amounts[0]))
            ),
            amount2=components.DecimalCreate(
                value="{:.2f}".format(float(get_failed_micro_deposit_amounts[0]))
            ),
        ),
        name=f"accounts/{enrolled_account_id}/bankRelationships/{create_bank_relationship_id}",
    )

    max_attempts = 3
    attempt_counts = 0
    while attempt_counts < max_attempts:
        attempt_counts += 1
        try:
            s.bank_relationships.verify_micro_deposits(
                account_id=enrolled_account_id,
                bank_relationship_id=create_bank_relationship_id,
                verify_micro_deposits_request_create=request,
            )
        except errors.Status as e:
            # handle exception
            continue
        except errors.SDKError as e:
            # handle exception
            raise e

    # Reissue micro deposits
    request = components.ReissueMicroDepositsRequestCreate(
        name=f"accounts/{enrolled_account_id}/bankRelationships/{create_bank_relationship_id}"
    )

    res = s.bank_relationships.reissue_micro_deposits(
        account_id=enrolled_account_id,
        bank_relationship_id=create_bank_relationship_id,
        reissue_micro_deposits_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_bank_relationships_transfers_verify_micro_deposits_verify_micro_deposits1(
    create_sdk,
    enrolled_account_id,
    create_bank_relationship_id,
    get_correct_micro_deposit_amounts,
):
    time.sleep(10)
    s = create_sdk

    assert s is not None

    micro_deposits_request = components.VerifyMicroDepositsRequestCreate(
        amounts=components.MicroDepositAmountsCreate(
            amount1=components.DecimalCreate(
                value=get_correct_micro_deposit_amounts[0]
            ),
            amount2=components.DecimalCreate(
                value=get_correct_micro_deposit_amounts[1]
            ),
        ),
        name=f"accounts/{enrolled_account_id}/bankRelationships/{create_bank_relationship_id}",
    )

    res = s.bank_relationships.verify_micro_deposits(
        account_id=enrolled_account_id,
        bank_relationship_id=create_bank_relationship_id,
        verify_micro_deposits_request_create=micro_deposits_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_bank_relationships_transfers_cancel_bank_relationship_cancel_bank_relationship1(
    create_sdk,
    enrolled_account_id,
    create_bank_relationship_id,
):
    s = create_sdk

    assert s is not None

    request = components.CancelBankRelationshipRequestCreate(
        name=f"accounts/{enrolled_account_id}/bankRelationships/{create_bank_relationship_id}",
        comment="Canceling Bank User Request",
    )

    res = s.bank_relationships.cancel_bank_relationship(
        account_id=enrolled_account_id,
        bank_relationship_id=create_bank_relationship_id,
        cancel_bank_relationship_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
