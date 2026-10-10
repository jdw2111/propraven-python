# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``verify`` namespace: ``client.verify``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Sequence, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["VerifyResource", "AsyncVerifyResource"]


class VerifyResource(SyncAPIResource):
    """``client.verify`` operations (sync)."""

    def get(
        self,
        *,
        parcel_id: str,
        fields: str,
        preview: Optional[str] = None,
        credit_token: Optional[str] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.VerifyGetResponse:
        """Verify facts for one parcel

        ``GET /api/v1/verify``

        Verify catalogued FACTS: one (parcel, field) assertion per lookup, batch (POST body {
        lookups: [{ parcel_id, fields }] }, up to 1000 parcels) or single (GET ?parcel_id&fields).
        Priced per lookup, bulk-discounted ($0.02/$0.012/$0.006), capped $20. Pay from a prepaid
        credit balance (X-CREDIT-TOKEN) or per call via x402. preview=true returns count+price free;
        empty/all-invalid is free. Fields whitelisted (is_sfha, flood_zone, nri_risk_score,
        owner_occupied, is_absentee, owner_name, assessed_value, market_value, building_sqft,
        year_built, property_type, zoning, lot_size_acres, last_sale_date/price,
        address/city/state/zip); unknown parcel -> found:false. `owner_name` is people data: it is
        verified for an account (API key or signed-in session), or for a caller without one once its
        x402 payment settles or its credit debit succeeds. An UNPAID caller without an account (no
        X-PAYMENT / X-CREDIT-TOKEN, or preview=true) that asks for owner_name is refused with HTTP
        401 `code: "account_required"` before the quote; every other field is unaffected.

        Args:
            parcel_id: Canonical state:county:parcel.
            fields: Comma-separated field aliases.
            preview: FREE count + price.
            credit_token (``X-CREDIT-TOKEN`` header): Prepaid credit token.
            payment (``X-PAYMENT`` header): Base64 x402 PaymentPayload.
        """
        return cast("_t.VerifyGetResponse", self._client._request(
            "GET",
            "/api/v1/verify",
            query={
                "parcel_id": parcel_id,
                "fields": fields,
                "preview": preview,
            },
            headers={"X-CREDIT-TOKEN": credit_token, "X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def batch(
        self,
        *,
        lookups: Sequence[_t.VerifyBatchParamsLookupsItem],
        preview: Optional[str] = None,
        credit_token: Optional[str] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.VerifyBatchResponse:
        """Verify facts (batch, paid per lookup) - FREE preview

        ``POST /api/v1/verify``

        Verify catalogued FACTS: one (parcel, field) assertion per lookup, batch (POST body {
        lookups: [{ parcel_id, fields }] }, up to 1000 parcels) or single (GET ?parcel_id&fields).
        Priced per lookup, bulk-discounted ($0.02/$0.012/$0.006), capped $20. Pay from a prepaid
        credit balance (X-CREDIT-TOKEN) or per call via x402. preview=true returns count+price free;
        empty/all-invalid is free. Fields whitelisted (is_sfha, flood_zone, nri_risk_score,
        owner_occupied, is_absentee, owner_name, assessed_value, market_value, building_sqft,
        year_built, property_type, zoning, lot_size_acres, last_sale_date/price,
        address/city/state/zip); unknown parcel -> found:false. `owner_name` is people data: it is
        verified for an account (API key or signed-in session), or for a caller without one once its
        x402 payment settles or its credit debit succeeds. An UNPAID caller without an account (no
        X-PAYMENT / X-CREDIT-TOKEN, or preview=true) that asks for owner_name is refused with HTTP
        401 `code: "account_required"` before the quote; every other field is unaffected.

        Args:
            preview: FREE count + price.
            credit_token (``X-CREDIT-TOKEN`` header): Prepaid credit token to debit the batch.
            payment (``X-PAYMENT`` header): Base64 x402 PaymentPayload.
        """
        return cast("_t.VerifyBatchResponse", self._client._request(
            "POST",
            "/api/v1/verify",
            query={
                "preview": preview,
            },
            headers={"X-CREDIT-TOKEN": credit_token, "X-PAYMENT": payment},
            body={
                "lookups": lookups,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncVerifyResource(AsyncAPIResource):
    """``client.verify`` operations (async)."""

    async def get(
        self,
        *,
        parcel_id: str,
        fields: str,
        preview: Optional[str] = None,
        credit_token: Optional[str] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.VerifyGetResponse:
        """Verify facts for one parcel

        ``GET /api/v1/verify``

        Verify catalogued FACTS: one (parcel, field) assertion per lookup, batch (POST body {
        lookups: [{ parcel_id, fields }] }, up to 1000 parcels) or single (GET ?parcel_id&fields).
        Priced per lookup, bulk-discounted ($0.02/$0.012/$0.006), capped $20. Pay from a prepaid
        credit balance (X-CREDIT-TOKEN) or per call via x402. preview=true returns count+price free;
        empty/all-invalid is free. Fields whitelisted (is_sfha, flood_zone, nri_risk_score,
        owner_occupied, is_absentee, owner_name, assessed_value, market_value, building_sqft,
        year_built, property_type, zoning, lot_size_acres, last_sale_date/price,
        address/city/state/zip); unknown parcel -> found:false. `owner_name` is people data: it is
        verified for an account (API key or signed-in session), or for a caller without one once its
        x402 payment settles or its credit debit succeeds. An UNPAID caller without an account (no
        X-PAYMENT / X-CREDIT-TOKEN, or preview=true) that asks for owner_name is refused with HTTP
        401 `code: "account_required"` before the quote; every other field is unaffected.

        Args:
            parcel_id: Canonical state:county:parcel.
            fields: Comma-separated field aliases.
            preview: FREE count + price.
            credit_token (``X-CREDIT-TOKEN`` header): Prepaid credit token.
            payment (``X-PAYMENT`` header): Base64 x402 PaymentPayload.
        """
        return cast("_t.VerifyGetResponse", await self._client._request(
            "GET",
            "/api/v1/verify",
            query={
                "parcel_id": parcel_id,
                "fields": fields,
                "preview": preview,
            },
            headers={"X-CREDIT-TOKEN": credit_token, "X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def batch(
        self,
        *,
        lookups: Sequence[_t.VerifyBatchParamsLookupsItem],
        preview: Optional[str] = None,
        credit_token: Optional[str] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.VerifyBatchResponse:
        """Verify facts (batch, paid per lookup) - FREE preview

        ``POST /api/v1/verify``

        Verify catalogued FACTS: one (parcel, field) assertion per lookup, batch (POST body {
        lookups: [{ parcel_id, fields }] }, up to 1000 parcels) or single (GET ?parcel_id&fields).
        Priced per lookup, bulk-discounted ($0.02/$0.012/$0.006), capped $20. Pay from a prepaid
        credit balance (X-CREDIT-TOKEN) or per call via x402. preview=true returns count+price free;
        empty/all-invalid is free. Fields whitelisted (is_sfha, flood_zone, nri_risk_score,
        owner_occupied, is_absentee, owner_name, assessed_value, market_value, building_sqft,
        year_built, property_type, zoning, lot_size_acres, last_sale_date/price,
        address/city/state/zip); unknown parcel -> found:false. `owner_name` is people data: it is
        verified for an account (API key or signed-in session), or for a caller without one once its
        x402 payment settles or its credit debit succeeds. An UNPAID caller without an account (no
        X-PAYMENT / X-CREDIT-TOKEN, or preview=true) that asks for owner_name is refused with HTTP
        401 `code: "account_required"` before the quote; every other field is unaffected.

        Args:
            preview: FREE count + price.
            credit_token (``X-CREDIT-TOKEN`` header): Prepaid credit token to debit the batch.
            payment (``X-PAYMENT`` header): Base64 x402 PaymentPayload.
        """
        return cast("_t.VerifyBatchResponse", await self._client._request(
            "POST",
            "/api/v1/verify",
            query={
                "preview": preview,
            },
            headers={"X-CREDIT-TOKEN": credit_token, "X-PAYMENT": payment},
            body={
                "lookups": lookups,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))
