# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``cmbs`` namespace: ``client.cmbs``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["CmbsResource", "AsyncCmbsResource"]


class CmbsResource(SyncAPIResource):
    """``client.cmbs`` operations (sync)."""

    def exposure(
        self,
        *,
        id: Optional[str] = None,
        owner: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CmbsExposureResponse:
        """CMBS loan exposure for a parcel or an owner

        ``GET /api/v1/cmbs/exposure``

        Commercial mortgage-backed security loans tied to one parcel (`id`) or to a borrower/sponsor
        portfolio (`owner`). Pass exactly one.

        Args:
            id: Parcel id (single-parcel mode).
            owner: Borrower or sponsor name (portfolio mode).
        """
        return cast("_t.CmbsExposureResponse", self._client._request(
            "GET",
            "/api/v1/cmbs/exposure",
            query={
                "id": id,
                "owner": owner,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncCmbsResource(AsyncAPIResource):
    """``client.cmbs`` operations (async)."""

    async def exposure(
        self,
        *,
        id: Optional[str] = None,
        owner: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CmbsExposureResponse:
        """CMBS loan exposure for a parcel or an owner

        ``GET /api/v1/cmbs/exposure``

        Commercial mortgage-backed security loans tied to one parcel (`id`) or to a borrower/sponsor
        portfolio (`owner`). Pass exactly one.

        Args:
            id: Parcel id (single-parcel mode).
            owner: Borrower or sponsor name (portfolio mode).
        """
        return cast("_t.CmbsExposureResponse", await self._client._request(
            "GET",
            "/api/v1/cmbs/exposure",
            query={
                "id": id,
                "owner": owner,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
