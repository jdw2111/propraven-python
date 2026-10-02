from __future__ import annotations

import json
import warnings

import httpx
import pytest

from propraven import AsyncPropRaven, AsyncPropraven, PropRaven, Propraven, RateLimit, __version__

from .conftest import BASE, Recorder


def test_auth_header_and_default_headers(client: PropRaven, server: Recorder) -> None:
    server.json({"parcel_id": "12104406"})
    result = client.parcels.get("37:119:12104406")
    assert result == {"parcel_id": "12104406"}
    req = server.last
    assert req.method == "GET"
    assert req.headers["authorization"] == "Bearer pz_test_key"
    assert req.headers["user-agent"] == f"propraven-python/{__version__}"
    assert req.headers["accept"] == "application/json"
    assert "content-type" not in req.headers


def test_path_param_is_url_encoded(client: PropRaven, server: Recorder) -> None:
    server.json({})
    client.parcels.get("37:119:12104406")
    assert server.last.url.raw_path == b"/api/v1/parcels/37%3A119%3A12104406"
    server.json({})
    client.owners.get("SMITH JOHN/A")
    assert server.last.url.raw_path == b"/api/v1/owners/SMITH%20JOHN%2FA"


def test_empty_path_param_rejected(client: PropRaven) -> None:
    with pytest.raises(ValueError):
        client.parcels.get("")


def test_query_encoding(client: PropRaven, server: Recorder) -> None:
    server.json({"data": []})
    client.deals.absentee(county_fips="37119", out_of_state=True, min_value=None, limit=5, offset=0)
    url = server.last.url
    assert url.path == "/api/v1/deals/absentee"
    assert url.params.get("county_fips") == "37119"
    assert url.params.get("out_of_state") == "true"
    assert url.params.get("limit") == "5"
    assert url.params.get("offset") == "0"
    assert "min_value" not in url.params  # None is omitted


def test_query_false_and_float(client: PropRaven, server: Recorder) -> None:
    server.json({"data": []})
    client.deals.absentee(out_of_state=False, min_value=250000.5)
    assert server.last.url.params.get("out_of_state") == "false"
    assert server.last.url.params.get("min_value") == "250000.5"


def test_query_array_comma_joined_and_explode() -> None:
    from propraven._transport import encode_query

    assert encode_query({"ids": ["a", "b"], "n": None, "flag": True}) == [("ids", "a,b"), ("flag", "true")]
    assert encode_query({"ids": ["a", "b"]}, explode={"ids"}) == [("ids", "a"), ("ids", "b")]


def test_json_body(client: PropRaven, server: Recorder) -> None:
    server.json({"data": [], "total": 0, "limit": 50, "offset": 0})
    client.search.parcels(
        bounds={"north": 35.215, "south": 35.205, "east": -80.855, "west": -80.865},
        filters={"valueRange": {"min": 100000, "max": None}},
        limit=50,
    )
    req = server.last
    assert req.method == "POST"
    assert req.url.path == "/api/v1/search"
    assert req.headers["content-type"] == "application/json"
    body = server.body()
    assert body == {
        "bounds": {"north": 35.215, "south": 35.205, "east": -80.855, "west": -80.865},
        # nested None is preserved (explicit null); unset top-level keywords are omitted
        "filters": {"valueRange": {"min": 100000, "max": None}},
        "limit": 50,
    }


def test_extra_body_query_headers(client: PropRaven, server: Recorder) -> None:
    server.json({})
    client.lookup.batch(
        queries=["a"],
        extra_body={"debug": True},
        extra_query={"trace": 1},
        extra_headers={"X-Test": "1"},
    )
    assert server.body() == {"queries": ["a"], "debug": True}
    assert server.last.url.params.get("trace") == "1"
    assert server.last.headers["x-test"] == "1"


def test_header_params_friendly_names(client: PropRaven, server: Recorder) -> None:
    server.json({"balance": 1})
    client.credits.balance(credit_token="ct_123")
    assert server.last.headers["x-credit-token"] == "ct_123"
    server.json({})
    client.parcels.report("37:119:1", payment=None)
    assert "x-payment" not in server.last.headers


