import datetime
import os
import random
import time
import uuid

from ascend_sdk.models import components
import pytest


@pytest.fixture(scope="module")
def deceased_account_id():
    return "01JHK07CRQ9X8P5XE9JWG4PFSP"


@pytest.fixture(scope="module")
def deceased_bank_relationship_id():
    return "6786a8e8ea916b424a53cc24"


@pytest.fixture(scope="module")
def wire_deposit_id():
    return "20250218014356"


@pytest.fixture(scope="module")
def completed_withdrawal_id(create_sdk, withdrawal_account_id):
    s = create_sdk

    # Cancel any approved relationships
    res = s.bank_relationships.list_bank_relationships(account_id=withdrawal_account_id)
    max_relationships = len(res.list_bank_relationships_response.bank_relationships)
    attempt_counts = 0
    while attempt_counts < max_relationships:
        if (
            res.list_bank_relationships_response.bank_relationships[
                attempt_counts
            ].state.state
            == "APPROVED"
            or "REJECTED"
        ):
            cancel_bank_relationship_id = (
                res.list_bank_relationships_response.bank_relationships[
                    attempt_counts
                ].name.split("/")[-1]
            )
            request = components.CancelBankRelationshipRequestCreate(
                name=f"accounts/{withdrawal_account_id}/bankRelationships/{cancel_bank_relationship_id}",
                comment="Canceling Bank User Request",
            )
            s.bank_relationships.cancel_bank_relationship(
                account_id=withdrawal_account_id,
                bank_relationship_id=cancel_bank_relationship_id,
                cancel_bank_relationship_request_create=request,
            )
        attempt_counts += 1

    # Create a new bank relationship
    bank_relationship_request = components.BankRelationshipCreate(
        bank_account=components.BankAccountCreate(
            account_number=str(random.randint(10000000, 99999999)),
            owner="TEST123",
            routing_number="112203216",
            type=components.BankAccountCreateType.SAVINGS,
        ),
        nickname="ACH TEST",
        verification_method=components.VerificationMethod.MICRO_DEPOSIT,
    )

    res = s.bank_relationships.create_bank_relationship(
        account_id=withdrawal_account_id,
        bank_relationship_create=bank_relationship_request,
    )
    bank_relationship_id = res.bank_relationship.name.split("/")[-1]

    res = s.test_simulation.get_micro_deposit_amounts(
        account_id=withdrawal_account_id, bank_relationship_id=bank_relationship_id
    )

    micro_deposits_request = components.VerifyMicroDepositsRequestCreate(
        amounts=components.MicroDepositAmountsCreate(
            amount1=components.DecimalCreate(
                value=res.micro_deposit_amounts.amount1.value
            ),
            amount2=components.DecimalCreate(
                value=res.micro_deposit_amounts.amount2.value
            ),
        ),
        name=f"accounts/{withdrawal_account_id}/bankRelationships/{bank_relationship_id}",
    )

    s.bank_relationships.verify_micro_deposits(
        account_id=withdrawal_account_id,
        bank_relationship_id=bank_relationship_id,
        verify_micro_deposits_request_create=micro_deposits_request,
    )

    ach_withdrawal_request = components.AchWithdrawalCreate(
        bank_relationship="accounts/"
        + withdrawal_account_id
        + "/bankRelationships/"
        + bank_relationship_id,
        amount=components.DecimalCreate(value="0.01"),
        client_transfer_id=str(uuid.uuid4()),
        full_disbursement=False,
        memo="ACH",
    )

    res = s.ach_transfers.create_ach_withdrawal(
        account_id=withdrawal_account_id, ach_withdrawal_create=ach_withdrawal_request
    )
    if res.http_meta.response.status_code == 200:
        return res.ach_withdrawal.name.split("/")[3]
    else:
        return None


@pytest.fixture(scope="module")
def get_failed_micro_deposit_amounts(
    create_sdk, enrolled_account_id, create_bank_relationship_id
):
    s = create_sdk

    res = s.test_simulation.get_micro_deposit_amounts(
        account_id=enrolled_account_id, bank_relationship_id=create_bank_relationship_id
    )
    if res.http_meta.response.status_code == 200:
        return (
            float(res.micro_deposit_amounts.amount1.value) + 0.01,
            float(res.micro_deposit_amounts.amount2.value) + 0.01,
        )
    else:
        return None


