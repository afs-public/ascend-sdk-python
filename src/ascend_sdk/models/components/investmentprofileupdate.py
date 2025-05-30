"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountgoalsupdate import AccountGoalsUpdate, AccountGoalsUpdateTypedDict
from .customerprofileupdate import CustomerProfileUpdate, CustomerProfileUpdateTypedDict
from ascend_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class InvestmentProfileUpdateTypedDict(TypedDict):
    r"""Investor profile."""

    account_goals: NotRequired[AccountGoalsUpdateTypedDict]
    r"""The account goals on an investor profile."""
    customer_profile: NotRequired[CustomerProfileUpdateTypedDict]
    r"""A detailed summary of financial and personal details of an investor, to help understand the investor's financial standing, investment experience and risk tolerance."""


class InvestmentProfileUpdate(BaseModel):
    r"""Investor profile."""

    account_goals: Optional[AccountGoalsUpdate] = None
    r"""The account goals on an investor profile."""

    customer_profile: Optional[CustomerProfileUpdate] = None
    r"""A detailed summary of financial and personal details of an investor, to help understand the investor's financial standing, investment experience and risk tolerance."""
