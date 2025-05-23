"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk import utils
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import validate_open_enum
from enum import Enum
from pydantic.functional_validators import PlainValidator
from typing_extensions import Annotated, TypedDict


class EndReason(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The end reason of the LTID."""

    REPORTABLE_ACCOUNT_EVENT_REASON_UNSPECIFIED = (
        "REPORTABLE_ACCOUNT_EVENT_REASON_UNSPECIFIED"
    )
    EVENT_REASON_CREATED = "EVENT_REASON_CREATED"
    EVENT_REASON_CORRECTION = "EVENT_REASON_CORRECTION"
    EVENT_REASON_ENDED = "EVENT_REASON_ENDED"
    EVENT_REASON_REPLACED = "EVENT_REASON_REPLACED"
    EVENT_REASON_TRANSFER = "EVENT_REASON_TRANSFER"
    EVENT_REASON_OTHER = "EVENT_REASON_OTHER"


class EndLargeTraderRequestCreateTypedDict(TypedDict):
    r"""The request to end a Large Trader on a Legal Natural Person/Legal Entity."""

    end_reason: EndReason
    r"""The end reason of the LTID."""


class EndLargeTraderRequestCreate(BaseModel):
    r"""The request to end a Large Trader on a Legal Natural Person/Legal Entity."""

    end_reason: Annotated[EndReason, PlainValidator(validate_open_enum(False))]
    r"""The end reason of the LTID."""
