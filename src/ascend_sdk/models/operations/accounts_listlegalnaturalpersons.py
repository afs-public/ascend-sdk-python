"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    httpmetadata as components_httpmetadata,
    listlegalnaturalpersonsresponse as components_listlegalnaturalpersonsresponse,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountsListLegalNaturalPersonsRequestTypedDict(TypedDict):
    page_size: NotRequired[int]
    r"""The maximum number of legal natural persons to return. The service may return fewer than this value. If unspecified, at most 25 legal natural persons will be returned. The maximum value is 100; values above 100 will be coerced to 100."""
    page_token: NotRequired[str]
    r"""A page token, received from a previous `ListLegalNaturalPersons` call. Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to `ListLegalNaturalPersons` must match the call that provided the page token.
    """
    order_by: NotRequired[str]
    r"""The order in which legal natural persons are listed."""
    filter_: NotRequired[str]
    r"""A CEL string to filter results; Use `upperAscii()` for case-insensitive searches; E.g. `given_name.upperAscii()==\"rUsTy\".upperAscii()`; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:
    `legal_natural_person_id`
    `correspondent_id`
    `given_name`
    `family_name`
    `tax_id`
    `tax_id_type`
    `investigation_id`
    """


class AccountsListLegalNaturalPersonsRequest(BaseModel):
    page_size: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The maximum number of legal natural persons to return. The service may return fewer than this value. If unspecified, at most 25 legal natural persons will be returned. The maximum value is 100; values above 100 will be coerced to 100."""

    page_token: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A page token, received from a previous `ListLegalNaturalPersons` call. Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to `ListLegalNaturalPersons` must match the call that provided the page token.
    """

    order_by: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The order in which legal natural persons are listed."""

    filter_: Annotated[
        Optional[str],
        pydantic.Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A CEL string to filter results; Use `upperAscii()` for case-insensitive searches; E.g. `given_name.upperAscii()==\"rUsTy\".upperAscii()`; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information; Filter options include:
    `legal_natural_person_id`
    `correspondent_id`
    `given_name`
    `family_name`
    `tax_id`
    `tax_id_type`
    `investigation_id`
    """


class AccountsListLegalNaturalPersonsResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    list_legal_natural_persons_response: NotRequired[
        components_listlegalnaturalpersonsresponse.ListLegalNaturalPersonsResponseTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""


class AccountsListLegalNaturalPersonsResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    list_legal_natural_persons_response: Optional[
        components_listlegalnaturalpersonsresponse.ListLegalNaturalPersonsResponse
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""
