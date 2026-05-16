# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    search_full_search_params,
    search_autocomplete_params,
    search_parcel_search_params,
    search_export_results_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.search_full_search_response import SearchFullSearchResponse
from ...types.v1.search_autocomplete_response import SearchAutocompleteResponse
from ...types.v1.search_parcel_search_response import SearchParcelSearchResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    """Geographic and filtered parcel search."""

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def autocomplete(
        self,
        *,
        q: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchAutocompleteResponse:
        """
        Fast prefix-matched autocomplete: returns cities/places, matching parcels, and
        Mapbox-geocoded addresses for the prefix. Three independent tiers run in
        parallel with per-tier timeouts so a slow DB query never blocks fast Mapbox
        results. Use for type-ahead UIs and address entry; for full-detail lookup use
        parcel lookup.

        Args:
          q: Search prefix. Minimum 2 chars.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/search/autocomplete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"q": q}, search_autocomplete_params.SearchAutocompleteParams),
            ),
            cast_to=SearchAutocompleteResponse,
        )

    def export_results(
        self,
        *,
        east: float | Omit = omit,
        limit: int | Omit = omit,
        north: float | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Literal[
            "address",
            "city",
            "state",
            "owner_name",
            "total_assessed_value",
            "zoning",
            "year_built",
            "lot_size_acres",
            "ownership_type",
        ]
        | Omit = omit,
        south: float | Omit = omit,
        west: float | Omit = omit,
        zoning_categories: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Returns up to 10,000 search-matched parcels as a CSV download.

        Accepts the same
        geographic + attribute filters as POST /api/v1/search. Designed for spreadsheet
        / Excel workflows; for programmatic ingestion, use the JSON search endpoint and
        paginate.

        Args:
          east: Bounding box: east longitude.

          limit: Row cap. Hard max 10,000.

          north: Bounding box: north latitude.

          order: Sort direction.

          sort: Sort column.

          south: Bounding box: south latitude.

          west: Bounding box: west longitude.

          zoning_categories: Comma-delimited zoning categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return self._get(
            "/api/v1/search/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "east": east,
                        "limit": limit,
                        "north": north,
                        "order": order,
                        "sort": sort,
                        "south": south,
                        "west": west,
                        "zoning_categories": zoning_categories,
                    },
                    search_export_results_params.SearchExportResultsParams,
                ),
            ),
            cast_to=str,
        )

    def full_search(
        self,
        *,
        q: str,
        city: str | Omit = omit,
        dir: Literal["asc", "desc"] | Omit = omit,
        field: Literal["all", "address", "owner_name", "city"] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort: Literal["address", "city", "state", "owner_name", "total_value", "year_built"] | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchFullSearchResponse:
        """
        Paginated search across the parcel search index by free-text query (`q`) and
        optional field/state/city filters. Distinct from POST /api/v1/search which is
        geo-bounded; this endpoint is text-anchored and works without a bounding box.
        Returns 50/page by default, 200 max.

        Args:
          q: Search query. Min 2 chars.

          city: City filter.

          dir: Sort direction.

          field: Field to match against.

          limit: Page size, max 200.

          page: 1-indexed page number.

          sort: Sort column.

          state: 2-letter state filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/search/full",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "city": city,
                        "dir": dir,
                        "field": field,
                        "limit": limit,
                        "page": page,
                        "sort": sort,
                        "state": state,
                    },
                    search_full_search_params.SearchFullSearchParams,
                ),
            ),
            cast_to=SearchFullSearchResponse,
        )

    def parcel_search(
        self,
        *,
        bounds: search_parcel_search_params.Bounds,
        filters: search_parcel_search_params.Filters | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Literal["assessed_value", "sale_price", "acreage", "year_built", "deal_score"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchParcelSearchResponse:
        """
        Search parcels within geographic bounds with optional filters, sorting, and
        pagination.

        Args:
          limit: Number of results to return.

          offset: Number of results to skip for pagination.

          sort: Sort field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/search",
            body=maybe_transform(
                {
                    "bounds": bounds,
                    "filters": filters,
                    "limit": limit,
                    "offset": offset,
                    "order": order,
                    "sort": sort,
                },
                search_parcel_search_params.SearchParcelSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchParcelSearchResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    """Geographic and filtered parcel search."""

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def autocomplete(
        self,
        *,
        q: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchAutocompleteResponse:
        """
        Fast prefix-matched autocomplete: returns cities/places, matching parcels, and
        Mapbox-geocoded addresses for the prefix. Three independent tiers run in
        parallel with per-tier timeouts so a slow DB query never blocks fast Mapbox
        results. Use for type-ahead UIs and address entry; for full-detail lookup use
        parcel lookup.

        Args:
          q: Search prefix. Minimum 2 chars.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/search/autocomplete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"q": q}, search_autocomplete_params.SearchAutocompleteParams),
            ),
            cast_to=SearchAutocompleteResponse,
        )

    async def export_results(
        self,
        *,
        east: float | Omit = omit,
        limit: int | Omit = omit,
        north: float | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Literal[
            "address",
            "city",
            "state",
            "owner_name",
            "total_assessed_value",
            "zoning",
            "year_built",
            "lot_size_acres",
            "ownership_type",
        ]
        | Omit = omit,
        south: float | Omit = omit,
        west: float | Omit = omit,
        zoning_categories: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Returns up to 10,000 search-matched parcels as a CSV download.

        Accepts the same
        geographic + attribute filters as POST /api/v1/search. Designed for spreadsheet
        / Excel workflows; for programmatic ingestion, use the JSON search endpoint and
        paginate.

        Args:
          east: Bounding box: east longitude.

          limit: Row cap. Hard max 10,000.

          north: Bounding box: north latitude.

          order: Sort direction.

          sort: Sort column.

          south: Bounding box: south latitude.

          west: Bounding box: west longitude.

          zoning_categories: Comma-delimited zoning categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return await self._get(
            "/api/v1/search/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "east": east,
                        "limit": limit,
                        "north": north,
                        "order": order,
                        "sort": sort,
                        "south": south,
                        "west": west,
                        "zoning_categories": zoning_categories,
                    },
                    search_export_results_params.SearchExportResultsParams,
                ),
            ),
            cast_to=str,
        )

    async def full_search(
        self,
        *,
        q: str,
        city: str | Omit = omit,
        dir: Literal["asc", "desc"] | Omit = omit,
        field: Literal["all", "address", "owner_name", "city"] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort: Literal["address", "city", "state", "owner_name", "total_value", "year_built"] | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchFullSearchResponse:
        """
        Paginated search across the parcel search index by free-text query (`q`) and
        optional field/state/city filters. Distinct from POST /api/v1/search which is
        geo-bounded; this endpoint is text-anchored and works without a bounding box.
        Returns 50/page by default, 200 max.

        Args:
          q: Search query. Min 2 chars.

          city: City filter.

          dir: Sort direction.

          field: Field to match against.

          limit: Page size, max 200.

          page: 1-indexed page number.

          sort: Sort column.

          state: 2-letter state filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/search/full",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "city": city,
                        "dir": dir,
                        "field": field,
                        "limit": limit,
                        "page": page,
                        "sort": sort,
                        "state": state,
                    },
                    search_full_search_params.SearchFullSearchParams,
                ),
            ),
            cast_to=SearchFullSearchResponse,
        )

    async def parcel_search(
        self,
        *,
        bounds: search_parcel_search_params.Bounds,
        filters: search_parcel_search_params.Filters | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Literal["assessed_value", "sale_price", "acreage", "year_built", "deal_score"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchParcelSearchResponse:
        """
        Search parcels within geographic bounds with optional filters, sorting, and
        pagination.

        Args:
          limit: Number of results to return.

          offset: Number of results to skip for pagination.

          sort: Sort field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/search",
            body=await async_maybe_transform(
                {
                    "bounds": bounds,
                    "filters": filters,
                    "limit": limit,
                    "offset": offset,
                    "order": order,
                    "sort": sort,
                },
                search_parcel_search_params.SearchParcelSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchParcelSearchResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.autocomplete = to_raw_response_wrapper(
            search.autocomplete,
        )
        self.export_results = to_raw_response_wrapper(
            search.export_results,
        )
        self.full_search = to_raw_response_wrapper(
            search.full_search,
        )
        self.parcel_search = to_raw_response_wrapper(
            search.parcel_search,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.autocomplete = async_to_raw_response_wrapper(
            search.autocomplete,
        )
        self.export_results = async_to_raw_response_wrapper(
            search.export_results,
        )
        self.full_search = async_to_raw_response_wrapper(
            search.full_search,
        )
        self.parcel_search = async_to_raw_response_wrapper(
            search.parcel_search,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.autocomplete = to_streamed_response_wrapper(
            search.autocomplete,
        )
        self.export_results = to_streamed_response_wrapper(
            search.export_results,
        )
        self.full_search = to_streamed_response_wrapper(
            search.full_search,
        )
        self.parcel_search = to_streamed_response_wrapper(
            search.parcel_search,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.autocomplete = async_to_streamed_response_wrapper(
            search.autocomplete,
        )
        self.export_results = async_to_streamed_response_wrapper(
            search.export_results,
        )
        self.full_search = async_to_streamed_response_wrapper(
            search.full_search,
        )
        self.parcel_search = async_to_streamed_response_wrapper(
            search.parcel_search,
        )
