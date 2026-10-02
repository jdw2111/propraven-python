"""Webhook signature verification.

PropRaven signs every delivery with the header::

    X-PropRaven-Signature: t=<unix_ms>,v1=<hex hmac-sha256>

where the HMAC key is the webhook secret exactly as issued (``whsec_...``) and the
signed message is ``f"{t}.{raw_body}"``. ``t`` is Unix time in **milliseconds**.

Example::

    from propraven.webhooks import verify

    event = verify(request.body, request.headers["X-PropRaven-Signature"], secret)
"""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Any, List, Optional, Tuple, Union

from ._errors import WebhookVerificationError

__all__ = ["verify", "verify_webhook", "sign", "WebhookVerificationError", "SIGNATURE_HEADER", "DEFAULT_TOLERANCE"]

SIGNATURE_HEADER = "X-PropRaven-Signature"
DEFAULT_TOLERANCE = 300


def _to_bytes(value: Union[bytes, bytearray, memoryview, str]) -> bytes:
    if isinstance(value, str):
        return value.encode("utf-8")
    return bytes(value)


def _parse_header(signature: str) -> Tuple[int, List[str]]:
    if not isinstance(signature, str) or not signature.strip():
        raise WebhookVerificationError("Missing webhook signature header")
    timestamp: Optional[int] = None
    signatures: List[str] = []
    for part in signature.split(","):
        key, sep, value = part.strip().partition("=")
        if not sep:
            continue
        key = key.strip()
        value = value.strip()
        if key == "t":
            try:
                timestamp = int(value)
            except ValueError:
                raise WebhookVerificationError("Malformed webhook signature header: bad timestamp") from None
        elif key == "v1" and value:
            signatures.append(value.lower())
    if timestamp is None:
        raise WebhookVerificationError("Malformed webhook signature header: no t= timestamp")
    if not signatures:
        raise WebhookVerificationError("Malformed webhook signature header: no v1= signature")
    return timestamp, signatures


def sign(payload: Union[bytes, str], secret: str, timestamp_ms: int) -> str:
    """Compute the ``X-PropRaven-Signature`` header value for ``payload`` (useful in tests)."""
    message = str(timestamp_ms).encode("utf-8") + b"." + _to_bytes(payload)
    digest = hmac.new(secret.encode("utf-8"), message, hashlib.sha256).hexdigest()
    return f"t={timestamp_ms},v1={digest}"


def verify(
    payload: Union[bytes, str],
    signature: str,
    secret: str,
    tolerance: float = DEFAULT_TOLERANCE,
    now: Optional[float] = None,
) -> Any:
    """Verify a webhook delivery and return the parsed JSON event.

    Args:
        payload: The raw request body (bytes or str) exactly as received.
        signature: The ``X-PropRaven-Signature`` header value.
        secret: The webhook secret (``whsec_...``), used as-is.
        tolerance: Maximum clock skew in seconds (default 300).
        now: Current time as Unix **milliseconds** (defaults to the system clock).

    Raises:
        WebhookVerificationError: malformed header, stale timestamp or bad signature.
    """
    if not secret:
        raise WebhookVerificationError("Webhook secret is empty")
    timestamp, candidates = _parse_header(signature)
    now_ms = time.time() * 1000 if now is None else now
    if abs(now_ms - timestamp) > tolerance * 1000:
        raise WebhookVerificationError("Webhook timestamp is outside the tolerance window")

    body = _to_bytes(payload)
    message = str(timestamp).encode("utf-8") + b"." + body
    expected = hmac.new(secret.encode("utf-8"), message, hashlib.sha256).hexdigest()
    if not any(hmac.compare_digest(expected, candidate) for candidate in candidates):
        raise WebhookVerificationError("Webhook signature does not match")

    try:
        return json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise WebhookVerificationError("Webhook payload is not valid JSON") from exc


verify_webhook = verify
