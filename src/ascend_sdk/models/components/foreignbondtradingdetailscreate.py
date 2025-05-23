"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .foreignbondtradingdetailcreate import (
    ForeignBondTradingDetailCreate,
    ForeignBondTradingDetailCreateTypedDict,
)
from ascend_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ForeignBondTradingDetailsCreateTypedDict(TypedDict):
    r"""Foreign bond trading detail"""

    foreign_bond_trading: bool
    r"""Does the account anticipate trading in foreign bonds"""
    foreign_bond_trading_detail: NotRequired[
        List[ForeignBondTradingDetailCreateTypedDict]
    ]
    r"""The foreign bond trading countries details. If yes, than please provide details"""


class ForeignBondTradingDetailsCreate(BaseModel):
    r"""Foreign bond trading detail"""

    foreign_bond_trading: bool
    r"""Does the account anticipate trading in foreign bonds"""

    foreign_bond_trading_detail: Optional[List[ForeignBondTradingDetailCreate]] = None
    r"""The foreign bond trading countries details. If yes, than please provide details"""
