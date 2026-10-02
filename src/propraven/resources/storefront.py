# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``storefront`` namespace: ``client.storefront``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["StorefrontResource", "AsyncStorefrontResource"]


class StorefrontResource(SyncAPIResource):
    """``client.storefront`` operations (sync)."""

    def catalog(
        self,
        *,
        state: Optional[str] = None,
        tier: Optional[str] = None,
        section: Optional[str] = None,
        grain: Optional[str] = None,
        min_coverage: Optional[str] = None,
        red_cells: Optional[str] = None,
        q: Optional[str] = None,
        include: Optional[str] = None,
        fields: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.StorefrontCatalogResponse:
        """Machine Storefront — sealed field catalog

        ``GET /api/v1/storefront/catalog``

        The data catalog IS the storefront: every column of the serving parcel relation with its
        measured national (and optional per-state) coverage, grain, tier, honesty flags, and
        pipeline freshness warts, plus the dossier pricing model and base quote (the per-parcel
        value-tiered price comes from /storefront/availability?parcel_id=). FREE -- authenticated
        callers are unmetered and uncapped (rate-limited at the scale window); anonymous callers are
        served and IP-throttled at the free tier. Answered from a committed, sealed artifact -- no
        database access.

        Args:
            state: USPS code ("NC") or 2-digit FIPS ("37"). Adds per-state coverage to every field
                and a state gaps block.
            tier: prime|strong|good|partial|sparse|trace — filter by coverage tier.
            section: Filter to one catalog section (identity, valuation, hazard, …).
            grain: parcel|county|tract|block_group|zip|unknown.
            min_coverage: 0..1 — only fields at/above this national coverage.
            red_cells: 1 → only fields carrying a red-cell honesty flag.
            q: Substring on name, label or description.
            include: plumbing → include the internal provenance columns.
            fields: none → metadata header only, without the ~615 field entries.
        """
        return cast("_t.StorefrontCatalogResponse", self._client._request(
            "GET",
            "/api/v1/storefront/catalog",
            query={
                "state": state,
                "tier": tier,
                "section": section,
                "grain": grain,
                "min_coverage": min_coverage,
                "red_cells": red_cells,
                "q": q,
                "include": include,
                "fields": fields,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def availability(
        self,
        *,
        parcel_id: Optional[str] = None,
        state: Optional[str] = None,
        county: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.StorefrontAvailabilityResponse:
        """Machine Storefront -- try-before-buy (jurisdiction coverage or per-parcel quote)

        ``GET /api/v1/storefront/availability``

        Try-before-buy at two scopes, both FREE and answered from the sealed catalog:

        JURISDICTION mode (pass ?state=, optional &county=): how complete each field is in that
        state/county side-by-side with the national average, plus the worst local gaps and the base
        dossier quote. No parcel scan.

        PARCEL mode (pass ?parcel_id=): the exact value-tiered dossier price for ONE parcel BEFORE
        paying, with the V/R/F multiplier breakdown, band, and the cheap signals it was derived
        from. This uses the SAME quote math as the x402 402 on /parcels/{id}/report, so the
        previewed price equals the amount the payer is charged. Does one light, indexed
        single-parcel read.

        Provide EITHER parcel_id OR state. Same access model as the catalog: authenticated callers
        unmetered/uncapped, anonymous callers served and IP-throttled.

        Args:
            parcel_id: PARCEL mode. A canonical state_fips:county_fips:parcel_id, a legacy
                5-digit-county:parcel_id, or a parcel UUID. When present, returns the value-tiered
                dossier quote for this parcel (state/county are ignored).
            state: JURISDICTION mode. USPS code ("NC") or 2-digit FIPS ("37"). Required unless
                parcel_id is given.
            county: 3-digit within-state code ("183") or 5-digit state+county ("37183"). Optional;
                narrows JURISDICTION mode to one county.
            limit: JURISDICTION mode only: cap on the returned county list (default 25, max 400).
        """
        return cast("_t.StorefrontAvailabilityResponse", self._client._request(
            "GET",
            "/api/v1/storefront/availability",
            query={
                "parcel_id": parcel_id,
                "state": state,
                "county": county,
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncStorefrontResource(AsyncAPIResource):
    """``client.storefront`` operations (async)."""

    async def catalog(
        self,
        *,
        state: Optional[str] = None,
        tier: Optional[str] = None,
        section: Optional[str] = None,
        grain: Optional[str] = None,
        min_coverage: Optional[str] = None,
        red_cells: Optional[str] = None,
        q: Optional[str] = None,
        include: Optional[str] = None,
        fields: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.StorefrontCatalogResponse:
        """Machine Storefront — sealed field catalog

        ``GET /api/v1/storefront/catalog``

        The data catalog IS the storefront: every column of the serving parcel relation with its
        measured national (and optional per-state) coverage, grain, tier, honesty flags, and
        pipeline freshness warts, plus the dossier pricing model and base quote (the per-parcel
        value-tiered price comes from /storefront/availability?parcel_id=). FREE -- authenticated
        callers are unmetered and uncapped (rate-limited at the scale window); anonymous callers are
        served and IP-throttled at the free tier. Answered from a committed, sealed artifact -- no
        database access.

        Args:
            state: USPS code ("NC") or 2-digit FIPS ("37"). Adds per-state coverage to every field
                and a state gaps block.
            tier: prime|strong|good|partial|sparse|trace — filter by coverage tier.
            section: Filter to one catalog section (identity, valuation, hazard, …).
            grain: parcel|county|tract|block_group|zip|unknown.
            min_coverage: 0..1 — only fields at/above this national coverage.
            red_cells: 1 → only fields carrying a red-cell honesty flag.
            q: Substring on name, label or description.
            include: plumbing → include the internal provenance columns.
            fields: none → metadata header only, without the ~615 field entries.
        """
        return cast("_t.StorefrontCatalogResponse", await self._client._request(
            "GET",
            "/api/v1/storefront/catalog",
            query={
                "state": state,
                "tier": tier,
                "section": section,
                "grain": grain,
                "min_coverage": min_coverage,
                "red_cells": red_cells,
                "q": q,
                "include": include,
                "fields": fields,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def availability(
        self,
        *,
        parcel_id: Optional[str] = None,
        state: Optional[str] = None,
        county: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.StorefrontAvailabilityResponse:
        """Machine Storefront -- try-before-buy (jurisdiction coverage or per-parcel quote)

        ``GET /api/v1/storefront/availability``

        Try-before-buy at two scopes, both FREE and answered from the sealed catalog:

        JURISDICTION mode (pass ?state=, optional &county=): how complete each field is in that
        state/county side-by-side with the national average, plus the worst local gaps and the base
        dossier quote. No parcel scan.

        PARCEL mode (pass ?parcel_id=): the exact value-tiered dossier price for ONE parcel BEFORE
        paying, with the V/R/F multiplier breakdown, band, and the cheap signals it was derived
        from. This uses the SAME quote math as the x402 402 on /parcels/{id}/report, so the
        previewed price equals the amount the payer is charged. Does one light, indexed
        single-parcel read.

        Provide EITHER parcel_id OR state. Same access model as the catalog: authenticated callers
        unmetered/uncapped, anonymous callers served and IP-throttled.

        Args:
            parcel_id: PARCEL mode. A canonical state_fips:county_fips:parcel_id, a legacy
                5-digit-county:parcel_id, or a parcel UUID. When present, returns the value-tiered
                dossier quote for this parcel (state/county are ignored).
            state: JURISDICTION mode. USPS code ("NC") or 2-digit FIPS ("37"). Required unless
                parcel_id is given.
            county: 3-digit within-state code ("183") or 5-digit state+county ("37183"). Optional;
                narrows JURISDICTION mode to one county.
            limit: JURISDICTION mode only: cap on the returned county list (default 25, max 400).
        """
        return cast("_t.StorefrontAvailabilityResponse", await self._client._request(
            "GET",
            "/api/v1/storefront/availability",
            query={
                "parcel_id": parcel_id,
                "state": state,
                "county": county,
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
