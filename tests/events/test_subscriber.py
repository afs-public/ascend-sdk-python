import time
from ascend_sdk.models import components


def test_subscriber_events_create_push_subscription_create_push_subscription1(
    subscriber_id,
):
    assert subscriber_id is not None


def test_subscriber_events_get_push_subscription_get_push_subscription1(
    create_sdk, subscriber_id
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    res = s.subscriber.get_push_subscription(subscription_id=subscriber_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_subscriber_events_update_push_subscription_update_push_subscription1(
    create_sdk, subscriber_id
):
    time.sleep(25)
    s = create_sdk

    assert s is not None

    # Update Push Subscription
    request = components.PushSubscriptionUpdate(
        event_types=["position.v2.updated"],
    )

    res = s.subscriber.update_push_subscription(
        subscription_id=subscriber_id, push_subscription_update=request
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_subscriber_events_list_subscription_event_deliveries_list_subscription_event_deliveries1(
    delivery_id,
):
    assert delivery_id is not None


def test_subscriber_events_get_subscription_event_delivery_get_subscription_event_delivery1(
    create_sdk, test_subscriber_id, delivery_id
):
    s = create_sdk

    assert s is not None

    res = s.subscriber.get_push_subscription_delivery(
        subscription_id=test_subscriber_id, delivery_id=delivery_id
    )
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200


def test_subscriber_events_delete_push_subscription_delete_push_subscription1(
    create_sdk, subscriber_id
):
    time.sleep(5)
    s = create_sdk

    assert s is not None

    res = s.subscriber.delete_push_subscription(subscription_id=subscriber_id)
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200