@pytest.fixture(scope="module")
def get_correct_micro_deposit_amounts(
    create_sdk, enrolled_account_id, create_bank_relationship_id
):
    s = create_sdk

    res = s.test_simulation.get_micro_deposit_amounts(
        account_id=enrolled_account_id, bank_relationship_id=create_bank_relationship_id
    )
    if res.http_meta.response.status_code == 200:
        return (
            res.micro_deposit_amounts.amount1.value,
            res.micro_deposit_amounts.amount2.value,
        )
    else:
        return None


@pytest.fixture(scope="module")
def create_ach_deposit_id(
    create_sdk, enrolled_account_id, verified_bank_relationship_id
):
    s = create_sdk

    ach_deposit_request = components.AchDepositCreate(
        amount=components.DecimalCreate(value="1000.00"),
        bank_relationship="accounts/"
        + enrolled_account_id
        + "/bankRelationships/"
        + verified_bank_relationship_id,
        client_transfer_id=str(uuid.uuid4()),
    )

    res = s.ach_transfers.create_ach_deposit(
        account_id=enrolled_account_id, ach_deposit_create=ach_deposit_request
    )
    if res.http_meta.response.status_code == 200:
        return res.ach_deposit.name.split("/")[3]
    else:
        return None


@pytest.fixture(scope="module")
def create_ach_withdrawal_id(
    create_sdk, enrolled_account_id, verified_bank_relationship_id
):
    s = create_sdk

    ach_withdrawal_request = components.AchWithdrawalCreate(
        bank_relationship="accounts/"
        + enrolled_account_id
        + "/bankRelationships/"
        + verified_bank_relationship_id,
        amount=components.DecimalCreate(value="0.01"),
        client_transfer_id=str(uuid.uuid4()),
        full_disbursement=False,
        memo="ACH",
    )

    res = s.ach_transfers.create_ach_withdrawal(
        account_id=enrolled_account_id, ach_withdrawal_create=ach_withdrawal_request
    )
    if res.http_meta.response.status_code == 200:
        return res.ach_withdrawal.name.split("/")[3]
    else:
        return None


@pytest.fixture(scope="module")
def create_fee_id(create_sdk, enrolled_account_id):
    s = create_sdk

    transfers_fee_create = components.TransfersFeeCreate(
        amount=components.DecimalCreate(value="10.00"),
        client_transfer_id=str(uuid.uuid4()),
        description="Fee charged",
        type=components.TransfersFeeCreateType.MANAGEMENT,
    )

    res = s.fees_and_credits.create_fee(
        account_id=enrolled_account_id, transfers_fee_create=transfers_fee_create
    )
    if res.http_meta.response.status_code == 200:
        return res.transfers_fee.name.split("/")[-1]
    else:
        return None


@pytest.fixture(scope="module")
def create_credit_id(create_sdk, enrolled_account_id):
    s = create_sdk

    transfers_credit_create = components.TransfersCreditCreate(
        amount=components.DecimalCreate(value="10.00"),
        client_transfer_id=str(uuid.uuid4()),
        description="Credit given as promotion",
        type=components.TransfersCreditCreateType.PROMOTIONAL,
    )

    res = s.fees_and_credits.create_credit(
        account_id=enrolled_account_id, transfers_credit_create=transfers_credit_create
    )
    if res.http_meta.response.status_code == 200:
        return res.transfers_credit.name.split("/")[-1]
    else:
        return None


@pytest.fixture(scope="module")
def create_ict_deposit_id(create_sdk, enrolled_account_id):
    s = create_sdk

    ict_deposit_request = components.IctDepositCreate(
        amount=components.DecimalCreate(value="1000.00"),
        client_transfer_id=str(uuid.uuid4()),
        program=components.Program.BROKER_PARTNER,
        travel_rule=components.IctDepositTravelRuleCreate(
            individual_originating_party=components.TravelRulePartyCreate(
                address=components.PostalAddressCreate(
                    address_lines=["19409 Sherilyn Courts"],
                    region_code="US",
                    postal_code="97035",
                    administrative_area="OR",
                    locality="Portland",
                ),
                family_name="Jacob",
                given_names=[
                    "Bob",
                ],
            ),
            individual_recipient_party=components.TravelRulePartyCreate(
                address=components.PostalAddressCreate(
                    address_lines=["19409 Sherilyn Courts"],
                    region_code="US",
                    postal_code="97035",
                    administrative_area="OR",
                    locality="Portland",
                ),
                family_name="Jacob",
                given_names=[
                    "Bob",
                ],
            ),
            originating_institution=components.InstitutionCreate(
                account_id="09673049", title="Default Bank"
            ),
        ),
    )

    res = s.instant_cash_transfer_ict.create_ict_deposit(
        account_id=enrolled_account_id, ict_deposit_create=ict_deposit_request
    )
    if res.http_meta.response.status_code == 200:
        return res.ict_deposit.name.split("/")[3]
    else:
        return None


