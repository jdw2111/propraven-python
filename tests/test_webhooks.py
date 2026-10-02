from __future__ import annotations

import hashlib
import hmac

import pytest

import propraven
from propraven import WebhookVerificationError, verify_webhook
from propraven.webhooks import sign, verify

SECRET = "whsec_test"
BODY = '{"type":"parcel.sold","id":"evt_1"}'
T = 1700000000000
# HMAC_SHA256("whsec_test", "1700000000000.{\"type\":\"parcel.sold\",\"id\":\"evt_1\"}")
EXPECTED_HEX = "5b5571cbfa4a4d4a2671f01bba9d4e2e60a3738433375ff005f2377d1f26a874"


def test_shared_test_vector() -> None:
    computed = hmac.new(SECRET.encode(), f"{T}.{BODY}".encode(), hashlib.sha256).hexdigest()
    assert computed == EXPECTED_HEX
    assert sign(BODY, SECRET, T) == f"t={T},v1={EXPECTED_HEX}"
    event = verify(BODY.encode(), f"t={T},v1={EXPECTED_HEX}", SECRET, now=T)
    assert event == {"type": "parcel.sold", "id": "evt_1"}


def test_str_payload_and_aliases() -> None:
    header = f"t={T},v1={EXPECTED_HEX}"
    assert verify(BODY, header, SECRET, now=T)["id"] == "evt_1"
    assert verify_webhook(BODY, header, SECRET, now=T)["id"] == "evt_1"
    assert propraven.webhooks.verify_webhook is verify


def test_bad_signature() -> None:
    with pytest.raises(WebhookVerificationError, match="does not match"):
        verify(BODY, f"t={T},v1={'0' * 64}", SECRET, now=T)


def test_wrong_secret() -> None:
    with pytest.raises(WebhookVerificationError):
        verify(BODY, f"t={T},v1={EXPECTED_HEX}", "whsec_other", now=T)


def test_tampered_body() -> None:
    with pytest.raises(WebhookVerificationError):
        verify(BODY.replace("evt_1", "evt_2"), f"t={T},v1={EXPECTED_HEX}", SECRET, now=T)


def test_expired_timestamp() -> None:
    header = f"t={T},v1={EXPECTED_HEX}"
    # 301 s later is outside the default 300 s tolerance
    with pytest.raises(WebhookVerificationError, match="tolerance"):
        verify(BODY, header, SECRET, now=T + 301_000)
    # ... and inside a widened tolerance
    assert verify(BODY, header, SECRET, tolerance=600, now=T + 301_000)["id"] == "evt_1"
    # future timestamps are rejected too
    with pytest.raises(WebhookVerificationError):
        verify(BODY, header, SECRET, now=T - 301_000)
    # exactly at the boundary is accepted
    assert verify(BODY, header, SECRET, now=T + 300_000)["id"] == "evt_1"


@pytest.mark.parametrize(
    "header",
    ["", "garbage", f"v1={EXPECTED_HEX}", f"t={T}", f"t=abc,v1={EXPECTED_HEX}", "t=,v1="],
)
def test_malformed_header(header: str) -> None:
    with pytest.raises(WebhookVerificationError):
        verify(BODY, header, SECRET, now=T)


def test_multiple_v1_entries() -> None:
    header = f"t={T},v1={'f' * 64},v1={EXPECTED_HEX}"
    assert verify(BODY, header, SECRET, now=T)["type"] == "parcel.sold"
    header_spaces = f"t={T}, v1={'a' * 64}, v1={EXPECTED_HEX.upper()}"
    assert verify(BODY, header_spaces, SECRET, now=T)["type"] == "parcel.sold"


def test_non_json_payload() -> None:
    header = sign("not json", SECRET, T)
    with pytest.raises(WebhookVerificationError, match="JSON"):
        verify("not json", header, SECRET, now=T)


def test_empty_secret() -> None:
    with pytest.raises(WebhookVerificationError):
        verify(BODY, f"t={T},v1={EXPECTED_HEX}", "", now=T)
