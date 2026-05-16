# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    parcel_retrieve_report_params,
    parcel_retrieve_geojson_params,
    parcel_retrieve_traffic_history_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.parcel import Parcel
from ...types.v1.risk_assessment import RiskAssessment
from ...types.v1.parcel_retrieve_deeds_response import ParcelRetrieveDeedsResponse
from ...types.v1.parcel_retrieve_owner_response import ParcelRetrieveOwnerResponse
from ...types.v1.parcel_retrieve_report_response import ParcelRetrieveReportResponse
from ...types.v1.parcel_retrieve_geojson_response import ParcelRetrieveGeojsonResponse
from ...types.v1.parcel_retrieve_permits_response import ParcelRetrievePermitsResponse
from ...types.v1.parcel_retrieve_traffic_history_response import ParcelRetrieveTrafficHistoryResponse

__all__ = ["ParcelsResource", "AsyncParcelsResource"]


class ParcelsResource(SyncAPIResource):
    """Parcel lookup, owner details, permits, deeds, and risk data."""

    @cached_property
    def with_raw_response(self) -> ParcelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jdw2111/propraven-python#accessing-raw-response-data-eg-headers
        """
        return ParcelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParcelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jdw2111/propraven-python#with_streaming_response
        """
        return ParcelsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Parcel:
        """
        Retrieve a single parcel by its composite ID (county_fips:parcel_id).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/parcels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Parcel,
        )

    def retrieve_deeds(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrieveDeedsResponse:
        """
        Retrieve deed transactions and transfer history for a parcel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/parcels/{id}/deeds", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParcelRetrieveDeedsResponse,
        )

    def retrieve_geojson(
        self,
        *,
        bbox: str,
        zoom: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrieveGeojsonResponse:
        """
        Returns parcel polygons inside a bounding box as a GeoJSON FeatureCollection.
        Only served at zoom ≥ 14 to limit data volume — coarser bbox returns an empty
        collection. Each feature's properties include parcel_id, county_fips,
        owner_name, assessed value, and basic attributes for rendering popups.

        Args:
          bbox: Bounding box `west,south,east,north`.

          zoom: Map zoom level. Below 14 returns an empty collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/parcels/geojson",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bbox": bbox,
                        "zoom": zoom,
                    },
                    parcel_retrieve_geojson_params.ParcelRetrieveGeojsonParams,
                ),
            ),
            cast_to=ParcelRetrieveGeojsonResponse,
        )

    def retrieve_owner(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrieveOwnerResponse:
        """
        Retrieve the owner of a parcel along with their portfolio summary and list of
        properties.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/parcels/{id}/owner", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParcelRetrieveOwnerResponse,
        )

    def retrieve_permits(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrievePermitsResponse:
        """
        Retrieve building and construction permits associated with a parcel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/parcels/{id}/permits", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParcelRetrievePermitsResponse,
        )

    def retrieve_report(
        self,
        id: str,
        *,
        county_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrieveReportResponse:
        """
        Returns the full canonical parcel record plus every enrichment: UCC liens,
        comparable sales, owner portfolio context, permits, deeds, hazard composite.
        This is the single most data-dense endpoint per parcel — designed for
        due-diligence and underwriting workflows. Heavier than parcels/{id}; cache
        aggressively when serving UIs.

        Args:
          county_fips: 5-digit county FIPS. Strongly recommended when passing a county-local id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/parcels/{id}/report", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"county_fips": county_fips}, parcel_retrieve_report_params.ParcelRetrieveReportParams
                ),
            ),
            cast_to=ParcelRetrieveReportResponse,
        )

    def retrieve_risks(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RiskAssessment:
        """
        Retrieve flood, wildfire, air quality, and crime risk data for a parcel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/parcels/{id}/risks", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RiskAssessment,
        )

    def retrieve_traffic_history(
        self,
        id: str,
        *,
        lat: float,
        lng: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrieveTrafficHistoryResponse:
        """
        Finds the AADT (annual average daily traffic) station nearest to the given
        coordinates and returns its historical time series plus 3/5/7-year CAGRs. Useful
        for retail / CRE site selection. Search radius ~2 miles; returns empty data if
        no station is in range.

        Args:
          lat: Latitude.

          lng: Longitude.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/parcels/{id}/traffic-history", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                    },
                    parcel_retrieve_traffic_history_params.ParcelRetrieveTrafficHistoryParams,
                ),
            ),
            cast_to=ParcelRetrieveTrafficHistoryResponse,
        )


