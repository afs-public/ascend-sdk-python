"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.types import BaseModel
from typing_extensions import TypedDict


class InstitutionCreateTypedDict(TypedDict):
    r"""Institution representing originator or recipient of funds from an Instant Cash Transfer"""

    account_id: str
    r"""Account id at institution"""
    title: str
    r"""Name of the institution"""


class InstitutionCreate(BaseModel):
    r"""Institution representing originator or recipient of funds from an Instant Cash Transfer"""

    account_id: str
    r"""Account id at institution"""

    title: str
    r"""Name of the institution"""
