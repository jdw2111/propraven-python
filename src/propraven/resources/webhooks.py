# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``webhooks`` namespace: ``client.webhooks``."""

from __future__ import annotations

from typing import Any, Literal, Mapping, Optional, Sequence, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    """``client.webhooks`` operations (sync)."""

    def list(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksListResponse:
        """List webhook endpoints

        ``GET /api/v1/webhooks``

        Returns every webhook endpoint of the calling account (active and disabled), plus the quota
        of the caller's API tier.
        """
        return cast("_t.WebhooksListResponse", self._client._request(
            "GET",
            "/api/v1/webhooks",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def create(
        self,
        *,
        url: str,
        event_types: Sequence[Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]],
        filter_kind: Literal["parcel_ids", "state_fips", "county_fips"],
        filter_value: _t.WebhookFilter,
        description: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksCreateResponse:
        """Create a webhook endpoint

        ``POST /api/v1/webhooks``

        Creates a new webhook subscription. The returned `secret` is shown ONCE — store it
        server-side and use it to verify every incoming delivery via the `X-PropRaven-Signature`
        header (HMAC-SHA256 over `<unix_ms>.<raw_body>`). Reject deliveries where `|now - t| >
        5min`. Every request field is validated before anything is created;
        `filter_value.parcel_ids` entries are stored as canonical ids
        (`state_fips:county_fips:parcel_id`). Only active endpoints count toward your quota.

        Args:
            url: Customer endpoint. https:// only.
            event_types: Event types to subscribe to. All three event types are live: create accepts
                each of them and PropRaven emits each of them.
            description: Optional human-readable label for your dashboard.
        """
        return cast("_t.WebhooksCreateResponse", self._client._request(
            "POST",
            "/api/v1/webhooks",
            body={
                "url": url,
                "event_types": event_types,
                "filter_kind": filter_kind,
                "filter_value": filter_value,
                "description": description,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def get(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksGetResponse:
        """Get a single webhook endpoint

        ``GET /api/v1/webhooks/{id}``

        Returns one endpoint as the same snake_case record GET /webhooks lists (the `Webhook`
        schema). The secret is never returned.

        Args:
            id: Webhook endpoint ID.
        """
        return cast("_t.WebhooksGetResponse", self._client._request(
            "GET",
            "/api/v1/webhooks/{id}",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def delete(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksDeleteResponse:
        """Soft-disable a webhook endpoint

        ``DELETE /api/v1/webhooks/{id}``

        Soft disable, not a delete: sets `is_active: false`, `disabled_reason: "user"` and
        `disabled_at`. The endpoint stays in GET /webhooks with its delivery history (readable via
        the deliveries route). Nothing more is sent to it, including deliveries already queued.
        There is no hard delete and no re-enable or update operation; create a new endpoint instead.
        A disabled endpoint does not count toward the quota.

        Args:
            id: Webhook endpoint ID.
        """
        return cast("_t.WebhooksDeleteResponse", self._client._request(
            "DELETE",
            "/api/v1/webhooks/{id}",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def deliveries(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksDeliveriesResponse:
        """Recent delivery attempts for a webhook

        ``GET /api/v1/webhooks/{id}/deliveries``

        Returns the last 100 delivery attempts for an endpoint — useful for debugging signature
        mismatches, retry visibility, and dead-letter inspection.

        Args:
            id: Webhook endpoint ID.
        """
        return cast("_t.WebhooksDeliveriesResponse", self._client._request(
            "GET",
            "/api/v1/webhooks/{id}/deliveries",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def retry_delivery(
        self,
        id: str,
        delivery_id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksRetryDeliveryResponse:
        """Re-queue a failed webhook delivery

        ``POST /api/v1/webhooks/{id}/deliveries/{deliveryId}/retry``

        Moves a `pending`, `failed` or `dead_lettered` delivery back to `pending` for immediate
        redelivery. A delivered one is a 409.

        Args:
            id: Webhook endpoint id.
            delivery_id: Delivery id.
        """
        return cast("_t.WebhooksRetryDeliveryResponse", self._client._request(
            "POST",
            "/api/v1/webhooks/{id}/deliveries/{deliveryId}/retry",
            path_params={"id": id, "deliveryId": delivery_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncWebhooksResource(AsyncAPIResource):
    """``client.webhooks`` operations (async)."""

    async def list(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksListResponse:
        """List webhook endpoints

        ``GET /api/v1/webhooks``

        Returns every webhook endpoint of the calling account (active and disabled), plus the quota
        of the caller's API tier.
        """
        return cast("_t.WebhooksListResponse", await self._client._request(
            "GET",
            "/api/v1/webhooks",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def create(
        self,
        *,
        url: str,
        event_types: Sequence[Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]],
        filter_kind: Literal["parcel_ids", "state_fips", "county_fips"],
        filter_value: _t.WebhookFilter,
        description: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksCreateResponse:
        """Create a webhook endpoint

        ``POST /api/v1/webhooks``

        Creates a new webhook subscription. The returned `secret` is shown ONCE — store it
        server-side and use it to verify every incoming delivery via the `X-PropRaven-Signature`
        header (HMAC-SHA256 over `<unix_ms>.<raw_body>`). Reject deliveries where `|now - t| >
        5min`. Every request field is validated before anything is created;
        `filter_value.parcel_ids` entries are stored as canonical ids
        (`state_fips:county_fips:parcel_id`). Only active endpoints count toward your quota.

        Args:
            url: Customer endpoint. https:// only.
            event_types: Event types to subscribe to. All three event types are live: create accepts
                each of them and PropRaven emits each of them.
            description: Optional human-readable label for your dashboard.
        """
        return cast("_t.WebhooksCreateResponse", await self._client._request(
            "POST",
            "/api/v1/webhooks",
            body={
                "url": url,
                "event_types": event_types,
                "filter_kind": filter_kind,
                "filter_value": filter_value,
                "description": description,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def get(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksGetResponse:
        """Get a single webhook endpoint

        ``GET /api/v1/webhooks/{id}``

        Returns one endpoint as the same snake_case record GET /webhooks lists (the `Webhook`
        schema). The secret is never returned.

        Args:
            id: Webhook endpoint ID.
        """
        return cast("_t.WebhooksGetResponse", await self._client._request(
            "GET",
            "/api/v1/webhooks/{id}",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def delete(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksDeleteResponse:
        """Soft-disable a webhook endpoint

        ``DELETE /api/v1/webhooks/{id}``

        Soft disable, not a delete: sets `is_active: false`, `disabled_reason: "user"` and
        `disabled_at`. The endpoint stays in GET /webhooks with its delivery history (readable via
        the deliveries route). Nothing more is sent to it, including deliveries already queued.
        There is no hard delete and no re-enable or update operation; create a new endpoint instead.
        A disabled endpoint does not count toward the quota.

        Args:
            id: Webhook endpoint ID.
        """
        return cast("_t.WebhooksDeleteResponse", await self._client._request(
            "DELETE",
            "/api/v1/webhooks/{id}",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def deliveries(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksDeliveriesResponse:
        """Recent delivery attempts for a webhook

        ``GET /api/v1/webhooks/{id}/deliveries``

        Returns the last 100 delivery attempts for an endpoint — useful for debugging signature
        mismatches, retry visibility, and dead-letter inspection.

        Args:
            id: Webhook endpoint ID.
        """
        return cast("_t.WebhooksDeliveriesResponse", await self._client._request(
            "GET",
            "/api/v1/webhooks/{id}/deliveries",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def retry_delivery(
        self,
        id: str,
        delivery_id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WebhooksRetryDeliveryResponse:
        """Re-queue a failed webhook delivery

        ``POST /api/v1/webhooks/{id}/deliveries/{deliveryId}/retry``

        Moves a `pending`, `failed` or `dead_lettered` delivery back to `pending` for immediate
        redelivery. A delivered one is a 409.

        Args:
            id: Webhook endpoint id.
            delivery_id: Delivery id.
        """
        return cast("_t.WebhooksRetryDeliveryResponse", await self._client._request(
            "POST",
            "/api/v1/webhooks/{id}/deliveries/{deliveryId}/retry",
            path_params={"id": id, "deliveryId": delivery_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
