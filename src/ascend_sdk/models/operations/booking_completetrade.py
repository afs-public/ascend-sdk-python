"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    completetraderequestcreate as components_completetraderequestcreate,
    completetraderesponse as components_completetraderesponse,
    httpmetadata as components_httpmetadata,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BookingCompleteTradeRequestTypedDict(TypedDict):
    account_id: str
    r"""The account id."""
    trade_id: str
    r"""The trade id."""
    complete_trade_request_create: (
        components_completetraderequestcreate.CompleteTradeRequestCreateTypedDict
    )


class BookingCompleteTradeRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account id."""

    trade_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The trade id."""

    complete_trade_request_create: Annotated[
        components_completetraderequestcreate.CompleteTradeRequestCreate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class BookingCompleteTradeResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    complete_trade_response: NotRequired[
        components_completetraderesponse.CompleteTradeResponseTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request is not valid.
    FAILED_PRECONDITION: The operation was rejected because the system is not in a state required for the operation's processing.
    """


class BookingCompleteTradeResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    complete_trade_response: Optional[
        components_completetraderesponse.CompleteTradeResponse
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request is not valid.
    FAILED_PRECONDITION: The operation was rejected because the system is not in a state required for the operation's processing.
    """
