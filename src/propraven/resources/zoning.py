# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``zoning`` namespace: ``client.zoning``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["ZoningResource", "AsyncZoningResource"]


class ZoningResource(SyncAPIResource):
    """``client.zoning`` operations (sync)."""

    def parcel(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ZoningParcelResponse:
        """Zoning of a parcel, from the issuing jurisdiction

        ``GET /api/v1/parcels/{id}/zoning``

        The parcel's zoning code exactly as the issuing jurisdiction published it, the issuing body
        (a city or town, not the county), overlays as a set, split zoning, and, where the ordinance
        has been parsed, the underwriting attributes (minimum lot area, height, FAR/density,
        setbacks, by-right multifamily, ADU), each with its ordinance section, verbatim quote and
        link in `attributes.citations`. Null is never zero or false. `{ zoning: null, reason:
        "not_collected" }` means the parcel's jurisdiction has not been collected yet; it says
        nothing about whether the parcel is zoned. A research starting point, not a legal
        determination. Account required.

        Args:
            id: Parcel identifier: the canonical `state_fips:county_fips:parcel_id` form (e.g.
                `37:119:12104406`), the legacy 5-digit `county_fips5:parcel_id` form, or a PropRaven
                parcel UUID. URL-encode it.
        """
        return cast("_t.ZoningParcelResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/zoning",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def search(
        self,
        *,
        state_fips: Optional[str] = None,
        county_fips: Optional[str] = None,
        jurisdiction_id: Optional[str] = None,
        raw_code: Optional[str] = None,
        base_code: Optional[str] = None,
        family: Optional[str] = None,
        has_overlay: Optional[str] = None,
        without_overlay: Optional[bool] = None,
        multifamily_by_right: Optional[bool] = None,
        adu_allowed: Optional[bool] = None,
        min_lot_area_sqft_max: Optional[float] = None,
        max_height_ft_min: Optional[float] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ZoningSearchResponse:
        """Screen parcels by zoning

        ``GET /api/v1/zoning/search``

        Parcels by exact raw code (case-sensitive), base code, overlay, derived family, or parsed
        ordinance attribute. Attribute filters EXCLUDE parcels whose code is unparsed, so an empty
        result means unknown, not none; `dictionary_warning` and `coverage` say how much was parsed.
        Unknown parameters are a 400. Account required.

        Args:
            raw_code: Exact published code(s), comma-separated or repeated.
        """
        return cast("_t.ZoningSearchResponse", self._client._request(
            "GET",
            "/api/v1/zoning/search",
            query={
                "state_fips": state_fips,
                "county_fips": county_fips,
                "jurisdiction_id": jurisdiction_id,
                "raw_code": raw_code,
                "base_code": base_code,
                "family": family,
                "has_overlay": has_overlay,
                "without_overlay": without_overlay,
                "multifamily_by_right": multifamily_by_right,
                "adu_allowed": adu_allowed,
                "min_lot_area_sqft_max": min_lot_area_sqft_max,
                "max_height_ft_min": max_height_ft_min,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def coverage(
        self,
        *,
        state_fips: Optional[str] = None,
        jurisdiction_id: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ZoningCoverageResponse:
        """Zoning coverage per jurisdiction

        ``GET /api/v1/zoning/coverage``

        One row per registered zoning body with its honest `servingStatus` (served / partial /
        no_zoning / failed / registered) and reason, parcels matched against a measured denominator,
        distinct codes, overlays, and how many codes have parsed ordinance attributes (zeros
        included). Account required; the same table is on https://propraven.com/coverage.
        """
        return cast("_t.ZoningCoverageResponse", self._client._request(
            "GET",
            "/api/v1/zoning/coverage",
            query={
                "state_fips": state_fips,
                "jurisdiction_id": jurisdiction_id,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncZoningResource(AsyncAPIResource):
    """``client.zoning`` operations (async)."""

    async def parcel(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ZoningParcelResponse:
        """Zoning of a parcel, from the issuing jurisdiction

        ``GET /api/v1/parcels/{id}/zoning``

        The parcel's zoning code exactly as the issuing jurisdiction published it, the issuing body
        (a city or town, not the county), overlays as a set, split zoning, and, where the ordinance
        has been parsed, the underwriting attributes (minimum lot area, height, FAR/density,
        setbacks, by-right multifamily, ADU), each with its ordinance section, verbatim quote and
        link in `attributes.citations`. Null is never zero or false. `{ zoning: null, reason:
        "not_collected" }` means the parcel's jurisdiction has not been collected yet; it says
        nothing about whether the parcel is zoned. A research starting point, not a legal
        determination. Account required.

        Args:
            id: Parcel identifier: the canonical `state_fips:county_fips:parcel_id` form (e.g.
                `37:119:12104406`), the legacy 5-digit `county_fips5:parcel_id` form, or a PropRaven
                parcel UUID. URL-encode it.
        """
        return cast("_t.ZoningParcelResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/zoning",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def search(
        self,
        *,
        state_fips: Optional[str] = None,
        county_fips: Optional[str] = None,
        jurisdiction_id: Optional[str] = None,
        raw_code: Optional[str] = None,
        base_code: Optional[str] = None,
        family: Optional[str] = None,
        has_overlay: Optional[str] = None,
        without_overlay: Optional[bool] = None,
        multifamily_by_right: Optional[bool] = None,
        adu_allowed: Optional[bool] = None,
        min_lot_area_sqft_max: Optional[float] = None,
        max_height_ft_min: Optional[float] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ZoningSearchResponse:
        """Screen parcels by zoning

        ``GET /api/v1/zoning/search``

        Parcels by exact raw code (case-sensitive), base code, overlay, derived family, or parsed
        ordinance attribute. Attribute filters EXCLUDE parcels whose code is unparsed, so an empty
        result means unknown, not none; `dictionary_warning` and `coverage` say how much was parsed.
        Unknown parameters are a 400. Account required.

        Args:
            raw_code: Exact published code(s), comma-separated or repeated.
        """
        return cast("_t.ZoningSearchResponse", await self._client._request(
            "GET",
            "/api/v1/zoning/search",
            query={
                "state_fips": state_fips,
                "county_fips": county_fips,
                "jurisdiction_id": jurisdiction_id,
                "raw_code": raw_code,
                "base_code": base_code,
                "family": family,
                "has_overlay": has_overlay,
                "without_overlay": without_overlay,
                "multifamily_by_right": multifamily_by_right,
                "adu_allowed": adu_allowed,
                "min_lot_area_sqft_max": min_lot_area_sqft_max,
                "max_height_ft_min": max_height_ft_min,
                "limit": limit,
                "offset": offset,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def coverage(
        self,
        *,
        state_fips: Optional[str] = None,
        jurisdiction_id: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ZoningCoverageResponse:
        """Zoning coverage per jurisdiction

        ``GET /api/v1/zoning/coverage``

        One row per registered zoning body with its honest `servingStatus` (served / partial /
        no_zoning / failed / registered) and reason, parcels matched against a measured denominator,
        distinct codes, overlays, and how many codes have parsed ordinance attributes (zeros
        included). Account required; the same table is on https://propraven.com/coverage.
        """
        return cast("_t.ZoningCoverageResponse", await self._client._request(
            "GET",
            "/api/v1/zoning/coverage",
            query={
                "state_fips": state_fips,
                "jurisdiction_id": jurisdiction_id,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
