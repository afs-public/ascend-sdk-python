"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    httpmetadata as components_httpmetadata,
    listtransfersresponse as components_listtransfersresponse,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountTransfersListTransfersRequestTypedDict(TypedDict):
    correspondent_id: str
    r"""The correspondent id."""
    account_id: str
    r"""The account id."""
    page_size: NotRequired[int]
    r"""The maximum number of transfers to return. The service may return fewer than this value. If unspecified, at most 100 transfers will be returned. The maximum value is 200; values above 200 will be coerced to 200."""
    page_token: NotRequired[str]
    r"""A page token, received from a previous `ListTransfers` call. Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to `ListTransfers` must match the call that provided the page token.
    """
    filter_: NotRequired[str]
    r"""A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information;

    Currently supported CEL filters: -------------------------------- * acat_control_number        (add to queries for better performance) * state     == State.* * nscc_status  == NsccStatus.* * direction   == Direction.* * transfer_type == TransferType.* * reject_code  == RejectCode.* * create_time * last_nscc_status_updated_time * receiver.account_id * receiver.account_number * receiver.participant_number * receiver.correspondent_code * receiver.correspondent_id * deliverer.account_id * deliverer.account_number * deliverer.participant_number * deliverer.correspondent_code * deliverer.correspondent_id

    - Empty filters are allowed, which return the most recent page_size worth of transfers, in practice this is not performant  and should be avoided if possible

    - Macros are NOT allowed, using them will result in an INVALID_ARGUMENT being returned

    - The following CEL operators are NOT allowed, using them will result in an INVALID_ARGUMENT being returned:    string.matches(substr)    +    -    /    *

    - Queries using acat_control_number will result in increased performance
    """


class AccountTransfersListTransfersRequest(BaseModel):
    correspondent_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The correspondent id."""

    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account id."""

    page_size: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The maximum number of transfers to return. The service may return fewer than this value. If unspecified, at most 100 transfers will be returned. The maximum value is 200; values above 200 will be coerced to 200."""

    page_token: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A page token, received from a previous `ListTransfers` call. Provide this to retrieve the subsequent page.

    When paginating, all other parameters provided to `ListTransfers` must match the call that provided the page token.
    """

    filter_: Annotated[
        Optional[str],
        pydantic.Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A CEL string to filter results; See the [CEL Search](https://developer.apexclearing.com/apex-fintech-solutions/docs/cel-search) page in Guides for more information;

    Currently supported CEL filters: -------------------------------- * acat_control_number        (add to queries for better performance) * state     == State.* * nscc_status  == NsccStatus.* * direction   == Direction.* * transfer_type == TransferType.* * reject_code  == RejectCode.* * create_time * last_nscc_status_updated_time * receiver.account_id * receiver.account_number * receiver.participant_number * receiver.correspondent_code * receiver.correspondent_id * deliverer.account_id * deliverer.account_number * deliverer.participant_number * deliverer.correspondent_code * deliverer.correspondent_id

    - Empty filters are allowed, which return the most recent page_size worth of transfers, in practice this is not performant  and should be avoided if possible

    - Macros are NOT allowed, using them will result in an INVALID_ARGUMENT being returned

    - The following CEL operators are NOT allowed, using them will result in an INVALID_ARGUMENT being returned:    string.matches(substr)    +    -    /    *

    - Queries using acat_control_number will result in increased performance
    """


class AccountTransfersListTransfersResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    list_transfers_response: NotRequired[
        components_listtransfersresponse.ListTransfersResponseTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request has an invalid argument."""


class AccountTransfersListTransfersResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    list_transfers_response: Optional[
        components_listtransfersresponse.ListTransfersResponse
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request has an invalid argument."""
