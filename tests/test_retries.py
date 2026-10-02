from __future__ import annotations

import time
from email.utils import formatdate
from typing import List

import httpx
import pytest

from propraven import (
    AsyncPropRaven,
    BadRequestError,
    InternalServerError,
    PaymentRequiredError,
    PropRaven,
    RateLimitError,
    ServiceUnavailableError,
)
from propraven._transport import backoff_delay, parse_retry_after, retry_delay

from .conftest import Recorder

P429 = {"type": "t", "title": "Too Many Requests", "status": 429, "detail": "slow down", "code": "rate_limited"}


def test_retry_on_429_with_retry_after(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(429, P429, headers={"Retry-After": "3"})
    server.json({"ok": True})
    assert client.account.usage() == {"ok": True}
    assert len(server.requests) == 2
    assert sleeps == [3.0]


def test_retry_on_429_post(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(429, P429, headers={"Retry-After": "1"})
    server.json({"data": []})
    client.search.parcels(limit=1)
    assert len(server.requests) == 2


def test_retry_on_503(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(503, {"code": "unavailable", "status": 503, "detail": "down"})
    server.json({"ok": 1})
    assert client.account.usage() == {"ok": 1}
    assert len(server.requests) == 2
    assert len(sleeps) == 1
    assert 0.375 <= sleeps[0] <= 0.625  # 0.5 s +/- 25 %


def test_retry_on_504_post(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(504, {"code": "query_timeout", "status": 504, "detail": "t"})
    server.json({"data": []})
    client.search.parcels(limit=1)
    assert len(server.requests) == 2


@pytest.mark.parametrize("status,exc", [(400, BadRequestError), (402, PaymentRequiredError)])
def test_no_retry_on_4xx(client: PropRaven, server: Recorder, sleeps: List[float], status: int, exc: type) -> None:
    server.problem(status, {"code": "x", "status": status, "detail": "d"}, headers={"Retry-After": "1"})
    with pytest.raises(exc):
        client.account.usage()
    assert len(server.requests) == 1
    assert sleeps == []


def test_no_retry_on_post_500(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(500, {"code": "internal_error", "status": 500, "detail": "d"})
    with pytest.raises(InternalServerError):
        client.search.parcels(limit=1)
    assert len(server.requests) == 1


def test_retry_on_get_500_and_502(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(500, {"code": "internal_error", "status": 500, "detail": "d"})
    server.problem(502, {"code": "bad_gateway", "status": 502, "detail": "d"})
    server.json({"ok": True})
    assert client.account.usage() == {"ok": True}
    assert len(server.requests) == 3
    assert len(sleeps) == 2
    assert 0.75 <= sleeps[1] <= 1.25  # 0.5 * 2**1 +/- 25 %


def test_retry_on_delete_500(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(500, {"code": "internal_error", "status": 500, "detail": "d"})
    server.json({"deleted": "w1"})
    assert client.webhooks.delete("w1") == {"deleted": "w1"}


def test_max_retries_exhausted(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    for _ in range(3):
        server.problem(503, {"code": "unavailable", "status": 503, "detail": "down"})
    with pytest.raises(ServiceUnavailableError):
        client.account.usage()
    assert len(server.requests) == 3  # 1 + max_retries(2)
    assert len(sleeps) == 2


def test_per_request_max_retries(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(503, {"code": "unavailable", "status": 503, "detail": "down"})
    with pytest.raises(ServiceUnavailableError):
        client.account.usage(max_retries=0)
    assert len(server.requests) == 1


def test_client_max_retries(server: Recorder, sleeps: List[float]) -> None:
    http = httpx.Client(transport=httpx.MockTransport(server.handle))
    c = PropRaven(api_key="pz_k", base_url="https://api.test", http_client=http, max_retries=4)
    for _ in range(5):
        server.problem(503, {"code": "unavailable", "status": 503, "detail": "down"})
    with pytest.raises(ServiceUnavailableError):
        c.account.usage()
    assert len(server.requests) == 5


def test_cap_60s_retry_after_too_long(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(429, P429, headers={"Retry-After": "3600"})
    with pytest.raises(RateLimitError) as info:
        client.account.usage()
    assert len(server.requests) == 1
    assert sleeps == []
    assert info.value.retry_after == 3600.0


def test_cap_60s_boundary_is_retried(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(429, P429, headers={"Retry-After": "60"})
    server.json({})
    client.account.usage()
    assert sleeps == [60.0]


def test_ratelimit_reset_fallback(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    reset = int(time.time()) + 10
    server.problem(429, P429, headers={"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": str(reset)})
    server.json({})
    client.account.usage()
    assert len(sleeps) == 1
    assert 8 <= sleeps[0] <= 10


def test_ratelimit_reset_too_far_raises(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    reset = int(time.time()) + 86400
    server.problem(429, P429, headers={"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": str(reset)})
    with pytest.raises(RateLimitError):
        client.account.usage()
    assert sleeps == []


def test_network_error_then_success(client: PropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.add(httpx.ConnectError("reset"))
    server.json({"ok": True})
    assert client.search.parcels(limit=1) == {"ok": True}  # network errors retry for any method
    assert len(sleeps) == 1


def test_parse_retry_after_http_date() -> None:
    now = 1_700_000_000.0
    headers = httpx.Headers({"Retry-After": formatdate(now + 30, usegmt=True)})
    assert parse_retry_after(headers, now=now) == pytest.approx(30, abs=1)
    assert parse_retry_after(httpx.Headers({"Retry-After": "junk"})) is None
    assert parse_retry_after(httpx.Headers({})) is None


def test_retry_delay_helpers() -> None:
    assert retry_delay(httpx.Headers({"Retry-After": "61"}), 0) is None
    assert retry_delay(httpx.Headers({"Retry-After": "2"}), 0) == 2.0
    for attempt in range(10):
        assert backoff_delay(attempt) <= 60.0


async def test_async_retry_on_429(aclient: AsyncPropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(429, P429, headers={"Retry-After": "2"})
    server.json({"ok": True})
    assert await aclient.account.usage() == {"ok": True}
    assert sleeps == [2.0]


async def test_async_no_retry_post_500(aclient: AsyncPropRaven, server: Recorder, sleeps: List[float]) -> None:
    server.problem(500, {"code": "internal_error", "status": 500, "detail": "d"})
    with pytest.raises(InternalServerError):
        await aclient.search.parcels(limit=1)
    assert len(server.requests) == 1
