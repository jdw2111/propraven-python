# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .deals import (
    DealsResource,
    AsyncDealsResource,
    DealsResourceWithRawResponse,
    AsyncDealsResourceWithRawResponse,
    DealsResourceWithStreamingResponse,
    AsyncDealsResourceWithStreamingResponse,
)
from .owners import (
    OwnersResource,
    AsyncOwnersResource,
    OwnersResourceWithRawResponse,
    AsyncOwnersResourceWithRawResponse,
    OwnersResourceWithStreamingResponse,
    AsyncOwnersResourceWithStreamingResponse,
)
from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)
from ...types import v1_retrieve_coverage_params
from .account import (
    AccountResource,
    AsyncAccountResource,
    AccountResourceWithRawResponse,
    AsyncAccountResourceWithRawResponse,
    AccountResourceWithStreamingResponse,
    AsyncAccountResourceWithStreamingResponse,
)
from .parcels import (
    ParcelsResource,
    AsyncParcelsResource,
    ParcelsResourceWithRawResponse,
    AsyncParcelsResourceWithRawResponse,
    ParcelsResourceWithStreamingResponse,
    AsyncParcelsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .market.market import (
    MarketResource,
    AsyncMarketResource,
    MarketResourceWithRawResponse,
    AsyncMarketResourceWithRawResponse,
    MarketResourceWithStreamingResponse,
    AsyncMarketResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.v1_retrieve_coverage_response import V1RetrieveCoverageResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    """Data coverage statistics."""

    @cached_property
    def parcels(self) -> ParcelsResource:
        """Parcel lookup, owner details, permits, deeds, and risk data."""
        return ParcelsResource(self._client)

    @cached_property
    def search(self) -> SearchResource:
        """Geographic and filtered parcel search."""
        return SearchResource(self._client)

    @cached_property
    def deals(self) -> DealsResource:
        """Deal sourcing: absentee owners, property flips."""
        return DealsResource(self._client)

    @cached_property
    def market(self) -> MarketResource:
        """County-level market statistics and trends."""
        return MarketResource(self._client)

    @cached_property
    def owners(self) -> OwnersResource:
        """Owner search, profiles, and portfolios."""
        return OwnersResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Webhook subscriptions and delivery history.

        Manage which events PropRaven pushes to your endpoints.
        """
        return WebhooksResource(self._client)

    @cached_property
    def account(self) -> AccountResource:
        """Account-scoped usage, quota, and key-level reporting."""
        return AccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def retrieve_coverage(
        self,
        *,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RetrieveCoverageResponse:
        """
        Retrieve parcel coverage statistics at the state or county level.

        Args:
          state: State FIPS code or abbreviation to filter coverage to a specific state and
              return county-level breakdown.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/coverage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"state": state}, v1_retrieve_coverage_params.V1RetrieveCoverageParams),
            ),
            cast_to=V1RetrieveCoverageResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    """Data coverage statistics."""

    @cached_property
    def parcels(self) -> AsyncParcelsResource:
        """Parcel lookup, owner details, permits, deeds, and risk data."""
        return AsyncParcelsResource(self._client)

    @cached_property
    def search(self) -> AsyncSearchResource:
        """Geographic and filtered parcel search."""
        return AsyncSearchResource(self._client)

    @cached_property
    def deals(self) -> AsyncDealsResource:
        """Deal sourcing: absentee owners, property flips."""
        return AsyncDealsResource(self._client)

    @cached_property
    def market(self) -> AsyncMarketResource:
        """County-level market statistics and trends."""
        return AsyncMarketResource(self._client)

    @cached_property
    def owners(self) -> AsyncOwnersResource:
        """Owner search, profiles, and portfolios."""
        return AsyncOwnersResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Webhook subscriptions and delivery history.

        Manage which events PropRaven pushes to your endpoints.
        """
        return AsyncWebhooksResource(self._client)

    @cached_property
    def account(self) -> AsyncAccountResource:
        """Account-scoped usage, quota, and key-level reporting."""
        return AsyncAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def retrieve_coverage(
        self,
        *,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RetrieveCoverageResponse:
        """
        Retrieve parcel coverage statistics at the state or county level.

        Args:
          state: State FIPS code or abbreviation to filter coverage to a specific state and
              return county-level breakdown.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/coverage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"state": state}, v1_retrieve_coverage_params.V1RetrieveCoverageParams
                ),
            ),
            cast_to=V1RetrieveCoverageResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.retrieve_coverage = to_raw_response_wrapper(
            v1.retrieve_coverage,
        )

    @cached_property
    def parcels(self) -> ParcelsResourceWithRawResponse:
        """Parcel lookup, owner details, permits, deeds, and risk data."""
        return ParcelsResourceWithRawResponse(self._v1.parcels)

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        """Geographic and filtered parcel search."""
        return SearchResourceWithRawResponse(self._v1.search)

    @cached_property
    def deals(self) -> DealsResourceWithRawResponse:
        """Deal sourcing: absentee owners, property flips."""
        return DealsResourceWithRawResponse(self._v1.deals)

    @cached_property
    def market(self) -> MarketResourceWithRawResponse:
        """County-level market statistics and trends."""
        return MarketResourceWithRawResponse(self._v1.market)

    @cached_property
    def owners(self) -> OwnersResourceWithRawResponse:
        """Owner search, profiles, and portfolios."""
        return OwnersResourceWithRawResponse(self._v1.owners)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        """Webhook subscriptions and delivery history.

        Manage which events PropRaven pushes to your endpoints.
        """
        return WebhooksResourceWithRawResponse(self._v1.webhooks)

    @cached_property
    def account(self) -> AccountResourceWithRawResponse:
        """Account-scoped usage, quota, and key-level reporting."""
        return AccountResourceWithRawResponse(self._v1.account)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.retrieve_coverage = async_to_raw_response_wrapper(
            v1.retrieve_coverage,
        )

    @cached_property
    def parcels(self) -> AsyncParcelsResourceWithRawResponse:
        """Parcel lookup, owner details, permits, deeds, and risk data."""
        return AsyncParcelsResourceWithRawResponse(self._v1.parcels)

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        """Geographic and filtered parcel search."""
        return AsyncSearchResourceWithRawResponse(self._v1.search)

    @cached_property
    def deals(self) -> AsyncDealsResourceWithRawResponse:
        """Deal sourcing: absentee owners, property flips."""
        return AsyncDealsResourceWithRawResponse(self._v1.deals)

    @cached_property
    def market(self) -> AsyncMarketResourceWithRawResponse:
        """County-level market statistics and trends."""
        return AsyncMarketResourceWithRawResponse(self._v1.market)

    @cached_property
    def owners(self) -> AsyncOwnersResourceWithRawResponse:
        """Owner search, profiles, and portfolios."""
        return AsyncOwnersResourceWithRawResponse(self._v1.owners)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        """Webhook subscriptions and delivery history.

        Manage which events PropRaven pushes to your endpoints.
        """
        return AsyncWebhooksResourceWithRawResponse(self._v1.webhooks)

    @cached_property
    def account(self) -> AsyncAccountResourceWithRawResponse:
        """Account-scoped usage, quota, and key-level reporting."""
        return AsyncAccountResourceWithRawResponse(self._v1.account)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.retrieve_coverage = to_streamed_response_wrapper(
            v1.retrieve_coverage,
        )

    @cached_property
    def parcels(self) -> ParcelsResourceWithStreamingResponse:
        """Parcel lookup, owner details, permits, deeds, and risk data."""
        return ParcelsResourceWithStreamingResponse(self._v1.parcels)

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        """Geographic and filtered parcel search."""
        return SearchResourceWithStreamingResponse(self._v1.search)

    @cached_property
    def deals(self) -> DealsResourceWithStreamingResponse:
        """Deal sourcing: absentee owners, property flips."""
        return DealsResourceWithStreamingResponse(self._v1.deals)

    @cached_property
    def market(self) -> MarketResourceWithStreamingResponse:
        """County-level market statistics and trends."""
        return MarketResourceWithStreamingResponse(self._v1.market)

    @cached_property
    def owners(self) -> OwnersResourceWithStreamingResponse:
        """Owner search, profiles, and portfolios."""
        return OwnersResourceWithStreamingResponse(self._v1.owners)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        """Webhook subscriptions and delivery history.

        Manage which events PropRaven pushes to your endpoints.
        """
        return WebhooksResourceWithStreamingResponse(self._v1.webhooks)

    @cached_property
    def account(self) -> AccountResourceWithStreamingResponse:
        """Account-scoped usage, quota, and key-level reporting."""
        return AccountResourceWithStreamingResponse(self._v1.account)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.retrieve_coverage = async_to_streamed_response_wrapper(
            v1.retrieve_coverage,
        )

    @cached_property
    def parcels(self) -> AsyncParcelsResourceWithStreamingResponse:
        """Parcel lookup, owner details, permits, deeds, and risk data."""
        return AsyncParcelsResourceWithStreamingResponse(self._v1.parcels)

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        """Geographic and filtered parcel search."""
        return AsyncSearchResourceWithStreamingResponse(self._v1.search)

    @cached_property
    def deals(self) -> AsyncDealsResourceWithStreamingResponse:
        """Deal sourcing: absentee owners, property flips."""
        return AsyncDealsResourceWithStreamingResponse(self._v1.deals)

    @cached_property
    def market(self) -> AsyncMarketResourceWithStreamingResponse:
        """County-level market statistics and trends."""
        return AsyncMarketResourceWithStreamingResponse(self._v1.market)

    @cached_property
    def owners(self) -> AsyncOwnersResourceWithStreamingResponse:
        """Owner search, profiles, and portfolios."""
        return AsyncOwnersResourceWithStreamingResponse(self._v1.owners)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """Webhook subscriptions and delivery history.

        Manage which events PropRaven pushes to your endpoints.
        """
        return AsyncWebhooksResourceWithStreamingResponse(self._v1.webhooks)

    @cached_property
    def account(self) -> AsyncAccountResourceWithStreamingResponse:
        """Account-scoped usage, quota, and key-level reporting."""
        return AsyncAccountResourceWithStreamingResponse(self._v1.account)
