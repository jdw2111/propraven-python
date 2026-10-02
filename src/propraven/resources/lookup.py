# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``lookup`` namespace: ``client.lookup``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Sequence, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["LookupResource", "AsyncLookupResource"]


class LookupResource(SyncAPIResource):
    """``client.lookup`` operations (sync)."""

    def get(
        self,
        *,
        q: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.LookupGetResponse:
        """Exact parcel lookup (UUID or APN)

        ``GET /api/v1/lookup``

        Resolve one parcel from an exact key: a PropRaven parcel UUID or an APN. Answered from the
        search index (the `parcel` fields are a subset of GET /parcels/{id}). Anonymous callers are
        IP-throttled on the restricted budget (100/day); fuzzy address input needs a key and is
        answered by POST /lookup/batch.

        Args:
            q: PropRaven parcel UUID or APN (min 2 chars).
        """
        return cast("_t.LookupGetResponse", self._client._request(
            "GET",
            "/api/v1/lookup",
            query={
                "q": q,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def batch(
        self,
        *,
        queries: Sequence[str],
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.LookupBatchResponse:
        """Resolve up to 500 parcel queries in one call

        ``POST /api/v1/lookup/batch``

        Each query resolves independently (UUID → APN → address), so a partial batch degrades row by
        row. Answered from the search index: fields listed in `unavailable_fields` are null on every
        row of this endpoint. Each matched row is one lookup against your plan.

        Args:
            queries: Parcel UUIDs, APNs, canonical ids or street addresses (≤ 500).
        """
        return cast("_t.LookupBatchResponse", self._client._request(
            "POST",
            "/api/v1/lookup/batch",
            body={
                "queries": queries,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncLookupResource(AsyncAPIResource):
    """``client.lookup`` operations (async)."""

    async def get(
        self,
        *,
        q: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.LookupGetResponse:
        """Exact parcel lookup (UUID or APN)

        ``GET /api/v1/lookup``

        Resolve one parcel from an exact key: a PropRaven parcel UUID or an APN. Answered from the
        search index (the `parcel` fields are a subset of GET /parcels/{id}). Anonymous callers are
        IP-throttled on the restricted budget (100/day); fuzzy address input needs a key and is
        answered by POST /lookup/batch.

        Args:
            q: PropRaven parcel UUID or APN (min 2 chars).
        """
        return cast("_t.LookupGetResponse", await self._client._request(
            "GET",
            "/api/v1/lookup",
            query={
                "q": q,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def batch(
        self,
        *,
        queries: Sequence[str],
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.LookupBatchResponse:
        """Resolve up to 500 parcel queries in one call

        ``POST /api/v1/lookup/batch``

        Each query resolves independently (UUID → APN → address), so a partial batch degrades row by
        row. Answered from the search index: fields listed in `unavailable_fields` are null on every
        row of this endpoint. Each matched row is one lookup against your plan.

        Args:
            queries: Parcel UUIDs, APNs, canonical ids or street addresses (≤ 500).
        """
        return cast("_t.LookupBatchResponse", await self._client._request(
            "POST",
            "/api/v1/lookup/batch",
            body={
                "queries": queries,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))
