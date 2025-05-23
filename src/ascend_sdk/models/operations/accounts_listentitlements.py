"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    httpmetadata as components_httpmetadata,
    listentitlementsresponse as components_listentitlementsresponse,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountsListEntitlementsRequestTypedDict(TypedDict):
    account_id: str
    r"""The account id."""
    page_size: NotRequired[int]
    r"""The maximum number of entitlements to return."""
    page_token: NotRequired[str]
    r"""A page token, received from a previous `ListEntitlements` call. Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to `ListEntitlements` must match the call that provided the page token.
    """


class AccountsListEntitlementsRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account id."""

    page_size: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The maximum number of entitlements to return."""

    page_token: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A page token, received from a previous `ListEntitlements` call. Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to `ListEntitlements` must match the call that provided the page token.
    """


class AccountsListEntitlementsResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    list_entitlements_response: NotRequired[
        components_listentitlementsresponse.ListEntitlementsResponseTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""


class AccountsListEntitlementsResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    list_entitlements_response: Optional[
        components_listentitlementsresponse.ListEntitlementsResponse
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""
