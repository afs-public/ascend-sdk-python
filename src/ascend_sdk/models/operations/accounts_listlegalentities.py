"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    httpmetadata as components_httpmetadata,
    listlegalentitiesresponse as components_listlegalentitiesresponse,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountsListLegalEntitiesRequestTypedDict(TypedDict):
    page_size: NotRequired[int]
    r"""The maximum number of legal entities to return. The service may return fewer than this value. If unspecified, at most 25 legal entities will be returned. The maximum value is 100; values above 100 will be coerced to 100."""
    page_token: NotRequired[str]
    r"""A page token, received from a previous `ListLegalEntities` call. Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to `ListLegalEntities` must match the call that provided the page token.
    """
    order_by: NotRequired[str]
    r"""The order in which legal entities are listed."""
    filter_: NotRequired[str]
    r"""A CEL string to filter results; Use `upperAscii()` for case-insensitive searches; E.g. `entity_name.upperAscii()==\"AcMe,InC\".upperAscii()`; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:
    `legal_entity_id`
    `investigation_id`
    `exempt_customer_reason`
    `exempt_verifying_beneficial_owners`
    """


class AccountsListLegalEntitiesRequest(BaseModel):
    page_size: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The maximum number of legal entities to return. The service may return fewer than this value. If unspecified, at most 25 legal entities will be returned. The maximum value is 100; values above 100 will be coerced to 100."""

    page_token: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A page token, received from a previous `ListLegalEntities` call. Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to `ListLegalEntities` must match the call that provided the page token.
    """

    order_by: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The order in which legal entities are listed."""

    filter_: Annotated[
        Optional[str],
        pydantic.Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A CEL string to filter results; Use `upperAscii()` for case-insensitive searches; E.g. `entity_name.upperAscii()==\"AcMe,InC\".upperAscii()`; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:
    `legal_entity_id`
    `investigation_id`
    `exempt_customer_reason`
    `exempt_verifying_beneficial_owners`
    """


class AccountsListLegalEntitiesResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    list_legal_entities_response: NotRequired[
        components_listlegalentitiesresponse.ListLegalEntitiesResponseTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""


class AccountsListLegalEntitiesResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    list_legal_entities_response: Optional[
        components_listlegalentitiesresponse.ListLegalEntitiesResponse
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""
