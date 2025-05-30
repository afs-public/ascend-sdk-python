"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    httpmetadata as components_httpmetadata,
    listeventmessagesresponse as components_listeventmessagesresponse,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ReaderListEventMessagesRequestTypedDict(TypedDict):
    filter_: NotRequired[str]
    r"""A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; If left empty, all events the user has permission to view are returned; Filter options include:
    `name`
    `message_id`
    `event_type`
    `publish_time`
    `partition_key`
    `client_id`
    `correspondent_id`
    `account_id`
    """
    page_size: NotRequired[int]
    r"""The number of entries to return in a single page; Default = 100; Maximum = 1000"""
    page_token: NotRequired[str]
    r"""Page token used for pagination; Supplying a page token returns the next page of results"""


class ReaderListEventMessagesRequest(BaseModel):
    filter_: Annotated[
        Optional[str],
        pydantic.Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; If left empty, all events the user has permission to view are returned; Filter options include:
    `name`
    `message_id`
    `event_type`
    `publish_time`
    `partition_key`
    `client_id`
    `correspondent_id`
    `account_id`
    """

    page_size: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The number of entries to return in a single page; Default = 100; Maximum = 1000"""

    page_token: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Page token used for pagination; Supplying a page token returns the next page of results"""


class ReaderListEventMessagesResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    list_event_messages_response: NotRequired[
        components_listeventmessagesresponse.ListEventMessagesResponseTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request was not well formed."""


class ReaderListEventMessagesResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    list_event_messages_response: Optional[
        components_listeventmessagesresponse.ListEventMessagesResponse
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request was not well formed."""
