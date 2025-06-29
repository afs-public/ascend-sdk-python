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


class LotPriceTypedDict(TypedDict):
    r"""Price of the trade lot"""

    value: NotRequired[str]
    r"""The decimal value, as a string; Refer to [Google’s Decimal type protocol buffer](https://github.com/googleapis/googleapis/blob/40203ca1880849480bbff7b8715491060bbccdf1/google/type/decimal.proto#L33) for details"""


class LotPrice(BaseModel):
    r"""Price of the trade lot"""

    value: Optional[str] = None
    r"""The decimal value, as a string; Refer to [Google’s Decimal type protocol buffer](https://github.com/googleapis/googleapis/blob/40203ca1880849480bbff7b8715491060bbccdf1/google/type/decimal.proto#L33) for details"""


class LotMoneyTypedDict(TypedDict):
    r"""Object containing currency/ price information for the trade lot"""

    currency_code: NotRequired[str]
    r"""Currency code of the price"""
    price: NotRequired[Nullable[LotPriceTypedDict]]
    r"""Price of the trade lot"""


class LotMoney(BaseModel):
    r"""Object containing currency/ price information for the trade lot"""

    currency_code: Optional[str] = None
    r"""Currency code of the price"""

    price: OptionalNullable[LotPrice] = UNSET
    r"""Price of the trade lot"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["currency_code", "price"]
        nullable_fields = ["price"]
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


class LotQuantityTypedDict(TypedDict):
    r"""Quantity of the trade lot"""

    value: NotRequired[str]
    r"""The decimal value, as a string; Refer to [Google’s Decimal type protocol buffer](https://github.com/googleapis/googleapis/blob/40203ca1880849480bbff7b8715491060bbccdf1/google/type/decimal.proto#L33) for details"""


class LotQuantity(BaseModel):
    r"""Quantity of the trade lot"""

    value: Optional[str] = None
    r"""The decimal value, as a string; Refer to [Google’s Decimal type protocol buffer](https://github.com/googleapis/googleapis/blob/40203ca1880849480bbff7b8715491060bbccdf1/google/type/decimal.proto#L33) for details"""


class LotTradeDateTypedDict(TypedDict):
    r"""Trade date of the trade lot"""

    day: NotRequired[int]
    r"""Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant."""
    month: NotRequired[int]
    r"""Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day."""
    year: NotRequired[int]
    r"""Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year."""


class LotTradeDate(BaseModel):
    r"""Trade date of the trade lot"""

    day: Optional[int] = None
    r"""Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant."""

    month: Optional[int] = None
    r"""Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day."""

    year: Optional[int] = None
    r"""Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year."""


class LotTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Client supplied id"""
    money: NotRequired[Nullable[LotMoneyTypedDict]]
    r"""Object containing currency/ price information for the trade lot"""
    quantity: NotRequired[Nullable[LotQuantityTypedDict]]
    r"""Quantity of the trade lot"""
    trade_date: NotRequired[Nullable[LotTradeDateTypedDict]]
    r"""Trade date of the trade lot"""


class Lot(BaseModel):
    id: Optional[str] = None
    r"""Client supplied id"""

    money: OptionalNullable[LotMoney] = UNSET
    r"""Object containing currency/ price information for the trade lot"""

    quantity: OptionalNullable[LotQuantity] = UNSET
    r"""Quantity of the trade lot"""

    trade_date: OptionalNullable[LotTradeDate] = UNSET
    r"""Trade date of the trade lot"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "money", "quantity", "trade_date"]
        nullable_fields = ["money", "quantity", "trade_date"]
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