class AsyncParcelsResource(AsyncAPIResource):
    """Parcel lookup, owner details, permits, deeds, and risk data."""

    @cached_property
    def with_raw_response(self) -> AsyncParcelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jdw2111/propraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParcelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParcelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jdw2111/propraven-python#with_streaming_response
        """
        return AsyncParcelsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Parcel:
        """
        Retrieve a single parcel by its composite ID (county_fips:parcel_id).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/parcels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Parcel,
        )

    async def retrieve_deeds(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrieveDeedsResponse:
        """
        Retrieve deed transactions and transfer history for a parcel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/parcels/{id}/deeds", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParcelRetrieveDeedsResponse,
        )

    async def retrieve_geojson(
        self,
        *,
        bbox: str,
        zoom: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrieveGeojsonResponse:
        """
        Returns parcel polygons inside a bounding box as a GeoJSON FeatureCollection.
        Only served at zoom ≥ 14 to limit data volume — coarser bbox returns an empty
        collection. Each feature's properties include parcel_id, county_fips,
        owner_name, assessed value, and basic attributes for rendering popups.

        Args:
          bbox: Bounding box `west,south,east,north`.

          zoom: Map zoom level. Below 14 returns an empty collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/parcels/geojson",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bbox": bbox,
                        "zoom": zoom,
                    },
                    parcel_retrieve_geojson_params.ParcelRetrieveGeojsonParams,
                ),
            ),
            cast_to=ParcelRetrieveGeojsonResponse,
        )

    async def retrieve_owner(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrieveOwnerResponse:
        """
        Retrieve the owner of a parcel along with their portfolio summary and list of
        properties.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/parcels/{id}/owner", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParcelRetrieveOwnerResponse,
        )

    async def retrieve_permits(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrievePermitsResponse:
        """
        Retrieve building and construction permits associated with a parcel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/parcels/{id}/permits", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParcelRetrievePermitsResponse,
        )

    async def retrieve_report(
        self,
        id: str,
        *,
        county_fips: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrieveReportResponse:
        """
        Returns the full canonical parcel record plus every enrichment: UCC liens,
        comparable sales, owner portfolio context, permits, deeds, hazard composite.
        This is the single most data-dense endpoint per parcel — designed for
        due-diligence and underwriting workflows. Heavier than parcels/{id}; cache
        aggressively when serving UIs.

        Args:
          county_fips: 5-digit county FIPS. Strongly recommended when passing a county-local id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/parcels/{id}/report", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"county_fips": county_fips}, parcel_retrieve_report_params.ParcelRetrieveReportParams
                ),
            ),
            cast_to=ParcelRetrieveReportResponse,
        )

    async def retrieve_risks(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RiskAssessment:
        """
        Retrieve flood, wildfire, air quality, and crime risk data for a parcel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/parcels/{id}/risks", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RiskAssessment,
        )

    async def retrieve_traffic_history(
        self,
        id: str,
        *,
        lat: float,
        lng: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParcelRetrieveTrafficHistoryResponse:
        """
        Finds the AADT (annual average daily traffic) station nearest to the given
        coordinates and returns its historical time series plus 3/5/7-year CAGRs. Useful
        for retail / CRE site selection. Search radius ~2 miles; returns empty data if
        no station is in range.

        Args:
          lat: Latitude.

          lng: Longitude.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/parcels/{id}/traffic-history", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                    },
                    parcel_retrieve_traffic_history_params.ParcelRetrieveTrafficHistoryParams,
                ),
            ),
            cast_to=ParcelRetrieveTrafficHistoryResponse,
        )


class ParcelsResourceWithRawResponse:
    def __init__(self, parcels: ParcelsResource) -> None:
        self._parcels = parcels

        self.retrieve = to_raw_response_wrapper(
            parcels.retrieve,
        )
        self.retrieve_deeds = to_raw_response_wrapper(
            parcels.retrieve_deeds,
        )
        self.retrieve_geojson = to_raw_response_wrapper(
            parcels.retrieve_geojson,
        )
        self.retrieve_owner = to_raw_response_wrapper(
            parcels.retrieve_owner,
        )
        self.retrieve_permits = to_raw_response_wrapper(
            parcels.retrieve_permits,
        )
        self.retrieve_report = to_raw_response_wrapper(
            parcels.retrieve_report,
        )
        self.retrieve_risks = to_raw_response_wrapper(
            parcels.retrieve_risks,
        )
        self.retrieve_traffic_history = to_raw_response_wrapper(
            parcels.retrieve_traffic_history,
        )


class AsyncParcelsResourceWithRawResponse:
    def __init__(self, parcels: AsyncParcelsResource) -> None:
        self._parcels = parcels

        self.retrieve = async_to_raw_response_wrapper(
            parcels.retrieve,
        )
        self.retrieve_deeds = async_to_raw_response_wrapper(
            parcels.retrieve_deeds,
        )
        self.retrieve_geojson = async_to_raw_response_wrapper(
            parcels.retrieve_geojson,
        )
        self.retrieve_owner = async_to_raw_response_wrapper(
            parcels.retrieve_owner,
        )
        self.retrieve_permits = async_to_raw_response_wrapper(
            parcels.retrieve_permits,
        )
        self.retrieve_report = async_to_raw_response_wrapper(
            parcels.retrieve_report,
        )
        self.retrieve_risks = async_to_raw_response_wrapper(
            parcels.retrieve_risks,
        )
        self.retrieve_traffic_history = async_to_raw_response_wrapper(
            parcels.retrieve_traffic_history,
        )


class ParcelsResourceWithStreamingResponse:
    def __init__(self, parcels: ParcelsResource) -> None:
        self._parcels = parcels

        self.retrieve = to_streamed_response_wrapper(
            parcels.retrieve,
        )
        self.retrieve_deeds = to_streamed_response_wrapper(
            parcels.retrieve_deeds,
        )
        self.retrieve_geojson = to_streamed_response_wrapper(
            parcels.retrieve_geojson,
        )
        self.retrieve_owner = to_streamed_response_wrapper(
            parcels.retrieve_owner,
        )
        self.retrieve_permits = to_streamed_response_wrapper(
            parcels.retrieve_permits,
        )
        self.retrieve_report = to_streamed_response_wrapper(
            parcels.retrieve_report,
        )
        self.retrieve_risks = to_streamed_response_wrapper(
            parcels.retrieve_risks,
        )
        self.retrieve_traffic_history = to_streamed_response_wrapper(
            parcels.retrieve_traffic_history,
        )


class AsyncParcelsResourceWithStreamingResponse:
    def __init__(self, parcels: AsyncParcelsResource) -> None:
        self._parcels = parcels

        self.retrieve = async_to_streamed_response_wrapper(
            parcels.retrieve,
        )
        self.retrieve_deeds = async_to_streamed_response_wrapper(
            parcels.retrieve_deeds,
        )
        self.retrieve_geojson = async_to_streamed_response_wrapper(
            parcels.retrieve_geojson,
        )
        self.retrieve_owner = async_to_streamed_response_wrapper(
            parcels.retrieve_owner,
        )
        self.retrieve_permits = async_to_streamed_response_wrapper(
            parcels.retrieve_permits,
        )
        self.retrieve_report = async_to_streamed_response_wrapper(
            parcels.retrieve_report,
        )
        self.retrieve_risks = async_to_streamed_response_wrapper(
            parcels.retrieve_risks,
        )
        self.retrieve_traffic_history = async_to_streamed_response_wrapper(
            parcels.retrieve_traffic_history,
        )
