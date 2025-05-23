"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .decimalcreate import DecimalCreate, DecimalCreateTypedDict
from ascend_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RetirementDistributionTaxWithholdingCreateTypedDict(TypedDict):
    r"""A representation of a tax withholding."""

    amount: NotRequired[DecimalCreateTypedDict]
    r"""A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal][].

    [BigDecimal]:
    https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html
    [decimal.Decimal]: https://docs.python.org/3/library/decimal.html
    """
    percentage: NotRequired[DecimalCreateTypedDict]
    r"""A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal][].

    [BigDecimal]:
    https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html
    [decimal.Decimal]: https://docs.python.org/3/library/decimal.html
    """


class RetirementDistributionTaxWithholdingCreate(BaseModel):
    r"""A representation of a tax withholding."""

    amount: Optional[DecimalCreate] = None
    r"""A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal][].

    [BigDecimal]:
    https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html
    [decimal.Decimal]: https://docs.python.org/3/library/decimal.html
    """

    percentage: Optional[DecimalCreate] = None
    r"""A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal][].

    [BigDecimal]:
    https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html
    [decimal.Decimal]: https://docs.python.org/3/library/decimal.html
    """
