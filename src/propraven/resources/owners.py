# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``owners`` namespace: ``client.owners``."""

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._pagination import aiterate_offset, iterate_offset
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["OwnersResource", "AsyncOwnersResource"]


class OwnersResource(SyncAPIResource):
    """``client.owners`` operations (sync)."""

    def search(
        self,
        *,
        q: str,
        min_properties: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersSearchResponse:
        """Search property owners

        ``GET /api/v1/owners/search``

        Search for property owners by name. Returns owner profiles with property counts and
        portfolio values.

        Args:
            q: Search query for owner name.
            min_properties: Minimum number of properties owned.
        """
        return cast("_t.OwnersSearchResponse", self._client._request(
            "GET",
            "/api/v1/owners/search",
            query={
                "q": q,
                "min_properties": min_properties,
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def get(
        self,
        name: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersGetResponse:
        """Get owner profile

        ``GET /api/v1/owners/{name}``

        Retrieve a specific owner profile by name, including property count, total assessed value,
        entity type, and states.

        Args:
            name: Owner name (URL-encoded).
        """
        return cast("_t.OwnersGetResponse", self._client._request(
            "GET",
            "/api/v1/owners/{name}",
            path_params={"name": name},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def properties(
        self,
        name: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersPropertiesResponse:
        """Get owner's properties

        ``GET /api/v1/owners/{name}/properties``

        Retrieve the list of properties owned by a specific owner.

        Args:
            name: Owner name (URL-encoded).
        """
        return cast("_t.OwnersPropertiesResponse", self._client._request(
            "GET",
            "/api/v1/owners/{name}/properties",
            path_params={"name": name},
            query={
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def properties_iter(
        self,
        name: str,
        *,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.OwnersPropertiesResponseDataItem]:
        """Get owner's properties

        ``GET /api/v1/owners/{name}/properties``

        Retrieve the list of properties owned by a specific owner.

        Auto-paginating iterator over every item (``data``) of :meth:`properties`. Pages are fetched
        on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            name: Owner name (URL-encoded).
        """
        return iterate_offset(
            lambda _limit, _pos: self.properties(name, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def portfolio(
        self,
        name: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersPortfolioResponse:
        """Get owner portfolio summary

        ``GET /api/v1/owners/{name}/portfolio``

        Retrieve an owner's portfolio with aggregated summary statistics and property breakdown.

        Args:
            name: Owner name (URL-encoded).
        """
        return cast("_t.OwnersPortfolioResponse", self._client._request(
            "GET",
            "/api/v1/owners/{name}/portfolio",
            path_params={"name": name},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def report(
        self,
        name: str,
        *,
        ticker: Optional[str] = None,
        state: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        preview: Optional[bool] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersReportResponse:
        """Owner intelligence report (paid, priced per resolution; account required) — with a free
        preview

        ``GET /api/v1/owners/{name}/report``

        The Machine Storefront's owner intelligence report: every parcel nationwide whose
        OWNER-OF-RECORD name matches one owner NAME's realistic spellings (or a public company
        TICKER's hand-curated entity list), deduped nationally and priced PER RESOLUTION.

        ACCOUNT REQUIRED (every mode, including the free preview): an API key (`Authorization:
        Bearer pz_...`) or a signed-in session. Payment alone (an x402 `X-PAYMENT` header or a
        prepaid `X-CREDIT-TOKEN`) is not an account. An anonymous call is refused with HTTP 401,
        `code: "account_required"`, `reason: "owner_lookup_requires_account"`, before any read,
        payment verification or credit debit.

        MATCHING is spelling matching, NOT a verified corporate or beneficial-ownership link:
        different owners can share a spelling and some of one owner's spellings can be missed. Every
        property carries `match_basis` (exact_spelling = the record's owner name is the requested
        name after case/punctuation/whitespace normalization; variant = matched only through an
        expanded suffix/hyphen/N.A. spelling; ticker_curated = on the hand-curated ticker list) and
        `match_confidence: "candidate"`. The report carries: owner {query_name, ticker, entity_type,
        resolved_variants, match}, summary {count, total_assessed_value, total_acreage, states,
        by_state[]}, properties[] (each with match_basis, canonical_id, address, valuation,
        lot/building, last sale, property_type), and provenance {as_of, source}.

        PRICE: per resolution = clamp($1.75 x P(portfolio size) x V(portfolio value), $0.25, $20). P
        is log-scaled on the distinct parcel count the match uncovers (the dominant axis); V is
        log-scaled on the summed assessed value; a missing value floors V rather than raising the
        price. A match that uncovers zero parcels is returned free and never charged. The exact
        price is advertised in the 402's accepts[0].maxAmountRequired (USDC atomic units, 6
        decimals).

        FREE PREVIEW: add preview=true for the summary (count, total value, states spanned, entity
        type), the exact price, and up to three MASKED sample properties (APN truncated to
        state:county, house number stripped). No payment; an account is still required.

        PAID ACCESS (preview omitted), for an authenticated account, requires ONE of: (a) x402
        pay-per-call — send a base64 signed x402 PaymentPayload in the `X-PAYMENT` header alongside
        your credentials; on a successful build the full portfolio is returned and the on-chain
        settlement receipt is in the `X-PAYMENT-RESPONSE` response header. (b) A prepaid
        `X-CREDIT-TOKEN` balance. (c) A genuine PAID PropRaven subscription entitlement (owner
        reports are included). Being merely authenticated is NOT sufficient. (d) Anything else ->
        HTTP 402 whose `accepts` array carries the exact payment requirements for this resolution.

        Args:
            name: Owner / entity name to resolve (URL-encoded).
            ticker: Optional public stock ticker; when it is on PropRaven's hand-curated list, that
                entity list is matched instead of expanding `name` (match_basis: ticker_curated —
                curated, not verified).
            state: Optional 2-letter USPS code (or 2-digit FIPS) to scope the portfolio to one
                state.
            limit: Properties per page in the paid report (the summary always covers the FULL
                portfolio).
            offset: Pagination offset into the property list.
            preview: FREE try-before-buy: the summary, the exact price and three masked sample
                properties. No payment; an account (API key or session) is still required.
            payment (``X-PAYMENT`` header): Base64-encoded x402 PaymentPayload (EIP-3009 signed).
                Present it to pay per call for the full report.
        """
        return cast("_t.OwnersReportResponse", self._client._request(
            "GET",
            "/api/v1/owners/{name}/report",
            path_params={"name": name},
            query={
                "ticker": ticker,
                "state": state,
                "limit": limit,
                "offset": offset,
                "preview": preview,
            },
            headers={"X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def transactions(
        self,
        name: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersTransactionsResponse:
        """Recorded deed transactions for an owner

        ``GET /api/v1/owners/{name}/transactions``

        Returns up to 100 most-recent deed events where the named owner is either grantor or
        grantee. Useful for building an owner's transaction timeline across their portfolio.

        Args:
            name: Owner name. URL-encoded; case-insensitive trimmed match against grantor / grantee.
        """
        return cast("_t.OwnersTransactionsResponse", self._client._request(
            "GET",
            "/api/v1/owners/{name}/transactions",
            path_params={"name": name},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def card(
        self,
        *,
        parcel_id: Optional[str] = None,
        name: Optional[str] = None,
        include_low_confidence: Optional[bool] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersCardResponse:
        """Owner card -- the owner of record and their mailing contact (account required)

        ``GET /api/v1/owners/card``

        The owner of record and how to reach them BY MAIL, for one parcel (`parcel_id`) or one owner
        name (`name`, the exact owner-of-record spelling). Returns the co-owners the same assessor
        record names (`co_owners`, `co_owner_status`: listed / none_listed / not_checked) and the
        best mailing address -- read from ONE address column family of the record, with its ZIP,
        flagged mail_ready / po_box / equals_situs, graded A-D with its source and as-of date
        (`as_of_basis`: roll_year = the record's tax year; release_vintage = the PropRaven parcel
        release that served a record with no roll year, never presented as the county's date;
        recording_date = a deed; null when there is no date) -- plus, for an owner name, the owner's
        distinct mailing addresses across up to 50 of their parcels (`parcels_citing`). `phones` are
        OWNER phones only: a building permit filed in the current owner's era published the phone
        for the owner role (the field name, the publisher, or a role column on the permit says so)
        and names the current owner; otherwise `phone_status` says none_published, or not_checked
        when the lookup could not run. `people_on_permits` separately lists applicant and contractor
        phones from the parcel's permits (role, name, permit, date, and `era`: filed in the current
        owner's era or before it); they are never the owner's phone, and a phone whose role the
        source does not state is never served. Every phone is E.164 with its extension split off and
        the published value kept verbatim (`phone_raw`). Grade-D (contradictory) addresses are
        hidden unless include_low_confidence=true.

        ACCOUNT REQUIRED: an API key, an MCP OAuth token or a signed-in session. Anonymous callers
        -- including x402 / credit-token wallets -- get HTTP 401 `code: "account_required"` before
        any read.

        LOOKUP CAP: on an account without a paid plan each card counts as ONE lookup against the
        monthly lookup cap, spent before any read (a card that is not served is refunded). At the
        cap: HTTP 402 `code: "lookup_cap_reached"` with used / limit / plan and the upgrade link.
        Each served card is recorded in PropRaven's people-data access log.

        Args:
            parcel_id: A canonical id (state:county:parcel) or a parcel UUID. Pass this OR `name`.
            name: An owner of record, exact spelling (e.g. from a parcel lookup). Pass this OR
                `parcel_id`.
            include_low_confidence: true -> also return grade-D (contradictory) addresses.
        """
        return cast("_t.OwnersCardResponse", self._client._request(
            "GET",
            "/api/v1/owners/card",
            query={
                "parcel_id": parcel_id,
                "name": name,
                "include_low_confidence": include_low_confidence,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncOwnersResource(AsyncAPIResource):
    """``client.owners`` operations (async)."""

    async def search(
        self,
        *,
        q: str,
        min_properties: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersSearchResponse:
        """Search property owners

        ``GET /api/v1/owners/search``

        Search for property owners by name. Returns owner profiles with property counts and
        portfolio values.

        Args:
            q: Search query for owner name.
            min_properties: Minimum number of properties owned.
        """
        return cast("_t.OwnersSearchResponse", await self._client._request(
            "GET",
            "/api/v1/owners/search",
            query={
                "q": q,
                "min_properties": min_properties,
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def get(
        self,
        name: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersGetResponse:
        """Get owner profile

        ``GET /api/v1/owners/{name}``

        Retrieve a specific owner profile by name, including property count, total assessed value,
        entity type, and states.

        Args:
            name: Owner name (URL-encoded).
        """
        return cast("_t.OwnersGetResponse", await self._client._request(
            "GET",
            "/api/v1/owners/{name}",
            path_params={"name": name},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def properties(
        self,
        name: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersPropertiesResponse:
        """Get owner's properties

        ``GET /api/v1/owners/{name}/properties``

        Retrieve the list of properties owned by a specific owner.

        Args:
            name: Owner name (URL-encoded).
        """
        return cast("_t.OwnersPropertiesResponse", await self._client._request(
            "GET",
            "/api/v1/owners/{name}/properties",
            path_params={"name": name},
            query={
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def properties_iter(
        self,
        name: str,
        *,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.OwnersPropertiesResponseDataItem]:
        """Get owner's properties

        ``GET /api/v1/owners/{name}/properties``

        Retrieve the list of properties owned by a specific owner.

        Auto-paginating iterator over every item (``data``) of :meth:`properties`. Pages are fetched
        on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            name: Owner name (URL-encoded).
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.properties(name, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def portfolio(
        self,
        name: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersPortfolioResponse:
        """Get owner portfolio summary

        ``GET /api/v1/owners/{name}/portfolio``

        Retrieve an owner's portfolio with aggregated summary statistics and property breakdown.

        Args:
            name: Owner name (URL-encoded).
        """
        return cast("_t.OwnersPortfolioResponse", await self._client._request(
            "GET",
            "/api/v1/owners/{name}/portfolio",
            path_params={"name": name},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def report(
        self,
        name: str,
        *,
        ticker: Optional[str] = None,
        state: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        preview: Optional[bool] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersReportResponse:
        """Owner intelligence report (paid, priced per resolution; account required) — with a free
        preview

        ``GET /api/v1/owners/{name}/report``

        The Machine Storefront's owner intelligence report: every parcel nationwide whose
        OWNER-OF-RECORD name matches one owner NAME's realistic spellings (or a public company
        TICKER's hand-curated entity list), deduped nationally and priced PER RESOLUTION.

        ACCOUNT REQUIRED (every mode, including the free preview): an API key (`Authorization:
        Bearer pz_...`) or a signed-in session. Payment alone (an x402 `X-PAYMENT` header or a
        prepaid `X-CREDIT-TOKEN`) is not an account. An anonymous call is refused with HTTP 401,
        `code: "account_required"`, `reason: "owner_lookup_requires_account"`, before any read,
        payment verification or credit debit.

        MATCHING is spelling matching, NOT a verified corporate or beneficial-ownership link:
        different owners can share a spelling and some of one owner's spellings can be missed. Every
        property carries `match_basis` (exact_spelling = the record's owner name is the requested
        name after case/punctuation/whitespace normalization; variant = matched only through an
        expanded suffix/hyphen/N.A. spelling; ticker_curated = on the hand-curated ticker list) and
        `match_confidence: "candidate"`. The report carries: owner {query_name, ticker, entity_type,
        resolved_variants, match}, summary {count, total_assessed_value, total_acreage, states,
        by_state[]}, properties[] (each with match_basis, canonical_id, address, valuation,
        lot/building, last sale, property_type), and provenance {as_of, source}.

        PRICE: per resolution = clamp($1.75 x P(portfolio size) x V(portfolio value), $0.25, $20). P
        is log-scaled on the distinct parcel count the match uncovers (the dominant axis); V is
        log-scaled on the summed assessed value; a missing value floors V rather than raising the
        price. A match that uncovers zero parcels is returned free and never charged. The exact
        price is advertised in the 402's accepts[0].maxAmountRequired (USDC atomic units, 6
        decimals).

        FREE PREVIEW: add preview=true for the summary (count, total value, states spanned, entity
        type), the exact price, and up to three MASKED sample properties (APN truncated to
        state:county, house number stripped). No payment; an account is still required.

        PAID ACCESS (preview omitted), for an authenticated account, requires ONE of: (a) x402
        pay-per-call — send a base64 signed x402 PaymentPayload in the `X-PAYMENT` header alongside
        your credentials; on a successful build the full portfolio is returned and the on-chain
        settlement receipt is in the `X-PAYMENT-RESPONSE` response header. (b) A prepaid
        `X-CREDIT-TOKEN` balance. (c) A genuine PAID PropRaven subscription entitlement (owner
        reports are included). Being merely authenticated is NOT sufficient. (d) Anything else ->
        HTTP 402 whose `accepts` array carries the exact payment requirements for this resolution.

        Args:
            name: Owner / entity name to resolve (URL-encoded).
            ticker: Optional public stock ticker; when it is on PropRaven's hand-curated list, that
                entity list is matched instead of expanding `name` (match_basis: ticker_curated —
                curated, not verified).
            state: Optional 2-letter USPS code (or 2-digit FIPS) to scope the portfolio to one
                state.
            limit: Properties per page in the paid report (the summary always covers the FULL
                portfolio).
            offset: Pagination offset into the property list.
            preview: FREE try-before-buy: the summary, the exact price and three masked sample
                properties. No payment; an account (API key or session) is still required.
            payment (``X-PAYMENT`` header): Base64-encoded x402 PaymentPayload (EIP-3009 signed).
                Present it to pay per call for the full report.
        """
        return cast("_t.OwnersReportResponse", await self._client._request(
            "GET",
            "/api/v1/owners/{name}/report",
            path_params={"name": name},
            query={
                "ticker": ticker,
                "state": state,
                "limit": limit,
                "offset": offset,
                "preview": preview,
            },
            headers={"X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def transactions(
        self,
        name: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersTransactionsResponse:
        """Recorded deed transactions for an owner

        ``GET /api/v1/owners/{name}/transactions``

        Returns up to 100 most-recent deed events where the named owner is either grantor or
        grantee. Useful for building an owner's transaction timeline across their portfolio.

        Args:
            name: Owner name. URL-encoded; case-insensitive trimmed match against grantor / grantee.
        """
        return cast("_t.OwnersTransactionsResponse", await self._client._request(
            "GET",
            "/api/v1/owners/{name}/transactions",
            path_params={"name": name},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def card(
        self,
        *,
        parcel_id: Optional[str] = None,
        name: Optional[str] = None,
        include_low_confidence: Optional[bool] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.OwnersCardResponse:
        """Owner card -- the owner of record and their mailing contact (account required)

        ``GET /api/v1/owners/card``

        The owner of record and how to reach them BY MAIL, for one parcel (`parcel_id`) or one owner
        name (`name`, the exact owner-of-record spelling). Returns the co-owners the same assessor
        record names (`co_owners`, `co_owner_status`: listed / none_listed / not_checked) and the
        best mailing address -- read from ONE address column family of the record, with its ZIP,
        flagged mail_ready / po_box / equals_situs, graded A-D with its source and as-of date
        (`as_of_basis`: roll_year = the record's tax year; release_vintage = the PropRaven parcel
        release that served a record with no roll year, never presented as the county's date;
        recording_date = a deed; null when there is no date) -- plus, for an owner name, the owner's
        distinct mailing addresses across up to 50 of their parcels (`parcels_citing`). `phones` are
        OWNER phones only: a building permit filed in the current owner's era published the phone
        for the owner role (the field name, the publisher, or a role column on the permit says so)
        and names the current owner; otherwise `phone_status` says none_published, or not_checked
        when the lookup could not run. `people_on_permits` separately lists applicant and contractor
        phones from the parcel's permits (role, name, permit, date, and `era`: filed in the current
        owner's era or before it); they are never the owner's phone, and a phone whose role the
        source does not state is never served. Every phone is E.164 with its extension split off and
        the published value kept verbatim (`phone_raw`). Grade-D (contradictory) addresses are
        hidden unless include_low_confidence=true.

        ACCOUNT REQUIRED: an API key, an MCP OAuth token or a signed-in session. Anonymous callers
        -- including x402 / credit-token wallets -- get HTTP 401 `code: "account_required"` before
        any read.

        LOOKUP CAP: on an account without a paid plan each card counts as ONE lookup against the
        monthly lookup cap, spent before any read (a card that is not served is refunded). At the
        cap: HTTP 402 `code: "lookup_cap_reached"` with used / limit / plan and the upgrade link.
        Each served card is recorded in PropRaven's people-data access log.

        Args:
            parcel_id: A canonical id (state:county:parcel) or a parcel UUID. Pass this OR `name`.
            name: An owner of record, exact spelling (e.g. from a parcel lookup). Pass this OR
                `parcel_id`.
            include_low_confidence: true -> also return grade-D (contradictory) addresses.
        """
        return cast("_t.OwnersCardResponse", await self._client._request(
            "GET",
            "/api/v1/owners/card",
            query={
                "parcel_id": parcel_id,
                "name": name,
                "include_low_confidence": include_low_confidence,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
