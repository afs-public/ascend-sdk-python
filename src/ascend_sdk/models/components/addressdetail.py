"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AddressDetailTypedDict(TypedDict):
    r"""Address detail used for Dow Jones Profile details"""

    address_city: NotRequired[str]
    r"""Dow Jones persons address city"""
    address_line: NotRequired[str]
    r"""Dow Jones persons address line"""
    administrative_area: NotRequired[str]
    r"""Dow Jones persons address administrative area"""
    postal_code: NotRequired[str]
    r"""Dow Jones persons address postal code"""
    region_code: NotRequired[str]
    r"""Two character region code, complies with https://cldr.unicode.org/index Example values: \"US\", \"CA\" """


class AddressDetail(BaseModel):
    r"""Address detail used for Dow Jones Profile details"""

    address_city: Optional[str] = None
    r"""Dow Jones persons address city"""

    address_line: Optional[str] = None
    r"""Dow Jones persons address line"""

    administrative_area: Optional[str] = None
    r"""Dow Jones persons address administrative area"""

    postal_code: Optional[str] = None
    r"""Dow Jones persons address postal code"""

    region_code: Optional[str] = None
    r"""Two character region code, complies with https://cldr.unicode.org/index Example values: \"US\", \"CA\" """
