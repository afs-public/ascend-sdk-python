"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    endlargetraderrequestcreate as components_endlargetraderrequestcreate,
    httpmetadata as components_httpmetadata,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountsEndLargeTraderLegalNaturalPersonRequestTypedDict(TypedDict):
    legal_natural_person_id: str
    r"""The legalNaturalPerson id."""
    end_large_trader_request_create: (
        components_endlargetraderrequestcreate.EndLargeTraderRequestCreateTypedDict
    )


class AccountsEndLargeTraderLegalNaturalPersonRequest(BaseModel):
    legal_natural_person_id: Annotated[
        str,
        pydantic.Field(alias="legalNaturalPerson_id"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The legalNaturalPerson id."""

    end_large_trader_request_create: Annotated[
        components_endlargetraderrequestcreate.EndLargeTraderRequestCreate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class AccountsEndLargeTraderLegalNaturalPersonResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""


class AccountsEndLargeTraderLegalNaturalPersonResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""
