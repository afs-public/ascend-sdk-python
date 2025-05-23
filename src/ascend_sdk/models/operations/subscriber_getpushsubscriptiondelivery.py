"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ascend_sdk.models.components import (
    httpmetadata as components_httpmetadata,
    pushsubscriptiondelivery as components_pushsubscriptiondelivery,
    status as components_status,
)
from ascend_sdk.types import BaseModel
from ascend_sdk.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SubscriberGetPushSubscriptionDeliveryRequestTypedDict(TypedDict):
    subscription_id: str
    r"""The subscription id."""
    delivery_id: str
    r"""The delivery id."""


class SubscriberGetPushSubscriptionDeliveryRequest(BaseModel):
    subscription_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The subscription id."""

    delivery_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The delivery id."""


class SubscriberGetPushSubscriptionDeliveryResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    push_subscription_delivery: NotRequired[
        components_pushsubscriptiondelivery.PushSubscriptionDeliveryTypedDict
    ]
    r"""OK"""
    status: NotRequired[components_status.StatusTypedDict]
    r"""INVALID_ARGUMENT: The request was not well formed."""


class SubscriberGetPushSubscriptionDeliveryResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    push_subscription_delivery: Optional[
        components_pushsubscriptiondelivery.PushSubscriptionDelivery
    ] = None
    r"""OK"""

    status: Optional[components_status.Status] = None
    r"""INVALID_ARGUMENT: The request was not well formed."""
