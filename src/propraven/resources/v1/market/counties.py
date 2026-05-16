# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.market import county_retrieve_statistics_params
from ....types.v1.market.county_retrieve_detail_response import CountyRetrieveDetailResponse
from ....types.v1.market.county_retrieve_statistics_response import CountyRetrieveStatisticsResponse

__all__ = ["CountiesResource", "AsyncCountiesResource"]


class CountiesResource(SyncAPIResource):
    """County-level market statistics and trends."""

    @cached_property
    def with_raw_response(self) -> CountiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jdw2111/propraven-python#accessing-raw-response-data-eg-headers
        """
        return CountiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CountiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jdw2111/propraven-python#with_streaming_response
        """
        return CountiesResourceWithStreamingResponse(self)

    def retrieve_detail(
        self,
        fips: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountyRetrieveDetailResponse:
        """
        Returns the full county profile: quarterly market stats (sale count, median
        price, YoY change, days on market), affordability index by year, parcel summary
        (count, avg assessed value), and flip activity. Use for county-detail
        dashboards.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fips:
            raise ValueError(f"Expected a non-empty value for `fips` but received {fips!r}")
        return self._get(
            path_template("/api/v1/market/counties/{fips}", fips=fips),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountyRetrieveDetailResponse,
        )

    def retrieve_statistics(
        self,
        *,
        limit: int | Omit = omit,
        min_sales: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        quarter: str | Omit = omit,
        sort: Literal["sale_count", "median_price", "yoy_change", "county_name"] | Omit = omit,
        state_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountyRetrieveStatisticsResponse:
        """
        Retrieve real estate market statistics aggregated at the county level, including
        sale counts, median prices, and year-over-year changes.

        Args:
          min_sales: Minimum number of sales in the period to include a county.

          quarter: Specific quarter to retrieve (e.g., 2025Q4). Defaults to latest available.

          sort: Sort field.

          state_fips: Filter by state FIPS code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/market/counties",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "min_sales": min_sales,
                        "offset": offset,
                        "order": order,
                        "quarter": quarter,
                        "sort": sort,
                        "state_fips": state_fips,
                    },
                    county_retrieve_statistics_params.CountyRetrieveStatisticsParams,
                ),
            ),
            cast_to=CountyRetrieveStatisticsResponse,
        )


class AsyncCountiesResource(AsyncAPIResource):
    """County-level market statistics and trends."""

    @cached_property
    def with_raw_response(self) -> AsyncCountiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jdw2111/propraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCountiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCountiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jdw2111/propraven-python#with_streaming_response
        """
        return AsyncCountiesResourceWithStreamingResponse(self)

    async def retrieve_detail(
        self,
        fips: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountyRetrieveDetailResponse:
        """
        Returns the full county profile: quarterly market stats (sale count, median
        price, YoY change, days on market), affordability index by year, parcel summary
        (count, avg assessed value), and flip activity. Use for county-detail
        dashboards.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fips:
            raise ValueError(f"Expected a non-empty value for `fips` but received {fips!r}")
        return await self._get(
            path_template("/api/v1/market/counties/{fips}", fips=fips),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountyRetrieveDetailResponse,
        )

    async def retrieve_statistics(
        self,
        *,
        limit: int | Omit = omit,
        min_sales: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        quarter: str | Omit = omit,
        sort: Literal["sale_count", "median_price", "yoy_change", "county_name"] | Omit = omit,
        state_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountyRetrieveStatisticsResponse:
        """
        Retrieve real estate market statistics aggregated at the county level, including
        sale counts, median prices, and year-over-year changes.

        Args:
          min_sales: Minimum number of sales in the period to include a county.

          quarter: Specific quarter to retrieve (e.g., 2025Q4). Defaults to latest available.

          sort: Sort field.

          state_fips: Filter by state FIPS code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/market/counties",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "min_sales": min_sales,
                        "offset": offset,
                        "order": order,
                        "quarter": quarter,
                        "sort": sort,
                        "state_fips": state_fips,
                    },
                    county_retrieve_statistics_params.CountyRetrieveStatisticsParams,
                ),
            ),
            cast_to=CountyRetrieveStatisticsResponse,
        )


class CountiesResourceWithRawResponse:
    def __init__(self, counties: CountiesResource) -> None:
        self._counties = counties

        self.retrieve_detail = to_raw_response_wrapper(
            counties.retrieve_detail,
        )
        self.retrieve_statistics = to_raw_response_wrapper(
            counties.retrieve_statistics,
        )


class AsyncCountiesResourceWithRawResponse:
    def __init__(self, counties: AsyncCountiesResource) -> None:
        self._counties = counties

        self.retrieve_detail = async_to_raw_response_wrapper(
            counties.retrieve_detail,
        )
        self.retrieve_statistics = async_to_raw_response_wrapper(
            counties.retrieve_statistics,
        )


class CountiesResourceWithStreamingResponse:
    def __init__(self, counties: CountiesResource) -> None:
        self._counties = counties

        self.retrieve_detail = to_streamed_response_wrapper(
            counties.retrieve_detail,
        )
        self.retrieve_statistics = to_streamed_response_wrapper(
            counties.retrieve_statistics,
        )


class AsyncCountiesResourceWithStreamingResponse:
    def __init__(self, counties: AsyncCountiesResource) -> None:
        self._counties = counties

        self.retrieve_detail = async_to_streamed_response_wrapper(
            counties.retrieve_detail,
        )
        self.retrieve_statistics = async_to_streamed_response_wrapper(
            counties.retrieve_statistics,
        )