def test_csv_endpoint_returns_string(client: PropRaven, server: Recorder) -> None:
    server.add(httpx.Response(200, content=b"parcel_id,address\n1,123 Main\n", headers={"content-type": "text/csv"}))
    out = client.search.export(north=35.2, south=35.1, east=-80.8, west=-80.9)
    assert out == "parcel_id,address\n1,123 Main\n"
    assert server.last.headers["accept"].startswith("text/csv")


def test_csv_or_json_endpoint_json_branch(client: PropRaven, server: Recorder) -> None:
    server.json({"preview": True, "mailing_rows": 3})
    out = client.cohorts.export("c1", preview=True)
    assert out == {"preview": True, "mailing_rows": 3}


def test_missing_key_is_allowed(server: Recorder) -> None:
    http = httpx.Client(transport=httpx.MockTransport(server.handle))
    c = PropRaven(base_url=BASE, http_client=http)
    assert c.api_key is None
    server.json({"status": "ok"})
    c.freshness.get()
    assert "authorization" not in server.last.headers


def test_env_key_and_base_url(monkeypatch: pytest.MonkeyPatch, server: Recorder) -> None:
    monkeypatch.setenv("PROPRAVEN_API_KEY", "pz_from_env")
    monkeypatch.setenv("PROPRAVEN_BASE_URL", "https://env.example/")
    http = httpx.Client(transport=httpx.MockTransport(server.handle))
    c = PropRaven(http_client=http)
    assert c.base_url == "https://env.example"
    server.json({})
    c.account.usage()
    assert str(server.last.url) == "https://env.example/api/v1/account/usage"
    assert server.last.headers["authorization"] == "Bearer pz_from_env"


def test_default_base_url() -> None:
    c = PropRaven(api_key="pz_x")
    assert c.base_url == "https://propraven.com"
    c.close()


def test_non_pz_key_warns_but_works(server: Recorder) -> None:
    http = httpx.Client(transport=httpx.MockTransport(server.handle))
    with pytest.warns(UserWarning, match="pz_"):
        c = PropRaven(api_key="sk_wrong", base_url=BASE, http_client=http)
    server.json({})
    c.account.usage()
    assert server.last.headers["authorization"] == "Bearer sk_wrong"


def test_pz_key_does_not_warn() -> None:
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        PropRaven(api_key="pz_ok").close()


def test_aliases() -> None:
    assert Propraven is PropRaven
    assert AsyncPropraven is AsyncPropRaven


def test_default_timeout_and_override(client: PropRaven, server: Recorder) -> None:
    seen = []

    def capture(request: httpx.Request) -> httpx.Response:
        seen.append(request.extensions.get("timeout"))
        return httpx.Response(200, json={})

    server.add(capture).add(capture)
    client.account.usage()
    client.account.usage(timeout=5)
    assert seen[0]["read"] == 60.0
    assert seen[1]["read"] == 5


def test_rate_limit_info(client: PropRaven, server: Recorder) -> None:
    assert client.last_rate_limit is None
    server.json(
        {}, headers={"X-RateLimit-Limit": "1000", "X-RateLimit-Remaining": "998", "X-RateLimit-Reset": "1700000000"}
    )
    client.account.usage()
    assert client.last_rate_limit == RateLimit(limit=1000, remaining=998, reset=1700000000)


def test_request_escape_hatch(client: PropRaven, server: Recorder) -> None:
    server.json({"ok": True})
    assert client.request("GET", "/api/v1/freshness", query={"x": True}) == {"ok": True}
    assert server.last.url.params.get("x") == "true"


def test_context_manager() -> None:
    with PropRaven(api_key="pz_x") as c:
        assert isinstance(c, PropRaven)


def test_body_keyword_required(client: PropRaven) -> None:
    with pytest.raises(TypeError):
        client.lookup.batch()  # type: ignore[call-arg]


async def test_async_client(aclient: AsyncPropRaven, server: Recorder) -> None:
    server.json({"parcel_id": "1"})
    out = await aclient.parcels.get("37:119:1")
    assert out == {"parcel_id": "1"}
    assert server.last.headers["authorization"] == "Bearer pz_test_key"
    server.json({"data": []})
    await aclient.search.parcels(limit=1)
    assert json.loads(server.last.content) == {"limit": 1}
    await aclient.close()


async def test_async_context_manager() -> None:
    async with AsyncPropRaven(api_key="pz_x") as c:
        assert isinstance(c, AsyncPropRaven)
