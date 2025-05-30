"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    bankrelationship as components_bankrelationship,
    cancelbankrelationshiprequestcreate as components_cancelbankrelationshiprequestcreate,
    httpmetadata as components_httpmetadata,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BankRelationshipsCancelBankRelationshipRequestTypedDict(TypedDict):
    account_id: str
    r"""The account id."""
    bank_relationship_id: str
    r"""The bankRelationship id."""
    cancel_bank_relationship_request_create: components_cancelbankrelationshiprequestcreate.CancelBankRelationshipRequestCreateTypedDict


class BankRelationshipsCancelBankRelationshipRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account id."""

    bank_relationship_id: Annotated[
        str,
        pydantic.Field(alias="bankRelationship_id"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The bankRelationship id."""

    cancel_bank_relationship_request_create: Annotated[
        components_cancelbankrelationshiprequestcreate.CancelBankRelationshipRequestCreate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class BankRelationshipsCancelBankRelationshipResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    bank_relationship: NotRequired[
        components_bankrelationship.BankRelationshipTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request has an invalid argument."""


class BankRelationshipsCancelBankRelationshipResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    bank_relationship: Optional[components_bankrelationship.BankRelationship] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request has an invalid argument."""
