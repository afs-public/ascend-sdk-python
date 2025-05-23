"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .legalagreement import LegalAgreement, LegalAgreementTypedDict
from ascend_sdk import utils
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import validate_open_enum
from enum import Enum
from pydantic.functional_validators import PlainValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class EnrollmentType(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The enrollment type."""

    ENROLLMENT_TYPE_UNSPECIFIED = "ENROLLMENT_TYPE_UNSPECIFIED"
    REGISTRATION_INDIVIDUAL = "REGISTRATION_INDIVIDUAL"
    LENDING_FULLY_PAID_STOCK_LOAN = "LENDING_FULLY_PAID_STOCK_LOAN"
    BENEFICIARY_DESIGNATION = "BENEFICIARY_DESIGNATION"
    REGISTRATION_JOINT_WROS = "REGISTRATION_JOINT_WROS"
    REGISTRATION_JOINT_TIC = "REGISTRATION_JOINT_TIC"
    REGISTRATION_JOINT_TBE = "REGISTRATION_JOINT_TBE"
    REGISTRATION_JOINT_CP = "REGISTRATION_JOINT_CP"
    REGISTRATION_ESTATE = "REGISTRATION_ESTATE"
    REGISTRATION_IRA_TRADITIONAL = "REGISTRATION_IRA_TRADITIONAL"
    REGISTRATION_IRA_SIMPLE = "REGISTRATION_IRA_SIMPLE"
    REGISTRATION_IRA_SEP = "REGISTRATION_IRA_SEP"
    REGISTRATION_IRA_ROTH = "REGISTRATION_IRA_ROTH"
    REGISTRATION_IRA_ROLLOVER = "REGISTRATION_IRA_ROLLOVER"
    REGISTRATION_TRUST = "REGISTRATION_TRUST"
    REGISTRATION_CORPORATION = "REGISTRATION_CORPORATION"
    REGISTRATION_LLC = "REGISTRATION_LLC"
    CASH_FDIC_CASH_SWEEP = "CASH_FDIC_CASH_SWEEP"
    RETIREMENT_BENEFICIARY_DESIGNATION = "RETIREMENT_BENEFICIARY_DESIGNATION"
    DIVIDEND_REINVESTMENT_PLAN = "DIVIDEND_REINVESTMENT_PLAN"
    REGISTRATION_IRA_BENEFICIARY_TRADITIONAL = (
        "REGISTRATION_IRA_BENEFICIARY_TRADITIONAL"
    )
    REGISTRATION_IRA_BENEFICIARY_ROTH = "REGISTRATION_IRA_BENEFICIARY_ROTH"
    REGISTRATION_INDIVIDUAL_FOREIGN = "REGISTRATION_INDIVIDUAL_FOREIGN"
    REGISTRATION_CUSTODIAL = "REGISTRATION_CUSTODIAL"
    VIRTUAL_ACCOUNT_NUMBER = "VIRTUAL_ACCOUNT_NUMBER"


class AvailableEnrollmentTypedDict(TypedDict):
    r"""Available Enrollment on an Account."""

    agreements: NotRequired[List[LegalAgreementTypedDict]]
    r"""A list of legal agreements associated with the enrollment."""
    enrollment_type: NotRequired[EnrollmentType]
    r"""The enrollment type."""


class AvailableEnrollment(BaseModel):
    r"""Available Enrollment on an Account."""

    agreements: Optional[List[LegalAgreement]] = None
    r"""A list of legal agreements associated with the enrollment."""

    enrollment_type: Annotated[
        Optional[EnrollmentType], PlainValidator(validate_open_enum(False))
    ] = None
    r"""The enrollment type."""
