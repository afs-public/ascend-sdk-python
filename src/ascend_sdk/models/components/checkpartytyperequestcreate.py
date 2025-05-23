"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.types import BaseModel
from typing_extensions import TypedDict


class CheckPartyTypeRequestCreateTypedDict(TypedDict):
    r"""Request to determine if a potential cash journal will be considered first party or third party"""

    destination_account: str
    r"""The destination account of the potential cash journal"""
    source_account: str
    r"""The source account of the potential cash journal"""


class CheckPartyTypeRequestCreate(BaseModel):
    r"""Request to determine if a potential cash journal will be considered first party or third party"""

    destination_account: str
    r"""The destination account of the potential cash journal"""

    source_account: str
    r"""The source account of the potential cash journal"""
