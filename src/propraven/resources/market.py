# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``market`` namespace: ``client.market``."""

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Literal, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._pagination import aiterate_offset, iterate_offset
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["MarketResource", "AsyncMarketResource"]


class MarketResource(SyncAPIResource):
    """``client.market`` operations (sync)."""

    def counties(
        self,
        *,
        state_fips: Optional[str] = None,
        min_sales: Optional[int] = None,
        quarter: Optional[str] = None,
        sort: Optional[Literal["median_sale_price", "sale_count", "total_volume", "price_yoy_pct"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.MarketCountiesResponse:
        """Get county market statistics

        ``GET /api/v1/market/counties``

        Retrieve real estate market statistics aggregated at the county level, including sale
        counts, median prices, and year-over-year changes. API key optional (county aggregates, no
        person-level fields): anonymous callers are rate-limited per IP at the free tier; a present
        but invalid key is a 401; keyed calls are metered.

        Args:
            state_fips: Filter by state FIPS code.
            min_sales: Minimum number of sales in the period to include a county.
            quarter: Exact quarter, e.g. 2025Q4; any other format is a 400.
            sort: Sort column. The former spellings median_price and yoy_change are accepted as
                deprecated aliases; any other value is a 400.
            order: Sort direction (case-insensitive); any other value is a 400.
        """
        return cast("_t.MarketCountiesResponse", self._client._request(
            "GET",
            "/api/v1/market/counties",
            query={
                "state_fips": state_fips,
                "min_sales": min_sales,
                "quarter": quarter,
                "sort": sort,
                "order": order,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def counties_iter(
        self,
        *,
        state_fips: Optional[str] = None,
        min_sales: Optional[int] = None,
        quarter: Optional[str] = None,
        sort: Optional[Literal["median_sale_price", "sale_count", "total_volume", "price_yoy_pct"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.MarketCountiesResponseDataItem]:
        """Get county market statistics

        ``GET /api/v1/market/counties``

        Retrieve real estate market statistics aggregated at the county level, including sale
        counts, median prices, and year-over-year changes. API key optional (county aggregates, no
        person-level fields): anonymous callers are rate-limited per IP at the free tier; a present
        but invalid key is a 401; keyed calls are metered.

        Auto-paginating iterator over every item (``data``) of :meth:`counties`. Pages are fetched
        on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            state_fips: Filter by state FIPS code.
            min_sales: Minimum number of sales in the period to include a county.
            quarter: Exact quarter, e.g. 2025Q4; any other format is a 400.
            sort: Sort column. The former spellings median_price and yoy_change are accepted as
                deprecated aliases; any other value is a 400.
            order: Sort direction (case-insensitive); any other value is a 400.
        """
        return iterate_offset(
            lambda _limit, _pos: self.counties(state_fips=state_fips, min_sales=min_sales, quarter=quarter, sort=sort, order=order, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def trends(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.MarketTrendsResponse:
        """Get market trends

        ``GET /api/v1/market/trends``

        Retrieve quarterly time series of market metrics for one or more counties or a state.
        Requires an API key (or a signed-in session); metered.

        Args:
            county_fips: Comma-separated list of county FIPS codes.
            state_fips: State FIPS code. Used if county_fips is not provided.
        """
        return cast("_t.MarketTrendsResponse", self._client._request(
            "GET",
            "/api/v1/market/trends",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def county(
        self,
        fips: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.MarketCountyResponse:
        """Detailed view for a single county

        ``GET /api/v1/market/counties/{fips}``

        Returns the full county profile: quarterly market stats (sale count, median price, YoY
        change, days on market), affordability index by year, parcel summary (count, avg assessed
        value), and flip activity. Use for county-detail dashboards.

        Args:
            fips: 5-digit county FIPS code.
        """
        return cast("_t.MarketCountyResponse", self._client._request(
            "GET",
            "/api/v1/market/counties/{fips}",
            path_params={"fips": fips},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def flips(
        self,
        *,
        state_fips: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.MarketFlipsResponse:
        """Flip-activity summary grouped by county

        ``GET /api/v1/market/flips``

        Aggregated flip activity per county: count, average ROI, average hold days, total profit.
        Use for surfacing the hottest flip markets. Differs from /api/v1/deals/flips which returns
        the underlying transactions. Requires an API key (or a signed-in session); metered.

        Args:
            state_fips: 2-digit state FIPS filter.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.MarketFlipsResponse", self._client._request(
            "GET",
            "/api/v1/market/flips",
            query={
                "state_fips": state_fips,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def flips_iter(
        self,
        *,
        state_fips: Optional[str] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.MarketFlipsRow]:
        """Flip-activity summary grouped by county

        ``GET /api/v1/market/flips``

        Aggregated flip activity per county: count, average ROI, average hold days, total profit.
        Use for surfacing the hottest flip markets. Differs from /api/v1/deals/flips which returns
        the underlying transactions. Requires an API key (or a signed-in session); metered.

        Auto-paginating iterator over every item (``data``) of :meth:`flips`. Pages are fetched on
        demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            state_fips: 2-digit state FIPS filter.
        """
        return iterate_offset(
            lambda _limit, _pos: self.flips(state_fips=state_fips, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def snapshot(
        self,
        *,
        county_fips: Optional[str] = None,
        tract: Optional[str] = None,
        cbsa: Optional[str] = None,
        zip: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.MarketSnapshotResponse:
        """Market snapshot for a geography

        ``GET /api/v1/market/snapshot``

        Demographics, economy, housing, lending, hazard and market context for exactly one
        geography: a county, census tract, CBSA or ZIP.

        Args:
            county_fips: 5-digit county FIPS.
            tract: 11-digit census tract GEOID.
            cbsa: CBSA code.
            zip: 5-digit ZIP.
        """
        return cast("_t.MarketSnapshotResponse", self._client._request(
            "GET",
            "/api/v1/market/snapshot",
            query={
                "county_fips": county_fips,
                "tract": tract,
                "cbsa": cbsa,
                "zip": zip,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncMarketResource(AsyncAPIResource):
    """``client.market`` operations (async)."""

    async def counties(
        self,
        *,
        state_fips: Optional[str] = None,
        min_sales: Optional[int] = None,
        quarter: Optional[str] = None,
        sort: Optional[Literal["median_sale_price", "sale_count", "total_volume", "price_yoy_pct"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.MarketCountiesResponse:
        """Get county market statistics

        ``GET /api/v1/market/counties``

        Retrieve real estate market statistics aggregated at the county level, including sale
        counts, median prices, and year-over-year changes. API key optional (county aggregates, no
        person-level fields): anonymous callers are rate-limited per IP at the free tier; a present
        but invalid key is a 401; keyed calls are metered.

        Args:
            state_fips: Filter by state FIPS code.
            min_sales: Minimum number of sales in the period to include a county.
            quarter: Exact quarter, e.g. 2025Q4; any other format is a 400.
            sort: Sort column. The former spellings median_price and yoy_change are accepted as
                deprecated aliases; any other value is a 400.
            order: Sort direction (case-insensitive); any other value is a 400.
        """
        return cast("_t.MarketCountiesResponse", await self._client._request(
            "GET",
            "/api/v1/market/counties",
            query={
                "state_fips": state_fips,
                "min_sales": min_sales,
                "quarter": quarter,
                "sort": sort,
                "order": order,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def counties_iter(
        self,
        *,
        state_fips: Optional[str] = None,
        min_sales: Optional[int] = None,
        quarter: Optional[str] = None,
        sort: Optional[Literal["median_sale_price", "sale_count", "total_volume", "price_yoy_pct"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.MarketCountiesResponseDataItem]:
        """Get county market statistics

        ``GET /api/v1/market/counties``

        Retrieve real estate market statistics aggregated at the county level, including sale
        counts, median prices, and year-over-year changes. API key optional (county aggregates, no
        person-level fields): anonymous callers are rate-limited per IP at the free tier; a present
        but invalid key is a 401; keyed calls are metered.

        Auto-paginating iterator over every item (``data``) of :meth:`counties`. Pages are fetched
        on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            state_fips: Filter by state FIPS code.
            min_sales: Minimum number of sales in the period to include a county.
            quarter: Exact quarter, e.g. 2025Q4; any other format is a 400.
            sort: Sort column. The former spellings median_price and yoy_change are accepted as
                deprecated aliases; any other value is a 400.
            order: Sort direction (case-insensitive); any other value is a 400.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.counties(state_fips=state_fips, min_sales=min_sales, quarter=quarter, sort=sort, order=order, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def trends(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.MarketTrendsResponse:
        """Get market trends

        ``GET /api/v1/market/trends``

        Retrieve quarterly time series of market metrics for one or more counties or a state.
        Requires an API key (or a signed-in session); metered.

        Args:
            county_fips: Comma-separated list of county FIPS codes.
            state_fips: State FIPS code. Used if county_fips is not provided.
        """
        return cast("_t.MarketTrendsResponse", await self._client._request(
            "GET",
            "/api/v1/market/trends",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def county(
        self,
        fips: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.MarketCountyResponse:
        """Detailed view for a single county

        ``GET /api/v1/market/counties/{fips}``

        Returns the full county profile: quarterly market stats (sale count, median price, YoY
        change, days on market), affordability index by year, parcel summary (count, avg assessed
        value), and flip activity. Use for county-detail dashboards.

        Args:
            fips: 5-digit county FIPS code.
        """
        return cast("_t.MarketCountyResponse", await self._client._request(
            "GET",
            "/api/v1/market/counties/{fips}",
            path_params={"fips": fips},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def flips(
        self,
        *,
        state_fips: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.MarketFlipsResponse:
        """Flip-activity summary grouped by county

        ``GET /api/v1/market/flips``

        Aggregated flip activity per county: count, average ROI, average hold days, total profit.
        Use for surfacing the hottest flip markets. Differs from /api/v1/deals/flips which returns
        the underlying transactions. Requires an API key (or a signed-in session); metered.

        Args:
            state_fips: 2-digit state FIPS filter.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.MarketFlipsResponse", await self._client._request(
            "GET",
            "/api/v1/market/flips",
            query={
                "state_fips": state_fips,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def flips_iter(
        self,
        *,
        state_fips: Optional[str] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.MarketFlipsRow]:
        """Flip-activity summary grouped by county

        ``GET /api/v1/market/flips``

        Aggregated flip activity per county: count, average ROI, average hold days, total profit.
        Use for surfacing the hottest flip markets. Differs from /api/v1/deals/flips which returns
        the underlying transactions. Requires an API key (or a signed-in session); metered.

        Auto-paginating iterator over every item (``data``) of :meth:`flips`. Pages are fetched on
        demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            state_fips: 2-digit state FIPS filter.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.flips(state_fips=state_fips, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def snapshot(
        self,
        *,
        county_fips: Optional[str] = None,
        tract: Optional[str] = None,
        cbsa: Optional[str] = None,
        zip: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.MarketSnapshotResponse:
        """Market snapshot for a geography

        ``GET /api/v1/market/snapshot``

        Demographics, economy, housing, lending, hazard and market context for exactly one
        geography: a county, census tract, CBSA or ZIP.

        Args:
            county_fips: 5-digit county FIPS.
            tract: 11-digit census tract GEOID.
            cbsa: CBSA code.
            zip: 5-digit ZIP.
        """
        return cast("_t.MarketSnapshotResponse", await self._client._request(
            "GET",
            "/api/v1/market/snapshot",
            query={
                "county_fips": county_fips,
                "tract": tract,
                "cbsa": cbsa,
                "zip": zip,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
