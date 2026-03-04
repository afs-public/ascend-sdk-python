from ascend_sdk.models import components, operations


def test_exercise_service_create_option_instruction(create_option_instruction_id):
    assert create_option_instruction_id is not None
    assert create_option_instruction_id["instruction_id"] is not None


def test_exercise_service_get_option_instruction(
    create_sdk, enrolled_account_id, create_option_instruction_id
):
    s = create_sdk

    assert s is not None

    res = s.option_instructions.get_option_instruction(
        account_id=enrolled_account_id,
        asset_id=create_option_instruction_id["asset_id"],
        instruction_id=create_option_instruction_id["instruction_id"],
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_exercise_service_list_option_instructions(
    create_sdk, enrolled_account_id, create_option_instruction_id
):
    s = create_sdk

    assert s is not None

    res = s.option_instructions.list_option_instructions(
        request=operations.ExerciseServiceListOptionInstructionsRequest(
            account_id=enrolled_account_id,
            asset_id=create_option_instruction_id["asset_id"],
        ),
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_exercise_service_cancel_option_instruction(
    create_sdk, enrolled_account_id, create_option_instruction_id
):
    s = create_sdk

    assert s is not None

    instruction_id = create_option_instruction_id["instruction_id"]
    asset_id = create_option_instruction_id["asset_id"]

    request = components.CancelOptionInstructionRequestCreate(
        name=f"accounts/{enrolled_account_id}/assets/{asset_id}/instructions/{instruction_id}",
    )

    res = s.option_instructions.cancel_option_instruction(
        account_id=enrolled_account_id,
        asset_id=asset_id,
        instruction_id=instruction_id,
        cancel_option_instruction_request_create=request,
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
