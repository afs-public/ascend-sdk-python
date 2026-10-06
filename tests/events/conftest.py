import os

from ascend_sdk.models import components
from ascend_sdk.models import errors
from datetime import datetime

import pytest

from tests.conftest import retry_on_transient_error


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


def find_subscription_delivery(s):
    """Atomically picks a subscription that has deliveries with its first
    delivery id. Callers that read a delivery should re-pick through this on
    failure: a concurrently running suite can delete the picked subscription
    between the pick and the read."""
    response = s.subscriber.list_push_subscriptions()
    if response.http_meta.response.status_code != 200:
        return None
    subscriptions = response.list_push_subscriptions_response.push_subscriptions or []
    for subscription in subscriptions:
        try:
            res = s.subscriber.list_push_subscription_deliveries(
                subscription_id=subscription.subscription_id
            )
        except errors.Status:
            continue
        deliveries = (
            res.list_push_subscription_deliveries_response.push_subscription_deliveries
        )
        if res.http_meta.response.status_code == 200 and deliveries:
            return (subscription.subscription_id, deliveries[0].delivery_id)
    return None


@pytest.fixture(scope="module")
def test_subscriber_id(create_sdk):
    s = create_sdk

    response = s.subscriber.list_push_subscriptions()
    if response.http_meta.response.status_code != 200:
        return None
    subscriptions = response.list_push_subscriptions_response.push_subscriptions
    if not subscriptions:
        return None

    # The first listed subscription can be a freshly created one with no
    # delivery history (e.g. from a concurrently running suite's create
    # test); prefer a subscription that already has deliveries. A concurrent
    # suite can also delete its subscription between the list and the
    # per-subscription read, so a NOT_FOUND here just means skip it.
    for subscription in subscriptions:
        try:
            res = s.subscriber.list_push_subscription_deliveries(
                subscription_id=subscription.subscription_id
            )
        except errors.Status:
            continue
        deliveries = (
            res.list_push_subscription_deliveries_response.push_subscription_deliveries
        )
        if res.http_meta.response.status_code == 200 and deliveries:
            return subscription.subscription_id
    return subscriptions[0].subscription_id


@pytest.fixture(scope="module")
def delivery_id(create_sdk, test_subscriber_id):
    s = create_sdk

    # Event deliveries are recorded asynchronously after the subscription's
    # first event fires; poll rather than reading once.
    def first_delivery_id():
        res = s.subscriber.list_push_subscription_deliveries(
            subscription_id=test_subscriber_id
        )
        deliveries = (
            res.list_push_subscription_deliveries_response.push_subscription_deliveries
        )
        if res.http_meta.response.status_code == 200 and deliveries:
            return deliveries[0].delivery_id
        raise LookupError("no deliveries recorded yet")

    try:
        return retry_on_transient_error(first_delivery_id)
    except Exception:
        return None
