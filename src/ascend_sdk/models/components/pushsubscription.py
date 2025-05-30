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
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class HTTPCallbackTypedDict(TypedDict):
    r"""The information about an HTTP target callback"""

    timeout_seconds: NotRequired[int]
    r"""The maximum amount of time, in seconds, the service will wait for an acknowledgement of a delivery. If a value of 0 or no value is specified, the timeout will default to 10 seconds."""
    url: NotRequired[str]
    r"""The URL address of the client HTTP server that will receive the events via POST; URLs must be in the form of https://{domain}[/{path}]"""


class HTTPCallback(BaseModel):
    r"""The information about an HTTP target callback"""

    timeout_seconds: Optional[int] = None
    r"""The maximum amount of time, in seconds, the service will wait for an acknowledgement of a delivery. If a value of 0 or no value is specified, the timeout will default to 10 seconds."""

    url: Optional[str] = None
    r"""The URL address of the client HTTP server that will receive the events via POST; URLs must be in the form of https://{domain}[/{path}]"""


class State(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The current status of the subscription"""

    PUSH_SUBSCRIPTION_STATE_UNSPECIFIED = "PUSH_SUBSCRIPTION_STATE_UNSPECIFIED"
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"


class PushSubscriptionTypedDict(TypedDict):
    r"""Configuration information about a push subscription"""

    client_id: NotRequired[str]
    r"""The client that owns the subscription. A client subscription will receive events for it and all of its correspondents. This can only be set at creation time and is mutually exclusive with correspondent_id."""
    correspondent_id: NotRequired[str]
    r"""The correspondent that owns the subscription. A correspondent subscription will receive events only for itself. This can only be set at creation time and is mutually exclusive with client_id."""
    display_name: NotRequired[str]
    r"""The user-defined name for the subscription"""
    event_types: NotRequired[List[str]]
    r"""Filter for event types; [\"\*\"] matches all values; Suffix wildcards using \"\*\" (e.g. [\"account.\*\"]) are supported"""
    http_callback: NotRequired[Nullable[HTTPCallbackTypedDict]]
    r"""The information about an HTTP target callback"""
    name: NotRequired[str]
    r"""The resource name of the subscription; Format: subscriptions/{subscription}"""
    state: NotRequired[State]
    r"""The current status of the subscription"""
    subscription_id: NotRequired[str]
    r"""The unique identifier for the subscription"""


class PushSubscription(BaseModel):
    r"""Configuration information about a push subscription"""

    client_id: Optional[str] = None
    r"""The client that owns the subscription. A client subscription will receive events for it and all of its correspondents. This can only be set at creation time and is mutually exclusive with correspondent_id."""

    correspondent_id: Optional[str] = None
    r"""The correspondent that owns the subscription. A correspondent subscription will receive events only for itself. This can only be set at creation time and is mutually exclusive with client_id."""

    display_name: Optional[str] = None
    r"""The user-defined name for the subscription"""

    event_types: Optional[List[str]] = None
    r"""Filter for event types; [\"\*\"] matches all values; Suffix wildcards using \"\*\" (e.g. [\"account.\*\"]) are supported"""

    http_callback: OptionalNullable[HTTPCallback] = UNSET
    r"""The information about an HTTP target callback"""

    name: Optional[str] = None
    r"""The resource name of the subscription; Format: subscriptions/{subscription}"""

    state: Annotated[Optional[State], PlainValidator(validate_open_enum(False))] = None
    r"""The current status of the subscription"""

    subscription_id: Optional[str] = None
    r"""The unique identifier for the subscription"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "client_id",
            "correspondent_id",
            "display_name",
            "event_types",
            "http_callback",
            "name",
            "state",
            "subscription_id",
        ]
        nullable_fields = ["http_callback"]
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
