"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CancelAchDepositRequestCreateTypedDict(TypedDict):
    r"""Request to cancel an existing ACH deposit."""

    name: str
    r"""The name of the ACH deposit to cancel."""
    reason: NotRequired[str]
    r"""Reason why the ACH deposit is being canceled."""


class CancelAchDepositRequestCreate(BaseModel):
    r"""Request to cancel an existing ACH deposit."""

    name: str
    r"""The name of the ACH deposit to cancel."""

    reason: Optional[str] = None
    r"""Reason why the ACH deposit is being canceled."""
