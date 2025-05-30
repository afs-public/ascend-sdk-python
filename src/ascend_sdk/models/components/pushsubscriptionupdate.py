"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httppushcallbackupdate import (
    HTTPPushCallbackUpdate,
    HTTPPushCallbackUpdateTypedDict,
)
from ascend_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PushSubscriptionUpdateTypedDict(TypedDict):
    r"""Configuration information about a push subscription"""

    display_name: NotRequired[str]
    r"""The user-defined name for the subscription"""
    event_types: NotRequired[List[str]]
    r"""Filter for event types; [\"\*\"] matches all values; Suffix wildcards using \"\*\" (e.g. [\"account.\*\"]) are supported"""
    http_callback: NotRequired[HTTPPushCallbackUpdateTypedDict]
    r"""Configuration information about an HTTP target callback"""


class PushSubscriptionUpdate(BaseModel):
    r"""Configuration information about a push subscription"""

    display_name: Optional[str] = None
    r"""The user-defined name for the subscription"""

    event_types: Optional[List[str]] = None
    r"""Filter for event types; [\"\*\"] matches all values; Suffix wildcards using \"\*\" (e.g. [\"account.\*\"]) are supported"""

    http_callback: Optional[HTTPPushCallbackUpdate] = None
    r"""Configuration information about an HTTP target callback"""
