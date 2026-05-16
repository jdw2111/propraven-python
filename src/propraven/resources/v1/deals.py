# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    deal_find_flips_params,
    deal_search_lenders_params,
    deal_search_contractors_params,
    deal_find_absentee_owners_params,
    deal_find_high_land_ratio_params,
    deal_find_portfolio_owners_params,
    deal_find_long_hold_parcels_params,
    deal_retrieve_market_summary_params,
    deal_find_entity_owned_parcels_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.deal_find_flips_response import DealFindFlipsResponse
from ...types.v1.deal_search_lenders_response import DealSearchLendersResponse
from ...types.v1.deal_search_contractors_response import DealSearchContractorsResponse
from ...types.v1.deal_find_absentee_owners_response import DealFindAbsenteeOwnersResponse
from ...types.v1.deal_find_high_land_ratio_response import DealFindHighLandRatioResponse
from ...types.v1.deal_find_portfolio_owners_response import DealFindPortfolioOwnersResponse
from ...types.v1.deal_find_long_hold_parcels_response import DealFindLongHoldParcelsResponse
from ...types.v1.deal_retrieve_market_summary_response import DealRetrieveMarketSummaryResponse
from ...types.v1.deal_find_entity_owned_parcels_response import DealFindEntityOwnedParcelsResponse

__all__ = ["DealsResource", "AsyncDealsResource"]


