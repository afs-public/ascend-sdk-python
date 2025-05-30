"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    httpmetadata as components_httpmetadata,
    interestedparty as components_interestedparty,
    interestedpartyupdate as components_interestedpartyupdate,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountsUpdateInterestedPartyRequestTypedDict(TypedDict):
    account_id: str
    r"""The account id."""
    interested_party_id: str
    r"""The interestedParty id."""
    interested_party_update: (
        components_interestedpartyupdate.InterestedPartyUpdateTypedDict
    )
    update_mask: NotRequired[str]
    r"""The list of fields to update. Updatable Fields  `recipient`  `statement_delivery_preference`  `trade_confirmation_delivery_preference`  `mailing_address.region_code`  `mailing_address.postal_code`  `mailing_address.administrative_area`  `mailing_address.locality`  `mailing_address.address_lines`"""


class AccountsUpdateInterestedPartyRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account id."""

    interested_party_id: Annotated[
        str,
        pydantic.Field(alias="interestedParty_id"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The interestedParty id."""

    interested_party_update: Annotated[
        components_interestedpartyupdate.InterestedPartyUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    update_mask: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The list of fields to update. Updatable Fields  `recipient`  `statement_delivery_preference`  `trade_confirmation_delivery_preference`  `mailing_address.region_code`  `mailing_address.postal_code`  `mailing_address.administrative_area`  `mailing_address.locality`  `mailing_address.address_lines`"""


class AccountsUpdateInterestedPartyResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    interested_party: NotRequired[components_interestedparty.InterestedPartyTypedDict]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""


class AccountsUpdateInterestedPartyResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    interested_party: Optional[components_interestedparty.InterestedParty] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""
