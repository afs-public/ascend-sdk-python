"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.types import BaseModel
from typing_extensions import TypedDict


class CustomerReferralSourceCreateTypedDict(TypedDict):
    r"""Customer Referral Source"""

    name: str
    r"""The name of the referrer"""
    relationship_to_applicant: str
    r"""The relationship of the referrer to the applicant"""
    relationship_years_with_applicant: int
    r"""The years the referrer has known the applicant If the referrer has known the applicant for less than a year, they must specify 1"""
    relationship_years_with_broker: int
    r"""The years the referrer has known the broker If the referrer has known the broker for less than a year, they must specify 1"""


class CustomerReferralSourceCreate(BaseModel):
    r"""Customer Referral Source"""

    name: str
    r"""The name of the referrer"""

    relationship_to_applicant: str
    r"""The relationship of the referrer to the applicant"""

    relationship_years_with_applicant: int
    r"""The years the referrer has known the applicant If the referrer has known the applicant for less than a year, they must specify 1"""

    relationship_years_with_broker: int
    r"""The years the referrer has known the broker If the referrer has known the broker for less than a year, they must specify 1"""
