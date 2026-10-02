# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``search`` namespace: ``client.search``."""

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Literal, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._pagination import aiterate_cursor, aiterate_offset, iterate_cursor, iterate_offset
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    """``client.search`` operations (sync)."""

    def parcels(
        self,
        *,
        bounds: Optional[_t.SearchParcelsParamsBounds] = None,
        filters: Optional[_t.SearchParcelsParamsFilters] = None,
        sort: Optional[Literal["assessed_value", "sale_price", "acreage", "year_built", "deal_score", "address", "city", "state", "owner_name", "total_assessed_value", "zoning", "lot_size_acres", "ownership_type"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.SearchParcelsResponse:
        """Search parcels

        ``POST /api/v1/search``

        Search parcels with optional geographic bounds and attribute filters. `bounds` and `filters`
        are both optional (`filters` defaults to `{}`); the body is validated and any bad member is
        a 400 naming it. `sort` applies to UNBOUNDED queries only: with `bounds`, rows come back in
        spatial-index order and the response says `sort_applied: false`. `total` is the exact number
        of matching parcels up to 10,000; beyond that it is 10,000 with `total_is_lower_bound:
        true`, and it is null if the count timed out (`total_status: "timed_out"`). Traffic-count
        columns are withheld until verified: they are returned as null with a `withhold_gate` block,
        and filters on them (minVpd, maxVpd, minVisibilityScore) are refused with 400
        `filter_withheld`.

        Args:
            bounds: Viewport in WGS84 degrees. north > south. west > east is an
                antimeridian-crossing box.
            filters: All optional; null means not set. Unknown members are a 400.
            sort: Sort field (unbounded queries only). The first five are the primary names; the
                rest are accepted column names. A legacy `{field, direction}` object is also
                accepted.
            limit: Page size. Values above 500 are clamped to 500 (the response echoes the effective
                limit).
        """
        return cast("_t.SearchParcelsResponse", self._client._request(
            "POST",
            "/api/v1/search",
            body={
                "bounds": bounds,
                "filters": filters,
                "sort": sort,
                "order": order,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def parcels_iter(
        self,
        *,
        bounds: Optional[_t.SearchParcelsParamsBounds] = None,
        filters: Optional[_t.SearchParcelsParamsFilters] = None,
        sort: Optional[Literal["assessed_value", "sale_price", "acreage", "year_built", "deal_score", "address", "city", "state", "owner_name", "total_assessed_value", "zoning", "lot_size_acres", "ownership_type"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.SearchParcelsResponseDataItem]:
        """Search parcels

        ``POST /api/v1/search``

        Search parcels with optional geographic bounds and attribute filters. `bounds` and `filters`
        are both optional (`filters` defaults to `{}`); the body is validated and any bad member is
        a 400 naming it. `sort` applies to UNBOUNDED queries only: with `bounds`, rows come back in
        spatial-index order and the response says `sort_applied: false`. `total` is the exact number
        of matching parcels up to 10,000; beyond that it is 10,000 with `total_is_lower_bound:
        true`, and it is null if the count timed out (`total_status: "timed_out"`). Traffic-count
        columns are withheld until verified: they are returned as null with a `withhold_gate` block,
        and filters on them (minVpd, maxVpd, minVisibilityScore) are refused with 400
        `filter_withheld`.

        Auto-paginating iterator over every item (``data``) of :meth:`parcels`. Pages are fetched on
        demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            bounds: Viewport in WGS84 degrees. north > south. west > east is an
                antimeridian-crossing box.
            filters: All optional; null means not set. Unknown members are a 400.
            sort: Sort field (unbounded queries only). The first five are the primary names; the
                rest are accepted column names. A legacy `{field, direction}` object is also
                accepted.
        """
        return iterate_offset(
            lambda _limit, _pos: self.parcels(bounds=bounds, filters=filters, sort=sort, order=order, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def autocomplete(
        self,
        *,
        q: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.SearchAutocompleteResponse:
        """Address / place / parcel autocomplete

        ``GET /api/v1/search/autocomplete``

        Fast prefix-matched autocomplete: returns cities/places, matching parcels, and
        Mapbox-geocoded addresses for the prefix. Three independent tiers run in parallel with
        per-tier timeouts so a slow DB query never blocks fast Mapbox results. Use for type-ahead
        UIs and address entry; for full-detail lookup use parcel lookup.

        Args:
            q: Search prefix. Minimum 2 chars.
        """
        return cast("_t.SearchAutocompleteResponse", self._client._request(
            "GET",
            "/api/v1/search/autocomplete",
            query={
                "q": q,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def export(
        self,
        *,
        north: Optional[float] = None,
        south: Optional[float] = None,
        east: Optional[float] = None,
        west: Optional[float] = None,
        zoningCategories: Optional[str] = None,
        sort: Optional[Literal["address", "city", "state", "owner_name", "total_assessed_value", "zoning", "year_built", "lot_size_acres", "ownership_type"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.SearchExportResponse:
        """Export search results as CSV

        ``GET /api/v1/search/export``

        Returns up to 10,000 search-matched parcels as a CSV download. Accepts the same geographic +
        attribute filters as POST /api/v1/search. Designed for spreadsheet / Excel workflows; for
        programmatic ingestion, use the JSON search endpoint and paginate.

        Args:
            north: Bounding box: north latitude.
            south: Bounding box: south latitude.
            east: Bounding box: east longitude.
            west: Bounding box: west longitude.
            zoningCategories: Comma-delimited zoning categories.
            sort: Sort column.
            order: Sort direction.
            limit: Row cap. Hard max 10,000.
        """
        return cast("_t.SearchExportResponse", self._client._request(
            "GET",
            "/api/v1/search/export",
            query={
                "north": north,
                "south": south,
                "east": east,
                "west": west,
                "zoningCategories": zoningCategories,
                "sort": sort,
                "order": order,
                "limit": limit,
            },
            accept="text/csv",
            kind="text",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def full(
        self,
        *,
        q: str,
        field: Optional[Literal["all", "address", "owner_name", "city"]] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[Literal["address", "city", "state", "owner_name", "total_value", "year_built"]] = None,
        dir: Optional[Literal["asc", "desc"]] = None,
        after: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.SearchFullResponse:
        """Full paginated text + attribute search

        ``GET /api/v1/search/full``

        Paginated search across the parcel search index by free-text query (`q`) and optional
        field/state/city filters. Distinct from POST /api/v1/search which is geo-bounded; this
        endpoint is text-anchored and works without a bounding box. Returns 50/page by default, 200
        max.

        Args:
            q: Search query. Min 2 chars.
            field: Field to match against.
            state: 2-letter state filter.
            city: City filter.
            page: 1-indexed page number.
            limit: Page size, max 200.
            sort: Sort column.
            dir: Sort direction.
            after: Opaque keyset cursor: pass the previous page's `nextCursor`. Preferred over
                `page`.
        """
        return cast("_t.SearchFullResponse", self._client._request(
            "GET",
            "/api/v1/search/full",
            query={
                "q": q,
                "field": field,
                "state": state,
                "city": city,
                "page": page,
                "limit": limit,
                "sort": sort,
                "dir": dir,
                "after": after,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def full_iter(
        self,
        *,
        q: str,
        field: Optional[Literal["all", "address", "owner_name", "city"]] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        page: Optional[int] = None,
        sort: Optional[Literal["address", "city", "state", "owner_name", "total_value", "year_built"]] = None,
        dir: Optional[Literal["asc", "desc"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.FullSearchResultResultsItem]:
        """Full paginated text + attribute search

        ``GET /api/v1/search/full``

        Paginated search across the parcel search index by free-text query (`q`) and optional
        field/state/city filters. Distinct from POST /api/v1/search which is geo-bounded; this
        endpoint is text-anchored and works without a bounding box. Returns 50/page by default, 200
        max.

        Auto-paginating iterator over every item (``results``) of :meth:`full`. Passes
        ``after=<nextCursor>`` until ``nextCursor`` is null/absent or ``hasMore`` is false.
        ``page_size`` is sent as ``limit``; ``max_items`` caps the number of items yielded.

        Args:
            q: Search query. Min 2 chars.
            field: Field to match against.
            state: 2-letter state filter.
            city: City filter.
            page: 1-indexed page number.
            sort: Sort column.
            dir: Sort direction.
        """
        return iterate_cursor(
            lambda _limit, _pos: self.full(q=q, field=field, state=state, city=city, page=page, limit=_limit, sort=sort, dir=dir, after=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="results", next_key="nextCursor", page_size=page_size, max_items=max_items,
        )


class AsyncSearchResource(AsyncAPIResource):
    """``client.search`` operations (async)."""

    async def parcels(
        self,
        *,
        bounds: Optional[_t.SearchParcelsParamsBounds] = None,
        filters: Optional[_t.SearchParcelsParamsFilters] = None,
        sort: Optional[Literal["assessed_value", "sale_price", "acreage", "year_built", "deal_score", "address", "city", "state", "owner_name", "total_assessed_value", "zoning", "lot_size_acres", "ownership_type"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.SearchParcelsResponse:
        """Search parcels

        ``POST /api/v1/search``

        Search parcels with optional geographic bounds and attribute filters. `bounds` and `filters`
        are both optional (`filters` defaults to `{}`); the body is validated and any bad member is
        a 400 naming it. `sort` applies to UNBOUNDED queries only: with `bounds`, rows come back in
        spatial-index order and the response says `sort_applied: false`. `total` is the exact number
        of matching parcels up to 10,000; beyond that it is 10,000 with `total_is_lower_bound:
        true`, and it is null if the count timed out (`total_status: "timed_out"`). Traffic-count
        columns are withheld until verified: they are returned as null with a `withhold_gate` block,
        and filters on them (minVpd, maxVpd, minVisibilityScore) are refused with 400
        `filter_withheld`.

        Args:
            bounds: Viewport in WGS84 degrees. north > south. west > east is an
                antimeridian-crossing box.
            filters: All optional; null means not set. Unknown members are a 400.
            sort: Sort field (unbounded queries only). The first five are the primary names; the
                rest are accepted column names. A legacy `{field, direction}` object is also
                accepted.
            limit: Page size. Values above 500 are clamped to 500 (the response echoes the effective
                limit).
        """
        return cast("_t.SearchParcelsResponse", await self._client._request(
            "POST",
            "/api/v1/search",
            body={
                "bounds": bounds,
                "filters": filters,
                "sort": sort,
                "order": order,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def parcels_iter(
        self,
        *,
        bounds: Optional[_t.SearchParcelsParamsBounds] = None,
        filters: Optional[_t.SearchParcelsParamsFilters] = None,
        sort: Optional[Literal["assessed_value", "sale_price", "acreage", "year_built", "deal_score", "address", "city", "state", "owner_name", "total_assessed_value", "zoning", "lot_size_acres", "ownership_type"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.SearchParcelsResponseDataItem]:
        """Search parcels

        ``POST /api/v1/search``

        Search parcels with optional geographic bounds and attribute filters. `bounds` and `filters`
        are both optional (`filters` defaults to `{}`); the body is validated and any bad member is
        a 400 naming it. `sort` applies to UNBOUNDED queries only: with `bounds`, rows come back in
        spatial-index order and the response says `sort_applied: false`. `total` is the exact number
        of matching parcels up to 10,000; beyond that it is 10,000 with `total_is_lower_bound:
        true`, and it is null if the count timed out (`total_status: "timed_out"`). Traffic-count
        columns are withheld until verified: they are returned as null with a `withhold_gate` block,
        and filters on them (minVpd, maxVpd, minVisibilityScore) are refused with 400
        `filter_withheld`.

        Auto-paginating iterator over every item (``data``) of :meth:`parcels`. Pages are fetched on
        demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            bounds: Viewport in WGS84 degrees. north > south. west > east is an
                antimeridian-crossing box.
            filters: All optional; null means not set. Unknown members are a 400.
            sort: Sort field (unbounded queries only). The first five are the primary names; the
                rest are accepted column names. A legacy `{field, direction}` object is also
                accepted.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.parcels(bounds=bounds, filters=filters, sort=sort, order=order, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def autocomplete(
        self,
        *,
        q: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.SearchAutocompleteResponse:
        """Address / place / parcel autocomplete

        ``GET /api/v1/search/autocomplete``

        Fast prefix-matched autocomplete: returns cities/places, matching parcels, and
        Mapbox-geocoded addresses for the prefix. Three independent tiers run in parallel with
        per-tier timeouts so a slow DB query never blocks fast Mapbox results. Use for type-ahead
        UIs and address entry; for full-detail lookup use parcel lookup.

        Args:
            q: Search prefix. Minimum 2 chars.
        """
        return cast("_t.SearchAutocompleteResponse", await self._client._request(
            "GET",
            "/api/v1/search/autocomplete",
            query={
                "q": q,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def export(
        self,
        *,
        north: Optional[float] = None,
        south: Optional[float] = None,
        east: Optional[float] = None,
        west: Optional[float] = None,
        zoningCategories: Optional[str] = None,
        sort: Optional[Literal["address", "city", "state", "owner_name", "total_assessed_value", "zoning", "year_built", "lot_size_acres", "ownership_type"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.SearchExportResponse:
        """Export search results as CSV

        ``GET /api/v1/search/export``

        Returns up to 10,000 search-matched parcels as a CSV download. Accepts the same geographic +
        attribute filters as POST /api/v1/search. Designed for spreadsheet / Excel workflows; for
        programmatic ingestion, use the JSON search endpoint and paginate.

        Args:
            north: Bounding box: north latitude.
            south: Bounding box: south latitude.
            east: Bounding box: east longitude.
            west: Bounding box: west longitude.
            zoningCategories: Comma-delimited zoning categories.
            sort: Sort column.
            order: Sort direction.
            limit: Row cap. Hard max 10,000.
        """
        return cast("_t.SearchExportResponse", await self._client._request(
            "GET",
            "/api/v1/search/export",
            query={
                "north": north,
                "south": south,
                "east": east,
                "west": west,
                "zoningCategories": zoningCategories,
                "sort": sort,
                "order": order,
                "limit": limit,
            },
            accept="text/csv",
            kind="text",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def full(
        self,
        *,
        q: str,
        field: Optional[Literal["all", "address", "owner_name", "city"]] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[Literal["address", "city", "state", "owner_name", "total_value", "year_built"]] = None,
        dir: Optional[Literal["asc", "desc"]] = None,
        after: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.SearchFullResponse:
        """Full paginated text + attribute search

        ``GET /api/v1/search/full``

        Paginated search across the parcel search index by free-text query (`q`) and optional
        field/state/city filters. Distinct from POST /api/v1/search which is geo-bounded; this
        endpoint is text-anchored and works without a bounding box. Returns 50/page by default, 200
        max.

        Args:
            q: Search query. Min 2 chars.
            field: Field to match against.
            state: 2-letter state filter.
            city: City filter.
            page: 1-indexed page number.
            limit: Page size, max 200.
            sort: Sort column.
            dir: Sort direction.
            after: Opaque keyset cursor: pass the previous page's `nextCursor`. Preferred over
                `page`.
        """
        return cast("_t.SearchFullResponse", await self._client._request(
            "GET",
            "/api/v1/search/full",
            query={
                "q": q,
                "field": field,
                "state": state,
                "city": city,
                "page": page,
                "limit": limit,
                "sort": sort,
                "dir": dir,
                "after": after,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def full_iter(
        self,
        *,
        q: str,
        field: Optional[Literal["all", "address", "owner_name", "city"]] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        page: Optional[int] = None,
        sort: Optional[Literal["address", "city", "state", "owner_name", "total_value", "year_built"]] = None,
        dir: Optional[Literal["asc", "desc"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.FullSearchResultResultsItem]:
        """Full paginated text + attribute search

        ``GET /api/v1/search/full``

        Paginated search across the parcel search index by free-text query (`q`) and optional
        field/state/city filters. Distinct from POST /api/v1/search which is geo-bounded; this
        endpoint is text-anchored and works without a bounding box. Returns 50/page by default, 200
        max.

        Auto-paginating iterator over every item (``results``) of :meth:`full`. Passes
        ``after=<nextCursor>`` until ``nextCursor`` is null/absent or ``hasMore`` is false.
        ``page_size`` is sent as ``limit``; ``max_items`` caps the number of items yielded.

        Args:
            q: Search query. Min 2 chars.
            field: Field to match against.
            state: 2-letter state filter.
            city: City filter.
            page: 1-indexed page number.
            sort: Sort column.
            dir: Sort direction.
        """
        async for item in aiterate_cursor(
            lambda _limit, _pos: self.full(q=q, field=field, state=state, city=city, page=page, limit=_limit, sort=sort, dir=dir, after=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="results", next_key="nextCursor", page_size=page_size, max_items=max_items,
        ):
            yield item
