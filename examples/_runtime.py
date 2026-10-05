"""Replay six exact requests in memory. No socket or API key is needed."""

from __future__ import annotations

import argparse
import json
import warnings
from contextlib import contextmanager
from pathlib import Path

import httpx

from propraven import PropRaven

FIXTURE = Path(__file__).parent / "fixtures" / "responses.json"


class Replay:
    def __init__(self):
        self.records = json.loads(FIXTURE.read_text())["records"]
        self.seen = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        if request.url.host != "example.invalid" or "authorization" in request.headers:
            raise AssertionError("Mock requests must use example.invalid without authorization")
        query = dict(request.url.params)
        body = json.loads(request.content) if request.content else None
        for row in self.records:
            if (request.method, request.url.path, query, body) == (
                row["method"], row["path"], row["query"], row["body"]
            ):
                self.seen.append(row["name"])
                return httpx.Response(200, json=row["response"], request=request)
        raise AssertionError("Unrecorded request: mock mode never falls back to the network")


@contextmanager
def client_context(mock=True):
    if not mock:
        with PropRaven() as client:
            yield client
        return
    replay = Replay()
    with httpx.Client(transport=httpx.MockTransport(replay), trust_env=False) as transport:
        # Explicit empty key avoids reading PROPRAVEN_API_KEY. This SDK version
        # warns about an empty key's prefix even though it sends no auth header.
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message="PropRaven API keys start with", category=UserWarning)
            client = PropRaven(api_key="", base_url="https://example.invalid", http_client=transport, max_retries=0)
        with client:
            yield client


def main(run):
    parser = argparse.ArgumentParser(description="Public SDK example; defaults to offline mock mode")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--mock", action="store_true", help="Replay schema-derived JSON in memory (default)")
    modes.add_argument("--live", action="store_true", help="Call the API using normal SDK environment configuration")
    args = parser.parse_args()
    with client_context(mock=not args.live) as client:
        print(json.dumps(run(client), indent=2))
