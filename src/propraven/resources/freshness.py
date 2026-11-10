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

        Two different clocks for the served national parcel snapshot. `content_as_of` is the CONTENT
        date of the served data: how current the records in it are. How it is measured is named in
        `content_date_basis` and explained in `content_date_note` (read both; the basis can change).
        `swapped_at` is the time the serving slot was last swapped, i.e. when the current snapshot
        went live; a swap re-serves data, it does not refresh it, so `swapped_at` can be weeks newer
        than `content_as_of`. `snapshot_built_at` is when that snapshot was built, `updated_at`
        mirrors `swapped_at` and `last_enriched_at` mirrors `content_as_of` (both kept for older
        clients). All values are national: a state still served from an earlier epoch is not
        reported separately here. Free; anonymous callers are IP-throttled.
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

        Two different clocks for the served national parcel snapshot. `content_as_of` is the CONTENT
        date of the served data: how current the records in it are. How it is measured is named in
        `content_date_basis` and explained in `content_date_note` (read both; the basis can change).
        `swapped_at` is the time the serving slot was last swapped, i.e. when the current snapshot
        went live; a swap re-serves data, it does not refresh it, so `swapped_at` can be weeks newer
        than `content_as_of`. `snapshot_built_at` is when that snapshot was built, `updated_at`
        mirrors `swapped_at` and `last_enriched_at` mirrors `content_as_of` (both kept for older
        clients). All values are national: a state still served from an earlier epoch is not
        reported separately here. Free; anonymous callers are IP-throttled.
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
