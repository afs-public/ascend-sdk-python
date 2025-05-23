"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dateupdate import DateUpdate, DateUpdateTypedDict
from ascend_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class LargeTraderUpdateTypedDict(TypedDict):
    r"""A large trader."""

    effective_date: NotRequired[DateUpdateTypedDict]
    r"""Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

    * A full date, with non-zero year, month, and day values * A month and day value, with a zero year, such as an anniversary * A year on its own, with zero month and day values * A year and month value, with a zero day, such as a credit card expiration date

    Related types are [google.type.TimeOfDay][google.type.TimeOfDay] and `google.protobuf.Timestamp`.
    """
    large_trader_id: NotRequired[str]
    r"""SEC-issued ID signifying the person/entity as a large trader; Required for CAIS regulatory reporting."""


class LargeTraderUpdate(BaseModel):
    r"""A large trader."""

    effective_date: Optional[DateUpdate] = None
    r"""Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

    * A full date, with non-zero year, month, and day values * A month and day value, with a zero year, such as an anniversary * A year on its own, with zero month and day values * A year and month value, with a zero day, such as a credit card expiration date

    Related types are [google.type.TimeOfDay][google.type.TimeOfDay] and `google.protobuf.Timestamp`.
    """

    large_trader_id: Optional[str] = None
    r"""SEC-issued ID signifying the person/entity as a large trader; Required for CAIS regulatory reporting."""
