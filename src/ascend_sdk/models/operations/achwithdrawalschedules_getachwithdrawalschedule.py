"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    achwithdrawalschedule as components_achwithdrawalschedule,
    httpmetadata as components_httpmetadata,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AchWithdrawalSchedulesGetAchWithdrawalScheduleRequestTypedDict(TypedDict):
    account_id: str
    r"""The account id."""
    ach_withdrawal_schedule_id: str
    r"""The achWithdrawalSchedule id."""


class AchWithdrawalSchedulesGetAchWithdrawalScheduleRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account id."""

    ach_withdrawal_schedule_id: Annotated[
        str,
        pydantic.Field(alias="achWithdrawalSchedule_id"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The achWithdrawalSchedule id."""


class AchWithdrawalSchedulesGetAchWithdrawalScheduleResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    ach_withdrawal_schedule: NotRequired[
        components_achwithdrawalschedule.AchWithdrawalScheduleTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request has an invalid argument."""


class AchWithdrawalSchedulesGetAchWithdrawalScheduleResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    ach_withdrawal_schedule: Optional[
        components_achwithdrawalschedule.AchWithdrawalSchedule
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request has an invalid argument."""
