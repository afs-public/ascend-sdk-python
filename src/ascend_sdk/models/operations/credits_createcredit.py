"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    httpmetadata as components_httpmetadata,
    status as components_status,
    transferscredit as components_transferscredit,
    transferscreditcreate as components_transferscreditcreate,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreditsCreateCreditRequestTypedDict(TypedDict):
    account_id: str
    r"""The account id."""
    transfers_credit_create: (
        components_transferscreditcreate.TransfersCreditCreateTypedDict
    )


class CreditsCreateCreditRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account id."""

    transfers_credit_create: Annotated[
        components_transferscreditcreate.TransfersCreditCreate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CreditsCreateCreditResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    transfers_credit: NotRequired[components_transferscredit.TransfersCreditTypedDict]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request has an invalid argument."""


class CreditsCreateCreditResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    transfers_credit: Optional[components_transferscredit.TransfersCredit] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request has an invalid argument."""
