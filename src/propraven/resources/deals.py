# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``deals`` namespace: ``client.deals``."""

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Literal, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._pagination import aiterate_offset, iterate_offset
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["DealsResource", "AsyncDealsResource"]


class DealsResource(SyncAPIResource):
    """``client.deals`` operations (sync)."""

    def absentee(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_value: Optional[float] = None,
        out_of_state: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsAbsenteeResponse:
        """Find absentee owners

        ``GET /api/v1/deals/absentee``

        Retrieve parcels owned by absentee owners, useful for off-market deal sourcing.

        Args:
            county_fips: Filter by county FIPS code.
            state_fips: Filter by state FIPS code.
            min_value: Minimum assessed value.
            out_of_state: Only return owners whose mailing address is in a different state.
        """
        return cast("_t.DealsAbsenteeResponse", self._client._request(
            "GET",
            "/api/v1/deals/absentee",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
                "min_value": min_value,
                "out_of_state": out_of_state,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def absentee_iter(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_value: Optional[float] = None,
        out_of_state: Optional[bool] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.DealsAbsenteeResponseDataItem]:
        """Find absentee owners

        ``GET /api/v1/deals/absentee``

        Retrieve parcels owned by absentee owners, useful for off-market deal sourcing.

        Auto-paginating iterator over every item (``data``) of :meth:`absentee`. Pages are fetched
        on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            county_fips: Filter by county FIPS code.
            state_fips: Filter by state FIPS code.
            min_value: Minimum assessed value.
            out_of_state: Only return owners whose mailing address is in a different state.
        """
        return iterate_offset(
            lambda _limit, _pos: self.absentee(county_fips=county_fips, state_fips=state_fips, min_value=min_value, out_of_state=out_of_state, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def flips(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        flip_tier: Optional[Literal["QUICK_FLIP", "SHORT_HOLD", "MEDIUM_HOLD"]] = None,
        min_profit: Optional[float] = None,
        view: Optional[Literal["flippers"]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsFlipsResponse:
        """Find property flips

        ``GET /api/v1/deals/flips``

        Retrieve recently flipped properties. Use ?view=flippers to get a ranked list of top
        flippers instead.

        Args:
            county_fips: Filter by county FIPS code.
            state_fips: Filter by state FIPS code.
            flip_tier: Filter by hold time between the two sales: QUICK_FLIP (< 180 days),
                SHORT_HOLD (180–364 days), MEDIUM_HOLD (365 days to 24 months). Case-insensitive.
                The former spellings quick / standard / long are accepted as deprecated aliases. Any
                other value is a 400.
            min_profit: Minimum estimated profit.
            view: Set to 'flippers' to return a ranked list of top flippers instead of individual
                flips.
        """
        return cast("_t.DealsFlipsResponse", self._client._request(
            "GET",
            "/api/v1/deals/flips",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
                "flip_tier": flip_tier,
                "min_profit": min_profit,
                "view": view,
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
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        flip_tier: Optional[Literal["QUICK_FLIP", "SHORT_HOLD", "MEDIUM_HOLD"]] = None,
        min_profit: Optional[float] = None,
        view: Optional[Literal["flippers"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.DealsFlipsResponseDataItem]:
        """Find property flips

        ``GET /api/v1/deals/flips``

        Retrieve recently flipped properties. Use ?view=flippers to get a ranked list of top
        flippers instead.

        Auto-paginating iterator over every item (``data``) of :meth:`flips`. Pages are fetched on
        demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            county_fips: Filter by county FIPS code.
            state_fips: Filter by state FIPS code.
            flip_tier: Filter by hold time between the two sales: QUICK_FLIP (< 180 days),
                SHORT_HOLD (180–364 days), MEDIUM_HOLD (365 days to 24 months). Case-insensitive.
                The former spellings quick / standard / long are accepted as deprecated aliases. Any
                other value is a 400.
            min_profit: Minimum estimated profit.
            view: Set to 'flippers' to return a ranked list of top flippers instead of individual
                flips.
        """
        return iterate_offset(
            lambda _limit, _pos: self.flips(county_fips=county_fips, state_fips=state_fips, flip_tier=flip_tier, min_profit=min_profit, view=view, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def contractors(
        self,
        *,
        search: Optional[str] = None,
        min_permits: Optional[int] = None,
        state: Optional[str] = None,
        min_value: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsContractorsResponse:
        """Search contractors by permit activity

        ``GET /api/v1/deals/contractors``

        Returns contractor profiles aggregated from 45M+ building permits. Each profile includes
        permit count, jurisdictions worked, total declared permit value, and activity dates. Use to
        identify active contractors in a market or find a specific contractor by name.

        Args:
            search: Contractor name search (case-insensitive substring).
            min_permits: Minimum permit count to include.
            state: 2-letter state filter.
            min_value: Minimum total declared permit value, USD.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsContractorsResponse", self._client._request(
            "GET",
            "/api/v1/deals/contractors",
            query={
                "search": search,
                "min_permits": min_permits,
                "state": state,
                "min_value": min_value,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def contractors_iter(
        self,
        *,
        search: Optional[str] = None,
        min_permits: Optional[int] = None,
        state: Optional[str] = None,
        min_value: Optional[int] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.Contractor]:
        """Search contractors by permit activity

        ``GET /api/v1/deals/contractors``

        Returns contractor profiles aggregated from 45M+ building permits. Each profile includes
        permit count, jurisdictions worked, total declared permit value, and activity dates. Use to
        identify active contractors in a market or find a specific contractor by name.

        Auto-paginating iterator over every item (``data``) of :meth:`contractors`. Pages are
        fetched on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset``
        until a short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number
        of items yielded.

        Args:
            search: Contractor name search (case-insensitive substring).
            min_permits: Minimum permit count to include.
            state: 2-letter state filter.
            min_value: Minimum total declared permit value, USD.
        """
        return iterate_offset(
            lambda _limit, _pos: self.contractors(search=search, min_permits=min_permits, state=state, min_value=min_value, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def entities(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        entity_type: Optional[Literal["LLC", "CORP", "TRUST", "LP", "LTD", "ASSOCIATION", "OTHER_ENTITY"]] = None,
        search: Optional[str] = None,
        min_value: Optional[int] = None,
        zoning: Optional[str] = None,
        top: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsEntitiesResponse:
        """Find entity-owned parcels (LLC, Corp, Trust, LP)

        ``GET /api/v1/deals/entities``

        Returns parcels owned by legal entities identified from owner-name pattern matching across
        221M+ parcels. Pass `top=true` to get aggregated entity rankings instead of per-parcel rows.
        One of `county_fips`, `state_fips`, `search`, or `top` is required.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            entity_type: Filter by entity classification. Case-insensitive; any other value is a
                400.
            search: Owner-name substring search.
            min_value: Minimum assessed value, USD.
            zoning: Zoning substring filter.
            top: If true, returns aggregated entity rankings with summary stats instead of
                per-parcel rows.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsEntitiesResponse", self._client._request(
            "GET",
            "/api/v1/deals/entities",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
                "entity_type": entity_type,
                "search": search,
                "min_value": min_value,
                "zoning": zoning,
                "top": top,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def entities_iter(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        entity_type: Optional[Literal["LLC", "CORP", "TRUST", "LP", "LTD", "ASSOCIATION", "OTHER_ENTITY"]] = None,
        search: Optional[str] = None,
        min_value: Optional[int] = None,
        zoning: Optional[str] = None,
        top: Optional[bool] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[Union[_t.EntityOwnedParcel, _t.EntityAggregate]]:
        """Find entity-owned parcels (LLC, Corp, Trust, LP)

        ``GET /api/v1/deals/entities``

        Returns parcels owned by legal entities identified from owner-name pattern matching across
        221M+ parcels. Pass `top=true` to get aggregated entity rankings instead of per-parcel rows.
        One of `county_fips`, `state_fips`, `search`, or `top` is required.

        Auto-paginating iterator over every item (``data``) of :meth:`entities`. Pages are fetched
        on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            entity_type: Filter by entity classification. Case-insensitive; any other value is a
                400.
            search: Owner-name substring search.
            min_value: Minimum assessed value, USD.
            zoning: Zoning substring filter.
            top: If true, returns aggregated entity rankings with summary stats instead of
                per-parcel rows.
        """
        return iterate_offset(
            lambda _limit, _pos: self.entities(county_fips=county_fips, state_fips=state_fips, entity_type=entity_type, search=search, min_value=min_value, zoning=zoning, top=top, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def high_land_ratio(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_ratio: Optional[float] = None,
        min_value: Optional[int] = None,
        zoning: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsHighLandRatioResponse:
        """Find parcels with high land-to-improvement ratio

        ``GET /api/v1/deals/high-land-ratio``

        Returns parcels where land value significantly exceeds improvement value — a signal for
        redevelopment, teardown, or assemblage opportunities. `county_fips` or `state_fips` is
        required.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            min_ratio: Minimum land/improvement ratio.
            min_value: Minimum land assessed value, USD.
            zoning: Zoning substring filter.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsHighLandRatioResponse", self._client._request(
            "GET",
            "/api/v1/deals/high-land-ratio",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
                "min_ratio": min_ratio,
                "min_value": min_value,
                "zoning": zoning,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def high_land_ratio_iter(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_ratio: Optional[float] = None,
        min_value: Optional[int] = None,
        zoning: Optional[str] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.HighLandRatioParcel]:
        """Find parcels with high land-to-improvement ratio

        ``GET /api/v1/deals/high-land-ratio``

        Returns parcels where land value significantly exceeds improvement value — a signal for
        redevelopment, teardown, or assemblage opportunities. `county_fips` or `state_fips` is
        required.

        Auto-paginating iterator over every item (``data``) of :meth:`high_land_ratio`. Pages are
        fetched on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset``
        until a short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number
        of items yielded.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            min_ratio: Minimum land/improvement ratio.
            min_value: Minimum land assessed value, USD.
            zoning: Zoning substring filter.
        """
        return iterate_offset(
            lambda _limit, _pos: self.high_land_ratio(county_fips=county_fips, state_fips=state_fips, min_ratio=min_ratio, min_value=min_value, zoning=zoning, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def lenders(
        self,
        *,
        search: Optional[str] = None,
        min_mortgages: Optional[int] = None,
        state: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsLendersResponse:
        """Search lender profiles

        ``GET /api/v1/deals/lenders``

        Returns lender profiles aggregated from deed/mortgage transactions. Includes mortgage count,
        total volume, geographic spread, and a national rank.

        Args:
            search: Lender name substring search.
            min_mortgages: Minimum mortgage count.
            state: 2-letter state filter.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsLendersResponse", self._client._request(
            "GET",
            "/api/v1/deals/lenders",
            query={
                "search": search,
                "min_mortgages": min_mortgages,
                "state": state,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def lenders_iter(
        self,
        *,
        search: Optional[str] = None,
        min_mortgages: Optional[int] = None,
        state: Optional[str] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.Lender]:
        """Search lender profiles

        ``GET /api/v1/deals/lenders``

        Returns lender profiles aggregated from deed/mortgage transactions. Includes mortgage count,
        total volume, geographic spread, and a national rank.

        Auto-paginating iterator over every item (``data``) of :meth:`lenders`. Pages are fetched on
        demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            search: Lender name substring search.
            min_mortgages: Minimum mortgage count.
            state: 2-letter state filter.
        """
        return iterate_offset(
            lambda _limit, _pos: self.lenders(search=search, min_mortgages=min_mortgages, state=state, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def long_hold(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_years: Optional[int] = None,
        hold_tier: Optional[Literal["10-15yr", "15-20yr", "20-30yr", "30yr+"]] = None,
        min_value: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsLongHoldResponse:
        """Find long-held parcels (10+ years)

        ``GET /api/v1/deals/long-hold``

        Returns parcels not sold in `min_years` or more. Long-hold owners are often motivated
        sellers — estate planning, deferred maintenance, life changes. `county_fips` or `state_fips`
        is required.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            min_years: Minimum years held.
            hold_tier: Filter by hold-period tier. Case-insensitive; any other value is a 400.
            min_value: Minimum assessed value, USD.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsLongHoldResponse", self._client._request(
            "GET",
            "/api/v1/deals/long-hold",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
                "min_years": min_years,
                "hold_tier": hold_tier,
                "min_value": min_value,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def long_hold_iter(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_years: Optional[int] = None,
        hold_tier: Optional[Literal["10-15yr", "15-20yr", "20-30yr", "30yr+"]] = None,
        min_value: Optional[int] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.LongHoldParcel]:
        """Find long-held parcels (10+ years)

        ``GET /api/v1/deals/long-hold``

        Returns parcels not sold in `min_years` or more. Long-hold owners are often motivated
        sellers — estate planning, deferred maintenance, life changes. `county_fips` or `state_fips`
        is required.

        Auto-paginating iterator over every item (``data``) of :meth:`long_hold`. Pages are fetched
        on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            min_years: Minimum years held.
            hold_tier: Filter by hold-period tier. Case-insensitive; any other value is a 400.
            min_value: Minimum assessed value, USD.
        """
        return iterate_offset(
            lambda _limit, _pos: self.long_hold(county_fips=county_fips, state_fips=state_fips, min_years=min_years, hold_tier=hold_tier, min_value=min_value, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def market(
        self,
        *,
        view: Optional[Literal["affordability"]] = None,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        year: Optional[str] = None,
        rating: Optional[Literal["AFFORDABLE", "MODERATE", "EXPENSIVE", "VERY_EXPENSIVE"]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsMarketResponse:
        """County-quarter transaction summary or affordability index

        ``GET /api/v1/deals/market``

        Default: returns county/quarter transaction summaries. Pass `view=affordability` to retrieve
        the home-affordability index instead (price-to-income ratios + rating).

        Args:
            view: Switch to the affordability-index dataset.
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            year: Year filter.
            rating: Affordability-rating filter (only meaningful with view=affordability).
                Case-insensitive; any other value is a 400.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsMarketResponse", self._client._request(
            "GET",
            "/api/v1/deals/market",
            query={
                "view": view,
                "county_fips": county_fips,
                "state_fips": state_fips,
                "year": year,
                "rating": rating,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def market_iter(
        self,
        *,
        view: Optional[Literal["affordability"]] = None,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        year: Optional[str] = None,
        rating: Optional[Literal["AFFORDABLE", "MODERATE", "EXPENSIVE", "VERY_EXPENSIVE"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[Union[_t.MarketSummary, _t.AffordabilityRow]]:
        """County-quarter transaction summary or affordability index

        ``GET /api/v1/deals/market``

        Default: returns county/quarter transaction summaries. Pass `view=affordability` to retrieve
        the home-affordability index instead (price-to-income ratios + rating).

        Auto-paginating iterator over every item (``data``) of :meth:`market`. Pages are fetched on
        demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            view: Switch to the affordability-index dataset.
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            year: Year filter.
            rating: Affordability-rating filter (only meaningful with view=affordability).
                Case-insensitive; any other value is a 400.
        """
        return iterate_offset(
            lambda _limit, _pos: self.market(view=view, county_fips=county_fips, state_fips=state_fips, year=year, rating=rating, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )

    def portfolio_owners(
        self,
        *,
        min_properties: Optional[int] = None,
        state: Optional[str] = None,
        min_value: Optional[int] = None,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsPortfolioOwnersResponse:
        """Find portfolio investors (owners of 2+ properties)

        ``GET /api/v1/deals/portfolio-owners``

        Returns portfolio owners ranked by property count and total assessed value. Useful for
        finding institutional buyers, small landlords, or specific investor families.

        Args:
            min_properties: Minimum properties owned.
            state: 2-letter owner mailing state filter.
            min_value: Minimum total portfolio assessed value, USD.
            search: Owner name substring search.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsPortfolioOwnersResponse", self._client._request(
            "GET",
            "/api/v1/deals/portfolio-owners",
            query={
                "min_properties": min_properties,
                "state": state,
                "min_value": min_value,
                "search": search,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def portfolio_owners_iter(
        self,
        *,
        min_properties: Optional[int] = None,
        state: Optional[str] = None,
        min_value: Optional[int] = None,
        search: Optional[str] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.PortfolioOwner]:
        """Find portfolio investors (owners of 2+ properties)

        ``GET /api/v1/deals/portfolio-owners``

        Returns portfolio owners ranked by property count and total assessed value. Useful for
        finding institutional buyers, small landlords, or specific investor families.

        Auto-paginating iterator over every item (``data``) of :meth:`portfolio_owners`. Pages are
        fetched on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset``
        until a short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number
        of items yielded.

        Args:
            min_properties: Minimum properties owned.
            state: 2-letter owner mailing state filter.
            min_value: Minimum total portfolio assessed value, USD.
            search: Owner name substring search.
        """
        return iterate_offset(
            lambda _limit, _pos: self.portfolio_owners(min_properties=min_properties, state=state, min_value=min_value, search=search, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        )


class AsyncDealsResource(AsyncAPIResource):
    """``client.deals`` operations (async)."""

    async def absentee(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_value: Optional[float] = None,
        out_of_state: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsAbsenteeResponse:
        """Find absentee owners

        ``GET /api/v1/deals/absentee``

        Retrieve parcels owned by absentee owners, useful for off-market deal sourcing.

        Args:
            county_fips: Filter by county FIPS code.
            state_fips: Filter by state FIPS code.
            min_value: Minimum assessed value.
            out_of_state: Only return owners whose mailing address is in a different state.
        """
        return cast("_t.DealsAbsenteeResponse", await self._client._request(
            "GET",
            "/api/v1/deals/absentee",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
                "min_value": min_value,
                "out_of_state": out_of_state,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def absentee_iter(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_value: Optional[float] = None,
        out_of_state: Optional[bool] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.DealsAbsenteeResponseDataItem]:
        """Find absentee owners

        ``GET /api/v1/deals/absentee``

        Retrieve parcels owned by absentee owners, useful for off-market deal sourcing.

        Auto-paginating iterator over every item (``data``) of :meth:`absentee`. Pages are fetched
        on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            county_fips: Filter by county FIPS code.
            state_fips: Filter by state FIPS code.
            min_value: Minimum assessed value.
            out_of_state: Only return owners whose mailing address is in a different state.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.absentee(county_fips=county_fips, state_fips=state_fips, min_value=min_value, out_of_state=out_of_state, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def flips(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        flip_tier: Optional[Literal["QUICK_FLIP", "SHORT_HOLD", "MEDIUM_HOLD"]] = None,
        min_profit: Optional[float] = None,
        view: Optional[Literal["flippers"]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsFlipsResponse:
        """Find property flips

        ``GET /api/v1/deals/flips``

        Retrieve recently flipped properties. Use ?view=flippers to get a ranked list of top
        flippers instead.

        Args:
            county_fips: Filter by county FIPS code.
            state_fips: Filter by state FIPS code.
            flip_tier: Filter by hold time between the two sales: QUICK_FLIP (< 180 days),
                SHORT_HOLD (180–364 days), MEDIUM_HOLD (365 days to 24 months). Case-insensitive.
                The former spellings quick / standard / long are accepted as deprecated aliases. Any
                other value is a 400.
            min_profit: Minimum estimated profit.
            view: Set to 'flippers' to return a ranked list of top flippers instead of individual
                flips.
        """
        return cast("_t.DealsFlipsResponse", await self._client._request(
            "GET",
            "/api/v1/deals/flips",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
                "flip_tier": flip_tier,
                "min_profit": min_profit,
                "view": view,
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
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        flip_tier: Optional[Literal["QUICK_FLIP", "SHORT_HOLD", "MEDIUM_HOLD"]] = None,
        min_profit: Optional[float] = None,
        view: Optional[Literal["flippers"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.DealsFlipsResponseDataItem]:
        """Find property flips

        ``GET /api/v1/deals/flips``

        Retrieve recently flipped properties. Use ?view=flippers to get a ranked list of top
        flippers instead.

        Auto-paginating iterator over every item (``data``) of :meth:`flips`. Pages are fetched on
        demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            county_fips: Filter by county FIPS code.
            state_fips: Filter by state FIPS code.
            flip_tier: Filter by hold time between the two sales: QUICK_FLIP (< 180 days),
                SHORT_HOLD (180–364 days), MEDIUM_HOLD (365 days to 24 months). Case-insensitive.
                The former spellings quick / standard / long are accepted as deprecated aliases. Any
                other value is a 400.
            min_profit: Minimum estimated profit.
            view: Set to 'flippers' to return a ranked list of top flippers instead of individual
                flips.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.flips(county_fips=county_fips, state_fips=state_fips, flip_tier=flip_tier, min_profit=min_profit, view=view, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def contractors(
        self,
        *,
        search: Optional[str] = None,
        min_permits: Optional[int] = None,
        state: Optional[str] = None,
        min_value: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsContractorsResponse:
        """Search contractors by permit activity

        ``GET /api/v1/deals/contractors``

        Returns contractor profiles aggregated from 45M+ building permits. Each profile includes
        permit count, jurisdictions worked, total declared permit value, and activity dates. Use to
        identify active contractors in a market or find a specific contractor by name.

        Args:
            search: Contractor name search (case-insensitive substring).
            min_permits: Minimum permit count to include.
            state: 2-letter state filter.
            min_value: Minimum total declared permit value, USD.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsContractorsResponse", await self._client._request(
            "GET",
            "/api/v1/deals/contractors",
            query={
                "search": search,
                "min_permits": min_permits,
                "state": state,
                "min_value": min_value,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def contractors_iter(
        self,
        *,
        search: Optional[str] = None,
        min_permits: Optional[int] = None,
        state: Optional[str] = None,
        min_value: Optional[int] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.Contractor]:
        """Search contractors by permit activity

        ``GET /api/v1/deals/contractors``

        Returns contractor profiles aggregated from 45M+ building permits. Each profile includes
        permit count, jurisdictions worked, total declared permit value, and activity dates. Use to
        identify active contractors in a market or find a specific contractor by name.

        Auto-paginating iterator over every item (``data``) of :meth:`contractors`. Pages are
        fetched on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset``
        until a short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number
        of items yielded.

        Args:
            search: Contractor name search (case-insensitive substring).
            min_permits: Minimum permit count to include.
            state: 2-letter state filter.
            min_value: Minimum total declared permit value, USD.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.contractors(search=search, min_permits=min_permits, state=state, min_value=min_value, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def entities(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        entity_type: Optional[Literal["LLC", "CORP", "TRUST", "LP", "LTD", "ASSOCIATION", "OTHER_ENTITY"]] = None,
        search: Optional[str] = None,
        min_value: Optional[int] = None,
        zoning: Optional[str] = None,
        top: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsEntitiesResponse:
        """Find entity-owned parcels (LLC, Corp, Trust, LP)

        ``GET /api/v1/deals/entities``

        Returns parcels owned by legal entities identified from owner-name pattern matching across
        221M+ parcels. Pass `top=true` to get aggregated entity rankings instead of per-parcel rows.
        One of `county_fips`, `state_fips`, `search`, or `top` is required.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            entity_type: Filter by entity classification. Case-insensitive; any other value is a
                400.
            search: Owner-name substring search.
            min_value: Minimum assessed value, USD.
            zoning: Zoning substring filter.
            top: If true, returns aggregated entity rankings with summary stats instead of
                per-parcel rows.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsEntitiesResponse", await self._client._request(
            "GET",
            "/api/v1/deals/entities",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
                "entity_type": entity_type,
                "search": search,
                "min_value": min_value,
                "zoning": zoning,
                "top": top,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def entities_iter(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        entity_type: Optional[Literal["LLC", "CORP", "TRUST", "LP", "LTD", "ASSOCIATION", "OTHER_ENTITY"]] = None,
        search: Optional[str] = None,
        min_value: Optional[int] = None,
        zoning: Optional[str] = None,
        top: Optional[bool] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[Union[_t.EntityOwnedParcel, _t.EntityAggregate]]:
        """Find entity-owned parcels (LLC, Corp, Trust, LP)

        ``GET /api/v1/deals/entities``

        Returns parcels owned by legal entities identified from owner-name pattern matching across
        221M+ parcels. Pass `top=true` to get aggregated entity rankings instead of per-parcel rows.
        One of `county_fips`, `state_fips`, `search`, or `top` is required.

        Auto-paginating iterator over every item (``data``) of :meth:`entities`. Pages are fetched
        on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            entity_type: Filter by entity classification. Case-insensitive; any other value is a
                400.
            search: Owner-name substring search.
            min_value: Minimum assessed value, USD.
            zoning: Zoning substring filter.
            top: If true, returns aggregated entity rankings with summary stats instead of
                per-parcel rows.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.entities(county_fips=county_fips, state_fips=state_fips, entity_type=entity_type, search=search, min_value=min_value, zoning=zoning, top=top, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def high_land_ratio(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_ratio: Optional[float] = None,
        min_value: Optional[int] = None,
        zoning: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsHighLandRatioResponse:
        """Find parcels with high land-to-improvement ratio

        ``GET /api/v1/deals/high-land-ratio``

        Returns parcels where land value significantly exceeds improvement value — a signal for
        redevelopment, teardown, or assemblage opportunities. `county_fips` or `state_fips` is
        required.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            min_ratio: Minimum land/improvement ratio.
            min_value: Minimum land assessed value, USD.
            zoning: Zoning substring filter.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsHighLandRatioResponse", await self._client._request(
            "GET",
            "/api/v1/deals/high-land-ratio",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
                "min_ratio": min_ratio,
                "min_value": min_value,
                "zoning": zoning,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def high_land_ratio_iter(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_ratio: Optional[float] = None,
        min_value: Optional[int] = None,
        zoning: Optional[str] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.HighLandRatioParcel]:
        """Find parcels with high land-to-improvement ratio

        ``GET /api/v1/deals/high-land-ratio``

        Returns parcels where land value significantly exceeds improvement value — a signal for
        redevelopment, teardown, or assemblage opportunities. `county_fips` or `state_fips` is
        required.

        Auto-paginating iterator over every item (``data``) of :meth:`high_land_ratio`. Pages are
        fetched on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset``
        until a short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number
        of items yielded.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            min_ratio: Minimum land/improvement ratio.
            min_value: Minimum land assessed value, USD.
            zoning: Zoning substring filter.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.high_land_ratio(county_fips=county_fips, state_fips=state_fips, min_ratio=min_ratio, min_value=min_value, zoning=zoning, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def lenders(
        self,
        *,
        search: Optional[str] = None,
        min_mortgages: Optional[int] = None,
        state: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsLendersResponse:
        """Search lender profiles

        ``GET /api/v1/deals/lenders``

        Returns lender profiles aggregated from deed/mortgage transactions. Includes mortgage count,
        total volume, geographic spread, and a national rank.

        Args:
            search: Lender name substring search.
            min_mortgages: Minimum mortgage count.
            state: 2-letter state filter.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsLendersResponse", await self._client._request(
            "GET",
            "/api/v1/deals/lenders",
            query={
                "search": search,
                "min_mortgages": min_mortgages,
                "state": state,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def lenders_iter(
        self,
        *,
        search: Optional[str] = None,
        min_mortgages: Optional[int] = None,
        state: Optional[str] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.Lender]:
        """Search lender profiles

        ``GET /api/v1/deals/lenders``

        Returns lender profiles aggregated from deed/mortgage transactions. Includes mortgage count,
        total volume, geographic spread, and a national rank.

        Auto-paginating iterator over every item (``data``) of :meth:`lenders`. Pages are fetched on
        demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            search: Lender name substring search.
            min_mortgages: Minimum mortgage count.
            state: 2-letter state filter.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.lenders(search=search, min_mortgages=min_mortgages, state=state, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def long_hold(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_years: Optional[int] = None,
        hold_tier: Optional[Literal["10-15yr", "15-20yr", "20-30yr", "30yr+"]] = None,
        min_value: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsLongHoldResponse:
        """Find long-held parcels (10+ years)

        ``GET /api/v1/deals/long-hold``

        Returns parcels not sold in `min_years` or more. Long-hold owners are often motivated
        sellers — estate planning, deferred maintenance, life changes. `county_fips` or `state_fips`
        is required.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            min_years: Minimum years held.
            hold_tier: Filter by hold-period tier. Case-insensitive; any other value is a 400.
            min_value: Minimum assessed value, USD.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsLongHoldResponse", await self._client._request(
            "GET",
            "/api/v1/deals/long-hold",
            query={
                "county_fips": county_fips,
                "state_fips": state_fips,
                "min_years": min_years,
                "hold_tier": hold_tier,
                "min_value": min_value,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def long_hold_iter(
        self,
        *,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        min_years: Optional[int] = None,
        hold_tier: Optional[Literal["10-15yr", "15-20yr", "20-30yr", "30yr+"]] = None,
        min_value: Optional[int] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.LongHoldParcel]:
        """Find long-held parcels (10+ years)

        ``GET /api/v1/deals/long-hold``

        Returns parcels not sold in `min_years` or more. Long-hold owners are often motivated
        sellers — estate planning, deferred maintenance, life changes. `county_fips` or `state_fips`
        is required.

        Auto-paginating iterator over every item (``data``) of :meth:`long_hold`. Pages are fetched
        on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            min_years: Minimum years held.
            hold_tier: Filter by hold-period tier. Case-insensitive; any other value is a 400.
            min_value: Minimum assessed value, USD.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.long_hold(county_fips=county_fips, state_fips=state_fips, min_years=min_years, hold_tier=hold_tier, min_value=min_value, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def market(
        self,
        *,
        view: Optional[Literal["affordability"]] = None,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        year: Optional[str] = None,
        rating: Optional[Literal["AFFORDABLE", "MODERATE", "EXPENSIVE", "VERY_EXPENSIVE"]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsMarketResponse:
        """County-quarter transaction summary or affordability index

        ``GET /api/v1/deals/market``

        Default: returns county/quarter transaction summaries. Pass `view=affordability` to retrieve
        the home-affordability index instead (price-to-income ratios + rating).

        Args:
            view: Switch to the affordability-index dataset.
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            year: Year filter.
            rating: Affordability-rating filter (only meaningful with view=affordability).
                Case-insensitive; any other value is a 400.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsMarketResponse", await self._client._request(
            "GET",
            "/api/v1/deals/market",
            query={
                "view": view,
                "county_fips": county_fips,
                "state_fips": state_fips,
                "year": year,
                "rating": rating,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def market_iter(
        self,
        *,
        view: Optional[Literal["affordability"]] = None,
        county_fips: Optional[str] = None,
        state_fips: Optional[str] = None,
        year: Optional[str] = None,
        rating: Optional[Literal["AFFORDABLE", "MODERATE", "EXPENSIVE", "VERY_EXPENSIVE"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[Union[_t.MarketSummary, _t.AffordabilityRow]]:
        """County-quarter transaction summary or affordability index

        ``GET /api/v1/deals/market``

        Default: returns county/quarter transaction summaries. Pass `view=affordability` to retrieve
        the home-affordability index instead (price-to-income ratios + rating).

        Auto-paginating iterator over every item (``data``) of :meth:`market`. Pages are fetched on
        demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset`` until a
        short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number of
        items yielded.

        Args:
            view: Switch to the affordability-index dataset.
            county_fips: 5-digit county FIPS filter.
            state_fips: 2-digit state FIPS filter.
            year: Year filter.
            rating: Affordability-rating filter (only meaningful with view=affordability).
                Case-insensitive; any other value is a 400.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.market(view=view, county_fips=county_fips, state_fips=state_fips, year=year, rating=rating, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item

    async def portfolio_owners(
        self,
        *,
        min_properties: Optional[int] = None,
        state: Optional[str] = None,
        min_value: Optional[int] = None,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DealsPortfolioOwnersResponse:
        """Find portfolio investors (owners of 2+ properties)

        ``GET /api/v1/deals/portfolio-owners``

        Returns portfolio owners ranked by property count and total assessed value. Useful for
        finding institutional buyers, small landlords, or specific investor families.

        Args:
            min_properties: Minimum properties owned.
            state: 2-letter owner mailing state filter.
            min_value: Minimum total portfolio assessed value, USD.
            search: Owner name substring search.
            limit: Page size, max 500.
            offset: Pagination offset.
        """
        return cast("_t.DealsPortfolioOwnersResponse", await self._client._request(
            "GET",
            "/api/v1/deals/portfolio-owners",
            query={
                "min_properties": min_properties,
                "state": state,
                "min_value": min_value,
                "search": search,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def portfolio_owners_iter(
        self,
        *,
        min_properties: Optional[int] = None,
        state: Optional[str] = None,
        min_value: Optional[int] = None,
        search: Optional[str] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.PortfolioOwner]:
        """Find portfolio investors (owners of 2+ properties)

        ``GET /api/v1/deals/portfolio-owners``

        Returns portfolio owners ranked by property count and total assessed value. Useful for
        finding institutional buyers, small landlords, or specific investor families.

        Auto-paginating iterator over every item (``data``) of :meth:`portfolio_owners`. Pages are
        fetched on demand, ``page_size`` items at a time (sent as ``limit``), advancing ``offset``
        until a short page, ``offset >= total`` or ``has_more`` false. ``max_items`` caps the number
        of items yielded.

        Args:
            min_properties: Minimum properties owned.
            state: 2-letter owner mailing state filter.
            min_value: Minimum total portfolio assessed value, USD.
            search: Owner name substring search.
        """
        async for item in aiterate_offset(
            lambda _limit, _pos: self.portfolio_owners(min_properties=min_properties, state=state, min_value=min_value, search=search, limit=_limit, offset=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", page_size=page_size, max_items=max_items,
        ):
            yield item
