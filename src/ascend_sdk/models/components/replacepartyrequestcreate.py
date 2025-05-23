"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .partyrequestcreate import PartyRequestCreate, PartyRequestCreateTypedDict
from ascend_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ReplacePartyRequestCreateTypedDict(TypedDict):
    r"""A request to replace a party on an account"""

    name: str
    r"""The ID of the party to replace Format: accounts/{account}/parties/{party}"""
    party: PartyRequestCreateTypedDict
    r"""A single record representing an owner or manager of an Account. Contains fully populated Party Identity object."""
    authorized_by_party_ids: NotRequired[List[str]]
    r"""A list of Party IDs on the account that have approved the replacing of a party. The required signers are defined by the Registration Type of the Account. e.g. Individual Registrations require one signer, Joint Registrations require all Joint Owners to sign"""


class ReplacePartyRequestCreate(BaseModel):
    r"""A request to replace a party on an account"""

    name: str
    r"""The ID of the party to replace Format: accounts/{account}/parties/{party}"""

    party: PartyRequestCreate
    r"""A single record representing an owner or manager of an Account. Contains fully populated Party Identity object."""

    authorized_by_party_ids: Optional[List[str]] = None
    r"""A list of Party IDs on the account that have approved the replacing of a party. The required signers are defined by the Registration Type of the Account. e.g. Individual Registrations require one signer, Joint Registrations require all Joint Owners to sign"""