class DealsResource(SyncAPIResource):
    """Deal sourcing: absentee owners, property flips."""

    @cached_property
    def with_raw_response(self) -> DealsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jdw2111/propraven-python#accessing-raw-response-data-eg-headers
        """
        return DealsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DealsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jdw2111/propraven-python#with_streaming_response
        """
        return DealsResourceWithStreamingResponse(self)

    def find_absentee_owners(
        self,
        *,
        county_fips: str | Omit = omit,
        limit: int | Omit = omit,
        min_value: float | Omit = omit,
        offset: int | Omit = omit,
        out_of_state: bool | Omit = omit,
        state_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindAbsenteeOwnersResponse:
        """
        Retrieve parcels owned by absentee owners, useful for off-market deal sourcing.

        Args:
          county_fips: Filter by county FIPS code.

          min_value: Minimum assessed value.

          out_of_state: Only return owners whose mailing address is in a different state.

          state_fips: Filter by state FIPS code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/deals/absentee",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "county_fips": county_fips,
                        "limit": limit,
                        "min_value": min_value,
                        "offset": offset,
                        "out_of_state": out_of_state,
                        "state_fips": state_fips,
                    },
                    deal_find_absentee_owners_params.DealFindAbsenteeOwnersParams,
                ),
            ),
            cast_to=DealFindAbsenteeOwnersResponse,
        )

    def find_entity_owned_parcels(
        self,
        *,
        county_fips: str | Omit = omit,
        entity_type: Literal["LLC", "CORP", "TRUST", "LP", "LTD", "ASSOCIATION", "OTHER_ENTITY"] | Omit = omit,
        limit: int | Omit = omit,
        min_value: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        state_fips: str | Omit = omit,
        top: bool | Omit = omit,
        zoning: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindEntityOwnedParcelsResponse:
        """
        Returns parcels owned by legal entities identified from owner-name pattern
        matching across 221M+ parcels. Pass `top=true` to get aggregated entity rankings
        instead of per-parcel rows. One of `county_fips`, `state_fips`, `search`, or
        `top` is required.

        Args:
          county_fips: 5-digit county FIPS filter.

          entity_type: Filter by entity classification.

          limit: Page size, max 500.

          min_value: Minimum assessed value, USD.

          offset: Pagination offset.

          search: Owner-name substring search.

          state_fips: 2-digit state FIPS filter.

          top: If true, returns aggregated entity rankings with summary stats instead of
              per-parcel rows.

          zoning: Zoning substring filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            DealFindEntityOwnedParcelsResponse,
            self._get(
                "/api/v1/deals/entities",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "county_fips": county_fips,
                            "entity_type": entity_type,
                            "limit": limit,
                            "min_value": min_value,
                            "offset": offset,
                            "search": search,
                            "state_fips": state_fips,
                            "top": top,
                            "zoning": zoning,
                        },
                        deal_find_entity_owned_parcels_params.DealFindEntityOwnedParcelsParams,
                    ),
                ),
                cast_to=cast(
                    Any, DealFindEntityOwnedParcelsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def find_flips(
        self,
        *,
        county_fips: str | Omit = omit,
        flip_tier: Literal["quick", "standard", "long"] | Omit = omit,
        limit: int | Omit = omit,
        min_profit: float | Omit = omit,
        offset: int | Omit = omit,
        state_fips: str | Omit = omit,
        view: Literal["flippers"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindFlipsResponse:
        """Retrieve recently flipped properties.

        Use ?view=flippers to get a ranked list of
        top flippers instead.

        Args:
          county_fips: Filter by county FIPS code.

          flip_tier: Filter by flip speed tier (quick: <6mo, standard: 6-12mo, long: 12-24mo).

          min_profit: Minimum estimated profit.

          state_fips: Filter by state FIPS code.

          view: Set to 'flippers' to return a ranked list of top flippers instead of individual
              flips.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/deals/flips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "county_fips": county_fips,
                        "flip_tier": flip_tier,
                        "limit": limit,
                        "min_profit": min_profit,
                        "offset": offset,
                        "state_fips": state_fips,
                        "view": view,
                    },
                    deal_find_flips_params.DealFindFlipsParams,
                ),
            ),
            cast_to=DealFindFlipsResponse,
        )

    def find_high_land_ratio(
        self,
        *,
        county_fips: str | Omit = omit,
        limit: int | Omit = omit,
        min_ratio: float | Omit = omit,
        min_value: int | Omit = omit,
        offset: int | Omit = omit,
        state_fips: str | Omit = omit,
        zoning: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindHighLandRatioResponse:
        """
        Returns parcels where land value significantly exceeds improvement value — a
        signal for redevelopment, teardown, or assemblage opportunities. `county_fips`
        or `state_fips` is required.

        Args:
          county_fips: 5-digit county FIPS filter.

          limit: Page size, max 500.

          min_ratio: Minimum land/improvement ratio.

          min_value: Minimum land assessed value, USD.

          offset: Pagination offset.

          state_fips: 2-digit state FIPS filter.

          zoning: Zoning substring filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/deals/high-land-ratio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "county_fips": county_fips,
                        "limit": limit,
                        "min_ratio": min_ratio,
                        "min_value": min_value,
                        "offset": offset,
                        "state_fips": state_fips,
                        "zoning": zoning,
                    },
                    deal_find_high_land_ratio_params.DealFindHighLandRatioParams,
                ),
            ),
            cast_to=DealFindHighLandRatioResponse,
        )

    def find_long_hold_parcels(
        self,
        *,
        county_fips: str | Omit = omit,
        hold_tier: Literal["10-15yr", "15-20yr", "20-30yr", "30yr+"] | Omit = omit,
        limit: int | Omit = omit,
        min_value: int | Omit = omit,
        min_years: int | Omit = omit,
        offset: int | Omit = omit,
        state_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindLongHoldParcelsResponse:
        """Returns parcels not sold in `min_years` or more.

        Long-hold owners are often
        motivated sellers — estate planning, deferred maintenance, life changes.
        `county_fips` or `state_fips` is required.

        Args:
          county_fips: 5-digit county FIPS filter.

          hold_tier: Filter by hold-period tier.

          limit: Page size, max 500.

          min_value: Minimum assessed value, USD.

          min_years: Minimum years held.

          offset: Pagination offset.

          state_fips: 2-digit state FIPS filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/deals/long-hold",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "county_fips": county_fips,
                        "hold_tier": hold_tier,
                        "limit": limit,
                        "min_value": min_value,
                        "min_years": min_years,
                        "offset": offset,
                        "state_fips": state_fips,
                    },
                    deal_find_long_hold_parcels_params.DealFindLongHoldParcelsParams,
                ),
            ),
            cast_to=DealFindLongHoldParcelsResponse,
        )

    def find_portfolio_owners(
        self,
        *,
        limit: int | Omit = omit,
        min_properties: int | Omit = omit,
        min_value: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindPortfolioOwnersResponse:
        """
        Returns portfolio owners ranked by property count and total assessed value.
        Useful for finding institutional buyers, small landlords, or specific investor
        families.

        Args:
          limit: Page size, max 500.

          min_properties: Minimum properties owned.

          min_value: Minimum total portfolio assessed value, USD.

          offset: Pagination offset.

          search: Owner name substring search.

          state: 2-letter owner mailing state filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/deals/portfolio-owners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "min_properties": min_properties,
                        "min_value": min_value,
                        "offset": offset,
                        "search": search,
                        "state": state,
                    },
                    deal_find_portfolio_owners_params.DealFindPortfolioOwnersParams,
                ),
            ),
            cast_to=DealFindPortfolioOwnersResponse,
        )

    def retrieve_market_summary(
        self,
        *,
        county_fips: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        rating: Literal["AFFORDABLE", "MODERATE", "EXPENSIVE", "VERY_EXPENSIVE"] | Omit = omit,
        state_fips: str | Omit = omit,
        view: Literal["affordability"] | Omit = omit,
        year: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealRetrieveMarketSummaryResponse:
        """Default: returns county/quarter transaction summaries.

        Pass `view=affordability`
        to retrieve the home-affordability index instead (price-to-income ratios +
        rating).

        Args:
          county_fips: 5-digit county FIPS filter.

          limit: Page size, max 500.

          offset: Pagination offset.

          rating: Affordability-rating filter (only meaningful with view=affordability).

          state_fips: 2-digit state FIPS filter.

          view: Switch to the affordability-index dataset.

          year: Year filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            DealRetrieveMarketSummaryResponse,
            self._get(
                "/api/v1/deals/market",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "county_fips": county_fips,
                            "limit": limit,
                            "offset": offset,
                            "rating": rating,
                            "state_fips": state_fips,
                            "view": view,
                            "year": year,
                        },
                        deal_retrieve_market_summary_params.DealRetrieveMarketSummaryParams,
                    ),
                ),
                cast_to=cast(
                    Any, DealRetrieveMarketSummaryResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def search_contractors(
        self,
        *,
        limit: int | Omit = omit,
        min_permits: int | Omit = omit,
        min_value: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealSearchContractorsResponse:
        """Returns contractor profiles aggregated from 45M+ building permits.

        Each profile
        includes permit count, jurisdictions worked, total declared permit value, and
        activity dates. Use to identify active contractors in a market or find a
        specific contractor by name.

        Args:
          limit: Page size, max 500.

          min_permits: Minimum permit count to include.

          min_value: Minimum total declared permit value, USD.

          offset: Pagination offset.

          search: Contractor name search (case-insensitive substring).

          state: 2-letter state filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/deals/contractors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "min_permits": min_permits,
                        "min_value": min_value,
                        "offset": offset,
                        "search": search,
                        "state": state,
                    },
                    deal_search_contractors_params.DealSearchContractorsParams,
                ),
            ),
            cast_to=DealSearchContractorsResponse,
        )

    def search_lenders(
        self,
        *,
        limit: int | Omit = omit,
        min_mortgages: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealSearchLendersResponse:
        """Returns lender profiles aggregated from deed/mortgage transactions.

        Includes
        mortgage count, total volume, geographic spread, and a national rank.

        Args:
          limit: Page size, max 500.

          min_mortgages: Minimum mortgage count.

          offset: Pagination offset.

          search: Lender name substring search.

          state: 2-letter state filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/deals/lenders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "min_mortgages": min_mortgages,
                        "offset": offset,
                        "search": search,
                        "state": state,
                    },
                    deal_search_lenders_params.DealSearchLendersParams,
                ),
            ),
            cast_to=DealSearchLendersResponse,
        )


class AsyncDealsResource(AsyncAPIResource):
    """Deal sourcing: absentee owners, property flips."""

    @cached_property
    def with_raw_response(self) -> AsyncDealsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jdw2111/propraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDealsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDealsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jdw2111/propraven-python#with_streaming_response
        """
        return AsyncDealsResourceWithStreamingResponse(self)

    async def find_absentee_owners(
        self,
        *,
        county_fips: str | Omit = omit,
        limit: int | Omit = omit,
        min_value: float | Omit = omit,
        offset: int | Omit = omit,
        out_of_state: bool | Omit = omit,
        state_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindAbsenteeOwnersResponse:
        """
        Retrieve parcels owned by absentee owners, useful for off-market deal sourcing.

        Args:
          county_fips: Filter by county FIPS code.

          min_value: Minimum assessed value.

          out_of_state: Only return owners whose mailing address is in a different state.

          state_fips: Filter by state FIPS code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/deals/absentee",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "county_fips": county_fips,
                        "limit": limit,
                        "min_value": min_value,
                        "offset": offset,
                        "out_of_state": out_of_state,
                        "state_fips": state_fips,
                    },
                    deal_find_absentee_owners_params.DealFindAbsenteeOwnersParams,
                ),
            ),
            cast_to=DealFindAbsenteeOwnersResponse,
        )

    async def find_entity_owned_parcels(
        self,
        *,
        county_fips: str | Omit = omit,
        entity_type: Literal["LLC", "CORP", "TRUST", "LP", "LTD", "ASSOCIATION", "OTHER_ENTITY"] | Omit = omit,
        limit: int | Omit = omit,
        min_value: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        state_fips: str | Omit = omit,
        top: bool | Omit = omit,
        zoning: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindEntityOwnedParcelsResponse:
        """
        Returns parcels owned by legal entities identified from owner-name pattern
        matching across 221M+ parcels. Pass `top=true` to get aggregated entity rankings
        instead of per-parcel rows. One of `county_fips`, `state_fips`, `search`, or
        `top` is required.

        Args:
          county_fips: 5-digit county FIPS filter.

          entity_type: Filter by entity classification.

          limit: Page size, max 500.

          min_value: Minimum assessed value, USD.

          offset: Pagination offset.

          search: Owner-name substring search.

          state_fips: 2-digit state FIPS filter.

          top: If true, returns aggregated entity rankings with summary stats instead of
              per-parcel rows.

          zoning: Zoning substring filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            DealFindEntityOwnedParcelsResponse,
            await self._get(
                "/api/v1/deals/entities",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "county_fips": county_fips,
                            "entity_type": entity_type,
                            "limit": limit,
                            "min_value": min_value,
                            "offset": offset,
                            "search": search,
                            "state_fips": state_fips,
                            "top": top,
                            "zoning": zoning,
                        },
                        deal_find_entity_owned_parcels_params.DealFindEntityOwnedParcelsParams,
                    ),
                ),
                cast_to=cast(
                    Any, DealFindEntityOwnedParcelsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def find_flips(
        self,
        *,
        county_fips: str | Omit = omit,
        flip_tier: Literal["quick", "standard", "long"] | Omit = omit,
        limit: int | Omit = omit,
        min_profit: float | Omit = omit,
        offset: int | Omit = omit,
        state_fips: str | Omit = omit,
        view: Literal["flippers"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindFlipsResponse:
        """Retrieve recently flipped properties.

        Use ?view=flippers to get a ranked list of
        top flippers instead.

        Args:
          county_fips: Filter by county FIPS code.

          flip_tier: Filter by flip speed tier (quick: <6mo, standard: 6-12mo, long: 12-24mo).

          min_profit: Minimum estimated profit.

          state_fips: Filter by state FIPS code.

          view: Set to 'flippers' to return a ranked list of top flippers instead of individual
              flips.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/deals/flips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "county_fips": county_fips,
                        "flip_tier": flip_tier,
                        "limit": limit,
                        "min_profit": min_profit,
                        "offset": offset,
                        "state_fips": state_fips,
                        "view": view,
                    },
                    deal_find_flips_params.DealFindFlipsParams,
                ),
            ),
            cast_to=DealFindFlipsResponse,
        )

    async def find_high_land_ratio(
        self,
        *,
        county_fips: str | Omit = omit,
        limit: int | Omit = omit,
        min_ratio: float | Omit = omit,
        min_value: int | Omit = omit,
        offset: int | Omit = omit,
        state_fips: str | Omit = omit,
        zoning: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindHighLandRatioResponse:
        """
        Returns parcels where land value significantly exceeds improvement value — a
        signal for redevelopment, teardown, or assemblage opportunities. `county_fips`
        or `state_fips` is required.

        Args:
          county_fips: 5-digit county FIPS filter.

          limit: Page size, max 500.

          min_ratio: Minimum land/improvement ratio.

          min_value: Minimum land assessed value, USD.

          offset: Pagination offset.

          state_fips: 2-digit state FIPS filter.

          zoning: Zoning substring filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/deals/high-land-ratio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "county_fips": county_fips,
                        "limit": limit,
                        "min_ratio": min_ratio,
                        "min_value": min_value,
                        "offset": offset,
                        "state_fips": state_fips,
                        "zoning": zoning,
                    },
                    deal_find_high_land_ratio_params.DealFindHighLandRatioParams,
                ),
            ),
            cast_to=DealFindHighLandRatioResponse,
        )

    async def find_long_hold_parcels(
        self,
        *,
        county_fips: str | Omit = omit,
        hold_tier: Literal["10-15yr", "15-20yr", "20-30yr", "30yr+"] | Omit = omit,
        limit: int | Omit = omit,
        min_value: int | Omit = omit,
        min_years: int | Omit = omit,
        offset: int | Omit = omit,
        state_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindLongHoldParcelsResponse:
        """Returns parcels not sold in `min_years` or more.

        Long-hold owners are often
        motivated sellers — estate planning, deferred maintenance, life changes.
        `county_fips` or `state_fips` is required.

        Args:
          county_fips: 5-digit county FIPS filter.

          hold_tier: Filter by hold-period tier.

          limit: Page size, max 500.

          min_value: Minimum assessed value, USD.

          min_years: Minimum years held.

          offset: Pagination offset.

          state_fips: 2-digit state FIPS filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/deals/long-hold",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "county_fips": county_fips,
                        "hold_tier": hold_tier,
                        "limit": limit,
                        "min_value": min_value,
                        "min_years": min_years,
                        "offset": offset,
                        "state_fips": state_fips,
                    },
                    deal_find_long_hold_parcels_params.DealFindLongHoldParcelsParams,
                ),
            ),
            cast_to=DealFindLongHoldParcelsResponse,
        )

    async def find_portfolio_owners(
        self,
        *,
        limit: int | Omit = omit,
        min_properties: int | Omit = omit,
        min_value: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealFindPortfolioOwnersResponse:
        """
        Returns portfolio owners ranked by property count and total assessed value.
        Useful for finding institutional buyers, small landlords, or specific investor
        families.

        Args:
          limit: Page size, max 500.

          min_properties: Minimum properties owned.

          min_value: Minimum total portfolio assessed value, USD.

          offset: Pagination offset.

          search: Owner name substring search.

          state: 2-letter owner mailing state filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/deals/portfolio-owners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "min_properties": min_properties,
                        "min_value": min_value,
                        "offset": offset,
                        "search": search,
                        "state": state,
                    },
                    deal_find_portfolio_owners_params.DealFindPortfolioOwnersParams,
                ),
            ),
            cast_to=DealFindPortfolioOwnersResponse,
        )

    async def retrieve_market_summary(
        self,
        *,
        county_fips: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        rating: Literal["AFFORDABLE", "MODERATE", "EXPENSIVE", "VERY_EXPENSIVE"] | Omit = omit,
        state_fips: str | Omit = omit,
        view: Literal["affordability"] | Omit = omit,
        year: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealRetrieveMarketSummaryResponse:
        """Default: returns county/quarter transaction summaries.

        Pass `view=affordability`
        to retrieve the home-affordability index instead (price-to-income ratios +
        rating).

        Args:
          county_fips: 5-digit county FIPS filter.

          limit: Page size, max 500.

          offset: Pagination offset.

          rating: Affordability-rating filter (only meaningful with view=affordability).

          state_fips: 2-digit state FIPS filter.

          view: Switch to the affordability-index dataset.

          year: Year filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            DealRetrieveMarketSummaryResponse,
            await self._get(
                "/api/v1/deals/market",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "county_fips": county_fips,
                            "limit": limit,
                            "offset": offset,
                            "rating": rating,
                            "state_fips": state_fips,
                            "view": view,
                            "year": year,
                        },
                        deal_retrieve_market_summary_params.DealRetrieveMarketSummaryParams,
                    ),
                ),
                cast_to=cast(
                    Any, DealRetrieveMarketSummaryResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def search_contractors(
        self,
        *,
        limit: int | Omit = omit,
        min_permits: int | Omit = omit,
        min_value: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealSearchContractorsResponse:
        """Returns contractor profiles aggregated from 45M+ building permits.

        Each profile
        includes permit count, jurisdictions worked, total declared permit value, and
        activity dates. Use to identify active contractors in a market or find a
        specific contractor by name.

        Args:
          limit: Page size, max 500.

          min_permits: Minimum permit count to include.

          min_value: Minimum total declared permit value, USD.

          offset: Pagination offset.

          search: Contractor name search (case-insensitive substring).

          state: 2-letter state filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/deals/contractors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "min_permits": min_permits,
                        "min_value": min_value,
                        "offset": offset,
                        "search": search,
                        "state": state,
                    },
                    deal_search_contractors_params.DealSearchContractorsParams,
                ),
            ),
            cast_to=DealSearchContractorsResponse,
        )

    async def search_lenders(
        self,
        *,
        limit: int | Omit = omit,
        min_mortgages: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealSearchLendersResponse:
        """Returns lender profiles aggregated from deed/mortgage transactions.

        Includes
        mortgage count, total volume, geographic spread, and a national rank.

        Args:
          limit: Page size, max 500.

          min_mortgages: Minimum mortgage count.

          offset: Pagination offset.

          search: Lender name substring search.

          state: 2-letter state filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/deals/lenders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "min_mortgages": min_mortgages,
                        "offset": offset,
                        "search": search,
                        "state": state,
                    },
                    deal_search_lenders_params.DealSearchLendersParams,
                ),
            ),
            cast_to=DealSearchLendersResponse,
        )


class DealsResourceWithRawResponse:
    def __init__(self, deals: DealsResource) -> None:
        self._deals = deals

        self.find_absentee_owners = to_raw_response_wrapper(
            deals.find_absentee_owners,
        )
        self.find_entity_owned_parcels = to_raw_response_wrapper(
            deals.find_entity_owned_parcels,
        )
        self.find_flips = to_raw_response_wrapper(
            deals.find_flips,
        )
        self.find_high_land_ratio = to_raw_response_wrapper(
            deals.find_high_land_ratio,
        )
        self.find_long_hold_parcels = to_raw_response_wrapper(
            deals.find_long_hold_parcels,
        )
        self.find_portfolio_owners = to_raw_response_wrapper(
            deals.find_portfolio_owners,
        )
        self.retrieve_market_summary = to_raw_response_wrapper(
            deals.retrieve_market_summary,
        )
        self.search_contractors = to_raw_response_wrapper(
            deals.search_contractors,
        )
        self.search_lenders = to_raw_response_wrapper(
            deals.search_lenders,
        )


class AsyncDealsResourceWithRawResponse:
    def __init__(self, deals: AsyncDealsResource) -> None:
        self._deals = deals

        self.find_absentee_owners = async_to_raw_response_wrapper(
            deals.find_absentee_owners,
        )
        self.find_entity_owned_parcels = async_to_raw_response_wrapper(
            deals.find_entity_owned_parcels,
        )
        self.find_flips = async_to_raw_response_wrapper(
            deals.find_flips,
        )
        self.find_high_land_ratio = async_to_raw_response_wrapper(
            deals.find_high_land_ratio,
        )
        self.find_long_hold_parcels = async_to_raw_response_wrapper(
            deals.find_long_hold_parcels,
        )
        self.find_portfolio_owners = async_to_raw_response_wrapper(
            deals.find_portfolio_owners,
        )
        self.retrieve_market_summary = async_to_raw_response_wrapper(
            deals.retrieve_market_summary,
        )
        self.search_contractors = async_to_raw_response_wrapper(
            deals.search_contractors,
        )
        self.search_lenders = async_to_raw_response_wrapper(
            deals.search_lenders,
        )


class DealsResourceWithStreamingResponse:
    def __init__(self, deals: DealsResource) -> None:
        self._deals = deals

        self.find_absentee_owners = to_streamed_response_wrapper(
            deals.find_absentee_owners,
        )
        self.find_entity_owned_parcels = to_streamed_response_wrapper(
            deals.find_entity_owned_parcels,
        )
        self.find_flips = to_streamed_response_wrapper(
            deals.find_flips,
        )
        self.find_high_land_ratio = to_streamed_response_wrapper(
            deals.find_high_land_ratio,
        )
        self.find_long_hold_parcels = to_streamed_response_wrapper(
            deals.find_long_hold_parcels,
        )
        self.find_portfolio_owners = to_streamed_response_wrapper(
            deals.find_portfolio_owners,
        )
        self.retrieve_market_summary = to_streamed_response_wrapper(
            deals.retrieve_market_summary,
        )
        self.search_contractors = to_streamed_response_wrapper(
            deals.search_contractors,
        )
        self.search_lenders = to_streamed_response_wrapper(
            deals.search_lenders,
        )


class AsyncDealsResourceWithStreamingResponse:
    def __init__(self, deals: AsyncDealsResource) -> None:
        self._deals = deals

        self.find_absentee_owners = async_to_streamed_response_wrapper(
            deals.find_absentee_owners,
        )
        self.find_entity_owned_parcels = async_to_streamed_response_wrapper(
            deals.find_entity_owned_parcels,
        )
        self.find_flips = async_to_streamed_response_wrapper(
            deals.find_flips,
        )
        self.find_high_land_ratio = async_to_streamed_response_wrapper(
            deals.find_high_land_ratio,
        )
        self.find_long_hold_parcels = async_to_streamed_response_wrapper(
            deals.find_long_hold_parcels,
        )
        self.find_portfolio_owners = async_to_streamed_response_wrapper(
            deals.find_portfolio_owners,
        )
        self.retrieve_market_summary = async_to_streamed_response_wrapper(
            deals.retrieve_market_summary,
        )
        self.search_contractors = async_to_streamed_response_wrapper(
            deals.search_contractors,
        )
        self.search_lenders = async_to_streamed_response_wrapper(
            deals.search_lenders,
        )
