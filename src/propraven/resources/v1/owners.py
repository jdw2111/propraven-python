# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import owner_search_owners_params, owner_retrieve_properties_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.owner import Owner
from ...types.v1.owner_search_owners_response import OwnerSearchOwnersResponse
from ...types.v1.owner_retrieve_properties_response import OwnerRetrievePropertiesResponse
from ...types.v1.owner_retrieve_transactions_response import OwnerRetrieveTransactionsResponse
from ...types.v1.owner_retrieve_portfolio_summary_response import OwnerRetrievePortfolioSummaryResponse

__all__ = ["OwnersResource", "AsyncOwnersResource"]


class OwnersResource(SyncAPIResource):
    """Owner search, profiles, and portfolios."""

    @cached_property
    def with_raw_response(self) -> OwnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jdw2111/propraven-python#accessing-raw-response-data-eg-headers
        """
        return OwnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OwnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jdw2111/propraven-python#with_streaming_response
        """
        return OwnersResourceWithStreamingResponse(self)

    def retrieve_portfolio_summary(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnerRetrievePortfolioSummaryResponse:
        """
        Retrieve an owner's portfolio with aggregated summary statistics and property
        breakdown.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/api/v1/owners/{name}/portfolio", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnerRetrievePortfolioSummaryResponse,
        )

    def retrieve_profile(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Owner:
        """
        Retrieve a specific owner profile by name, including property count, total
        assessed value, entity type, and states.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/api/v1/owners/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Owner,
        )

    def retrieve_properties(
        self,
        name: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnerRetrievePropertiesResponse:
        """
        Retrieve the list of properties owned by a specific owner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/api/v1/owners/{name}/properties", name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    owner_retrieve_properties_params.OwnerRetrievePropertiesParams,
                ),
            ),
            cast_to=OwnerRetrievePropertiesResponse,
        )

    def retrieve_transactions(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnerRetrieveTransactionsResponse:
        """
        Returns up to 100 most-recent deed events where the named owner is either
        grantor or grantee. Useful for building an owner's transaction timeline across
        their portfolio.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/api/v1/owners/{name}/transactions", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnerRetrieveTransactionsResponse,
        )

    def search_owners(
        self,
        *,
        q: str,
        limit: int | Omit = omit,
        min_properties: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnerSearchOwnersResponse:
        """Search for property owners by name.

        Returns owner profiles with property counts
        and portfolio values.

        Args:
          q: Search query for owner name.

          min_properties: Minimum number of properties owned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/owners/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                        "min_properties": min_properties,
                    },
                    owner_search_owners_params.OwnerSearchOwnersParams,
                ),
            ),
            cast_to=OwnerSearchOwnersResponse,
        )


class AsyncOwnersResource(AsyncAPIResource):
    """Owner search, profiles, and portfolios."""

    @cached_property
    def with_raw_response(self) -> AsyncOwnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jdw2111/propraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOwnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOwnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jdw2111/propraven-python#with_streaming_response
        """
        return AsyncOwnersResourceWithStreamingResponse(self)

    async def retrieve_portfolio_summary(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnerRetrievePortfolioSummaryResponse:
        """
        Retrieve an owner's portfolio with aggregated summary statistics and property
        breakdown.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/api/v1/owners/{name}/portfolio", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnerRetrievePortfolioSummaryResponse,
        )

    async def retrieve_profile(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Owner:
        """
        Retrieve a specific owner profile by name, including property count, total
        assessed value, entity type, and states.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/api/v1/owners/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Owner,
        )

    async def retrieve_properties(
        self,
        name: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnerRetrievePropertiesResponse:
        """
        Retrieve the list of properties owned by a specific owner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/api/v1/owners/{name}/properties", name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    owner_retrieve_properties_params.OwnerRetrievePropertiesParams,
                ),
            ),
            cast_to=OwnerRetrievePropertiesResponse,
        )

    async def retrieve_transactions(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnerRetrieveTransactionsResponse:
        """
        Returns up to 100 most-recent deed events where the named owner is either
        grantor or grantee. Useful for building an owner's transaction timeline across
        their portfolio.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/api/v1/owners/{name}/transactions", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OwnerRetrieveTransactionsResponse,
        )

    async def search_owners(
        self,
        *,
        q: str,
        limit: int | Omit = omit,
        min_properties: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OwnerSearchOwnersResponse:
        """Search for property owners by name.

        Returns owner profiles with property counts
        and portfolio values.

        Args:
          q: Search query for owner name.

          min_properties: Minimum number of properties owned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/owners/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                        "min_properties": min_properties,
                    },
                    owner_search_owners_params.OwnerSearchOwnersParams,
                ),
            ),
            cast_to=OwnerSearchOwnersResponse,
        )


class OwnersResourceWithRawResponse:
    def __init__(self, owners: OwnersResource) -> None:
        self._owners = owners

        self.retrieve_portfolio_summary = to_raw_response_wrapper(
            owners.retrieve_portfolio_summary,
        )
        self.retrieve_profile = to_raw_response_wrapper(
            owners.retrieve_profile,
        )
        self.retrieve_properties = to_raw_response_wrapper(
            owners.retrieve_properties,
        )
        self.retrieve_transactions = to_raw_response_wrapper(
            owners.retrieve_transactions,
        )
        self.search_owners = to_raw_response_wrapper(
            owners.search_owners,
        )


class AsyncOwnersResourceWithRawResponse:
    def __init__(self, owners: AsyncOwnersResource) -> None:
        self._owners = owners

        self.retrieve_portfolio_summary = async_to_raw_response_wrapper(
            owners.retrieve_portfolio_summary,
        )
        self.retrieve_profile = async_to_raw_response_wrapper(
            owners.retrieve_profile,
        )
        self.retrieve_properties = async_to_raw_response_wrapper(
            owners.retrieve_properties,
        )
        self.retrieve_transactions = async_to_raw_response_wrapper(
            owners.retrieve_transactions,
        )
        self.search_owners = async_to_raw_response_wrapper(
            owners.search_owners,
        )


class OwnersResourceWithStreamingResponse:
    def __init__(self, owners: OwnersResource) -> None:
        self._owners = owners

        self.retrieve_portfolio_summary = to_streamed_response_wrapper(
            owners.retrieve_portfolio_summary,
        )
        self.retrieve_profile = to_streamed_response_wrapper(
            owners.retrieve_profile,
        )
        self.retrieve_properties = to_streamed_response_wrapper(
            owners.retrieve_properties,
        )
        self.retrieve_transactions = to_streamed_response_wrapper(
            owners.retrieve_transactions,
        )
        self.search_owners = to_streamed_response_wrapper(
            owners.search_owners,
        )


class AsyncOwnersResourceWithStreamingResponse:
    def __init__(self, owners: AsyncOwnersResource) -> None:
        self._owners = owners

        self.retrieve_portfolio_summary = async_to_streamed_response_wrapper(
            owners.retrieve_portfolio_summary,
        )
        self.retrieve_profile = async_to_streamed_response_wrapper(
            owners.retrieve_profile,
        )
        self.retrieve_properties = async_to_streamed_response_wrapper(
            owners.retrieve_properties,
        )
        self.retrieve_transactions = async_to_streamed_response_wrapper(
            owners.retrieve_transactions,
        )
        self.search_owners = async_to_streamed_response_wrapper(
            owners.search_owners,
        )
