import os

from ascend_sdk.models import components
from datetime import datetime

import pytest


@pytest.fixture(scope="module")
def message_id(create_sdk):
    s = create_sdk

    res = s.reader.list_event_messages()

    if (
        res.http_meta.response.status_code == 200
        and res.list_event_messages_response.event_messages is not None
    ):
        return res.list_event_messages_response.event_messages[0].message_id
    else:
        return None


@pytest.fixture(scope="module")
def subscriber_id(create_sdk):
    s = create_sdk

    now = datetime.now()
    request = components.PushSubscriptionCreate(
        correspondent_id=os.getenv("CORRESPONDENT_ID"),
        display_name=now.strftime("%c"),
        event_types=["position.v1.updated"],
        http_callback=components.HTTPPushCallbackCreate(
            client_secret="mysecretkey1",
            timeout_seconds=30,
            url="https://brokercheck.finra.org/",
        ),
    )

    res = s.subscriber.create_push_subscription(request=request)

    if res.http_meta.response.status_code == 200:
        return res.push_subscription.name.split("/")[-1]
    else:
        return None


@pytest.fixture(scope="module")
def test_subscriber_id(create_sdk):
    s = create_sdk

    response = s.subscriber.list_push_subscriptions()
    subscriptions = response.list_push_subscriptions_response.push_subscriptions
    if (
        response.http_meta.response.status_code == 200
        and response.list_push_subscriptions_response.push_subscriptions is not None
    ):
        return subscriptions[0].subscription_id
    else:
        return None


@pytest.fixture(scope="module")
def delivery_id(create_sdk, test_subscriber_id):
    s = create_sdk

    res = s.subscriber.list_push_subscription_deliveries(
        subscription_id=test_subscriber_id
    )

    if (
        res.http_meta.response.status_code == 200
        and res.list_push_subscription_deliveries_response.push_subscription_deliveries
        is not None
    ):
        return (
            res.list_push_subscription_deliveries_response.push_subscription_deliveries[
                0
            ].delivery_id
        )
    else:
        return None
