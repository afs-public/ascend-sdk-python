"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    account as components_account,
    httpmetadata as components_httpmetadata,
    status as components_status,
)
from ascend_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountsCreateAccountResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    account: NotRequired[components_account.AccountTypedDict]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""


class AccountsCreateAccountResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    account: Optional[components_account.Account] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request is not valid, additional information may be present in the BadRequest details."""
