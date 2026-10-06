import time
from ascend_sdk.models import components
from ascend_sdk.models import errors

from tests.conftest import retry_on_transient_error
from tests.events.conftest import find_subscription_delivery


def test_subscriber_events_create_push_subscription_create_push_subscription1(
    subscriber_id,
):
    assert subscriber_id is not None


def test_subscriber_events_get_push_subscription_get_push_subscription1(
    create_sdk, subscriber_id
):
    s = create_sdk

    assert s is not None

    res = s.subscriber.get_push_subscription(subscription_id=subscriber_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_subscriber_events_update_push_subscription_update_push_subscription1(
    create_sdk, subscriber_id
):
    s = create_sdk

    assert s is not None

    # Update Push Subscription
    request = components.PushSubscriptionUpdate(
        event_types=["position.v2.updated"],
    )

    res = retry_on_transient_error(
        lambda: s.subscriber.update_push_subscription(
            subscription_id=subscriber_id, push_subscription_update=request
        )
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_subscriber_events_list_subscription_event_deliveries_list_subscription_event_deliveries1(
    delivery_id,
):
    assert delivery_id is not None


def test_subscriber_events_get_subscription_event_delivery_get_subscription_event_delivery1(
    create_sdk,
):
    s = create_sdk

    assert s is not None

    # Re-pick the subscription/delivery pair on each attempt: a concurrently
    # running suite can delete the picked subscription between the pick and
    # the read.
    def get_delivery():
        pair = find_subscription_delivery(s)
        if pair is None:
            raise LookupError("no subscription with deliveries found")
        subscription_id, delivery_id = pair
        return s.subscriber.get_push_subscription_delivery(
            subscription_id=subscription_id, delivery_id=delivery_id
        )

    res = retry_on_transient_error(get_delivery, max_attempts=5)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_subscriber_events_delete_push_subscription_delete_push_subscription1(
    create_sdk, subscriber_id
):
    s = create_sdk

    assert s is not None

    # Deletes are not idempotent: if an earlier attempt succeeded server-side
    # but its response was lost, retries see NOT_FOUND. Treat that as success
    # instead of retrying a completed delete into a guaranteed failure.
    def delete_subscription():
        try:
            return s.subscriber.delete_push_subscription(
                subscription_id=subscriber_id
            )
        except errors.Status as status:
            if status.data.code == 5:
                return None
            raise

    res = retry_on_transient_error(delete_subscription)
    if res is not None:
        assert res.http_meta is not None
        assert res.http_meta.response is not None
        assert res.http_meta.response.status_code == 200
