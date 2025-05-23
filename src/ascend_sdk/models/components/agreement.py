"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk import utils
from ascend_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from ascend_sdk.utils import validate_open_enum
from datetime import datetime
from enum import Enum
from pydantic import model_serializer
from pydantic.functional_validators import PlainValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AgreementSource(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""An internal indicator from where the agreement was generated; Typically `ACCOUNTS_SERVICE` if accessing our public APIs"""

    AGREEMENT_SOURCE_UNSPECIFIED = "AGREEMENT_SOURCE_UNSPECIFIED"
    ATLAS_FORM = "ATLAS_FORM"
    OTHER_SOURCE = "OTHER_SOURCE"
    ACCOUNTS_SERVICE = "ACCOUNTS_SERVICE"


class AgreementState(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The status of an agreement which blocks an enrollment; `REQUIRED` if not yet received, or `AFFIRMED` if acknowledgement has been received by AFS"""

    AGREEMENT_STATE_UNSPECIFIED = "AGREEMENT_STATE_UNSPECIFIED"
    REQUIRED = "REQUIRED"
    AFFIRMED = "AFFIRMED"
    VOIDED = "VOIDED"


class AgreementTypedDict(TypedDict):
    r"""A legal Agreement for an Account."""

    affirmation_time: NotRequired[Nullable[datetime]]
    r"""The time recorded relating to when a given agreement is `AFFIRMED` by the Customer; This is set to the time when the affirmation is processed by AFS"""
    agreement_id: NotRequired[str]
    r"""An Apex-generated identifier used to reference a single legal agreement associated with the account"""
    agreement_name: NotRequired[str]
    r"""The friendly name of the agreement; Typically mirrors the enrollment it is attached to (e.g., `LENDING_FULLY_PAID_STOCK_LOAN`)"""
    agreement_source: NotRequired[AgreementSource]
    r"""An internal indicator from where the agreement was generated; Typically `ACCOUNTS_SERVICE` if accessing our public APIs"""
    agreement_state: NotRequired[AgreementState]
    r"""The status of an agreement which blocks an enrollment; `REQUIRED` if not yet received, or `AFFIRMED` if acknowledgement has been received by AFS"""
    agreement_uri: NotRequired[str]
    r"""A URI referencing a static PDF containing the legalese of a given agreement; All agreements of the same nature link to the same publicly-available PDF."""
    agreement_version: NotRequired[str]
    r"""An internal version number based on typographical revisions of the related agreement; Version numbers are automatically updated when new agreements are available and should be of no technical concern to the integrator"""
    enrollment_id: NotRequired[str]
    r"""A system-generated unique identifier referencing a single instance of an enrollment; Used to access the record after creation"""
    legal_entity_id: NotRequired[str]
    r"""References a single entity"""
    legal_natural_person_id: NotRequired[str]
    r"""References a single natural person"""
    name: NotRequired[str]
    r"""The name field Format: accounts/{account}/agreements/{agreement}"""


class Agreement(BaseModel):
    r"""A legal Agreement for an Account."""

    affirmation_time: OptionalNullable[datetime] = UNSET
    r"""The time recorded relating to when a given agreement is `AFFIRMED` by the Customer; This is set to the time when the affirmation is processed by AFS"""

    agreement_id: Optional[str] = None
    r"""An Apex-generated identifier used to reference a single legal agreement associated with the account"""

    agreement_name: Optional[str] = None
    r"""The friendly name of the agreement; Typically mirrors the enrollment it is attached to (e.g., `LENDING_FULLY_PAID_STOCK_LOAN`)"""

    agreement_source: Annotated[
        Optional[AgreementSource], PlainValidator(validate_open_enum(False))
    ] = None
    r"""An internal indicator from where the agreement was generated; Typically `ACCOUNTS_SERVICE` if accessing our public APIs"""

    agreement_state: Annotated[
        Optional[AgreementState], PlainValidator(validate_open_enum(False))
    ] = None
    r"""The status of an agreement which blocks an enrollment; `REQUIRED` if not yet received, or `AFFIRMED` if acknowledgement has been received by AFS"""

    agreement_uri: Optional[str] = None
    r"""A URI referencing a static PDF containing the legalese of a given agreement; All agreements of the same nature link to the same publicly-available PDF."""

    agreement_version: Optional[str] = None
    r"""An internal version number based on typographical revisions of the related agreement; Version numbers are automatically updated when new agreements are available and should be of no technical concern to the integrator"""

    enrollment_id: Optional[str] = None
    r"""A system-generated unique identifier referencing a single instance of an enrollment; Used to access the record after creation"""

    legal_entity_id: Optional[str] = None
    r"""References a single entity"""

    legal_natural_person_id: Optional[str] = None
    r"""References a single natural person"""

    name: Optional[str] = None
    r"""The name field Format: accounts/{account}/agreements/{agreement}"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "affirmation_time",
            "agreement_id",
            "agreement_name",
            "agreement_source",
            "agreement_state",
            "agreement_uri",
            "agreement_version",
            "enrollment_id",
            "legal_entity_id",
            "legal_natural_person_id",
            "name",
        ]
        nullable_fields = ["affirmation_time"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
