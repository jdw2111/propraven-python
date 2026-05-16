# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .counties import (
    CountiesResource,
    AsyncCountiesResource,
    CountiesResourceWithRawResponse,
    AsyncCountiesResourceWithRawResponse,
    CountiesResourceWithStreamingResponse,
    AsyncCountiesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import market_retrieve_trends_params, market_retrieve_flip_activity_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.market_retrieve_trends_response import MarketRetrieveTrendsResponse
from ....types.v1.market_retrieve_flip_activity_response import MarketRetrieveFlipActivityResponse

__all__ = ["MarketResource", "AsyncMarketResource"]


class MarketResource(SyncAPIResource):
    """County-level market statistics and trends."""

    @cached_property
    def counties(self) -> CountiesResource:
        """County-level market statistics and trends."""
        return CountiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MarketResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#accessing-raw-response-data-eg-headers
        """
        return MarketResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#with_streaming_response
        """
        return MarketResourceWithStreamingResponse(self)

    def retrieve_flip_activity(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        state_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketRetrieveFlipActivityResponse:
        """
        Aggregated flip activity per county: count, average ROI, average hold days,
        total profit. Use for surfacing the hottest flip markets. Differs from
        /api/v1/deals/flips which returns the underlying transactions.

        Args:
          limit: Page size, max 500.

          offset: Pagination offset.

          state_fips: 2-digit state FIPS filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/market/flips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "state_fips": state_fips,
                    },
                    market_retrieve_flip_activity_params.MarketRetrieveFlipActivityParams,
                ),
            ),
            cast_to=MarketRetrieveFlipActivityResponse,
        )

    def retrieve_trends(
        self,
        *,
        county_fips: str | Omit = omit,
        state_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketRetrieveTrendsResponse:
        """
        Retrieve quarterly time series of market metrics for one or more counties or a
        state.

        Args:
          county_fips: Comma-separated list of county FIPS codes.

          state_fips: State FIPS code. Used if county_fips is not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/market/trends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "county_fips": county_fips,
                        "state_fips": state_fips,
                    },
                    market_retrieve_trends_params.MarketRetrieveTrendsParams,
                ),
            ),
            cast_to=MarketRetrieveTrendsResponse,
        )


class AsyncMarketResource(AsyncAPIResource):
    """County-level market statistics and trends."""

    @cached_property
    def counties(self) -> AsyncCountiesResource:
        """County-level market statistics and trends."""
        return AsyncCountiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMarketResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#with_streaming_response
        """
        return AsyncMarketResourceWithStreamingResponse(self)

    async def retrieve_flip_activity(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        state_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketRetrieveFlipActivityResponse:
        """
        Aggregated flip activity per county: count, average ROI, average hold days,
        total profit. Use for surfacing the hottest flip markets. Differs from
        /api/v1/deals/flips which returns the underlying transactions.

        Args:
          limit: Page size, max 500.

          offset: Pagination offset.

          state_fips: 2-digit state FIPS filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/market/flips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "state_fips": state_fips,
                    },
                    market_retrieve_flip_activity_params.MarketRetrieveFlipActivityParams,
                ),
            ),
            cast_to=MarketRetrieveFlipActivityResponse,
        )

    async def retrieve_trends(
        self,
        *,
        county_fips: str | Omit = omit,
        state_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketRetrieveTrendsResponse:
        """
        Retrieve quarterly time series of market metrics for one or more counties or a
        state.

        Args:
          county_fips: Comma-separated list of county FIPS codes.

          state_fips: State FIPS code. Used if county_fips is not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/market/trends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "county_fips": county_fips,
                        "state_fips": state_fips,
                    },
                    market_retrieve_trends_params.MarketRetrieveTrendsParams,
                ),
            ),
            cast_to=MarketRetrieveTrendsResponse,
        )


class MarketResourceWithRawResponse:
    def __init__(self, market: MarketResource) -> None:
        self._market = market

        self.retrieve_flip_activity = to_raw_response_wrapper(
            market.retrieve_flip_activity,
        )
        self.retrieve_trends = to_raw_response_wrapper(
            market.retrieve_trends,
        )

    @cached_property
    def counties(self) -> CountiesResourceWithRawResponse:
        """County-level market statistics and trends."""
        return CountiesResourceWithRawResponse(self._market.counties)


class AsyncMarketResourceWithRawResponse:
    def __init__(self, market: AsyncMarketResource) -> None:
        self._market = market

        self.retrieve_flip_activity = async_to_raw_response_wrapper(
            market.retrieve_flip_activity,
        )
        self.retrieve_trends = async_to_raw_response_wrapper(
            market.retrieve_trends,
        )

    @cached_property
    def counties(self) -> AsyncCountiesResourceWithRawResponse:
        """County-level market statistics and trends."""
        return AsyncCountiesResourceWithRawResponse(self._market.counties)


class MarketResourceWithStreamingResponse:
    def __init__(self, market: MarketResource) -> None:
        self._market = market

        self.retrieve_flip_activity = to_streamed_response_wrapper(
            market.retrieve_flip_activity,
        )
        self.retrieve_trends = to_streamed_response_wrapper(
            market.retrieve_trends,
        )

    @cached_property
    def counties(self) -> CountiesResourceWithStreamingResponse:
        """County-level market statistics and trends."""
        return CountiesResourceWithStreamingResponse(self._market.counties)


class AsyncMarketResourceWithStreamingResponse:
    def __init__(self, market: AsyncMarketResource) -> None:
        self._market = market

        self.retrieve_flip_activity = async_to_streamed_response_wrapper(
            market.retrieve_flip_activity,
        )
        self.retrieve_trends = async_to_streamed_response_wrapper(
            market.retrieve_trends,
        )

    @cached_property
    def counties(self) -> AsyncCountiesResourceWithStreamingResponse:
        """County-level market statistics and trends."""
        return AsyncCountiesResourceWithStreamingResponse(self._market.counties)
