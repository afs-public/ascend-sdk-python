"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    cancelexecutionrequestcreate as components_cancelexecutionrequestcreate,
    cancelexecutionresponse as components_cancelexecutionresponse,
    httpmetadata as components_httpmetadata,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BookingCancelExecutionRequestTypedDict(TypedDict):
    account_id: str
    r"""The account id."""
    trade_id: str
    r"""The trade id."""
    execution_id: str
    r"""The execution id."""
    cancel_execution_request_create: (
        components_cancelexecutionrequestcreate.CancelExecutionRequestCreateTypedDict
    )


class BookingCancelExecutionRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account id."""

    trade_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The trade id."""

    execution_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The execution id."""

    cancel_execution_request_create: Annotated[
        components_cancelexecutionrequestcreate.CancelExecutionRequestCreate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class BookingCancelExecutionResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    cancel_execution_response: NotRequired[
        components_cancelexecutionresponse.CancelExecutionResponseTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request is not valid.
    FAILED_PRECONDITION: The operation was rejected because the system is not in a state required for the operation's processing.
    """


class BookingCancelExecutionResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    cancel_execution_response: Optional[
        components_cancelexecutionresponse.CancelExecutionResponse
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request is not valid.
    FAILED_PRECONDITION: The operation was rejected because the system is not in a state required for the operation's processing.
    """
