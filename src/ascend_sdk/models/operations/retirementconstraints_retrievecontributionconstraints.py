"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    contributionconstraints as components_contributionconstraints,
    httpmetadata as components_httpmetadata,
    retrievecontributionconstraintsrequestcreate as components_retrievecontributionconstraintsrequestcreate,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RetirementConstraintsRetrieveContributionConstraintsRequestTypedDict(TypedDict):
    account_id: str
    r"""The account id."""
    retrieve_contribution_constraints_request_create: components_retrievecontributionconstraintsrequestcreate.RetrieveContributionConstraintsRequestCreateTypedDict


class RetirementConstraintsRetrieveContributionConstraintsRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account id."""

    retrieve_contribution_constraints_request_create: Annotated[
        components_retrievecontributionconstraintsrequestcreate.RetrieveContributionConstraintsRequestCreate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class RetirementConstraintsRetrieveContributionConstraintsResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    contribution_constraints: NotRequired[
        components_contributionconstraints.ContributionConstraintsTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request has an invalid argument."""


class RetirementConstraintsRetrieveContributionConstraintsResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    contribution_constraints: Optional[
        components_contributionconstraints.ContributionConstraints
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request has an invalid argument."""
