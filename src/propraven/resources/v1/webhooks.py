# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import webhook_create_endpoint_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.webhook import Webhook
from ...types.v1.webhook_filter_param import WebhookFilterParam
from ...types.v1.webhook_list_endpoints_response import WebhookListEndpointsResponse
from ...types.v1.webhook_create_endpoint_response import WebhookCreateEndpointResponse
from ...types.v1.webhook_disable_endpoint_response import WebhookDisableEndpointResponse
from ...types.v1.webhook_retrieve_deliveries_response import WebhookRetrieveDeliveriesResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    """Webhook subscriptions and delivery history.

    Manage which events PropRaven pushes to your endpoints.
    """

    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create_endpoint(
        self,
        *,
        event_types: List[Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]],
        filter_kind: Literal["parcel_ids", "state_fips", "county_fips"],
        filter_value: WebhookFilterParam,
        url: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateEndpointResponse:
        """Creates a new webhook subscription.

        The returned `secret` is shown ONCE — store
        it server-side and use it to verify every incoming delivery via the
        `X-PropRaven-Signature` header (HMAC-SHA256 over `<unix_ms>.<raw_body>`). Reject
        deliveries where `|now - t| > 5min`.

        Args:
          event_types: Event types to subscribe to. NOTE: only parcel.sold is live in v1.0; others 501.

          filter_value: Shape varies with filter_kind. parcel_ids: explicit list. state_fips: all
              parcels in a state. county_fips: all parcels in a county within a state.

          url: Customer endpoint. https:// only.

          description: Optional human-readable label for your dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/webhooks",
            body=maybe_transform(
                {
                    "event_types": event_types,
                    "filter_kind": filter_kind,
                    "filter_value": filter_value,
                    "url": url,
                    "description": description,
                },
                webhook_create_endpoint_params.WebhookCreateEndpointParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateEndpointResponse,
        )

    def disable_endpoint(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDisableEndpointResponse:
        """Marks the endpoint inactive.

        Delivery history is preserved. The endpoint can no
        longer receive new events but past deliveries remain queryable via the
        deliveries route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/api/v1/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDisableEndpointResponse,
        )

    def list_endpoints(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListEndpointsResponse:
        """Returns all webhook endpoints for the calling account, plus the per-tier quota."""
        return self._get(
            "/api/v1/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListEndpointsResponse,
        )

    def retrieve_deliveries(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveDeliveriesResponse:
        """
        Returns the last 100 delivery attempts for an endpoint — useful for debugging
        signature mismatches, retry visibility, and dead-letter inspection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/webhooks/{id}/deliveries", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveDeliveriesResponse,
        )

    def retrieve_endpoint(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Returns the full endpoint record (without the secret).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    """Webhook subscriptions and delivery history.

    Manage which events PropRaven pushes to your endpoints.
    """

    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/propraven-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create_endpoint(
        self,
        *,
        event_types: List[Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]],
        filter_kind: Literal["parcel_ids", "state_fips", "county_fips"],
        filter_value: WebhookFilterParam,
        url: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateEndpointResponse:
        """Creates a new webhook subscription.

        The returned `secret` is shown ONCE — store
        it server-side and use it to verify every incoming delivery via the
        `X-PropRaven-Signature` header (HMAC-SHA256 over `<unix_ms>.<raw_body>`). Reject
        deliveries where `|now - t| > 5min`.

        Args:
          event_types: Event types to subscribe to. NOTE: only parcel.sold is live in v1.0; others 501.

          filter_value: Shape varies with filter_kind. parcel_ids: explicit list. state_fips: all
              parcels in a state. county_fips: all parcels in a county within a state.

          url: Customer endpoint. https:// only.

          description: Optional human-readable label for your dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/webhooks",
            body=await async_maybe_transform(
                {
                    "event_types": event_types,
                    "filter_kind": filter_kind,
                    "filter_value": filter_value,
                    "url": url,
                    "description": description,
                },
                webhook_create_endpoint_params.WebhookCreateEndpointParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateEndpointResponse,
        )

    async def disable_endpoint(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDisableEndpointResponse:
        """Marks the endpoint inactive.

        Delivery history is preserved. The endpoint can no
        longer receive new events but past deliveries remain queryable via the
        deliveries route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/api/v1/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDisableEndpointResponse,
        )

    async def list_endpoints(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListEndpointsResponse:
        """Returns all webhook endpoints for the calling account, plus the per-tier quota."""
        return await self._get(
            "/api/v1/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListEndpointsResponse,
        )

    async def retrieve_deliveries(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveDeliveriesResponse:
        """
        Returns the last 100 delivery attempts for an endpoint — useful for debugging
        signature mismatches, retry visibility, and dead-letter inspection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/webhooks/{id}/deliveries", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveDeliveriesResponse,
        )

    async def retrieve_endpoint(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Returns the full endpoint record (without the secret).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_endpoint = to_raw_response_wrapper(
            webhooks.create_endpoint,
        )
        self.disable_endpoint = to_raw_response_wrapper(
            webhooks.disable_endpoint,
        )
        self.list_endpoints = to_raw_response_wrapper(
            webhooks.list_endpoints,
        )
        self.retrieve_deliveries = to_raw_response_wrapper(
            webhooks.retrieve_deliveries,
        )
        self.retrieve_endpoint = to_raw_response_wrapper(
            webhooks.retrieve_endpoint,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_endpoint = async_to_raw_response_wrapper(
            webhooks.create_endpoint,
        )
        self.disable_endpoint = async_to_raw_response_wrapper(
            webhooks.disable_endpoint,
        )
        self.list_endpoints = async_to_raw_response_wrapper(
            webhooks.list_endpoints,
        )
        self.retrieve_deliveries = async_to_raw_response_wrapper(
            webhooks.retrieve_deliveries,
        )
        self.retrieve_endpoint = async_to_raw_response_wrapper(
            webhooks.retrieve_endpoint,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_endpoint = to_streamed_response_wrapper(
            webhooks.create_endpoint,
        )
        self.disable_endpoint = to_streamed_response_wrapper(
            webhooks.disable_endpoint,
        )
        self.list_endpoints = to_streamed_response_wrapper(
            webhooks.list_endpoints,
        )
        self.retrieve_deliveries = to_streamed_response_wrapper(
            webhooks.retrieve_deliveries,
        )
        self.retrieve_endpoint = to_streamed_response_wrapper(
            webhooks.retrieve_endpoint,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_endpoint = async_to_streamed_response_wrapper(
            webhooks.create_endpoint,
        )
        self.disable_endpoint = async_to_streamed_response_wrapper(
            webhooks.disable_endpoint,
        )
        self.list_endpoints = async_to_streamed_response_wrapper(
            webhooks.list_endpoints,
        )
        self.retrieve_deliveries = async_to_streamed_response_wrapper(
            webhooks.retrieve_deliveries,
        )
        self.retrieve_endpoint = async_to_streamed_response_wrapper(
            webhooks.retrieve_endpoint,
        )
