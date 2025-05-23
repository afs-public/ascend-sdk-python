"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    httpmetadata as components_httpmetadata,
    status as components_status,
    watchlistitem as components_watchlistitem,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class WatchlistServiceGetWatchlistItemRequestTypedDict(TypedDict):
    watchlist_id: str
    r"""The watchlist id."""
    item_id: str
    r"""The item id."""


class WatchlistServiceGetWatchlistItemRequest(BaseModel):
    watchlist_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The watchlist id."""

    item_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The item id."""


class WatchlistServiceGetWatchlistItemResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    watchlist_item: NotRequired[components_watchlistitem.WatchlistItemTypedDict]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""


class WatchlistServiceGetWatchlistItemResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    watchlist_item: Optional[components_watchlistitem.WatchlistItem] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""