@pytest.fixture(scope="module")
def create_ict_withdrawal_id(create_sdk, enrolled_account_id):
    s = create_sdk

    ict_withdrawal_request = components.IctWithdrawalCreate(
        client_transfer_id=str(uuid.uuid4()),
        program=components.IctWithdrawalCreateProgram.BROKER_PARTNER,
        full_disbursement=True,
        travel_rule=components.IctWithdrawalTravelRuleCreate(
            recipient_institution=components.InstitutionCreate(
                account_id="09673049", title="Default Bank"
            )
        ),
    )

    res = s.instant_cash_transfer_ict.create_ict_withdrawal(
        account_id=enrolled_account_id, ict_withdrawal_create=ict_withdrawal_request
    )
    if res.http_meta.response.status_code == 200:
        return res.ict_withdrawal.name.split("/")[3]
    else:
        return None


@pytest.fixture(scope="module")
def create_ach_deposit_schedule_id(
    create_sdk, enrolled_account_id, verified_bank_relationship_id
):
    s = create_sdk

    today = datetime.datetime.now()
    ach_deposit_schedule_request = components.AchDepositScheduleCreate(
        bank_relationship="accounts/"
        + enrolled_account_id
        + "/bankRelationships/"
        + verified_bank_relationship_id,
        schedule_details=components.DepositScheduleDetailsCreate(
            amount=components.DecimalCreate(
                value="100",
            ),
            client_schedule_id=str(uuid.uuid4()),
            schedule_properties=components.SchedulePropertiesCreate(
                start_date=components.DateCreate(
                    year=str(today.year),
                    month=str(today.month),
                    day=str(today.day),
                ),
                time_unit=components.TimeUnit.MONTH,
                unit_multiplier=1,
                occurrences=12,
            ),
        ),
    )

    res = s.schedule_transfers.create_ach_deposit_schedule(
        account_id=enrolled_account_id,
        ach_deposit_schedule_create=ach_deposit_schedule_request,
    )
    if res.http_meta.response.status_code == 200:
        return res.ach_deposit_schedule.name.split("/")[3]
    else:
        return None


@pytest.fixture(scope="module")
def create_ach_withdrawal_schedule_id(
    create_sdk, enrolled_account_id, verified_bank_relationship_id
):
    s = create_sdk

    today = datetime.datetime.now().date()
    ach_withdrawal_schedule_request = components.AchWithdrawalScheduleCreate(
        bank_relationship="accounts/"
        + enrolled_account_id
        + "/bankRelationships/"
        + verified_bank_relationship_id,
        schedule_details=components.WithdrawalScheduleDetailsCreate(
            amount=components.DecimalCreate(
                value="100",
            ),
            client_schedule_id=str(uuid.uuid4()),
            schedule_properties=components.SchedulePropertiesCreate(
                occurrences=10,
                start_date=components.DateCreate(
                    year=str(today.year),
                    month=str(today.month),
                    day=str(today.day),
                ),
                time_unit=components.TimeUnit.MONTH,
                unit_multiplier=1,
            ),
        ),
    )

    res = s.schedule_transfers.create_ach_withdrawal_schedule(
        account_id=enrolled_account_id,
        ach_withdrawal_schedule_create=ach_withdrawal_schedule_request,
    )
    if res.http_meta.response.status_code == 200:
        return res.ach_withdrawal_schedule.name.split("/")[3]
    else:
        return None


@pytest.fixture
def ach_deposit_factory(create_sdk):
    def _factory(account_id, bank_relationship_id, amount="1000.00"):
        ach_deposit_request = components.AchDepositCreate(
            amount=components.DecimalCreate(value=amount),
            bank_relationship=f"accounts/{account_id}/bankRelationships/{bank_relationship_id}",
            client_transfer_id=str(uuid.uuid4()),
        )
        response = create_sdk.ach_transfers.create_ach_deposit(
            account_id=account_id, ach_deposit_create=ach_deposit_request
        )
        deposit_id = response.ach_deposit.name.split("/")[-1]
        return deposit_id

    return _factory


