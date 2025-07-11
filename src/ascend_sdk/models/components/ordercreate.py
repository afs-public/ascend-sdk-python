"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .commissioncreate import CommissionCreate, CommissionCreateTypedDict
from .datecreate import DateCreate, DateCreateTypedDict
from .decimalcreate import DecimalCreate, DecimalCreateTypedDict
from .feecreate import FeeCreate, FeeCreateTypedDict
from .letterofintentcreate import LetterOfIntentCreate, LetterOfIntentCreateTypedDict
from .limitpricecreate import LimitPriceCreate, LimitPriceCreateTypedDict
from .rightsofaccumulationcreate import (
    RightsOfAccumulationCreate,
    RightsOfAccumulationCreateTypedDict,
)
from .stoppricecreate import StopPriceCreate, StopPriceCreateTypedDict
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
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssetType(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The type of the asset in this order, which must be one of the following:
    EQUITY, MUTUAL_FUND, and FIXED_INCOME.
    """

    EQUITY = "EQUITY"
    FIXED_INCOME = "FIXED_INCOME"
    MUTUAL_FUND = "MUTUAL_FUND"


class BrokerCapacity(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Defaults to \"AGENCY\" if not specified. For Equities: Only \"AGENCY\" is allowed. For Mutual Funds: Only \"AGENCY\" is allowed. For Fixed Income: Either \"AGENCY\" or \"PRINCIPAL\" are allowed."""

    BROKER_CAPACITY_UNSPECIFIED = "BROKER_CAPACITY_UNSPECIFIED"
    AGENCY = "AGENCY"
    PRINCIPAL = "PRINCIPAL"


class IdentifierType(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The identifier type of the asset being ordered. For Equities: only SYMBOL is supported For Mutual Funds: only SYMBOL and CUSIP are supported For Fixed Income: only CUSIP and ISIN are supported"""

    SYMBOL = "SYMBOL"
    CUSIP = "CUSIP"
    ISIN = "ISIN"


class OrderType(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The execution type of this order. For Equities: MARKET, LIMIT, or STOP are supported. For Mutual Funds: only MARKET is supported. For Fixed Income: only LIMIT is supported."""

    ORDER_TYPE_UNSPECIFIED = "ORDER_TYPE_UNSPECIFIED"
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    STOP = "STOP"


class Side(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The side of this order."""

    SIDE_UNSPECIFIED = "SIDE_UNSPECIFIED"
    BUY = "BUY"
    SELL = "SELL"


class SpecialReportingInstructions(str, Enum, metaclass=utils.OpenEnumMeta):
    SPECIAL_REPORTING_INSTRUCTIONS_UNSPECIFIED = (
        "SPECIAL_REPORTING_INSTRUCTIONS_UNSPECIFIED"
    )
    CUSTOMER_DIRECTED = "CUSTOMER_DIRECTED"
    WITH_DIVIDEND = "WITH_DIVIDEND"
    WITH_RIGHTS = "WITH_RIGHTS"
    DISCRETION_EXERCISED = "DISCRETION_EXERCISED"
    DISCRETION_NOT_EXERCISED = "DISCRETION_NOT_EXERCISED"
    BROKER_DEALER_ORDER = "BROKER_DEALER_ORDER"
    FULLY_REGISTERED = "FULLY_REGISTERED"
    ODDLOT_DIFF_ON_REQUEST = "ODDLOT_DIFF_ON_REQUEST"
    PROSPECTUS_ENCLOSED = "PROSPECTUS_ENCLOSED"
    PROSPECTUS_SEPARATE_MAIL = "PROSPECTUS_SEPARATE_MAIL"
    SOLICITED = "SOLICITED"
    UNSOLICITED = "UNSOLICITED"
    X_DIVIDEND = "X_DIVIDEND"
    ACTING_AS_PRINCIPAL = "ACTING_AS_PRINCIPAL"
    AVERAGE_PRICE = "AVERAGE_PRICE"
    BROKER_LIQUIDATION = "BROKER_LIQUIDATION"
    INTERNET_ORDER = "INTERNET_ORDER"
    MARGIN_SELLOUT = "MARGIN_SELLOUT"
    NEGATIVE_NET_PROCEED = "NEGATIVE_NET_PROCEED"
    RISKLESS_PRINCIPAL = "RISKLESS_PRINCIPAL"
    THIRD_MARKET = "THIRD_MARKET"
    SUPPRESS_TRACE_REPORTING = "SUPPRESS_TRACE_REPORTING"
    WHEN_DISTRIBUTED = "WHEN_DISTRIBUTED"


class TimeInForce(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Must be the value \"DAY\". Regulatory requirements dictate that the system capture the intended time_in_force, which is why this a mandatory field."""

    TIME_IN_FORCE_UNSPECIFIED = "TIME_IN_FORCE_UNSPECIFIED"
    DAY = "DAY"


class TradingStrategy(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Which TradingStrategy Session to trade in, defaults to 'CORE'. Only available for Equity orders."""

    CORE = "CORE"


class OrderCreateTypedDict(TypedDict):
    r"""The message describing an order"""

    asset_type: AssetType
    r"""The type of the asset in this order, which must be one of the following:
    EQUITY, MUTUAL_FUND, and FIXED_INCOME.
    """
    client_order_id: str
    r"""User-supplied unique order ID. Cannot be more than 40 characters long."""
    identifier: str
    r"""Identifier of the asset (of the type specified in `identifier_type`)."""
    identifier_type: IdentifierType
    r"""The identifier type of the asset being ordered. For Equities: only SYMBOL is supported For Mutual Funds: only SYMBOL and CUSIP are supported For Fixed Income: only CUSIP and ISIN are supported"""
    order_date: DateCreateTypedDict
    r"""Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

    * A full date, with non-zero year, month, and day values * A month and day value, with a zero year, such as an anniversary * A year on its own, with zero month and day values * A year and month value, with a zero day, such as a credit card expiration date

    Related types are [google.type.TimeOfDay][google.type.TimeOfDay] and `google.protobuf.Timestamp`.
    """
    order_type: OrderType
    r"""The execution type of this order. For Equities: MARKET, LIMIT, or STOP are supported. For Mutual Funds: only MARKET is supported. For Fixed Income: only LIMIT is supported."""
    side: Side
    r"""The side of this order."""
    time_in_force: TimeInForce
    r"""Must be the value \"DAY\". Regulatory requirements dictate that the system capture the intended time_in_force, which is why this a mandatory field."""
    broker_capacity: NotRequired[BrokerCapacity]
    r"""Defaults to \"AGENCY\" if not specified. For Equities: Only \"AGENCY\" is allowed. For Mutual Funds: Only \"AGENCY\" is allowed. For Fixed Income: Either \"AGENCY\" or \"PRINCIPAL\" are allowed."""
    client_received_time: NotRequired[Nullable[datetime]]
    r"""Required for Equity Orders for any client who is having Apex do CAT reporting on their behalf. A value may be provided for non-Equity orders, and will be remembered, but valid timestamps will have no impact on how they are processed."""
    commission: NotRequired[CommissionCreateTypedDict]
    r"""A custom commission applied to an order"""
    currency_code: NotRequired[str]
    r"""Defaults to \"USD\". Only \"USD\" is supported. Full list of currency codes is defined at: https://en.wikipedia.org/wiki/ISO_4217"""
    fees: NotRequired[List[FeeCreateTypedDict]]
    r"""Fees that will be applied to this order. Only the BROKER_FEE type is supported."""
    identifier_issuing_region_code: NotRequired[str]
    r"""A string attribute denoting the country of issuance or where the asset is trading. Only available for Mutual Fund orders. Defaults to US, when trading non US mutual funds this field must be provided Complies with ISO-3166 Alpha-2 Codes"""
    letter_of_intent: NotRequired[LetterOfIntentCreateTypedDict]
    r"""Letter of Intent (LOI). An LOI allows investors to receive sales charge discounts based on a commitment to buy a specified monetary amount of shares over a period of time, usually 13 months."""
    limit_price: NotRequired[LimitPriceCreateTypedDict]
    r"""A limit price definition"""
    max_sell_quantity: NotRequired[DecimalCreateTypedDict]
    r"""A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal][].

    [BigDecimal]:
    https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html
    [decimal.Decimal]: https://docs.python.org/3/library/decimal.html
    """
    notional_value: NotRequired[DecimalCreateTypedDict]
    r"""A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal][].

    [BigDecimal]:
    https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html
    [decimal.Decimal]: https://docs.python.org/3/library/decimal.html
    """
    quantity: NotRequired[DecimalCreateTypedDict]
    r"""A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal][].

    [BigDecimal]:
    https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html
    [decimal.Decimal]: https://docs.python.org/3/library/decimal.html
    """
    rights_of_accumulation: NotRequired[RightsOfAccumulationCreateTypedDict]
    r"""Rights of Accumulation (ROA). An ROA allows an investor to aggregate their own fund shares with the holdings of certain related parties toward achieving the investment thresholds at which sales charge discounts become available."""
    special_reporting_instructions: NotRequired[List[SpecialReportingInstructions]]
    r"""Special Reporting Instructions to be applied to this order. Can include multiple Instructions."""
    stop_price: NotRequired[StopPriceCreateTypedDict]
    r"""A stop price definition"""
    trading_strategy: NotRequired[TradingStrategy]
    r"""Which TradingStrategy Session to trade in, defaults to 'CORE'. Only available for Equity orders."""


class OrderCreate(BaseModel):
    r"""The message describing an order"""

    asset_type: Annotated[AssetType, PlainValidator(validate_open_enum(False))]
    r"""The type of the asset in this order, which must be one of the following:
    EQUITY, MUTUAL_FUND, and FIXED_INCOME.
    """

    client_order_id: str
    r"""User-supplied unique order ID. Cannot be more than 40 characters long."""

    identifier: str
    r"""Identifier of the asset (of the type specified in `identifier_type`)."""

    identifier_type: Annotated[
        IdentifierType, PlainValidator(validate_open_enum(False))
    ]
    r"""The identifier type of the asset being ordered. For Equities: only SYMBOL is supported For Mutual Funds: only SYMBOL and CUSIP are supported For Fixed Income: only CUSIP and ISIN are supported"""

    order_date: DateCreate
    r"""Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

    * A full date, with non-zero year, month, and day values * A month and day value, with a zero year, such as an anniversary * A year on its own, with zero month and day values * A year and month value, with a zero day, such as a credit card expiration date

    Related types are [google.type.TimeOfDay][google.type.TimeOfDay] and `google.protobuf.Timestamp`.
    """

    order_type: Annotated[OrderType, PlainValidator(validate_open_enum(False))]
    r"""The execution type of this order. For Equities: MARKET, LIMIT, or STOP are supported. For Mutual Funds: only MARKET is supported. For Fixed Income: only LIMIT is supported."""

    side: Annotated[Side, PlainValidator(validate_open_enum(False))]
    r"""The side of this order."""

    time_in_force: Annotated[TimeInForce, PlainValidator(validate_open_enum(False))]
    r"""Must be the value \"DAY\". Regulatory requirements dictate that the system capture the intended time_in_force, which is why this a mandatory field."""

    broker_capacity: Annotated[
        Optional[BrokerCapacity], PlainValidator(validate_open_enum(False))
    ] = None
    r"""Defaults to \"AGENCY\" if not specified. For Equities: Only \"AGENCY\" is allowed. For Mutual Funds: Only \"AGENCY\" is allowed. For Fixed Income: Either \"AGENCY\" or \"PRINCIPAL\" are allowed."""

    client_received_time: OptionalNullable[datetime] = UNSET
    r"""Required for Equity Orders for any client who is having Apex do CAT reporting on their behalf. A value may be provided for non-Equity orders, and will be remembered, but valid timestamps will have no impact on how they are processed."""

    commission: Optional[CommissionCreate] = None
    r"""A custom commission applied to an order"""

    currency_code: Optional[str] = None
    r"""Defaults to \"USD\". Only \"USD\" is supported. Full list of currency codes is defined at: https://en.wikipedia.org/wiki/ISO_4217"""

    fees: Optional[List[FeeCreate]] = None
    r"""Fees that will be applied to this order. Only the BROKER_FEE type is supported."""

    identifier_issuing_region_code: Optional[str] = None
    r"""A string attribute denoting the country of issuance or where the asset is trading. Only available for Mutual Fund orders. Defaults to US, when trading non US mutual funds this field must be provided Complies with ISO-3166 Alpha-2 Codes"""

    letter_of_intent: Optional[LetterOfIntentCreate] = None
    r"""Letter of Intent (LOI). An LOI allows investors to receive sales charge discounts based on a commitment to buy a specified monetary amount of shares over a period of time, usually 13 months."""

    limit_price: Optional[LimitPriceCreate] = None
    r"""A limit price definition"""

    max_sell_quantity: Optional[DecimalCreate] = None
    r"""A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal][].

    [BigDecimal]:
    https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html
    [decimal.Decimal]: https://docs.python.org/3/library/decimal.html
    """

    notional_value: Optional[DecimalCreate] = None
    r"""A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal][].

    [BigDecimal]:
    https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html
    [decimal.Decimal]: https://docs.python.org/3/library/decimal.html
    """

    quantity: Optional[DecimalCreate] = None
    r"""A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal][].

    [BigDecimal]:
    https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html
    [decimal.Decimal]: https://docs.python.org/3/library/decimal.html
    """

    rights_of_accumulation: Optional[RightsOfAccumulationCreate] = None
    r"""Rights of Accumulation (ROA). An ROA allows an investor to aggregate their own fund shares with the holdings of certain related parties toward achieving the investment thresholds at which sales charge discounts become available."""

    special_reporting_instructions: Optional[
        List[
            Annotated[
                SpecialReportingInstructions, PlainValidator(validate_open_enum(False))
            ]
        ]
    ] = None
    r"""Special Reporting Instructions to be applied to this order. Can include multiple Instructions."""

    stop_price: Optional[StopPriceCreate] = None
    r"""A stop price definition"""

    trading_strategy: Annotated[
        Optional[TradingStrategy], PlainValidator(validate_open_enum(False))
    ] = None
    r"""Which TradingStrategy Session to trade in, defaults to 'CORE'. Only available for Equity orders."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "broker_capacity",
            "client_received_time",
            "commission",
            "currency_code",
            "fees",
            "identifier_issuing_region_code",
            "letter_of_intent",
            "limit_price",
            "max_sell_quantity",
            "notional_value",
            "quantity",
            "rights_of_accumulation",
            "special_reporting_instructions",
            "stop_price",
            "trading_strategy",
        ]
        nullable_fields = ["client_received_time"]
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
