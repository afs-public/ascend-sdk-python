"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .addresscreate import AddressCreate, AddressCreateTypedDict
from ascend_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class WireWithdrawalBeneficiaryCreateTypedDict(TypedDict):
    r"""The person or entity taking receipt of the wired funds"""

    account: str
    r"""The bank account of the person or entity taking receipt of the wired funds. Limited to 25 characters if intermediaryDetails.account is set"""
    account_title: NotRequired[str]
    r"""The name of the person or entity taking receipt of the wired funds. This field defaults to the name of the account owner and should only be populated when performing a third party wire transfer"""
    address: NotRequired[AddressCreateTypedDict]
    r"""The data structure containing attributes describing the location of an underlying entity."""
    third_party: NotRequired[bool]
    r"""Indicates if this beneficiary is a third party beneficiary. A wire transfer is considered third party if the beneficiary is not the exact same person and/or entity that the funds originated from. This includes wire transfers where the originator account is an individual account and the beneficiary account is a joint account"""


class WireWithdrawalBeneficiaryCreate(BaseModel):
    r"""The person or entity taking receipt of the wired funds"""

    account: str
    r"""The bank account of the person or entity taking receipt of the wired funds. Limited to 25 characters if intermediaryDetails.account is set"""

    account_title: Optional[str] = None
    r"""The name of the person or entity taking receipt of the wired funds. This field defaults to the name of the account owner and should only be populated when performing a third party wire transfer"""

    address: Optional[AddressCreate] = None
    r"""The data structure containing attributes describing the location of an underlying entity."""

    third_party: Optional[bool] = None
    r"""Indicates if this beneficiary is a third party beneficiary. A wire transfer is considered third party if the beneficiary is not the exact same person and/or entity that the funds originated from. This includes wire transfers where the originator account is an individual account and the beneficiary account is a joint account"""