@pytest.fixture
def pending_ach_deposit(ach_deposit_factory):
    def _pending(account_id, bank_relationship_id):
        return ach_deposit_factory(account_id, bank_relationship_id)

    return _pending


@pytest.fixture
def ach_withdrawal_factory(create_sdk):
    def _factory(account_id, bank_relationship_id, amount="0.01"):
        res = create_sdk.cash_balances.calculate_cash_balance(account_id=account_id)
        if res.calculate_cash_balance_response.available_cash_to_withdraw_amount == 0:
            pytest.skip("Insufficient funds to create withdrawal")
        ach_withdrawal_request = components.AchWithdrawalCreate(
            bank_relationship="accounts/"
            + account_id
            + "/bankRelationships/"
            + bank_relationship_id,
            amount=components.DecimalCreate(value=amount),
            client_transfer_id=str(uuid.uuid4()),
            full_disbursement=False,
            memo="ACH",
        )
        response = create_sdk.ach_transfers.create_ach_withdrawal(
            account_id=account_id, ach_withdrawal_create=ach_withdrawal_request
        )
        withdrawal_id = response.ach_withdrawal.name.split("/")[-1]
        return withdrawal_id

    return _factory


@pytest.fixture
def pending_ach_withdrawal(ach_withdrawal_factory):
    def _pending(account_id, bank_relationship_id):
        return ach_withdrawal_factory(account_id, bank_relationship_id)

    return _pending


@pytest.fixture(scope="module")
def external_financial_institution_account_id():
    return "09673049"


@pytest.fixture
def ict_deposit_factory(create_sdk, external_financial_institution_account_id):
    def _factory(account_id, amount="1000.00"):
        ict_deposit_request = components.IctDepositCreate(
            amount=components.DecimalCreate(value=amount),
            client_transfer_id=str(uuid.uuid4()),
            program=components.Program.BROKER_PARTNER,
            travel_rule=components.IctDepositTravelRuleCreate(
                individual_originating_party=components.TravelRulePartyCreate(
                    address=components.PostalAddressCreate(
                        address_lines=["19409 Sherilyn Courts"],
                        region_code="US",
                        postal_code="97035",
                        administrative_area="OR",
                        locality="Portland",
                    ),
                    family_name="Jacob",
                    given_names=[
                        "Bob",
                    ],
                ),
                individual_recipient_party=components.TravelRulePartyCreate(
                    address=components.PostalAddressCreate(
                        address_lines=["19409 Sherilyn Courts"],
                        region_code="US",
                        postal_code="97035",
                        administrative_area="OR",
                        locality="Portland",
                    ),
                    family_name="Jacob",
                    given_names=[
                        "Bob",
                    ],
                ),
                originating_institution=components.InstitutionCreate(
                    account_id=external_financial_institution_account_id,
                    title="Default Bank",
                ),
            ),
        )
        response = create_sdk.instant_cash_transfer_ict.create_ict_deposit(
            account_id=account_id, ict_deposit_create=ict_deposit_request
        )
        deposit_id = response.ict_deposit.name.split("/")[-1]
        return deposit_id

    return _factory


@pytest.fixture
def pending_ict_deposit(ict_deposit_factory):
    def _pending(account_id):
        return ict_deposit_factory(account_id)

    return _pending


@pytest.fixture
def ict_withdrawal_factory(create_sdk, external_financial_institution_account_id):
    def _factory(account_id, amount="1000.00"):
        ict_withdrawal_request = components.IctWithdrawalCreate(
            client_transfer_id=str(uuid.uuid4()),
            program=components.IctWithdrawalCreateProgram.BROKER_PARTNER,
            travel_rule=components.IctWithdrawalTravelRuleCreate(
                recipient_institution=components.InstitutionCreate(
                    account_id=external_financial_institution_account_id,
                    title="Default Bank",
                )
            ),
            amount=components.DecimalCreate(value=amount),
        )
        response = create_sdk.instant_cash_transfer_ict.create_ict_withdrawal(
            account_id=account_id, ict_withdrawal_create=ict_withdrawal_request
        )
        withdrawal_id = response.ict_withdrawal.name.split("/")[-1]
        return withdrawal_id

    return _factory


