# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``crime`` namespace: ``client.crime``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["CrimeResource", "AsyncCrimeResource"]


class CrimeResource(SyncAPIResource):
    """``client.crime`` operations (sync)."""

    def lookup(
        self,
        *,
        lat: float,
        lng: float,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CrimeLookupResponse:
        """Crime score near a point

        ``GET /api/v1/crime/lookup``

        The crime score of the nearest scored parcel within about 500 m of the point, or `crime:
        null`. Free; IP-throttled.

        Args:
            lat: Latitude.
            lng: Longitude.
        """
        return cast("_t.CrimeLookupResponse", self._client._request(
            "GET",
            "/api/v1/crime/lookup",
            query={
                "lat": lat,
                "lng": lng,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncCrimeResource(AsyncAPIResource):
    """``client.crime`` operations (async)."""

    async def lookup(
        self,
        *,
        lat: float,
        lng: float,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CrimeLookupResponse:
        """Crime score near a point

        ``GET /api/v1/crime/lookup``

        The crime score of the nearest scored parcel within about 500 m of the point, or `crime:
        null`. Free; IP-throttled.

        Args:
            lat: Latitude.
            lng: Longitude.
        """
        return cast("_t.CrimeLookupResponse", await self._client._request(
            "GET",
            "/api/v1/crime/lookup",
            query={
                "lat": lat,
                "lng": lng,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
