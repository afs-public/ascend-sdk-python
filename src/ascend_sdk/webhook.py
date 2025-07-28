"""Code manually maintained by the SDK team."""

import hmac
import hashlib
import json
from datetime import datetime, timedelta
from typing import Optional
from ascend_sdk.models import components


def validate_event_payload(
    request, webhook_secret: str, allowed_event_age: timedelta
) -> Optional[components.EventMessage]:
    """
    Validates an incoming webhook request.
    It checks the signature to ensure the request is authentic,
    verifies the timestamp to prevent replay attacks,
    and unmarshals the payload into an EventMessage.
    """
    if (
        "x-apex-event-signature" not in request.headers
        or "x-apex-event-send-time" not in request.headers
    ):
        raise ValueError(
            "Missing required headers: x-apex-event-signature and/or x-apex-event-send-time"
        )
    signature_header = request.headers.get("x-apex-event-signature")
    send_time_header = request.headers.get("x-apex-event-send-time")

    if not signature_header:
        raise ValueError("Missing required header: x-apex-event-signature")
    if not send_time_header:
        raise ValueError("Missing required header: x-apex-event-send-time")

    try:
        request_body = request.get_data(as_text=True).strip()
    except Exception as e:
        raise ValueError(f"Failed to read request body: {e}")

    try:
        send_time = datetime.fromisoformat(send_time_header)
    except Exception:
        raise ValueError("Invalid send time format")

    if event_out_of_range(send_time, allowed_event_age):
        raise ValueError(
            "Event age is out of range, it must be sent within the allowed event age"
        )

    verify_signature(signature_header, send_time_header, request_body, webhook_secret)

    try:
        event_message_data = json.loads(request_body)
        event_message = components.EventMessage(**event_message_data)
    except Exception:
        raise ValueError("Failed to unmarshal event message")

    return event_message


def event_out_of_range(send_time: datetime, allowed_event_age: timedelta) -> bool:
    """
    Determines if the event age is out of range.
    """
    current_time = datetime.utcnow()
    is_too_old = send_time < (current_time - allowed_event_age)
    is_in_the_future = send_time > (current_time + allowed_event_age)
    return is_too_old or is_in_the_future


def verify_signature(
    header_signature: str, send_time_header: str, body: str, secret: str
):
    """
    Verifies the provided signature against a calculated HMAC.
    """
    payload = f"{body}.{send_time_header}"
    mac = hmac.new(secret.encode(), payload.encode(), hashlib.sha256)
    expected_signature = mac.hexdigest()

    if not hmac.compare_digest(expected_signature, header_signature):
        raise ValueError("Provided signature does not match calculated signature")
