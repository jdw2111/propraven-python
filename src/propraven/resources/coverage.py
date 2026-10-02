# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``coverage`` namespace: ``client.coverage``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["CoverageResource", "AsyncCoverageResource"]


class CoverageResource(SyncAPIResource):
    """``client.coverage`` operations (sync)."""

    def get(
        self,
        *,
        state: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CoverageGetResponse:
        """Get coverage statistics

        ``GET /api/v1/coverage``

        Retrieve parcel coverage statistics at the state or county level. API key optional:
        anonymous callers are rate-limited per IP; a present but invalid key is a 401; a valid key
        is rate-limited at its own tier and is not metered.

        Args:
            state: State FIPS code or abbreviation to filter coverage to a specific state and return
                county-level breakdown.
        """
        return cast("_t.CoverageGetResponse", self._client._request(
            "GET",
            "/api/v1/coverage",
            query={
                "state": state,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def map(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CoverageMapResponse:
        """County coverage map data

        ``GET /api/v1/coverage/map``

        Per-county parcel coverage for the national coverage map (compact keys). Free; IP-throttled
        on the restricted budget; cached for an hour.
        """
        return cast("_t.CoverageMapResponse", self._client._request(
            "GET",
            "/api/v1/coverage/map",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncCoverageResource(AsyncAPIResource):
    """``client.coverage`` operations (async)."""

    async def get(
        self,
        *,
        state: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CoverageGetResponse:
        """Get coverage statistics

        ``GET /api/v1/coverage``

        Retrieve parcel coverage statistics at the state or county level. API key optional:
        anonymous callers are rate-limited per IP; a present but invalid key is a 401; a valid key
        is rate-limited at its own tier and is not metered.

        Args:
            state: State FIPS code or abbreviation to filter coverage to a specific state and return
                county-level breakdown.
        """
        return cast("_t.CoverageGetResponse", await self._client._request(
            "GET",
            "/api/v1/coverage",
            query={
                "state": state,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def map(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CoverageMapResponse:
        """County coverage map data

        ``GET /api/v1/coverage/map``

        Per-county parcel coverage for the national coverage map (compact keys). Free; IP-throttled
        on the restricted budget; cached for an hour.
        """
        return cast("_t.CoverageMapResponse", await self._client._request(
            "GET",
            "/api/v1/coverage/map",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
