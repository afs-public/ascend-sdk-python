"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.types import BaseModel
from typing_extensions import TypedDict


class CancelBankRelationshipRequestCreateTypedDict(TypedDict):
    r"""Request to cancel an existing bank relationship."""

    comment: str
    r"""Comment when canceling the bank relationship."""
    name: str
    r"""The name of the bank relationship to be canceled."""


class CancelBankRelationshipRequestCreate(BaseModel):
    r"""Request to cancel an existing bank relationship."""

    comment: str
    r"""Comment when canceling the bank relationship."""

    name: str
    r"""The name of the bank relationship to be canceled."""
