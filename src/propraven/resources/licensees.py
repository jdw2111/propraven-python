# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``licensees`` namespace: ``client.licensees``."""

from __future__ import annotations

from typing import Any, Literal, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["LicenseesResource", "AsyncLicenseesResource"]


class LicenseesResource(SyncAPIResource):
    """``client.licensees`` operations (sync)."""

    def firms(
        self,
        *,
        state: Literal["FL", "CA", "NY", "CT", "VA"],
        profession: Optional[Literal["real_estate", "insurance", "cpa", "cam"]] = None,
        city: Optional[str] = None,
        zip: Optional[str] = None,
        status: Optional[Literal["active", "inactive", "delinquent", "void", "expired", "other", "any"]] = None,
        min_locations: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.LicenseesFirmsResponse:
        """Search licensed firms in a place

        ``GET /api/v1/licensees/firms``

        Firms licensed by the issuing state boards (FL DBPR and DFS, CA DRE and the Board of
        Accountancy, NY DOS, CT DCP, VA DPOR) in one city or zip, grouped by name and by the
        issuer's parent-license link, with their distinct street locations. `min_locations=3` finds
        firms with at least three licensed locations there. Requires an account; a person-shaped
        firm is people data and each response serving one is logged. 503
        `licensee_layer_unavailable` until the layer is loaded.

        Args:
            state: A state the licensee layer serves (Texas licensee files are a QA witness and
                never served).
            profession: License profession.
            city: City as the licensee address publishes it (case-insensitive). A city or a zip is
                required.
            zip: 5-digit ZIP. A city or a zip is required.
            status: License status as published, mapped.
            min_locations: Minimum distinct locations per firm in the place.
            limit: Firms returned (largest first).
        """
        return cast("_t.LicenseesFirmsResponse", self._client._request(
            "GET",
            "/api/v1/licensees/firms",
            query={
                "state": state,
                "profession": profession,
                "city": city,
                "zip": zip,
                "status": status,
                "min_locations": min_locations,
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncLicenseesResource(AsyncAPIResource):
    """``client.licensees`` operations (async)."""

    async def firms(
        self,
        *,
        state: Literal["FL", "CA", "NY", "CT", "VA"],
        profession: Optional[Literal["real_estate", "insurance", "cpa", "cam"]] = None,
        city: Optional[str] = None,
        zip: Optional[str] = None,
        status: Optional[Literal["active", "inactive", "delinquent", "void", "expired", "other", "any"]] = None,
        min_locations: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.LicenseesFirmsResponse:
        """Search licensed firms in a place

        ``GET /api/v1/licensees/firms``

        Firms licensed by the issuing state boards (FL DBPR and DFS, CA DRE and the Board of
        Accountancy, NY DOS, CT DCP, VA DPOR) in one city or zip, grouped by name and by the
        issuer's parent-license link, with their distinct street locations. `min_locations=3` finds
        firms with at least three licensed locations there. Requires an account; a person-shaped
        firm is people data and each response serving one is logged. 503
        `licensee_layer_unavailable` until the layer is loaded.

        Args:
            state: A state the licensee layer serves (Texas licensee files are a QA witness and
                never served).
            profession: License profession.
            city: City as the licensee address publishes it (case-insensitive). A city or a zip is
                required.
            zip: 5-digit ZIP. A city or a zip is required.
            status: License status as published, mapped.
            min_locations: Minimum distinct locations per firm in the place.
            limit: Firms returned (largest first).
        """
        return cast("_t.LicenseesFirmsResponse", await self._client._request(
            "GET",
            "/api/v1/licensees/firms",
            query={
                "state": state,
                "profession": profession,
                "city": city,
                "zip": zip,
                "status": status,
                "min_locations": min_locations,
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
