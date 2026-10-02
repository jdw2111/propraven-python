# Changelog

## 0.2.0 (2026-10-02)

A rewrite. The Stainless-generated 0.1.0 client is replaced with a small hand-written core
(transport, retries, errors, pagination, webhooks) and a typed layer generated in-repo from
`openapi.json` by `scripts/generate.py`. The SDK now covers all 69 operations of API v1.2.0, up from
37.

### Breaking changes

- **Client name and namespaces.** The client is `PropRaven` / `AsyncPropRaven`. `Propraven` /
  `AsyncPropraven` remain as aliases. The `client.v1.` prefix is gone: namespaces hang directly off
  the client (`client.parcels`, `client.deals`, ...), and method names follow the API's
  `x-sdk-method` names. See the migration table below.
- **Responses are `TypedDict`s, not pydantic models.** Results are plain `dict`s with full type
  hints. Use `parcel["address"]` or `parcel.get("address")` instead of `parcel.address`. pydantic,
  anyio, distro, sniffio and typing-extensions are no longer dependencies; `httpx` is the only one.
- **Numbers are numbers.** Numeric fields are typed as `float` / `int`, matching the API, which now
  emits JSON numbers. Identifiers (`parcel_id`, `apn`, `county_fips`, `state_fips`, `zip`) stay strings.
- **Errors follow RFC 7807.** `APIError` (`APIStatusError` is an alias) exposes `status`, `type`,
  `title`, `detail`, `code`, `errors`, `request_id`, `headers` and `body`, and its message is
  `"<status> <code>: <detail>"`. New status classes: `PaymentRequiredError` (402, with x402
  `accepts`), `MethodNotAllowedError` (405), `PayloadTooLargeError` (413),
  `ServiceUnavailableError` (503) and `GatewayTimeoutError` (504). `RateLimitError` carries
  `retry_after`. The base class is `PropRavenError`.
- **Retry policy.** 429, 503 and 504 are retried for every method (honouring `Retry-After`, then
  `X-RateLimit-Reset`); other 5xx only for GET/HEAD/DELETE/OPTIONS; 402 and other 4xx never. A
  requested wait longer than 60 s raises instead of sleeping.
- **Call style.** Path parameters are positional; every other parameter (query, header, JSON body)
  is a keyword argument with its wire name. Header parameters have friendly names
  (`X-CREDIT-TOKEN` -> `credit_token`, `X-PAYMENT` -> `payment`). `extra_headers`,
  `extra_query`, `extra_body`, `timeout` and `max_retries` are accepted per call. The Stainless
  `with_raw_response` / `with_streaming_response` wrappers and the
  aiohttp extra are gone.
- **Python 3.9+, typed (`py.typed`).** Default timeout is 60 s; default base URL is
  `https://propraven.com` (override with `base_url` or `PROPRAVEN_BASE_URL`).

### Added

- 32 operations that 0.1.0 lacked, including lookup, batch lookups, comps, occupants, violations, POIs,
  market snapshot, CMBS exposure, freshness, crime, traffic, storefront, leads, credits, watch,
  verify, cohorts, owner cards and webhook delivery retry.
- Auto-pagination: every paginated method `m` has `m_iter(...)` (sync generator / async generator),
  with `page_size` and `max_items`. Offset and cursor (`search.full`) styles are both supported.
- Webhook verification: `propraven.webhooks.verify(payload, signature, secret, tolerance=300)`
  (alias `propraven.verify_webhook`), raising `WebhookVerificationError`.
- `client.last_rate_limit` (`RateLimit(limit, remaining, reset)`) and `client.request(...)` for calling
  any endpoint directly.
- A warning when an API key does not start with `pz_`.
- `scripts/generate.py` (standard library only, deterministic) plus a daily `Regenerate from OpenAPI`
  workflow that opens a `spec-sync` PR when the published spec changes.

### Migration table

| 0.1.0 | 0.2.0 |
| --- | --- |
| `client.v1.retrieve_coverage` | `client.coverage.get` |
| `client.v1.parcels.retrieve` | `client.parcels.get` |
| `client.v1.parcels.retrieve_deeds` | `client.parcels.deeds` |
| `client.v1.parcels.retrieve_geojson` | `client.parcels.geojson` |
| `client.v1.parcels.retrieve_owner` | `client.parcels.owner` |
| `client.v1.parcels.retrieve_permits` | `client.parcels.permits` |
| `client.v1.parcels.retrieve_report` | `client.parcels.report` |
| `client.v1.parcels.retrieve_risks` | `client.parcels.risks` |
| `client.v1.parcels.retrieve_traffic_history` | `client.parcels.traffic_history` |
| `client.v1.search.autocomplete` | `client.search.autocomplete` |
| `client.v1.search.export_results` | `client.search.export` |
| `client.v1.search.full_search` | `client.search.full` |
| `client.v1.search.parcel_search` | `client.search.parcels` |
| `client.v1.deals.find_absentee_owners` | `client.deals.absentee` |
| `client.v1.deals.find_entity_owned_parcels` | `client.deals.entities` |
| `client.v1.deals.find_flips` | `client.deals.flips` |
| `client.v1.deals.find_high_land_ratio` | `client.deals.high_land_ratio` |
| `client.v1.deals.find_long_hold_parcels` | `client.deals.long_hold` |
| `client.v1.deals.find_portfolio_owners` | `client.deals.portfolio_owners` |
| `client.v1.deals.retrieve_market_summary` | `client.deals.market` |
| `client.v1.deals.search_contractors` | `client.deals.contractors` |
| `client.v1.deals.search_lenders` | `client.deals.lenders` |
| `client.v1.market.retrieve_flip_activity` | `client.market.flips` |
| `client.v1.market.retrieve_trends` | `client.market.trends` |
| `client.v1.market.counties.retrieve_detail` | `client.market.county` |
| `client.v1.market.counties.retrieve_statistics` | `client.market.counties` |
| `client.v1.owners.retrieve_portfolio_summary` | `client.owners.portfolio` |
| `client.v1.owners.retrieve_profile` | `client.owners.get` |
| `client.v1.owners.retrieve_properties` | `client.owners.properties` |
| `client.v1.owners.retrieve_transactions` | `client.owners.transactions` |
| `client.v1.owners.search_owners` | `client.owners.search` |
| `client.v1.webhooks.create_endpoint` | `client.webhooks.create` |
| `client.v1.webhooks.disable_endpoint` | `client.webhooks.delete` |
| `client.v1.webhooks.list_endpoints` | `client.webhooks.list` |
| `client.v1.webhooks.retrieve_deliveries` | `client.webhooks.deliveries` |
| `client.v1.webhooks.retrieve_endpoint` | `client.webhooks.get` |
| `client.v1.account.retrieve_usage` | `client.account.usage` |

## 0.1.0 (2026-05-16)

Initial Stainless-generated release (37 endpoints under `client.v1`).
