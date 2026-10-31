# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``distribution`` namespace: ``client.distribution``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["DistributionResource", "AsyncDistributionResource"]


class DistributionResource(SyncAPIResource):
    """``client.distribution`` operations (sync)."""

    def r2_info(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DistributionR2InfoResponse:
        """R2 delivery metadata

        ``GET /api/v1/r2-credentials``

        Returns the R2 bucket, the prefixes a credential may name, the credential TTL limits in
        seconds, the catalog object and whether the caller's plan carries R2 delivery. AUTHENTICATED
        (signed-in session only): an anonymous call gets HTTP 401 from the session gate and an API
        key is not accepted. Credentials themselves are minted with POST on the same path from a
        signed-in session (see https://propraven.com/docs/r2); that operation is not part of the
        API-key contract.
        """
        return cast("_t.DistributionR2InfoResponse", self._client._request(
            "GET",
            "/api/v1/r2-credentials",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def databricks_info(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DistributionDatabricksInfoResponse:
        """Databricks Delta Sharing metadata

        ``GET /api/v1/data/databricks/grant``

        Returns the Delta Share name, the recipient types, whether delivery is configured and
        whether the channel is paused, with the channel status and its date. AUTHENTICATED
        (signed-in session only): an anonymous call gets HTTP 401 from the session gate and an API
        key is not accepted. Provisioning is POST on the same path from a signed-in session (see
        https://propraven.com/docs/databricks); while the channel is paused it returns 503 with a
        waitlist message. That operation is not part of the API-key contract.
        """
        return cast("_t.DistributionDatabricksInfoResponse", self._client._request(
            "GET",
            "/api/v1/data/databricks/grant",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncDistributionResource(AsyncAPIResource):
    """``client.distribution`` operations (async)."""

    async def r2_info(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DistributionR2InfoResponse:
        """R2 delivery metadata

        ``GET /api/v1/r2-credentials``

        Returns the R2 bucket, the prefixes a credential may name, the credential TTL limits in
        seconds, the catalog object and whether the caller's plan carries R2 delivery. AUTHENTICATED
        (signed-in session only): an anonymous call gets HTTP 401 from the session gate and an API
        key is not accepted. Credentials themselves are minted with POST on the same path from a
        signed-in session (see https://propraven.com/docs/r2); that operation is not part of the
        API-key contract.
        """
        return cast("_t.DistributionR2InfoResponse", await self._client._request(
            "GET",
            "/api/v1/r2-credentials",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def databricks_info(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.DistributionDatabricksInfoResponse:
        """Databricks Delta Sharing metadata

        ``GET /api/v1/data/databricks/grant``

        Returns the Delta Share name, the recipient types, whether delivery is configured and
        whether the channel is paused, with the channel status and its date. AUTHENTICATED
        (signed-in session only): an anonymous call gets HTTP 401 from the session gate and an API
        key is not accepted. Provisioning is POST on the same path from a signed-in session (see
        https://propraven.com/docs/databricks); while the channel is paused it returns 503 with a
        waitlist message. That operation is not part of the API-key contract.
        """
        return cast("_t.DistributionDatabricksInfoResponse", await self._client._request(
            "GET",
            "/api/v1/data/databricks/grant",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
