import os
import uuid

import pytest

from ascend_sdk.models import components


@pytest.fixture(scope="module")
def create_option_instruction_id(create_sdk, enrolled_account_id):
    s = create_sdk

    # Fund Account with Credit
    transfers_credit_create = components.TransfersCreditCreate(
        amount=components.DecimalCreate(value="1000000.00"),
        client_transfer_id=str(uuid.uuid4()),
        description="Credit given as promotion",
        type=components.TransfersCreditCreateType.PROMOTIONAL,
    )

    s.fees_and_credits.create_credit(
        account_id=enrolled_account_id, transfers_credit_create=transfers_credit_create
    )

    asset_id = "9098656"

    option_instruction_create = components.OptionInstructionCreate(
        account_id=enrolled_account_id,
        identifier=asset_id,
        identifier_type=components.OptionInstructionCreateIdentifierType.ASSET_ID,
        quantity=components.DecimalCreate(value="1"),
        type=components.OptionInstructionCreateType.DO_NOT_EXERCISE,
    )

    res = s.option_instructions.create_option_instruction(
        account_id=enrolled_account_id,
        asset_id=asset_id,
        option_instruction_create=option_instruction_create,
    )

    if res.http_meta.response.status_code == 200:
        return {
            "instruction_id": res.option_instruction.instruction_id,
            "asset_id": asset_id,
        }
    else:
        return None
