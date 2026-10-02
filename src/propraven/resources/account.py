# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``account`` namespace: ``client.account``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["AccountResource", "AsyncAccountResource"]


class AccountResource(SyncAPIResource):
    """``client.account`` operations (sync)."""

    def usage(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.AccountUsageResponse:
        """Current-period usage and quota

        ``GET /api/v1/account/usage``

        Returns the calling key's current-period API usage, included allotment, remaining calls,
        configured per-minute and per-day rate limits, and the hard-cap status. Per-user (all of a
        user's API keys roll up to the same monthly counter, since they share a Stripe
        subscription).
        """
        return cast("_t.AccountUsageResponse", self._client._request(
            "GET",
            "/api/v1/account/usage",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncAccountResource(AsyncAPIResource):
    """``client.account`` operations (async)."""

    async def usage(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.AccountUsageResponse:
        """Current-period usage and quota

        ``GET /api/v1/account/usage``

        Returns the calling key's current-period API usage, included allotment, remaining calls,
        configured per-minute and per-day rate limits, and the hard-cap status. Per-user (all of a
        user's API keys roll up to the same monthly counter, since they share a Stripe
        subscription).
        """
        return cast("_t.AccountUsageResponse", await self._client._request(
            "GET",
            "/api/v1/account/usage",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
