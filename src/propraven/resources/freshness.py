# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``freshness`` namespace: ``client.freshness``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["FreshnessResource", "AsyncFreshnessResource"]


class FreshnessResource(SyncAPIResource):
    """``client.freshness`` operations (sync)."""

    def get(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.FreshnessGetResponse:
        """How fresh the served parcel snapshot is

        ``GET /api/v1/freshness``

        Build and swap times of the served snapshot, plus a source-registry freshness proxy
        (`content_*`). Free; anonymous callers are IP-throttled.
        """
        return cast("_t.FreshnessGetResponse", self._client._request(
            "GET",
            "/api/v1/freshness",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def datasets(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.FreshnessDatasetsResponse:
        """Per-dataset availability and freshness

        ``GET /api/v1/freshness/datasets``
        """
        return cast("_t.FreshnessDatasetsResponse", self._client._request(
            "GET",
            "/api/v1/freshness/datasets",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncFreshnessResource(AsyncAPIResource):
    """``client.freshness`` operations (async)."""

    async def get(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.FreshnessGetResponse:
        """How fresh the served parcel snapshot is

        ``GET /api/v1/freshness``

        Build and swap times of the served snapshot, plus a source-registry freshness proxy
        (`content_*`). Free; anonymous callers are IP-throttled.
        """
        return cast("_t.FreshnessGetResponse", await self._client._request(
            "GET",
            "/api/v1/freshness",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def datasets(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.FreshnessDatasetsResponse:
        """Per-dataset availability and freshness

        ``GET /api/v1/freshness/datasets``
        """
        return cast("_t.FreshnessDatasetsResponse", await self._client._request(
            "GET",
            "/api/v1/freshness/datasets",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
