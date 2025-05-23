"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .agreement import Agreement, AgreementTypedDict
from ascend_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ListAgreementsResponseTypedDict(TypedDict):
    r"""The response to list Agreements on an Account."""

    agreements: NotRequired[List[AgreementTypedDict]]
    r"""The list of Agreements on an Account"""
    next_page_token: NotRequired[str]
    r"""A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages."""


class ListAgreementsResponse(BaseModel):
    r"""The response to list Agreements on an Account."""

    agreements: Optional[List[Agreement]] = None
    r"""The list of Agreements on an Account"""

    next_page_token: Optional[str] = None
    r"""A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages."""
