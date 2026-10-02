from __future__ import annotations

from typing import Type

import httpx
import pytest

import propraven
from propraven import (
    APIError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    GatewayTimeoutError,
    InternalServerError,
    MethodNotAllowedError,
    NotFoundError,
    PayloadTooLargeError,
    PaymentRequiredError,
    PermissionDeniedError,
    PropRaven,
    PropRavenError,
    RateLimitError,
    ServiceUnavailableError,
    UnprocessableEntityError,
)

from .conftest import Recorder


def problem(status: int, code: str, detail: str = "something went wrong", **extra: object) -> dict:
    body = {
        "type": f"https://api.propraven.com/errors/{code.replace('_', '-')}",
        "title": "Title",
        "status": status,
        "detail": detail,
        "code": code,
        "request_id": "req_123",
    }
    body.update(extra)
    return body


@pytest.mark.parametrize(
    "status,cls",
    [
        (400, BadRequestError),
        (401, AuthenticationError),
        (402, PaymentRequiredError),
        (403, PermissionDeniedError),
        (404, NotFoundError),
        (405, MethodNotAllowedError),
        (409, ConflictError),
        (413, PayloadTooLargeError),
        (422, UnprocessableEntityError),
        (429, RateLimitError),
        (500, InternalServerError),
        (501, InternalServerError),
        (502, InternalServerError),
        (503, ServiceUnavailableError),
        (504, GatewayTimeoutError),
        (418, APIError),
    ],
)
def test_error_class_from_problem_body(status: int, cls: Type[APIError], server: Recorder, sleeps: list) -> None:
    http = httpx.Client(transport=httpx.MockTransport(server.handle))
    c = PropRaven(api_key="pz_k", base_url="https://api.test", http_client=http, max_retries=0)
    server.problem(status, problem(status, "some_code", "the detail"))
    with pytest.raises(cls) as info:
        c.account.usage()
    err = info.value
    assert type(err) is cls
    assert isinstance(err, APIError)
    assert isinstance(err, PropRavenError)
    assert err.status == status
    assert err.status_code == status
    assert err.code == "some_code"
    assert err.detail == "the detail"
    assert err.title == "Title"
    assert err.type == "https://api.propraven.com/errors/some-code"
    assert err.request_id == "req_123"
    assert err.body["code"] == "some_code"
    assert str(err) == f"{status} some_code: the detail"


def test_validation_errors_list(client: PropRaven, server: Recorder) -> None:
    server.problem(
        400,
        problem(
            400, "invalid_parameter", "limit: must be >= 1", errors=[{"param": "limit", "message": "must be >= 1"}]
        ),
    )
    with pytest.raises(BadRequestError) as info:
        client.deals.absentee(limit=0)
    assert info.value.errors == [{"param": "limit", "message": "must be >= 1"}]
    assert str(info.value) == "400 invalid_parameter: limit: must be >= 1"


def test_legacy_error_body(client: PropRaven, server: Recorder) -> None:
    server.json({"error": "Parcel not found"}, status=404)
    with pytest.raises(NotFoundError) as info:
        client.parcels.get("1:2:3")
    err = info.value
    assert err.detail == "Parcel not found"
    assert err.code is None
    assert str(err).startswith("404 ")
    assert str(err).endswith(": Parcel not found")


def test_x402_body(client: PropRaven, server: Recorder) -> None:
    accepts = [{"scheme": "exact", "network": "base", "maxAmountRequired": "5000000", "payTo": "0xabc"}]
    server.json({"x402Version": 1, "error": "X-PAYMENT header is required", "accepts": accepts}, status=402)
    with pytest.raises(PaymentRequiredError) as info:
        client.parcels.report("37:119:1")
    err = info.value
    assert err.accepts == accepts
    assert err.detail == "X-PAYMENT header is required"
    assert err.code == "payment_required"
    assert str(err) == "402 payment_required: X-PAYMENT header is required"


def test_402_problem_has_empty_accepts(client: PropRaven, server: Recorder) -> None:
    server.problem(402, problem(402, "monthly_cap_reached", "Free tier is capped", used=100, limit=100))
    with pytest.raises(PaymentRequiredError) as info:
        client.account.usage()
    assert info.value.accepts == []
    assert info.value.body["used"] == 100


def test_rate_limit_error_retry_after(server: Recorder, sleeps: list) -> None:
    http = httpx.Client(transport=httpx.MockTransport(server.handle))
    c = PropRaven(api_key="pz_k", base_url="https://api.test", http_client=http, max_retries=0)
    server.problem(429, problem(429, "rate_limited"), headers={"Retry-After": "7"})
    with pytest.raises(RateLimitError) as info:
        c.account.usage()
    assert info.value.retry_after == 7.0


def test_rate_limit_error_without_retry_after(server: Recorder, sleeps: list) -> None:
    http = httpx.Client(transport=httpx.MockTransport(server.handle))
    c = PropRaven(api_key="pz_k", base_url="https://api.test", http_client=http, max_retries=0)
    server.problem(429, problem(429, "rate_limited"))
    with pytest.raises(RateLimitError) as info:
        c.account.usage()
    assert info.value.retry_after is None


def test_non_json_error_body(client: PropRaven, server: Recorder) -> None:
    server.add(httpx.Response(404, content=b"<html>nope</html>", headers={"content-type": "text/html"}))
    with pytest.raises(NotFoundError) as info:
        client.account.usage()
    assert info.value.body == "<html>nope</html>"
    assert info.value.detail == "<html>nope</html>"


def test_connection_error(client: PropRaven, server: Recorder, sleeps: list) -> None:
    for _ in range(3):
        server.add(httpx.ConnectError("boom"))
    with pytest.raises(propraven.APIConnectionError):
        client.account.usage()
    assert len(server.requests) == 3


def test_timeout_error(client: PropRaven, server: Recorder, sleeps: list) -> None:
    for _ in range(3):
        server.add(httpx.ReadTimeout("slow"))
    with pytest.raises(propraven.APITimeoutError) as info:
        client.account.usage()
    assert isinstance(info.value, propraven.APIConnectionError)
    assert len(server.requests) == 3
