# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``cohorts`` namespace: ``client.cohorts``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["CohortsResource", "AsyncCohortsResource"]


class CohortsResource(SyncAPIResource):
    """``client.cohorts`` operations (sync)."""

    def export(
        self,
        id: str,
        *,
        preview: Optional[bool] = None,
        credit_token: Optional[str] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CohortsExportResponse:
        """Mail-merge export of one of your lists (account required; included for subscribers, per row
        otherwise)

        ``GET /api/v1/cohorts/{id}/export``

        A mail-merge CSV of one of the caller's own lists: one row per MAILING ADDRESS (owner,
        mailing line1 / city / state / ZIP, the property address(es), their canonical ids, stage,
        source, as_of, as_of_basis, grade). Every address is read from ONE address column family of
        a parcel's record, with its ZIP; only mail-ready addresses become rows, and
        `X-Export-Parcels-Not-Mail-Ready` counts the rest.

        ACCOUNT REQUIRED: an API key or a signed-in session; anonymous callers -- including x402 /
        credit-token wallets -- get HTTP 401 `code: "account_required"` before any read. The list
        must be the caller's own (404 otherwise).

        PRICE: INCLUDED for a paid PropRaven subscription. Any other account pays $0.10 per mailing
        row, the quote capped at $20, from a prepaid credit balance (`X-CREDIT-TOKEN`) or per call
        via x402 (`X-PAYMENT`, sent with your credentials); with neither, HTTP 402 carrying the
        exact quote. `preview=true` returns the row count and the quote, free, with no data.

        Each export is recorded in PropRaven's people-data access log BEFORE the CSV is returned
        (and before an x402 payment settles). If the log cannot be written the export is refused
        (503) and any charge refunded or released.

        Args:
            id: The list (cohort) id.
            preview: true -> the free row count and exact quote, no data.
            credit_token (``X-CREDIT-TOKEN`` header): A prepaid credit token (pzc_...) to draw the
                per-row price from.
            payment (``X-PAYMENT`` header): x402 payment for the quoted total, sent together with
                your account credentials.
        """
        return cast("_t.CohortsExportResponse", self._client._request(
            "GET",
            "/api/v1/cohorts/{id}/export",
            path_params={"id": id},
            query={
                "preview": preview,
            },
            headers={"X-CREDIT-TOKEN": credit_token, "X-PAYMENT": payment},
            accept="text/csv, application/json",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CohortsListResponse:
        """List your saved parcel lists (cohorts)

        ``GET /api/v1/cohorts``

        Cohorts are saved parcel lists built in the PropRaven app; export one with GET
        /cohorts/{id}/export.
        """
        return cast("_t.CohortsListResponse", self._client._request(
            "GET",
            "/api/v1/cohorts",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncCohortsResource(AsyncAPIResource):
    """``client.cohorts`` operations (async)."""

    async def export(
        self,
        id: str,
        *,
        preview: Optional[bool] = None,
        credit_token: Optional[str] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CohortsExportResponse:
        """Mail-merge export of one of your lists (account required; included for subscribers, per row
        otherwise)

        ``GET /api/v1/cohorts/{id}/export``

        A mail-merge CSV of one of the caller's own lists: one row per MAILING ADDRESS (owner,
        mailing line1 / city / state / ZIP, the property address(es), their canonical ids, stage,
        source, as_of, as_of_basis, grade). Every address is read from ONE address column family of
        a parcel's record, with its ZIP; only mail-ready addresses become rows, and
        `X-Export-Parcels-Not-Mail-Ready` counts the rest.

        ACCOUNT REQUIRED: an API key or a signed-in session; anonymous callers -- including x402 /
        credit-token wallets -- get HTTP 401 `code: "account_required"` before any read. The list
        must be the caller's own (404 otherwise).

        PRICE: INCLUDED for a paid PropRaven subscription. Any other account pays $0.10 per mailing
        row, the quote capped at $20, from a prepaid credit balance (`X-CREDIT-TOKEN`) or per call
        via x402 (`X-PAYMENT`, sent with your credentials); with neither, HTTP 402 carrying the
        exact quote. `preview=true` returns the row count and the quote, free, with no data.

        Each export is recorded in PropRaven's people-data access log BEFORE the CSV is returned
        (and before an x402 payment settles). If the log cannot be written the export is refused
        (503) and any charge refunded or released.

        Args:
            id: The list (cohort) id.
            preview: true -> the free row count and exact quote, no data.
            credit_token (``X-CREDIT-TOKEN`` header): A prepaid credit token (pzc_...) to draw the
                per-row price from.
            payment (``X-PAYMENT`` header): x402 payment for the quoted total, sent together with
                your account credentials.
        """
        return cast("_t.CohortsExportResponse", await self._client._request(
            "GET",
            "/api/v1/cohorts/{id}/export",
            path_params={"id": id},
            query={
                "preview": preview,
            },
            headers={"X-CREDIT-TOKEN": credit_token, "X-PAYMENT": payment},
            accept="text/csv, application/json",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def list(
        self,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CohortsListResponse:
        """List your saved parcel lists (cohorts)

        ``GET /api/v1/cohorts``

        Cohorts are saved parcel lists built in the PropRaven app; export one with GET
        /cohorts/{id}/export.
        """
        return cast("_t.CohortsListResponse", await self._client._request(
            "GET",
            "/api/v1/cohorts",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
