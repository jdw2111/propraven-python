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
        state: Literal["FL", "CA", "NY", "CT", "VA", "AZ", "OH", "OR", "NJ", "WV"],
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
        Accountancy, NY DOS, CT DCP, VA DPOR, AZ ADRE, OH Division of Real Estate, OR Real Estate
        Agency, NJ Division of Consumer Affairs, WV Real Estate Commission) in one city or zip,
        grouped by name and by the issuer's parent-license link, with their distinct street
        locations. `min_locations=3` finds firms with at least three licensed locations there.
        Requires an account; a person-shaped firm is people data and each response serving one is
        logged. 503 `licensee_layer_unavailable` until the layer is loaded.

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

    def individuals(
        self,
        *,
        state: Literal["NV", "OR", "WV"],
        name: Optional[str] = None,
        license_number: Optional[str] = None,
        city: Optional[str] = None,
        zip: Optional[str] = None,
        profession: Optional[Literal["real_estate", "cam"]] = None,
        status: Optional[Literal["active", "inactive", "void", "expired", "other", "any"]] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.LicenseesIndividualsResponse:
        """Search licensed individuals (people data)

        ``GET /api/v1/licensees/individuals``

        Licensed individuals as their boards publish them: Nevada Real Estate Division (brokers,
        property managers, community managers), Oregon Real Estate Agency (brokers, principal
        brokers, property managers; active and inactive) and West Virginia Real Estate Commission
        (brokers). Search by name (every word, any order), license_number, city or zip. People data:
        requires an account (an anonymous call gets 401), each page that serves rows counts as one
        lookup and is logged, and a person on the privacy suppression list is withheld
        (`privacy_suppressed`). The address is the board's published address with the board's own
        label; it is not a claim that the person works there. 503 `licensee_layer_unavailable` until
        the list is loaded.

        Args:
            state: A state whose individual licensees are served.
            name: Name words (at least 3 letters); every word must appear in the published name, in
                any order. One of name, license_number, city or zip is required.
            license_number: License number as published (exact, case-insensitive).
            city: City of the published address (case-insensitive).
            zip: 5-digit ZIP of the published address.
            profession: License profession.
            status: License status as published, mapped.
            limit: Individuals returned (name order).
        """
        return cast("_t.LicenseesIndividualsResponse", self._client._request(
            "GET",
            "/api/v1/licensees/individuals",
            query={
                "state": state,
                "name": name,
                "license_number": license_number,
                "city": city,
                "zip": zip,
                "profession": profession,
                "status": status,
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
        state: Literal["FL", "CA", "NY", "CT", "VA", "AZ", "OH", "OR", "NJ", "WV"],
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
        Accountancy, NY DOS, CT DCP, VA DPOR, AZ ADRE, OH Division of Real Estate, OR Real Estate
        Agency, NJ Division of Consumer Affairs, WV Real Estate Commission) in one city or zip,
        grouped by name and by the issuer's parent-license link, with their distinct street
        locations. `min_locations=3` finds firms with at least three licensed locations there.
        Requires an account; a person-shaped firm is people data and each response serving one is
        logged. 503 `licensee_layer_unavailable` until the layer is loaded.

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

    async def individuals(
        self,
        *,
        state: Literal["NV", "OR", "WV"],
        name: Optional[str] = None,
        license_number: Optional[str] = None,
        city: Optional[str] = None,
        zip: Optional[str] = None,
        profession: Optional[Literal["real_estate", "cam"]] = None,
        status: Optional[Literal["active", "inactive", "void", "expired", "other", "any"]] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.LicenseesIndividualsResponse:
        """Search licensed individuals (people data)

        ``GET /api/v1/licensees/individuals``

        Licensed individuals as their boards publish them: Nevada Real Estate Division (brokers,
        property managers, community managers), Oregon Real Estate Agency (brokers, principal
        brokers, property managers; active and inactive) and West Virginia Real Estate Commission
        (brokers). Search by name (every word, any order), license_number, city or zip. People data:
        requires an account (an anonymous call gets 401), each page that serves rows counts as one
        lookup and is logged, and a person on the privacy suppression list is withheld
        (`privacy_suppressed`). The address is the board's published address with the board's own
        label; it is not a claim that the person works there. 503 `licensee_layer_unavailable` until
        the list is loaded.

        Args:
            state: A state whose individual licensees are served.
            name: Name words (at least 3 letters); every word must appear in the published name, in
                any order. One of name, license_number, city or zip is required.
            license_number: License number as published (exact, case-insensitive).
            city: City of the published address (case-insensitive).
            zip: 5-digit ZIP of the published address.
            profession: License profession.
            status: License status as published, mapped.
            limit: Individuals returned (name order).
        """
        return cast("_t.LicenseesIndividualsResponse", await self._client._request(
            "GET",
            "/api/v1/licensees/individuals",
            query={
                "state": state,
                "name": name,
                "license_number": license_number,
                "city": city,
                "zip": zip,
                "profession": profession,
                "status": status,
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
