import time
import datetime
import pytest
import uuid
from ascend_sdk.models import components
from ascend_sdk.models import errors


def test_test_simulation_transfers_get_micro_deposit_get_micro_deposit1(
    get_correct_micro_deposit_amounts,
):
    assert get_correct_micro_deposit_amounts is not None


def test_test_simulation_transfers_force_approve_ach_deposit_force_approve_ach_deposit1(
    create_sdk,
    pending_ach_deposit,
    deceased_account_id,
    deceased_bank_relationship_id,
    current_time,
):
    if not (
        datetime.time(23, 30) <= current_time.time()
        or current_time.time() <= datetime.time(18, 0)
    ):
        pytest.skip("Skipping Endpoint Test: ACH Deposit Approval")
    s = create_sdk

    assert s is not None

    pending_deposit_id = pending_ach_deposit(
        deceased_account_id, deceased_bank_relationship_id
    )
    time.sleep(5)

    # Force approve an ACH deposit
    request = components.ForceApproveAchDepositRequestCreate(
        name=f"accounts/{deceased_account_id}/achDeposits/{deceased_bank_relationship_id}",
    )

    try:
        res = s.test_simulation.force_approve_ach_deposit(
            account_id=deceased_account_id,
            ach_deposit_id=pending_deposit_id,
            force_approve_ach_deposit_request_create=request,
        )

        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "that does not need review" in status.data.message.lower()


