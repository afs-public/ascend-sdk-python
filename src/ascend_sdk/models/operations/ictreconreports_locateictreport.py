"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    httpmetadata as components_httpmetadata,
    locateictreportresponse as components_locateictreportresponse,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ProgramDateFilterProgram(str, Enum):
    r"""The ICT program for which to locate the report."""

    ICT_PROGRAM_UNSPECIFIED = "ICT_PROGRAM_UNSPECIFIED"
    BROKER_PARTNER = "BROKER_PARTNER"
    DEPOSIT_ONLY = "DEPOSIT_ONLY"
    BANKING_PARTNER = "BANKING_PARTNER"
    WITHDRAWAL_ONLY = "WITHDRAWAL_ONLY"
    DIGITAL_PARTNER = "DIGITAL_PARTNER"


class IctReconReportsLocateIctReportRequestTypedDict(TypedDict):
    correspondent_id: str
    r"""The correspondent id."""
    batch_id: NotRequired[str]
    r"""The id of the ICT batch for which to locate the report."""
    program_date_filter_program: NotRequired[ProgramDateFilterProgram]
    r"""The ICT program for which to locate the report."""
    program_date_filter_process_date_year: NotRequired[int]
    r"""Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year."""
    program_date_filter_process_date_month: NotRequired[int]
    r"""Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day."""
    program_date_filter_process_date_day: NotRequired[int]
    r"""Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant."""


class IctReconReportsLocateIctReportRequest(BaseModel):
    correspondent_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The correspondent id."""

    batch_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The id of the ICT batch for which to locate the report."""

    program_date_filter_program: Annotated[
        Optional[ProgramDateFilterProgram],
        pydantic.Field(alias="program_date_filter.program"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The ICT program for which to locate the report."""

    program_date_filter_process_date_year: Annotated[
        Optional[int],
        pydantic.Field(alias="program_date_filter.process_date.year"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year."""

    program_date_filter_process_date_month: Annotated[
        Optional[int],
        pydantic.Field(alias="program_date_filter.process_date.month"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day."""

    program_date_filter_process_date_day: Annotated[
        Optional[int],
        pydantic.Field(alias="program_date_filter.process_date.day"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant."""


class IctReconReportsLocateIctReportResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    locate_ict_report_response: NotRequired[
        components_locateictreportresponse.LocateIctReportResponseTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request has an invalid argument."""


class IctReconReportsLocateIctReportResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    locate_ict_report_response: Optional[
        components_locateictreportresponse.LocateIctReportResponse
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request has an invalid argument."""
