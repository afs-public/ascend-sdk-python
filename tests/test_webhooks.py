import json
import hmac
import hashlib
from datetime import datetime, timedelta
from types import SimpleNamespace
import pytest
from ascend_sdk.webhook import validate_event_payload

# Constants used in testing
TEST_SECRET = "my-super-secret-webhook-key"
TEST_ALLOWED_AGE = timedelta(minutes=5)
TEST_MESSAGE_ID = "msg_2WpGqg8fH9jZ7kY6aB3dX2eF1c"
TEST_EVENT_TYPE = "transaction.created"
TEST_ACCOUNT_ID = "acc_1a2b3c4d5e6f7g8h9i"
TEST_CLIENT_ID = "cli_j0k1l2m3n4p5q6r7s8"
TEST_PARTITION_KEY = "user_xyz"


def create_test_body(publish_time: datetime) -> str:
    """
    Mimics the EventMessage structure as a test body.
    """
    event_payload = {
        "message_id": TEST_MESSAGE_ID,
        "event_type": TEST_EVENT_TYPE,
        "account_id": TEST_ACCOUNT_ID,
        "client_id": TEST_CLIENT_ID,
        "name": f"messages/{TEST_MESSAGE_ID}",
        "partition_key": TEST_PARTITION_KEY,
        "publish_time": publish_time.isoformat(),
        "data": {
            "transactionId": "txn_abcdef123456",
            "amount": 100.50,
            "currency": "USD",
            "status": "completed",
        },
    }
    return json.dumps(event_payload)


def generate_signature(send_time_str: str, body: str, secret: str) -> str:
    """
    Generates a signature for test validation.
    """
    payload = f"{body}.{send_time_str}"
    mac = hmac.new(secret.encode(), payload.encode(), hashlib.sha256)
    return mac.hexdigest()


def validate_success_message(event_message, valid_send_time):
    """Validates a successful webhook payload."""
    assert event_message is not None, "Expected EventMessage to be non-nil"
    assert event_message.message_id == TEST_MESSAGE_ID
    assert event_message.event_type == TEST_EVENT_TYPE
    assert event_message.account_id == TEST_ACCOUNT_ID
    assert event_message.client_id == TEST_CLIENT_ID
    assert event_message.name == f"messages/{TEST_MESSAGE_ID}"
    assert event_message.publish_time.isoformat() == valid_send_time.isoformat()
    assert event_message.data["status"] == "completed"


class MockRequest:
    """Mocks an HTTP request object."""

    def __init__(self, body, headers):
        self.body = body
        self.headers = headers

    def get_data(self, as_text=False):
        return self.body if as_text else self.body.encode()

    def __getitem__(self, key):
        return self.headers.get(key)


@pytest.mark.parametrize(
    "name, send_time, body, signature, headers, expect_error, error_contains, validate_message",
    [
        # Success test case
        (
            "Success - Valid Payload",
            datetime.utcnow().replace(microsecond=0),
            lambda send_time: create_test_body(send_time),
            None,
            {},
            False,
            None,
            validate_success_message,
        ),
        # Invalid signature
        (
            "Error - Invalid Signature",
            datetime.utcnow().replace(microsecond=0),
            lambda send_time: create_test_body(send_time),
            "invalid-signature",
            {},
            True,
            "Provided signature does not match calculated signature",
            None,
        ),
        # Expired event
        (
            "Error - Expired Event",
            datetime.utcnow() - (TEST_ALLOWED_AGE + timedelta(minutes=1)),
            lambda send_time: create_test_body(send_time),
            None,
            {},
            True,
            "Event age is out of range, it must be sent within the allowed event age",
            None,
        ),
        # Missing signature header
        (
            "Error - Missing Signature Header",
            datetime.utcnow(),
            lambda send_time: create_test_body(send_time),
            None,
            {"x-apex-event-signature": ""},
            True,
            "Missing required headers: x-apex-event-signature and/or x-apex-event-send-time",
            None,
        ),
        # Missing `x-apex-event-send-time` header
        (
            "Error - Missing Send Time Header",
            datetime.utcnow(),
            lambda send_time: create_test_body(send_time),
            None,
            {"x-apex-event-send-time": ""},
            True,
            "Missing required headers: x-apex-event-signature and/or x-apex-event-send-time",
            None,
        ),
        # Invalid send time format
        (
            "Error - Invalid Send Time Format",
            datetime.utcnow(),
            lambda send_time: create_test_body(send_time),
            None,
            {"x-apex-event-send-time": "not-a-valid-time"},
            True,
            "Invalid send time format",
            None,
        ),
        # Invalid JSON body
        (
            "Error - Invalid JSON Body",
            datetime.utcnow(),
            lambda send_time: '{"id":"evt_123", "type": "user.created" "data":{}}',
            None,
            {},
            True,
            "Failed to unmarshal event message",
            None,
        ),
    ],
)
def test_event_payload_validation(
    name,
    send_time,
    body,
    signature,
    headers,
    expect_error,
    error_contains,
    validate_message,
):
    """Runs tests for the webhook validation."""
    send_time_str = send_time.isoformat()

    # Generate body and signature if needed
    if callable(body):
        body = body(send_time)
    if signature is None:
        signature = generate_signature(send_time_str, body, TEST_SECRET)

    # Prepare headers
    request_headers = {
        "x-apex-event-signature": signature,
        "x-apex-event-send-time": send_time_str,
    }

    for key, val in headers.items():
        if val == "":
            request_headers.pop(key, None)
        else:
            request_headers[key] = val

    mock_request = MockRequest(body, request_headers)

    # Run the validation and assert results
    if expect_error:
        with pytest.raises(ValueError) as excinfo:
            validate_event_payload(mock_request, TEST_SECRET, TEST_ALLOWED_AGE)
        assert error_contains in str(excinfo.value)
    else:
        event_message = validate_event_payload(
            mock_request, TEST_SECRET, TEST_ALLOWED_AGE
        )
        assert event_message is not None
        if validate_message:
            validate_message(event_message, send_time)


def test_integration_get_event_message_and_validate(create_sdk):
    s = create_sdk
    assert s is not None

    res = s.reader.list_event_messages()
    assert res.http_meta is not None
    assert res.http_meta.response is not None
    assert res.http_meta.response.status_code == 200

    assert res.list_event_messages_response is not None
    assert res.list_event_messages_response.event_messages is not None
    assert len(res.list_event_messages_response.event_messages) > 0

    event_message = res.list_event_messages_response.event_messages[0]
    assert event_message is not None

    assert event_message.message_id is not None
    event_message_id = event_message.message_id

    event = s.reader.get_event_message(message_id=event_message_id)
    assert event.http_meta is not None
    assert event.http_meta.response is not None
    assert event.http_meta.response.status_code == 200

    assert event.event_message is not None

    simulated_body = json.dumps(event.event_message.dict(), indent=2, default=str)
    print(f"Simulated body: {simulated_body}")

    secret_key = "super-secret-key"
    send_time = datetime.utcnow()
    send_time_str = send_time.isoformat()

    signature = generate_signature(send_time_str, simulated_body, secret_key)

    simulated_request = SimpleNamespace(
        headers={
            "x-apex-event-signature": signature,
            "x-apex-event-send-time": send_time_str,
            "Content-Type": "application/json",
        },
        get_data=lambda as_text=False: simulated_body
        if as_text
        else simulated_body.encode(),
    )

    validated_event = validate_event_payload(
        simulated_request, secret_key, TEST_ALLOWED_AGE
    )
    assert validated_event is not None
