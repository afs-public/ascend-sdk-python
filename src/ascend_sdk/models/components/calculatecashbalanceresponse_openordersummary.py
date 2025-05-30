"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ExpectedNotionalCeilingAmountTypedDict(TypedDict):
    r"""The notional value the order is not reasonably expected to exceed in USD. This value is always positive."""

    value: NotRequired[str]
    r"""The decimal value, as a string; Refer to [Google’s Decimal type protocol buffer](https://github.com/googleapis/googleapis/blob/40203ca1880849480bbff7b8715491060bbccdf1/google/type/decimal.proto#L33) for details"""


class ExpectedNotionalCeilingAmount(BaseModel):
    r"""The notional value the order is not reasonably expected to exceed in USD. This value is always positive."""

    value: Optional[str] = None
    r"""The decimal value, as a string; Refer to [Google’s Decimal type protocol buffer](https://github.com/googleapis/googleapis/blob/40203ca1880849480bbff7b8715491060bbccdf1/google/type/decimal.proto#L33) for details"""


class CalculateCashBalanceResponseOpenOrderSummaryTypedDict(TypedDict):
    r"""A summary of an open order."""

    asset: NotRequired[str]
    r"""The asset for the open order."""
    expected_notional_ceiling_amount: NotRequired[
        Nullable[ExpectedNotionalCeilingAmountTypedDict]
    ]
    r"""The notional value the order is not reasonably expected to exceed in USD. This value is always positive."""


class CalculateCashBalanceResponseOpenOrderSummary(BaseModel):
    r"""A summary of an open order."""

    asset: Optional[str] = None
    r"""The asset for the open order."""

    expected_notional_ceiling_amount: OptionalNullable[
        ExpectedNotionalCeilingAmount
    ] = UNSET
    r"""The notional value the order is not reasonably expected to exceed in USD. This value is always positive."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["asset", "expected_notional_ceiling_amount"]
        nullable_fields = ["expected_notional_ceiling_amount"]
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
