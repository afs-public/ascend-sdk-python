"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accounttaxprofileupdate import (
    AccountTaxProfileUpdate,
    AccountTaxProfileUpdateTypedDict,
)
from .identifierupdate import IdentifierUpdate, IdentifierUpdateTypedDict
from .interestedpartyupdate import InterestedPartyUpdate, InterestedPartyUpdateTypedDict
from .investmentprofileupdate import (
    InvestmentProfileUpdate,
    InvestmentProfileUpdateTypedDict,
)
from .partyrequestupdate import PartyRequestUpdate, PartyRequestUpdateTypedDict
from .trustedcontactupdate import TrustedContactUpdate, TrustedContactUpdateTypedDict
from ascend_sdk import utils
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import validate_open_enum
from enum import Enum
from pydantic.functional_validators import PlainValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountRequestUpdateCatAccountHolderType(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The FINRA CAT classification for the Account Holder; Is set automatically based on attributes of the owners and account type"""

    CAT_ACCOUNT_HOLDER_TYPE_UNSPECIFIED = "CAT_ACCOUNT_HOLDER_TYPE_UNSPECIFIED"
    A_INSTITUTIONAL_CUSTOMER = "A_INSTITUTIONAL_CUSTOMER"
    E_EMPLOYEE_ACCOUNT = "E_EMPLOYEE_ACCOUNT"
    F_FOREIGN = "F_FOREIGN"
    I_INDIVIDUAL = "I_INDIVIDUAL"
    O_MARKET_MAKING = "O_MARKET_MAKING"
    V_AGENCY_AVERAGE_PRICE_ACCOUNT = "V_AGENCY_AVERAGE_PRICE_ACCOUNT"
    P_OTHER_PROPRIETARY = "P_OTHER_PROPRIETARY"
    X_ERROR_ACCOUNT = "X_ERROR_ACCOUNT"


class AccountRequestUpdateTypedDict(TypedDict):
    r"""A single record representing an owner or manager of an Account."""

    accepts_issuer_direct_communication: NotRequired[bool]
    r"""Indicates if the issuer of a security held by the account is permitted to communicate directly with the shareholder versus through the brokerage firm; This can include sending proxy statements, annual reports, and other important information directly to the shareholder's address on file with the brokerage firm"""
    advised: NotRequired[bool]
    r"""A boolean to indicate if an account is advised"""
    cat_account_holder_type: NotRequired[AccountRequestUpdateCatAccountHolderType]
    r"""The FINRA CAT classification for the Account Holder; Is set automatically based on attributes of the owners and account type"""
    identifiers: NotRequired[List[IdentifierUpdateTypedDict]]
    r"""A list of identifiers associated with the account"""
    interested_parties: NotRequired[List[InterestedPartyUpdateTypedDict]]
    r"""A list of natural persons indicated to receive selected account documents such as account statements"""
    investment_profile: NotRequired[InvestmentProfileUpdateTypedDict]
    r"""Investor profile."""
    managed: NotRequired[bool]
    r"""A boolean to indicate if an account is managed"""
    parties: NotRequired[List[PartyRequestUpdateTypedDict]]
    r"""Parties associated with the account (e.g. custodian)."""
    primary_registered_rep_id: NotRequired[str]
    r"""The primary registered representative for the account"""
    tax_profile: NotRequired[AccountTaxProfileUpdateTypedDict]
    r"""The account tax profile."""
    trusted_contacts: NotRequired[List[TrustedContactUpdateTypedDict]]
    r"""A list of persons designated to verify the well being of the account holder."""
    wrap_fee_billed: NotRequired[bool]
    r"""A boolean to indicate if an account is a wrap brokerage account"""


class AccountRequestUpdate(BaseModel):
    r"""A single record representing an owner or manager of an Account."""

    accepts_issuer_direct_communication: Optional[bool] = None
    r"""Indicates if the issuer of a security held by the account is permitted to communicate directly with the shareholder versus through the brokerage firm; This can include sending proxy statements, annual reports, and other important information directly to the shareholder's address on file with the brokerage firm"""

    advised: Optional[bool] = None
    r"""A boolean to indicate if an account is advised"""

    cat_account_holder_type: Annotated[
        Optional[AccountRequestUpdateCatAccountHolderType],
        PlainValidator(validate_open_enum(False)),
    ] = None
    r"""The FINRA CAT classification for the Account Holder; Is set automatically based on attributes of the owners and account type"""

    identifiers: Optional[List[IdentifierUpdate]] = None
    r"""A list of identifiers associated with the account"""

    interested_parties: Optional[List[InterestedPartyUpdate]] = None
    r"""A list of natural persons indicated to receive selected account documents such as account statements"""

    investment_profile: Optional[InvestmentProfileUpdate] = None
    r"""Investor profile."""

    managed: Optional[bool] = None
    r"""A boolean to indicate if an account is managed"""

    parties: Optional[List[PartyRequestUpdate]] = None
    r"""Parties associated with the account (e.g. custodian)."""

    primary_registered_rep_id: Optional[str] = None
    r"""The primary registered representative for the account"""

    tax_profile: Optional[AccountTaxProfileUpdate] = None
    r"""The account tax profile."""

    trusted_contacts: Optional[List[TrustedContactUpdate]] = None
    r"""A list of persons designated to verify the well being of the account holder."""

    wrap_fee_billed: Optional[bool] = None
    r"""A boolean to indicate if an account is a wrap brokerage account"""
