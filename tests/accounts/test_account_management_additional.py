import time

from ascend_sdk.models import components


def test_account_management_accounts_update_account_update_account1(
    create_sdk, create_account_id
):
    s = create_sdk

    assert s is not None

    account_update = components.AccountRequestUpdate(
        cat_account_holder_type=components.AccountRequestUpdateCatAccountHolderType.I_INDIVIDUAL,
    )

    res = s.account_management.update_account(
        account_id=create_account_id, account_request_update=account_update
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_management_accounts_add_party_add_party1(add_party_id):
    assert add_party_id is not None


def test_account_management_accounts_update_party_update_party1(
    create_sdk, create_account_id, add_party_id
):
    s = create_sdk

    assert s is not None

    party_update = components.PartyRequestUpdate(
        email_address="email@example.com",
    )

    res = s.account_management.update_party(
        account_id=create_account_id,
        party_id=add_party_id,
        party_request_update=party_update,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_management_accounts_replace_party_replace_party1(replace_party_id):
    assert replace_party_id is not None


def test_account_management_accounts_remove_party_remove_party1(
    create_sdk, create_account_id, replace_party_id
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    request = components.RemovePartyRequestCreate(
        authorized_by_party_ids=[
            "8096110d-fb55-4f9d-b883-b84f0b70d3ea",
            "8096110d-fb55-4f9d-b883-b84f0b70d3rb",
        ],
        name=f"accounts/{create_account_id}/parties/{replace_party_id}",
    )

    res = s.account_management.remove_party(
        account_id=create_account_id,
        party_id=replace_party_id,
        remove_party_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_management_accounts_create_trusted_contact_create_trusted_contact1(
    create_trusted_contact_id,
):
    assert create_trusted_contact_id is not None


def test_account_management_accounts_update_trusted_contact_update_trusted_contact1(
    create_sdk, create_account_id, create_trusted_contact_id
):
    s = create_sdk

    assert s is not None

    trusted_contact_request = components.TrustedContactUpdate(
        email_address="email@email.com"
    )

    res = s.account_management.update_trusted_contact(
        account_id=create_account_id,
        trusted_contact_id=create_trusted_contact_id,
        trusted_contact_update=trusted_contact_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_management_accounts_delete_trusted_contact_delete_trusted_contact1(
    create_sdk, create_account_id, create_trusted_contact_id
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    res = s.account_management.delete_trusted_contact(
        account_id=create_account_id, trusted_contact_id=create_trusted_contact_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_management_accounts_create_interested_party_create_interested_party1(
    create_interested_party_id,
):
    assert create_interested_party_id is not None


def test_account_management_accounts_update_interested_party_update_interested_party1(
    create_sdk, create_account_id, create_interested_party_id
):
    s = create_sdk

    assert s is not None

    interested_party_request = components.InterestedPartyUpdate(
        recipient="John Doe",
    )

    res = s.account_management.update_interested_party(
        account_id=create_account_id,
        interested_party_id=create_interested_party_id,
        interested_party_update=interested_party_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_management_accounts_delete_interested_party_delete_interested_party1(
    create_sdk, create_account_id, create_interested_party_id
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    res = s.account_management.delete_interested_party(
        account_id=create_account_id, interested_party_id=create_interested_party_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_management_accounts_list_available_restrictions_list_available_restrictions1(
    create_sdk, create_account_id
):
    s = create_sdk

    assert s is not None

    res = s.account_management.list_available_restrictions(account_id=create_account_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_management_accounts_create_restriction_create_restrictions1(
    create_restriction_code,
):
    assert create_restriction_code is not None


def test_account_management_accounts_end_restriction_end_restrictions(
    create_sdk, create_account_id, create_restriction_code
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    restriction_request = components.EndRestrictionRequestCreate(
        reason="Some reason for removing",
    )

    res = s.account_management.end_restriction(
        account_id=create_account_id,
        restriction_id=create_restriction_code,
        end_restriction_request_create=restriction_request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_account_management_accounts_close_account_close_account1(
    create_sdk, create_account_id
):
    s = create_sdk

    assert s is not None

    request = components.CloseAccountRequestCreate()

    res = s.account_management.close_account(
        account_id=create_account_id, close_account_request_create=request
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
