"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .enrollment import Enrollment, EnrollmentTypedDict
from ascend_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ListEnrollmentsResponseTypedDict(TypedDict):
    r"""The response to list Enrollments on an Account."""

    enrollments: NotRequired[List[EnrollmentTypedDict]]
    r"""The list of available enrollments"""
    next_page_token: NotRequired[str]
    r"""A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages."""


class ListEnrollmentsResponse(BaseModel):
    r"""The response to list Enrollments on an Account."""

    enrollments: Optional[List[Enrollment]] = None
    r"""The list of available enrollments"""

    next_page_token: Optional[str] = None
    r"""A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages."""
