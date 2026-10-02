#!/usr/bin/env python3
"""Live smoke test against the real PropRaven API. NOT run in CI.

    PROPRAVEN_API_KEY=pz_... python scripts/live_smoke.py [--extended]

* At most 12 HTTP requests by default (14 with ``--extended``, which adds
  coverage.get and freshness.get); a hard request budget aborts beyond that.
* At most 2 requests per second (>= 0.55 s between requests); retries disabled.
* Read-only: never calls purchase/paid operations, never sends a payment header,
  never creates webhooks, watches or cohorts.
* Prints only statuses, counts and key names -- never the API key or record values.
"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
import threading
import time
from pathlib import Path
from typing import Any, Callable, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import httpx  # noqa: E402

import propraven  # noqa: E402
from propraven import AsyncPropRaven, BadRequestError, NotFoundError, PropRaven  # noqa: E402

MIN_INTERVAL = 0.55
FALLBACK_ID = "37:119:12104406"
BOUNDS = {"north": 35.215, "south": 35.205, "east": -80.855, "west": -80.865}


class Budget:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.count = 0
        self.last = 0.0
        self.statuses: List[int] = []
        self.lock = threading.Lock()

    def before(self, request: httpx.Request) -> None:
        with self.lock:
            if self.count >= self.limit:
                raise RuntimeError(
                    f"request budget of {self.limit} exhausted; refusing {request.method} {request.url.path}"
                )
            for header in ("x-payment", "x-credit-token"):
                if header in request.headers:
                    raise RuntimeError("smoke test must never send payment/credit headers")
            wait = self.last + MIN_INTERVAL - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            self.last = time.monotonic()
            self.count += 1

    def after(self, response: httpx.Response) -> None:
        self.statuses.append(response.status_code)


def describe(value: Any) -> str:
    if isinstance(value, dict):
        keys = sorted(value)
        parts = [f"{len(keys)} keys"]
        for k in ("data", "results", "deliveries"):
            if isinstance(value.get(k), list):
                parts.append(f"{k}={len(value[k])}")
        shown = ", ".join(keys[:8]) + (", ..." if len(keys) > 8 else "")
        return f"dict({'; '.join(parts)}) [{shown}]"
    if isinstance(value, list):
        return f"list(len={len(value)})"
    if isinstance(value, str):
        return f"str(len={len(value)})"
    return type(value).__name__


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--extended", action="store_true", help="also call coverage.get and freshness.get (14 requests)"
    )
    args = parser.parse_args()

    if not os.environ.get("PROPRAVEN_API_KEY"):
        print("PROPRAVEN_API_KEY is not set", file=sys.stderr)
        return 2

    budget = Budget(14 if args.extended else 12)
    http = httpx.Client(event_hooks={"request": [budget.before], "response": [budget.after]}, follow_redirects=True)
    client = PropRaven(max_retries=0, http_client=http, timeout=60)

    print(f"propraven-python {propraven.__version__} live smoke against {client.base_url}")
    print(f"key present: yes (prefix ok: {str(client.api_key).startswith('pz_')})")
    failures = 0

    def step(name: str, fn: Callable[[], Any], expect: Optional[type] = None) -> Any:
        nonlocal failures
        before = len(budget.statuses)
        t0 = time.monotonic()
        try:
            result = fn()
            took = time.monotonic() - t0
            codes = budget.statuses[before:]
            if expect is not None:
                failures += 1
                print(f"FAIL  {name:<34} http={codes} expected {expect.__name__} but call succeeded ({took:.2f}s)")
                return None
            print(f"ok    {name:<34} http={codes} {describe(result)} ({took:.2f}s)")
            return result
        except Exception as exc:  # noqa: BLE001
            took = time.monotonic() - t0
            codes = budget.statuses[before:]
            if expect is not None and isinstance(exc, expect):
                code = getattr(exc, "code", None)
                print(f"ok    {name:<34} http={codes} raised {type(exc).__name__} code={code} ({took:.2f}s)")
                return None
            failures += 1
            print(f"FAIL  {name:<34} http={codes} {type(exc).__name__}: {str(exc)[:200]} ({took:.2f}s)")
            return None

    # 1. search.parcels (POST body) -- also yields a real parcel id for the next calls
    found = step("search.parcels", lambda: client.search.parcels(bounds=BOUNDS, limit=2))
    parcel_id = FALLBACK_ID
    if isinstance(found, dict) and found.get("data"):
        row = found["data"][0]
        if row.get("canonical_id"):
            parcel_id = str(row["canonical_id"])
        elif row.get("state_fips") and row.get("county_fips") and row.get("parcel_id"):
            parcel_id = f"{row['state_fips']}:{str(row['county_fips'])[-3:]}:{row['parcel_id']}"
    print(f"      (using parcel id from {'search' if parcel_id != FALLBACK_ID else 'fallback'})")

    # 2-3. parcels.get / parcels.permits
    parcel = step("parcels.get", lambda: client.parcels.get(parcel_id))
    step("parcels.permits(shape=envelope)", lambda: client.parcels.permits(parcel_id, shape="envelope"))

    # 4-5. search.full + one cursor page via the iterator
    step("search.full_iter(page_size=2) x2", lambda: list(client.search.full_iter(q="main", page_size=2, max_items=4)))

    # 6-7. deals.absentee: two pages via the offset iterator
    step(
        "deals.absentee_iter(page_size=2) x2",
        lambda: list(client.deals.absentee_iter(county_fips="37119", page_size=2, max_items=4)),
    )

    # 8. market.counties
    step("market.counties(limit=2)", lambda: client.market.counties(limit=2))

    # 9. owners.get
    owner = parcel.get("owner_name") if isinstance(parcel, dict) else None
    step("owners.get", lambda: client.owners.get(str(owner or "MECKLENBURG COUNTY")))

    # 10. account.usage via the ASYNC client
    async def usage() -> Any:
        async def abefore(request: httpx.Request) -> None:
            budget.before(request)

        async def aafter(response: httpx.Response) -> None:
            budget.after(response)

        ahttp = httpx.AsyncClient(event_hooks={"request": [abefore], "response": [aafter]}, follow_redirects=True)
        async with AsyncPropRaven(max_retries=0, http_client=ahttp) as aclient:
            try:
                return await aclient.account.usage()
            finally:
                await ahttp.aclose()

    step("account.usage (async)", lambda: asyncio.run(usage()))

    if args.extended:
        step("coverage.get", lambda: client.coverage.get())
        step("freshness.get", lambda: client.freshness.get())

    # 11-12. error paths
    step("parcels.get(nonexistent)", lambda: client.parcels.get("37:119:SDKSMOKE0000000000"), expect=NotFoundError)
    step("deals.absentee(limit=0)", lambda: client.deals.absentee(county_fips="37119", limit=0), expect=BadRequestError)

    rl = client.last_rate_limit
    print(f"requests made: {budget.count} (budget {budget.limit}); last rate limit: {rl}")
    print("RESULT:", "PASS" if failures == 0 else f"{failures} FAILED")
    client.close()
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
