# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``traffic`` namespace: ``client.traffic``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["TrafficResource", "AsyncTrafficResource"]


class TrafficResource(SyncAPIResource):
    """``client.traffic`` operations (sync)."""

    def stations(
        self,
        *,
        bbox: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.TrafficStationsResponse:
        """Traffic count stations in a bounding box

        ``GET /api/v1/traffic/stations``

        Up to 150 traffic count stations (AADT) inside `bbox`, busiest first.

        Args:
            bbox: `west,south,east,north` in decimal degrees.
        """
        return cast("_t.TrafficStationsResponse", self._client._request(
            "GET",
            "/api/v1/traffic/stations",
            query={
                "bbox": bbox,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncTrafficResource(AsyncAPIResource):
    """``client.traffic`` operations (async)."""

    async def stations(
        self,
        *,
        bbox: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.TrafficStationsResponse:
        """Traffic count stations in a bounding box

        ``GET /api/v1/traffic/stations``

        Up to 150 traffic count stations (AADT) inside `bbox`, busiest first.

        Args:
            bbox: `west,south,east,north` in decimal degrees.
        """
        return cast("_t.TrafficStationsResponse", await self._client._request(
            "GET",
            "/api/v1/traffic/stations",
            query={
                "bbox": bbox,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