@pytest.fixture
def pending_ict_withdrawal(ict_withdrawal_factory):
    def _pending(account_id):
        return ict_withdrawal_factory(account_id)

    return _pending


@pytest.fixture
def create_wire_withdrawal_id(create_sdk, withdrawal_account_id):
    s = create_sdk

    wire_withdrawal_request = components.WireWithdrawalCreate(
        amount=components.DecimalCreate(value="1.00"),
        beneficiary=components.WireWithdrawalBeneficiaryCreate(
            account=withdrawal_account_id,
            account_title="Test",
            address=components.AddressCreate(
                street_address=["123 Main St"],
                city="Portland",
                state="OR",
                postal_code="97201",
                country="USA",
            ),
            third_party=True,
        ),
        recipient_bank=components.WireWithdrawalRecipientBankCreate(
            bank_id=components.RecipientBankBankIDCreate(
                id="011000028",
                type=components.RecipientBankBankIDCreateType.ABA,
            )
        ),
        client_transfer_id=str(uuid.uuid4()),
    )

    res = s.wires.create_wire_withdrawal(
        account_id=withdrawal_account_id, wire_withdrawal_create=wire_withdrawal_request
    )
    if res.http_meta.response.status_code == 200:
        return res.wire_withdrawal.name.split("/")[3]
    else:
        return None


@pytest.fixture
def create_cash_journal_id(create_sdk, deceased_account_id, withdrawal_account_id):
    s = create_sdk

    cash_journal_request = components.CashJournalCreate(
        client_transfer_id=str(uuid.uuid4()),
        destination_account="accounts/" + deceased_account_id,
        amount=components.DecimalCreate(value="500001.00"),
        source_account="accounts/" + withdrawal_account_id,
    )

    res = s.journals.create_cash_journal(request=cash_journal_request)

    if res.http_meta.response.status_code == 200:
        return res.cash_journal.name.split("/")[1]
    else:
        return None


@pytest.fixture
def create_wire_withdrawal_schedule_id(create_sdk, enrolled_account_id):
    s = create_sdk

    today = datetime.datetime.now().date()
    wire_withdrawal_schedule_request = components.WireWithdrawalScheduleCreate(
        beneficiary=components.WireWithdrawalBeneficiaryCreate(
            account=enrolled_account_id
        ),
        recipient_bank=components.WireWithdrawalRecipientBankCreate(
            bank_id=components.RecipientBankBankIDCreate(
                id="ABNANL2AXXX", type=components.RecipientBankBankIDCreateType.ABA
            )
        ),
        schedule_details=components.WithdrawalScheduleDetailsCreate(
            amount=components.DecimalCreate(
                value="100",
            ),
            client_schedule_id=str(uuid.uuid4()),
            schedule_properties=components.SchedulePropertiesCreate(
                start_date=components.DateCreate(
                    year=str(today.year),
                    month=str(today.month),
                    day=str(today.day),
                ),
                time_unit=components.TimeUnit.MONTH,
                unit_multiplier=1,
                occurrences=12,
            ),
        ),
    )

    res = s.schedule_transfers.create_wire_withdrawal_schedule(
        account_id=enrolled_account_id,
        wire_withdrawal_schedule_create=wire_withdrawal_schedule_request,
    )

    if res.http_meta.response.status_code == 200:
        return res.wire_withdrawal_schedule.name.split("/")[3]
    else:
        return None


@pytest.fixture
def create_reuse_account_id(create_sdk, create_legal_natural_person_id):
    s = create_sdk

    request = components.AccountRequestCreate(
        account_group_id=os.getenv("ACCOUNT_GROUP_ID"),
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        parties=[
            components.PartyRequestCreate(
                legal_natural_person_id=create_legal_natural_person_id,
                relation_type=components.RelationType.PRIMARY_OWNER,
                email_address="mail@example.com",
                phone_number=components.PhoneNumberCreate(
                    e164_number="+14155552671",
                    extension="123",
                ),
                mailing_address=components.PostalAddressCreate(
                    address_lines=["1 Main Street"],
                    region_code="US",
                    postal_code="12345",
                    administrative_area="NY",
                    locality="New York",
                ),
            )
        ],
    )

    res = s.account_creation.create_account(request=request)
    if res.http_meta.response.status_code == 200:
        return res.account.account_id
    else:
        return None
