"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .position import Position, PositionTypedDict
from ascend_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ListPositionsResponseTypedDict(TypedDict):
    r"""positions with 0 values will be returned if there are offsetting position deltas or a position was reduced to 0"""

    next_page_token: NotRequired[str]
    r"""The next page token returned by this call. Can be provided in another request to retrieve the subsequent page"""
    positions: NotRequired[List[PositionTypedDict]]
    r"""The positions returned"""


class ListPositionsResponse(BaseModel):
    r"""positions with 0 values will be returned if there are offsetting position deltas or a position was reduced to 0"""

    next_page_token: Optional[str] = None
    r"""The next page token returned by this call. Can be provided in another request to retrieve the subsequent page"""

    positions: Optional[List[Position]] = None
    r"""The positions returned"""
