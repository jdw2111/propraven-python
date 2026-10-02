from __future__ import annotations

import json
from typing import Any, Callable, Dict, List, Optional, Union

import httpx
import pytest

import propraven._client as client_module
from propraven import AsyncPropRaven, PropRaven

BASE = "https://api.test"

Handler = Callable[[httpx.Request], httpx.Response]


class Recorder:
    """A scripted mock server: returns queued responses in order and records requests."""

    def __init__(self) -> None:
        self.requests: List[httpx.Request] = []
        self.queue: List[Union[httpx.Response, Exception, Handler]] = []

    def add(self, item: Union[httpx.Response, Exception, Handler]) -> Recorder:
        self.queue.append(item)
        return self

    def json(self, body: Any, status: int = 200, headers: Optional[Dict[str, str]] = None) -> Recorder:
        h = {"content-type": "application/json"}
        h.update(headers or {})
        return self.add(httpx.Response(status, content=json.dumps(body).encode(), headers=h))

    def problem(self, status: int, body: Any, headers: Optional[Dict[str, str]] = None) -> Recorder:
        h = {"content-type": "application/problem+json"}
        h.update(headers or {})
        return self.add(httpx.Response(status, content=json.dumps(body).encode(), headers=h))

    def handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if not self.queue:
            raise AssertionError(f"unexpected request {request.method} {request.url}")
        item = self.queue.pop(0)
        if isinstance(item, Exception):
            raise item
        if callable(item) and not isinstance(item, httpx.Response):
            return item(request)
        return item

    @property
    def last(self) -> httpx.Request:
        return self.requests[-1]

    def body(self, index: int = -1) -> Any:
        return json.loads(self.requests[index].content.decode())


@pytest.fixture
def server() -> Recorder:
    return Recorder()


@pytest.fixture
def sleeps(monkeypatch: pytest.MonkeyPatch) -> List[float]:
    recorded: List[float] = []

    def fake_sleep(seconds: float) -> None:
        recorded.append(seconds)

    async def fake_asleep(seconds: float) -> None:
        recorded.append(seconds)

    monkeypatch.setattr(client_module, "_sleep", fake_sleep)
    monkeypatch.setattr(client_module, "_asleep", fake_asleep)
    return recorded


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("PROPRAVEN_API_KEY", raising=False)
    monkeypatch.delenv("PROPRAVEN_BASE_URL", raising=False)


@pytest.fixture
def client(server: Recorder, sleeps: List[float]) -> PropRaven:
    http = httpx.Client(transport=httpx.MockTransport(server.handle))
    return PropRaven(api_key="pz_test_key", base_url=BASE, http_client=http)


@pytest.fixture
def aclient(server: Recorder, sleeps: List[float]) -> AsyncPropRaven:
    http = httpx.AsyncClient(transport=httpx.MockTransport(server.handle))
    return AsyncPropRaven(api_key="pz_test_key", base_url=BASE, http_client=http)
