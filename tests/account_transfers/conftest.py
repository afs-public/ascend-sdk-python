import time

from ascend_sdk.models import components
import pytest
import os


@pytest.fixture(scope="module")
def account_number():
    return "1234567890"


@pytest.fixture(scope="module")
def create_account_transfer_id(create_sdk, account_number, enrolled_account_id):
    time.sleep(5)
    s = create_sdk

    request = components.TransferCreate(
        deliverer=components.TransferAccountCreate(
            external_account=components.ExternalAccountCreate(
                account_number=account_number,
                participant_number="987",
            ),
        ),
    )
    res = s.account_transfers.create_transfer(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        account_id=enrolled_account_id,
        transfer_create=request,
    )
    if res.http_meta.response.status_code == 200:
        return res.acats_transfer.name.split("/")[-1]
    else:
        return None