def test_test_simulation_transfers_force_noc_ach_deposit_force_noc_ach_deposit1(
    create_sdk, enrolled_account_id, create_ach_deposit_id, current_time
):
    if not (
        datetime.time(23, 30) <= current_time.time()
        or current_time.time() <= datetime.time(18, 0)
    ):
        pytest.skip("Skipping Endpoint Test: NOC for a Deposit")
    s = create_sdk

    assert s is not None

    # Force NOC an ACH deposit
    request = components.ForceNocAchDepositRequestCreate(
        nacha_noc=components.NachaNocCreate(
            code=components.Code.C05,
            updated_bank_account_type=components.UpdatedBankAccountType.CHECKING,
        ),
        name=f"accounts/{enrolled_account_id}/achDeposits/{create_ach_deposit_id}",
    )

    res = s.test_simulation.force_noc_ach_deposit(
        account_id=enrolled_account_id,
        ach_deposit_id=create_ach_deposit_id,
        force_noc_ach_deposit_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_test_simulation_transfers_force_reject_ach_deposit_force_reject_ach_deposit1(
    create_sdk,
    pending_ach_deposit,
    deceased_account_id,
    deceased_bank_relationship_id,
    current_time,
):
    if not (
        datetime.time(23, 30) <= current_time.time()
        or current_time.time() <= datetime.time(18, 0)
    ):
        pytest.skip("Skipping Endpoint Test: ACH Deposit Rejection")
    s = create_sdk

    assert s is not None

    pending_deposit_id = pending_ach_deposit(
        deceased_account_id, deceased_bank_relationship_id
    )
    time.sleep(5)

    # Force reject an ACH deposit
    request = components.ForceRejectAchDepositRequestCreate(
        name=f"accounts/{deceased_account_id}/achDeposits/{pending_deposit_id}",
    )
    try:
        res = s.test_simulation.force_reject_ach_deposit(
            account_id=deceased_account_id,
            ach_deposit_id=pending_deposit_id,
            force_reject_ach_deposit_request_create=request,
        )

        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "that does not need review" in status.data.message.lower()


def test_test_simulation_transfers_force_ach_deposit_return_force_ach_deposit_return1(
    create_sdk, enrolled_account_id, create_ach_deposit_id, current_time
):
    if not (
        datetime.time(23, 30) <= current_time.time()
        or current_time.time() <= datetime.time(18, 0)
    ):
        pytest.skip("Skipping Endpoint Test: ACH Deposit Return")
    s = create_sdk

    assert s is not None

    # Force return an ACH deposit
    request = components.ForceReturnAchDepositRequestCreate(
        nacha_return=components.NachaReturnCreate(
            code=components.NachaReturnCreateCode.R16,
        ),
        name=f"accounts/{enrolled_account_id}/achDeposits/{create_ach_deposit_id}",
    )

    try:
        res = s.test_simulation.force_return_ach_deposit(
            account_id=enrolled_account_id,
            ach_deposit_id=create_ach_deposit_id,
            force_return_ach_deposit_request_create=request,
        )
        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "current state" in status.data.message.lower()


def test_test_simulation_transfers_force_approve_ach_withdrawal_force_approve_ach_withdrawal1(
    create_sdk,
    pending_ach_withdrawal,
    deceased_account_id,
    deceased_bank_relationship_id,
    current_time,
):
    if not (
        datetime.time(23, 30) <= current_time.time()
        or current_time.time() <= datetime.time(18, 0)
    ):
        pytest.skip("Skipping Endpoint Test: ACH Withdrawal Approval")
    s = create_sdk

    assert s is not None

    pending_withdrawal_id = pending_ach_withdrawal(
        deceased_account_id, deceased_bank_relationship_id
    )
    time.sleep(10)

    # Force approve an ACH withdrawal
    request = components.ForceApproveAchWithdrawalRequestCreate(
        name=f"accounts/{deceased_account_id}/achWithdrawals/{pending_withdrawal_id}",
    )

    try:
        res = s.test_simulation.force_approve_ach_withdrawal(
            account_id=deceased_account_id,
            ach_withdrawal_id=pending_withdrawal_id,
            force_approve_ach_withdrawal_request_create=request,
        )

        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "that does not need review" in status.data.message.lower()


def test_test_simulation_transfers_force_noc_ach_withdrawal_force_noc_ach_withdrawal1(
    create_sdk, withdrawal_account_id, completed_withdrawal_id, current_time
):
    if not (
        datetime.time(23, 30) <= current_time.time()
        or current_time.time() <= datetime.time(18, 0)
    ):
        pytest.skip("Skipping Endpoint Test: ACH Withdrawal NOC")
    s = create_sdk

    assert s is not None

    # Force NOC an ACH withdrawal
    request = components.ForceNocAchWithdrawalRequestCreate(
        nacha_noc=components.NachaNocCreate(
            code=components.Code.C05,
            updated_bank_account_type=components.UpdatedBankAccountType.CHECKING,
        ),
        name=f"accounts/{withdrawal_account_id}/achWithdrawals/{completed_withdrawal_id}",
    )

    res = s.test_simulation.force_noc_ach_withdrawal(
        account_id=withdrawal_account_id,
        ach_withdrawal_id=completed_withdrawal_id,
        force_noc_ach_withdrawal_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_test_simulation_transfers_force_reject_ach_withdrawal_force_reject_ach_withdrawal1(
    create_sdk,
    pending_ach_withdrawal,
    deceased_account_id,
    deceased_bank_relationship_id,
    current_time,
):
    if not (
        datetime.time(23, 30) <= current_time.time()
        or current_time.time() <= datetime.time(18, 0)
    ):
        pytest.skip("Skipping Endpoint Test: ACH Withdrawal Rejection")
    s = create_sdk

    assert s is not None

    pending_withdrawal_id = pending_ach_withdrawal(
        deceased_account_id, deceased_bank_relationship_id
    )

    time.sleep(5)

    # Force reject an ACH withdrawal
    request = components.ForceRejectAchWithdrawalRequestCreate(
        name=f"accounts/{deceased_account_id}/achWithdrawals/{pending_withdrawal_id}",
    )

    try:
        res = s.test_simulation.force_reject_ach_withdrawal(
            account_id=deceased_account_id,
            ach_withdrawal_id=pending_withdrawal_id,
            force_reject_ach_withdrawal_request_create=request,
        )

        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "that does not need review" in status.data.message.lower()


def test_test_simulation_transfers_force_ach_withdrawal_return_force_ach_withdrawal_return1(
    create_sdk, withdrawal_account_id, completed_withdrawal_id, current_time
):
    if not (
        datetime.time(23, 30) <= current_time.time()
        or current_time.time() <= datetime.time(18, 0)
    ):
        pytest.skip("Skipping Endpoint Test: ACH Withdrawal Return")
    s = create_sdk

    assert s is not None

    # Force return an ACH withdrawal
    request = components.ForceReturnAchWithdrawalRequestCreate(
        nacha_return=components.NachaReturnCreate(
            code=components.NachaReturnCreateCode.R16,
        ),
        name=f"accounts/{withdrawal_account_id}/achWithdrawals/{completed_withdrawal_id}",
    )

    try:
        res = s.test_simulation.force_return_ach_withdrawal(
            account_id=withdrawal_account_id,
            ach_withdrawal_id=completed_withdrawal_id,
            force_return_ach_withdrawal_request_create=request,
        )

        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "current state" in status.data.message.lower()


def test_test_simulation_transfers_force_ict_deposit_approve_force_ict_deposit_approve1(
    create_sdk, pending_ict_deposit, deceased_account_id, current_time
):
    if not (datetime.time(6, 0) <= current_time.time() <= datetime.time(15, 0)):
        pytest.skip("Skipping Endpoint Test: Force Approve ICT Deposit")
    time.sleep(10)
    s = create_sdk

    assert s is not None

    pending_deposit_id = pending_ict_deposit(deceased_account_id)

    time.sleep(10)

    # Force approve an ICT deposit
    request = components.ForceApproveIctDepositRequestCreate(
        name=f"accounts/{deceased_account_id}/ictDeposits/{pending_deposit_id}",
    )

    try:
        res = s.test_simulation.force_approve_ict_deposit(
            account_id=deceased_account_id,
            ict_deposit_id=pending_deposit_id,
            force_approve_ict_deposit_request_create=request,
        )

        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "that does not need review" in status.data.message.lower()


def test_test_simulation_transfers_force_ict_deposit_reject_force_ict_deposit_reject1(
    create_sdk, pending_ict_deposit, deceased_account_id, current_time
):
    if not (datetime.time(6, 0) <= current_time.time() <= datetime.time(15, 0)):
        pytest.skip("Skipping Endpoint Test: Force Reject ICT Deposit")
    time.sleep(10)
    s = create_sdk

    assert s is not None

    pending_deposit_id = pending_ict_deposit(deceased_account_id)

    time.sleep(10)

    # Force reject an ICT deposit
    request = components.ForceRejectIctDepositRequestCreate(
        name=f"accounts/{deceased_account_id}/ictDeposits/{pending_deposit_id}",
    )

    try:
        res = s.test_simulation.force_reject_ict_deposit(
            account_id=deceased_account_id,
            ict_deposit_id=pending_deposit_id,
            force_reject_ict_deposit_request_create=request,
        )

        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "that does not need review" in status.data.message.lower()


def test_test_simulation_transfers_force_ict_withdrawal_approve_force_ict_withdrawal_approve1(
    create_sdk, pending_ict_withdrawal, deceased_account_id, current_time
):
    if not (datetime.time(6, 0) <= current_time.time() <= datetime.time(15, 0)):
        pytest.skip("Skipping Endpoint Test: Force Approve ICT Withdrawal")
    time.sleep(5)
    s = create_sdk

    assert s is not None

    pending_withdrawal_id = pending_ict_withdrawal(deceased_account_id)

    time.sleep(10)

    # Force approve an ICT withdrawal
    request = components.ForceApproveIctWithdrawalRequestCreate(
        name=f"accounts/{deceased_account_id}/ictWithdrawals/{pending_withdrawal_id}",
    )

    try:
        res = s.test_simulation.force_approve_ict_withdrawal(
            account_id=deceased_account_id,
            ict_withdrawal_id=pending_withdrawal_id,
            force_approve_ict_withdrawal_request_create=request,
        )

        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "that does not need review" in status.data.message.lower()


def test_test_simulation_transfers_force_ict_withdrawal_reject_force_ict_withdrawal_reject1(
    create_sdk, pending_ict_withdrawal, deceased_account_id, current_time
):
    if not (datetime.time(6, 0) <= current_time.time() <= datetime.time(15, 0)):
        pytest.skip("Skipping Endpoint Test: Force Reject ICT Withdrawal")
    time.sleep(5)
    s = create_sdk

    assert s is not None

    pending_withdrawal_id = pending_ict_withdrawal(deceased_account_id)

    time.sleep(10)

    # Force reject an ICT withdrawal
    request = components.ForceRejectIctWithdrawalRequestCreate(
        name=f"accounts/{deceased_account_id}/ictWithdrawals/{pending_withdrawal_id}",
    )

    try:
        res = s.test_simulation.force_reject_ict_withdrawal(
            account_id=deceased_account_id,
            ict_withdrawal_id=pending_withdrawal_id,
            force_reject_ict_withdrawal_request_create=request,
        )

        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
    except errors.Status as status:
        assert status.data.code == 3
        assert "that does not need review" in status.data.message.lower()


def test_test_simulation_transfers_force_approve_wire_withdrawal_force_approve_wire_withdrawal1(
    create_sdk, withdrawal_account_id, create_wire_withdrawal_id, current_time
):
    if not (datetime.time(7, 0) <= current_time.time() <= datetime.time(14, 30)):
        pytest.skip("Skipping Endpoint Test: Force Approve Wire Withdrawal")
    s = create_sdk

    assert s is not None

    time.sleep(5)

    request = components.ForceApproveWireWithdrawalRequestCreate(
        name=f"accounts/{withdrawal_account_id}/wireWithdrawals/{create_wire_withdrawal_id}",
    )

    res = s.test_simulation.force_approve_wire_withdrawal(
        account_id=withdrawal_account_id,
        wire_withdrawal_id=create_wire_withdrawal_id,
        force_approve_wire_withdrawal_request_create=request,
    )

    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_test_simulation_transfers_force_wire_withdrawal_reject_force_wire_withdrawal_reject1(
    create_sdk, create_wire_withdrawal_id, withdrawal_account_id, current_time
):
    if not (datetime.time(7, 0) <= current_time.time() <= datetime.time(14, 30)):
        pytest.skip("Skipping Endpoint Test: Force Reject Wire Withdrawal")
    s = create_sdk

    assert s is not None

    time.sleep(5)

    request = components.ForceRejectWireWithdrawalRequestCreate(
        name=f"accounts/{withdrawal_account_id}/wireWithdrawals/{create_wire_withdrawal_id}",
    )

    result = s.test_simulation.force_reject_wire_withdrawal(
        force_reject_wire_withdrawal_request_create=request,
        account_id=withdrawal_account_id,
        wire_withdrawal_id=create_wire_withdrawal_id,
    )
    assert result.http_meta is not None
    assert result.http_meta.response is not None
    assert result.http_meta.response.status_code == 200


def test_test_simulation_transfers_force_cash_journal_approve_force_cash_journal_approve1(
    create_sdk, create_cash_journal_id, withdrawal_account_id, current_time
):
    if not (datetime.time(6, 0) <= current_time.time() <= datetime.time(19, 0)):
        pytest.skip("Skipping Endpoint Test: Force Approve Cash Journal")

    s = create_sdk
    assert s is not None

    # Counter the amount of money the cash journal is taking
    transfers_credit_create = components.TransfersCreditCreate(
        amount=components.DecimalCreate(value="5000000.00"),
        client_transfer_id=str(uuid.uuid4()),
        description="Credit given as promotion",
        type=components.TransfersCreditCreateType.PROMOTIONAL,
    )

    s.fees_and_credits.create_credit(
        account_id=withdrawal_account_id,
        transfers_credit_create=transfers_credit_create,
    )

    request = components.ForceApproveCashJournalRequestCreate(
        name=f"cashJournals/{create_cash_journal_id}",
    )

    time.sleep(5)

    result = s.test_simulation.force_approve_cash_journal(
        force_approve_cash_journal_request_create=request,
        cash_journal_id=create_cash_journal_id,
    )
    assert result.http_meta is not None
    assert result.http_meta.response is not None
    assert result.http_meta.response.status_code == 200


def test_test_simulation_transfers_force_cash_journal_reject_force_cash_journal_reject1(
    create_sdk, create_cash_journal_id, current_time
):
    if not (datetime.time(6, 0) <= current_time.time() <= datetime.time(19, 0)):
        pytest.skip("Skipping Endpoint Test: Force Reject Cash Journal")

    s = create_sdk
    assert s is not None

    request = components.ForceRejectCashJournalRequestCreate(
        name=f"cashJournals/{create_cash_journal_id}",
    )

    time.sleep(5)

    result = s.test_simulation.force_reject_cash_journal(
        force_reject_cash_journal_request_create=request,
        cash_journal_id=create_cash_journal_id,
    )
    assert result.http_meta is not None
    assert result.http_meta.response is not None
    assert result.http_meta.response.status_code == 200
