from __future__ import annotations

import json
from typing import Any, Callable, Dict, List, Optional

import httpx

from propraven import AsyncPropRaven, PropRaven

from .conftest import Recorder

ROWS = [{"parcel_id": str(i)} for i in range(25)]


def offset_page(total: Optional[int] = None, include_total: bool = True, has_more: bool = False) -> Callable:
    """Handler serving ROWS[:total] by limit/offset from the query string or JSON body."""
    rows = ROWS if total is None else ROWS[:total]

    def handler(request: httpx.Request) -> httpx.Response:
        if request.method == "POST":
            body = json.loads(request.content)
            limit, offset = int(body.get("limit", 10)), int(body.get("offset", 0))
        else:
            limit = int(request.url.params.get("limit", 10))
            offset = int(request.url.params.get("offset", 0))
        data = rows[offset : offset + limit]
        page: Dict[str, Any] = {"data": data, "limit": limit, "offset": offset}
        if include_total:
            page["total"] = len(rows)
        if has_more:
            page["has_more"] = offset + len(data) < len(rows)
        return httpx.Response(200, json=page)

    return handler


def offsets(server: Recorder) -> List[int]:
    return [int(r.url.params.get("offset", 0)) for r in server.requests]


def test_offset_three_pages_stops_on_short_page(client: PropRaven, server: Recorder) -> None:
    handler = offset_page(include_total=False)
    for _ in range(3):
        server.add(handler)
    items = list(client.deals.absentee_iter(county_fips="37119", page_size=10))
    assert [r["parcel_id"] for r in items] == [str(i) for i in range(25)]
    assert offsets(server) == [0, 10, 20]
    assert all(r.url.params.get("limit") == "10" for r in server.requests)
    assert all(r.url.params.get("county_fips") == "37119" for r in server.requests)


def test_offset_stops_on_total(client: PropRaven, server: Recorder) -> None:
    handler = offset_page(total=20)
    for _ in range(2):
        server.add(handler)
    items = list(client.deals.absentee_iter(page_size=10))
    assert len(items) == 20
    assert offsets(server) == [0, 10]  # no third request for an empty page


def test_offset_stops_on_has_more_false(client: PropRaven, server: Recorder) -> None:
    handler = offset_page(total=20, include_total=False, has_more=True)
    for _ in range(2):
        server.add(handler)
    assert len(list(client.deals.absentee_iter(page_size=10))) == 20
    assert len(server.requests) == 2


def test_offset_max_items(client: PropRaven, server: Recorder) -> None:
    handler = offset_page()
    for _ in range(2):
        server.add(handler)
    items = list(client.deals.absentee_iter(page_size=10, max_items=15))
    assert len(items) == 15
    assert len(server.requests) == 2


def test_offset_is_lazy(client: PropRaven, server: Recorder) -> None:
    server.add(offset_page())
    it = client.deals.absentee_iter(page_size=10)
    assert server.requests == []
    next(iter(it))
    assert len(server.requests) == 1


def test_offset_uses_echoed_limit_when_server_clamps(client: PropRaven, server: Recorder) -> None:
    # Ask for 1000; the server clamps to 10 and echoes limit=10, so a full page of 10 is not "short".
    def clamped(request: httpx.Request) -> httpx.Response:
        offset = int(request.url.params.get("offset", 0))
        data = ROWS[offset : offset + 10]
        return httpx.Response(200, json={"data": data, "limit": 10, "offset": offset})

    for _ in range(3):
        server.add(clamped)
    assert len(list(client.deals.absentee_iter(page_size=1000))) == 25


def test_offset_in_post_body(client: PropRaven, server: Recorder) -> None:
    handler = offset_page()
    for _ in range(3):
        server.add(handler)
    items = list(client.search.parcels_iter(bounds={"north": 1, "south": 0, "east": 1, "west": 0}, page_size=10))
    assert len(items) == 25
    bodies = [json.loads(r.content) for r in server.requests]
    assert [b["offset"] for b in bodies] == [0, 10, 20]
    assert all(b["limit"] == 10 and "bounds" in b for b in bodies)


def test_offset_path_param(client: PropRaven, server: Recorder) -> None:
    handler = offset_page(total=5)
    server.add(handler)
    items = list(client.owners.properties_iter("ACME LLC", page_size=10))
    assert len(items) == 5
    assert server.last.url.raw_path.startswith(b"/api/v1/owners/ACME%20LLC/properties")


def cursor_handler(pages: Dict[Optional[str], Dict[str, Any]]) -> Callable:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=pages[request.url.params.get("after")])

    return handler


def test_cursor_pagination(client: PropRaven, server: Recorder) -> None:
    pages = {
        None: {"results": [{"id": 1}, {"id": 2}], "nextCursor": "c1", "hasMore": True},
        "c1": {"results": [{"id": 3}, {"id": 4}], "nextCursor": "c2", "hasMore": True},
        "c2": {"results": [{"id": 5}], "nextCursor": None, "hasMore": False},
    }
    h = cursor_handler(pages)
    for _ in range(3):
        server.add(h)
    items = list(client.search.full_iter(q="main", page_size=2))
    assert [i["id"] for i in items] == [1, 2, 3, 4, 5]
    assert [r.url.params.get("after") for r in server.requests] == [None, "c1", "c2"]
    assert all(r.url.params.get("q") == "main" and r.url.params.get("limit") == "2" for r in server.requests)


def test_cursor_stops_when_has_more_false(client: PropRaven, server: Recorder) -> None:
    server.add(cursor_handler({None: {"results": [{"id": 1}], "nextCursor": "c1", "hasMore": False}}))
    assert len(list(client.search.full_iter(q="x"))) == 1
    assert len(server.requests) == 1


def test_cursor_stops_when_next_absent(client: PropRaven, server: Recorder) -> None:
    server.add(cursor_handler({None: {"results": [{"id": 1}]}}))
    assert len(list(client.search.full_iter(q="x"))) == 1


async def test_async_offset_iter(aclient: AsyncPropRaven, server: Recorder) -> None:
    handler = offset_page(include_total=False)
    for _ in range(3):
        server.add(handler)
    items = [row async for row in aclient.deals.absentee_iter(page_size=10)]
    assert len(items) == 25
    assert offsets(server) == [0, 10, 20]


async def test_async_cursor_iter(aclient: AsyncPropRaven, server: Recorder) -> None:
    pages = {
        None: {"results": [{"id": 1}], "nextCursor": "c1"},
        "c1": {"results": [{"id": 2}], "nextCursor": None},
    }
    h = cursor_handler(pages)
    server.add(h).add(h)
    items = [row async for row in aclient.search.full_iter(q="x", max_items=10)]
    assert [i["id"] for i in items] == [1, 2]
