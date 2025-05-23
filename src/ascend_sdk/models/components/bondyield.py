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
from enum import Enum
from pydantic import model_serializer
from pydantic.functional_validators import PlainValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PercentTypedDict(TypedDict):
    r"""The percentage yield."""

    value: NotRequired[str]
    r"""The decimal value, as a string; Refer to [Google’s Decimal type protocol buffer](https://github.com/googleapis/googleapis/blob/40203ca1880849480bbff7b8715491060bbccdf1/google/type/decimal.proto#L33) for details"""


class Percent(BaseModel):
    r"""The percentage yield."""

    value: Optional[str] = None
    r"""The decimal value, as a string; Refer to [Google’s Decimal type protocol buffer](https://github.com/googleapis/googleapis/blob/40203ca1880849480bbff7b8715491060bbccdf1/google/type/decimal.proto#L33) for details"""


class BondYieldYieldType(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The type of yield."""

    YIELD_TYPE_UNSPECIFIED = "YIELD_TYPE_UNSPECIFIED"
    YIELD_TO_CALL = "YIELD_TO_CALL"
    YIELD_TO_MATURITY = "YIELD_TO_MATURITY"
    YIELD_TO_PUT = "YIELD_TO_PUT"
    YIELD_TO_WORST = "YIELD_TO_WORST"


class BondYieldTypedDict(TypedDict):
    r"""A percentage yield"""

    percent: NotRequired[Nullable[PercentTypedDict]]
    r"""The percentage yield."""
    yield_type: NotRequired[BondYieldYieldType]
    r"""The type of yield."""


class BondYield(BaseModel):
    r"""A percentage yield"""

    percent: OptionalNullable[Percent] = UNSET
    r"""The percentage yield."""

    yield_type: Annotated[
        Optional[BondYieldYieldType], PlainValidator(validate_open_enum(False))
    ] = None
    r"""The type of yield."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["percent", "yield_type"]
        nullable_fields = ["percent"]
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
