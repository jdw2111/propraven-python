# PropRaven Python SDK

[![PyPI version](https://img.shields.io/pypi/v/propraven.svg)](https://pypi.org/project/propraven/)

The official Python client for the [PropRaven](https://propraven.com) property-intelligence API:
US parcels with ownership, valuation, permits, deeds, risk and market data.

- Sync (`PropRaven`) and async (`AsyncPropRaven`) clients, Python 3.9+.
- One runtime dependency: [`httpx`](https://www.python-httpx.org/).
- Every response is typed as a `TypedDict` (plain `dict`s at runtime, no validation step).
- Automatic retries with `Retry-After` support, typed RFC 7807 errors, auto-pagination and
  webhook signature verification.

Documentation: [developer hub](https://propraven.com/developers) ·
[REST API v1 reference](https://propraven.com/docs/v1) ·
[hosted MCP server](https://propraven.com/docs/mcp)

## Installation

```sh
pip install propraven
```

## Quick start

```python
from propraven import PropRaven

client = PropRaven()  # reads PROPRAVEN_API_KEY from the environment

parcel = client.parcels.get("37:119:12104406")
print(parcel.get("address"), parcel.get("owner_name"))

page = client.search.parcels(
    bounds={"north": 35.215, "south": 35.205, "east": -80.855, "west": -80.865},
    filters={"valueRange": {"min": 100_000}},
    limit=50,
)
print(page["total"], len(page["data"]))
```

Methods mirror the API: `client.<namespace>.<method>(path_params..., **params)`. Path parameters are
positional; query parameters, header parameters and JSON body fields are keyword arguments with
their wire names (`county_fips`, `min_value`, ...). A keyword left as `None` is not sent. Every method
also accepts `extra_headers`, `extra_query`, `extra_body` (body endpoints), `timeout` and
`max_retries`.

### Async

```python
import asyncio
from propraven import AsyncPropRaven


async def main() -> None:
    async with AsyncPropRaven() as client:
        usage = await client.account.usage()
        async for row in client.deals.absentee_iter(county_fips="37119", max_items=100):
            print(row.get("parcel_id"))


asyncio.run(main())
```

## Authentication

Pass `api_key="pz_..."` or set `PROPRAVEN_API_KEY`. The key is sent as `Authorization: Bearer <key>`.
Keys start with `pz_`; the client warns (but still sends the request) when a key does not.
The key is optional: key-optional endpoints work anonymously (100 calls a day per IP), and endpoints
that need a key answer `401`, raised as `AuthenticationError`.

**Server-side only.** API keys are secrets and the REST API sends no CORS headers, so use this SDK
from servers, scripts and notebooks, never from code shipped to browsers or end-user devices.

## Configuration

```python
client = PropRaven(
    api_key="pz_...",                  # default: PROPRAVEN_API_KEY
    base_url="https://propraven.com",  # default: PROPRAVEN_BASE_URL or https://propraven.com
    timeout=60.0,                      # seconds or an httpx.Timeout; per request: timeout=...
    max_retries=2,                     # per request: max_retries=...
    default_headers={"X-Team": "ops"},
    http_client=None,                  # bring your own httpx.Client / httpx.AsyncClient
)
```

`client.request("GET", "/api/v1/freshness")` calls any endpoint directly with the same auth, retries
and error handling.

## Errors

Error responses are RFC 7807 problem documents. Each status maps to an exception class, all
subclasses of `propraven.APIError` (itself a `propraven.PropRavenError`):

| Status | Exception |
| --- | --- |
| 400 | `BadRequestError` |
| 401 | `AuthenticationError` |
| 402 | `PaymentRequiredError` (`.accepts` holds x402 payment requirements, else `[]`) |
| 403 | `PermissionDeniedError` |
| 404 | `NotFoundError` |
| 405 | `MethodNotAllowedError` |
| 409 | `ConflictError` |
| 413 | `PayloadTooLargeError` |
| 422 | `UnprocessableEntityError` |
| 429 | `RateLimitError` (`.retry_after` in seconds, or `None`) |
| 503 | `ServiceUnavailableError` |
| 504 | `GatewayTimeoutError` |
| other 5xx | `InternalServerError` |

Every `APIError` has `status`, `type`, `title`, `detail`, `code`, `errors` (a list of
`{param, message}`), `request_id`, `headers` and `body`; `str(err)` is `"<status> <code>: <detail>"`.
Network failures raise `APIConnectionError`, and timeouts raise its subclass `APITimeoutError`.

```python
import propraven

try:
    client.deals.absentee(county_fips="37119", limit=0)
except propraven.BadRequestError as err:
    print(err.code, err.errors)  # invalid_parameter [{'param': 'limit', 'message': ...}]
except propraven.RateLimitError as err:
    print("retry in", err.retry_after)
except propraven.APIError as err:
    print(err.status, err.detail, err.request_id)
```

The SDK never signs x402 payments; a paid resource without payment raises `PaymentRequiredError`.

## Retries

Requests are retried up to `max_retries` times (default 2) on network errors and timeouts and on
429, 503 and 504 for every HTTP method. Other 5xx responses are retried only for GET, HEAD, DELETE
and OPTIONS. Other 4xx responses are never retried, 402 included.

The wait is `Retry-After` (seconds or an HTTP date) when present. Without it, the client waits until
`X-RateLimit-Reset` when `X-RateLimit-Remaining` is `0`, and otherwise backs off exponentially
(0.5 s × 2^attempt, ±25 % jitter). One wait is capped at 60 s: if the server asks for longer
(a monthly cap's `Retry-After` is measured in days), the error is raised at once.

## Pagination

Every paginated method `m` has an auto-paginating sibling `m_iter` (a generator, or an async generator
on `AsyncPropRaven`) that fetches pages on demand:

```python
for parcel in client.deals.absentee_iter(county_fips="37119", page_size=100, max_items=1000):
    ...

for hit in client.search.full_iter(q="main st", page_size=50):  # cursor-paginated
    ...
```

Offset pagination advances `offset` by the page length. It stops on a short or empty page, when
`offset >= total`, or when `has_more` is false. Cursor pagination (`search.full`) passes
`after=<nextCursor>` until `nextCursor` is null or absent, or `hasMore` is false. `page_size` is sent as
`limit`, and `max_items` caps the number of items returned.

## Webhooks

Verify deliveries with the raw request body and the `X-PropRaven-Signature` header
(`t=<unix_ms>,v1=<hex hmac-sha256>`, signed over `"<t>.<raw body>"` with your `whsec_...` secret):

```python
from propraven import WebhookVerificationError
from propraven.webhooks import verify

try:
    event = verify(raw_body, headers["X-PropRaven-Signature"], secret)  # tolerance=300 s
except WebhookVerificationError:
    return 400
print(event["type"])
```

`propraven.verify_webhook` is an alias. Multiple `v1=` signatures are accepted (secret rotation), and
signatures are compared in constant time.

## Rate-limit info

`client.last_rate_limit` holds the `X-RateLimit-Limit` / `-Remaining` / `-Reset` headers of the most
recent response as a `RateLimit(limit, remaining, reset)` (reset is a Unix epoch in seconds), or `None`
when that response had none.

## Types

Response and request shapes live in `propraven.types`, one `TypedDict` per schema in the OpenAPI spec,
plus `<Namespace><Method>Response` for every operation (`ParcelsPermitsResponse`,
`SearchParcelsResponse`, ...). They are plain dicts at runtime, so unknown keys pass through
untouched. Numeric fields are typed as numbers, and identifiers (`parcel_id`, `apn`, `county_fips`,
`state_fips`, `zip`) as strings. Responses that are CSV (`search.export`) are returned as `str`.

## Methods

<!-- BEGIN GENERATED METHODS (scripts/generate.py) -->

70 operations. Every method exists on both `PropRaven` and `AsyncPropRaven`; methods marked *iter* also have an auto-paginating `<method>_iter(...)` sibling.

| Method | HTTP | Summary |
| --- | --- | --- |
| `client.parcels.assessment_history(id)` | `GET /api/v1/parcels/{id}/assessment-history` | Get recorded annual assessment history |
| `client.parcels.get(id)` | `GET /api/v1/parcels/{id}` | Get parcel by ID |
| `client.parcels.owner(id)` | `GET /api/v1/parcels/{id}/owner` | Get parcel owner details and portfolio |
| `client.parcels.permits(id)` | `GET /api/v1/parcels/{id}/permits` | Get parcel permits |
| `client.parcels.deeds(id)` | `GET /api/v1/parcels/{id}/deeds` | Get parcel deed history |
| `client.parcels.risks(id)` | `GET /api/v1/parcels/{id}/risks` | Get parcel risk assessment |
| `client.parcels.geojson()` | `GET /api/v1/parcels/geojson` | Parcel polygons as GeoJSON for a bounding box |
| `client.parcels.report(id)` | `GET /api/v1/parcels/{id}/report` | Parcel dossier (paid, provenance-first) |
| `client.parcels.comp_pack(id)` | `GET /api/v1/parcels/{id}/comp-pack` | Comp pack (paid, priced per pack) — with a FREE preview |
| `client.parcels.risk_score(id)` | `GET /api/v1/parcels/{id}/risk-score` | Risk score (paid, priced per assessment) — with a FREE preview |
| `client.parcels.traffic_history(id)` | `GET /api/v1/parcels/{id}/traffic-history` | Nearest traffic station + AADT history |
| `client.parcels.batch()` | `POST /api/v1/parcels/batch` | Fetch up to 100 parcels by (state, county, parcel) tuple |
| `client.parcels.comps(id)` | `GET /api/v1/parcels/{id}/comps` | Comparable sales for a parcel |
| `client.parcels.occupants(id)` | `GET /api/v1/parcels/{id}/occupants` | Business occupants of a parcel |
| `client.parcels.violations(id)` | `GET /api/v1/parcels/{id}/violations` | Code violations on a parcel |
| `client.parcels.pois()` | `GET /api/v1/parcels/poi` | Business parcels in a small bounding box |
| `client.search.parcels()` (*iter*) | `POST /api/v1/search` | Search parcels |
| `client.search.autocomplete()` | `GET /api/v1/search/autocomplete` | Address / place / parcel autocomplete |
| `client.search.export()` | `GET /api/v1/search/export` | Export search results as CSV |
| `client.search.full()` (*iter*) | `GET /api/v1/search/full` | Full paginated text + attribute search |
| `client.coverage.get()` | `GET /api/v1/coverage` | Get coverage statistics |
| `client.coverage.map()` | `GET /api/v1/coverage/map` | County coverage map data |
| `client.deals.absentee()` (*iter*) | `GET /api/v1/deals/absentee` | Find absentee owners |
| `client.deals.flips()` (*iter*) | `GET /api/v1/deals/flips` | Find property flips |
| `client.deals.contractors()` (*iter*) | `GET /api/v1/deals/contractors` | Search contractors by permit activity |
| `client.deals.entities()` (*iter*) | `GET /api/v1/deals/entities` | Find entity-owned parcels (LLC, Corp, Trust, LP) |
| `client.deals.high_land_ratio()` (*iter*) | `GET /api/v1/deals/high-land-ratio` | Find parcels with high land-to-improvement ratio |
| `client.deals.lenders()` (*iter*) | `GET /api/v1/deals/lenders` | Search lender profiles |
| `client.deals.long_hold()` (*iter*) | `GET /api/v1/deals/long-hold` | Find long-held parcels (10+ years) |
| `client.deals.market()` (*iter*) | `GET /api/v1/deals/market` | County-quarter transaction summary or affordability index |
| `client.deals.portfolio_owners()` (*iter*) | `GET /api/v1/deals/portfolio-owners` | Find portfolio investors (owners of 2+ properties) |
| `client.market.counties()` (*iter*) | `GET /api/v1/market/counties` | Get county market statistics |
| `client.market.trends()` | `GET /api/v1/market/trends` | Get market trends |
| `client.market.county(fips)` | `GET /api/v1/market/counties/{fips}` | Detailed view for a single county |
| `client.market.flips()` (*iter*) | `GET /api/v1/market/flips` | Flip-activity summary grouped by county |
| `client.market.snapshot()` | `GET /api/v1/market/snapshot` | Market snapshot for a geography |
| `client.owners.search()` | `GET /api/v1/owners/search` | Search property owners |
| `client.owners.get(name)` | `GET /api/v1/owners/{name}` | Get owner profile |
| `client.owners.properties(name)` (*iter*) | `GET /api/v1/owners/{name}/properties` | Get owner's properties |
| `client.owners.portfolio(name)` | `GET /api/v1/owners/{name}/portfolio` | Get owner portfolio summary |
| `client.owners.report(name)` | `GET /api/v1/owners/{name}/report` | Owner intelligence report (paid, priced per resolution; account required) — with a free preview |
| `client.owners.transactions(name)` | `GET /api/v1/owners/{name}/transactions` | Recorded deed transactions for an owner |
| `client.owners.card()` | `GET /api/v1/owners/card` | Owner card -- the owner of record and their mailing contact (account required) |
| `client.webhooks.list()` | `GET /api/v1/webhooks` | List webhook endpoints |
| `client.webhooks.create()` | `POST /api/v1/webhooks` | Create a webhook endpoint |
| `client.webhooks.get(id)` | `GET /api/v1/webhooks/{id}` | Get a single webhook endpoint |
| `client.webhooks.delete(id)` | `DELETE /api/v1/webhooks/{id}` | Soft-disable a webhook endpoint |
| `client.webhooks.deliveries(id)` | `GET /api/v1/webhooks/{id}/deliveries` | Recent delivery attempts for a webhook |
| `client.webhooks.retry_delivery(id, delivery_id)` | `POST /api/v1/webhooks/{id}/deliveries/{deliveryId}/retry` | Re-queue a failed webhook delivery |
| `client.account.usage()` | `GET /api/v1/account/usage` | Current-period usage and quota |
| `client.storefront.catalog()` | `GET /api/v1/storefront/catalog` | Machine Storefront — sealed field catalog |
| `client.storefront.availability()` | `GET /api/v1/storefront/availability` | Machine Storefront -- try-before-buy (jurisdiction coverage or per-parcel quote) |
| `client.leads.find()` | `GET /api/v1/leads/find` | Lead feed (paid, priced per lead) — with a FREE preview |
| `client.credits.topup()` | `GET /api/v1/storefront/credits/topup` | Fund a prepaid credit balance over x402 |
| `client.credits.balance()` | `GET /api/v1/storefront/credits/balance` | Read a prepaid credit balance + ledger |
| `client.watch.list()` | `GET /api/v1/watch` | List your watches |
| `client.watch.create()` | `POST /api/v1/watch` | Create a watch (free) |
| `client.watch.poll(id)` | `GET /api/v1/watch/{id}` | Poll a watch for new changes (priced per delta) |
| `client.watch.delete(id)` | `DELETE /api/v1/watch/{id}` | Delete a watch |
| `client.verify.get()` | `GET /api/v1/verify` | Verify facts for one parcel |
| `client.verify.batch()` | `POST /api/v1/verify` | Verify facts (batch, paid per lookup) - FREE preview |
| `client.cohorts.export(id)` | `GET /api/v1/cohorts/{id}/export` | Mail-merge export of one of your lists (account required; included for subscribers, per row otherwise) |
| `client.cohorts.list()` | `GET /api/v1/cohorts` | List your saved parcel lists (cohorts) |
| `client.lookup.get()` | `GET /api/v1/lookup` | Exact parcel lookup (UUID or APN) |
| `client.lookup.batch()` | `POST /api/v1/lookup/batch` | Resolve up to 500 parcel queries in one call |
| `client.cmbs.exposure()` | `GET /api/v1/cmbs/exposure` | CMBS loan exposure for a parcel or an owner |
| `client.freshness.get()` | `GET /api/v1/freshness` | How fresh the served parcel snapshot is |
| `client.freshness.datasets()` | `GET /api/v1/freshness/datasets` | Per-dataset availability and freshness |
| `client.crime.lookup()` | `GET /api/v1/crime/lookup` | Crime score near a point |
| `client.traffic.stations()` | `GET /api/v1/traffic/stations` | Traffic count stations in a bounding box |

<!-- END GENERATED METHODS -->

## Regenerating

The typed layer (`src/propraven/types`, `src/propraven/resources`, the table above) is generated from
`openapi.json`:

```sh
curl -fsSL https://propraven.com/openapi.json -o openapi.json   # or copy a new spec in
python scripts/generate.py                                      # standard library only
python -m pytest -q
```

`python scripts/generate.py --check` fails when the generated files are stale. The
`Regenerate from OpenAPI` workflow does this daily and opens a `spec-sync` pull request when the
published spec changes.

## License

Apache-2.0
