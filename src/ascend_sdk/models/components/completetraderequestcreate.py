"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .feecreate import FeeCreate, FeeCreateTypedDict
from ascend_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class CompleteTradeRequestCreateTypedDict(TypedDict):
    r"""A request for completing a trade."""

    name: str
    r"""The name of the trade to complete."""
    fees: NotRequired[List[FeeCreateTypedDict]]
    r"""Client calculated fees to use while completing an existing trade."""


class CompleteTradeRequestCreate(BaseModel):
    r"""A request for completing a trade."""

    name: str
    r"""The name of the trade to complete."""

    fees: Optional[List[FeeCreate]] = None
    r"""Client calculated fees to use while completing an existing trade."""
