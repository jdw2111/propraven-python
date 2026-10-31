# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``permits`` namespace: ``client.permits``."""

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Literal, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._pagination import aiterate_cursor, iterate_cursor
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["PermitsResource", "AsyncPermitsResource"]


class PermitsResource(SyncAPIResource):
    """``client.permits`` operations (sync)."""

    def events(
        self,
        permit_id: str,
        *,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.PermitsEventsResponse:
        """Get one permit's events

        ``GET /api/v1/permits/{permitId}/events``

        One permit's inspections, fees, conditions (stipulations), plan reviews and other child
        records, as its jurisdiction publishes them, newest first (default 100, at most 500), with
        the true count and counts by type (#868). The permit_id is the one GET
        /api/v1/parcels/{id}/permits lists. ACCOUNT REQUIRED (the same access as the parcel permits
        route). The events' people fields (people_fields_published) count as ONE lookup per response
        against the account's monthly lookup cap; at the cap they are null and the events are still
        returned.

        Args:
            permit_id: The permit's permit_id, as GET /api/v1/parcels/{id}/permits lists it.
        """
        return cast("_t.PermitsEventsResponse", self._client._request(
            "GET",
            "/api/v1/permits/{permitId}/events",
            path_params={"permitId": permit_id},
            query={
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def search(
        self,
        *,
        permit_id: Optional[str] = None,
        permit_number: Optional[str] = None,
        address: Optional[str] = None,
        source: Optional[str] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        issued_from: Optional[str] = None,
        issued_to: Optional[str] = None,
        type: Optional[str] = None,
        status: Optional[str] = None,
        matched: Optional[Literal["any", "true", "false"]] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.PermitsSearchResponse:
        """Search permits, matched to a parcel or not

        ``GET /api/v1/permits/search``

        Find permits whether or not they are matched to a parcel (#868: about half of the permits
        served are not linked to a parcel, so GET /api/v1/parcels/{id}/permits cannot list them).
        Give one of permit_id (exact), permit_number (punctuation, spaces and case ignored), address
        (house number + street, with state or zip: suffixes, directionals and ordinals are
        normalised and a unit is ignored; a stored unit, city or zip after the street still matches)
        or source (the permit's jurisdiction_id, newest issued first). The other parameters filter;
        a state-only scan is refused (400 search_scope_required). Results are ordered issued_date
        DESC NULLS LAST, permit_id DESC and paged with an opaque keyset cursor (next_cursor). A
        request has a 15 s deadline: past it, 504 search_timeout with Retry-After. ACCOUNT REQUIRED;
        owner_name / applicant_name count as ONE people lookup per response, and at the cap they are
        null and the permits are still returned.

        Args:
            permit_id: Exact permit_id.
            permit_number: Permit number; punctuation, spaces and case are ignored.
            address: House number and street. Needs state or zip.
            source: The permit's jurisdiction_id (source dataset key).
            state: Two-letter state or 2-digit FIPS.
            zip: ZIP code. With an address and a state, rows that publish no zip are kept
                (address_basis.zip = not_published).
            city: City filter; rows that publish no city are kept.
            issued_from: Issued on or after.
            issued_to: Issued on or before.
            type: permit_type, permit_type_raw or permit_category (case-insensitive).
            status: permit_status (case-insensitive).
            matched: Only matched (true) or unmatched (false) permits.
            limit: Page size.
            cursor: next_cursor from the previous page.
        """
        return cast("_t.PermitsSearchResponse", self._client._request(
            "GET",
            "/api/v1/permits/search",
            query={
                "permit_id": permit_id,
                "permit_number": permit_number,
                "address": address,
                "source": source,
                "state": state,
                "zip": zip,
                "city": city,
                "issued_from": issued_from,
                "issued_to": issued_to,
                "type": type,
                "status": status,
                "matched": matched,
                "limit": limit,
                "cursor": cursor,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def search_iter(
        self,
        *,
        permit_id: Optional[str] = None,
        permit_number: Optional[str] = None,
        address: Optional[str] = None,
        source: Optional[str] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        issued_from: Optional[str] = None,
        issued_to: Optional[str] = None,
        type: Optional[str] = None,
        status: Optional[str] = None,
        matched: Optional[Literal["any", "true", "false"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[_t.PermitSearchResult]:
        """Search permits, matched to a parcel or not

        ``GET /api/v1/permits/search``

        Find permits whether or not they are matched to a parcel (#868: about half of the permits
        served are not linked to a parcel, so GET /api/v1/parcels/{id}/permits cannot list them).
        Give one of permit_id (exact), permit_number (punctuation, spaces and case ignored), address
        (house number + street, with state or zip: suffixes, directionals and ordinals are
        normalised and a unit is ignored; a stored unit, city or zip after the street still matches)
        or source (the permit's jurisdiction_id, newest issued first). The other parameters filter;
        a state-only scan is refused (400 search_scope_required). Results are ordered issued_date
        DESC NULLS LAST, permit_id DESC and paged with an opaque keyset cursor (next_cursor). A
        request has a 15 s deadline: past it, 504 search_timeout with Retry-After. ACCOUNT REQUIRED;
        owner_name / applicant_name count as ONE people lookup per response, and at the cap they are
        null and the permits are still returned.

        Auto-paginating iterator over every item (``data``) of :meth:`search`. Passes
        ``cursor=<next_cursor>`` until ``next_cursor`` is null/absent or ``hasMore`` is false.
        ``page_size`` is sent as ``limit``; ``max_items`` caps the number of items yielded.

        Args:
            permit_id: Exact permit_id.
            permit_number: Permit number; punctuation, spaces and case are ignored.
            address: House number and street. Needs state or zip.
            source: The permit's jurisdiction_id (source dataset key).
            state: Two-letter state or 2-digit FIPS.
            zip: ZIP code. With an address and a state, rows that publish no zip are kept
                (address_basis.zip = not_published).
            city: City filter; rows that publish no city are kept.
            issued_from: Issued on or after.
            issued_to: Issued on or before.
            type: permit_type, permit_type_raw or permit_category (case-insensitive).
            status: permit_status (case-insensitive).
            matched: Only matched (true) or unmatched (false) permits.
        """
        return iterate_cursor(
            lambda _limit, _pos: self.search(permit_id=permit_id, permit_number=permit_number, address=address, source=source, state=state, zip=zip, city=city, issued_from=issued_from, issued_to=issued_to, type=type, status=status, matched=matched, limit=_limit, cursor=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", next_key="next_cursor", page_size=page_size, max_items=max_items,
        )


class AsyncPermitsResource(AsyncAPIResource):
    """``client.permits`` operations (async)."""

    async def events(
        self,
        permit_id: str,
        *,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.PermitsEventsResponse:
        """Get one permit's events

        ``GET /api/v1/permits/{permitId}/events``

        One permit's inspections, fees, conditions (stipulations), plan reviews and other child
        records, as its jurisdiction publishes them, newest first (default 100, at most 500), with
        the true count and counts by type (#868). The permit_id is the one GET
        /api/v1/parcels/{id}/permits lists. ACCOUNT REQUIRED (the same access as the parcel permits
        route). The events' people fields (people_fields_published) count as ONE lookup per response
        against the account's monthly lookup cap; at the cap they are null and the events are still
        returned.

        Args:
            permit_id: The permit's permit_id, as GET /api/v1/parcels/{id}/permits lists it.
        """
        return cast("_t.PermitsEventsResponse", await self._client._request(
            "GET",
            "/api/v1/permits/{permitId}/events",
            path_params={"permitId": permit_id},
            query={
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def search(
        self,
        *,
        permit_id: Optional[str] = None,
        permit_number: Optional[str] = None,
        address: Optional[str] = None,
        source: Optional[str] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        issued_from: Optional[str] = None,
        issued_to: Optional[str] = None,
        type: Optional[str] = None,
        status: Optional[str] = None,
        matched: Optional[Literal["any", "true", "false"]] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.PermitsSearchResponse:
        """Search permits, matched to a parcel or not

        ``GET /api/v1/permits/search``

        Find permits whether or not they are matched to a parcel (#868: about half of the permits
        served are not linked to a parcel, so GET /api/v1/parcels/{id}/permits cannot list them).
        Give one of permit_id (exact), permit_number (punctuation, spaces and case ignored), address
        (house number + street, with state or zip: suffixes, directionals and ordinals are
        normalised and a unit is ignored; a stored unit, city or zip after the street still matches)
        or source (the permit's jurisdiction_id, newest issued first). The other parameters filter;
        a state-only scan is refused (400 search_scope_required). Results are ordered issued_date
        DESC NULLS LAST, permit_id DESC and paged with an opaque keyset cursor (next_cursor). A
        request has a 15 s deadline: past it, 504 search_timeout with Retry-After. ACCOUNT REQUIRED;
        owner_name / applicant_name count as ONE people lookup per response, and at the cap they are
        null and the permits are still returned.

        Args:
            permit_id: Exact permit_id.
            permit_number: Permit number; punctuation, spaces and case are ignored.
            address: House number and street. Needs state or zip.
            source: The permit's jurisdiction_id (source dataset key).
            state: Two-letter state or 2-digit FIPS.
            zip: ZIP code. With an address and a state, rows that publish no zip are kept
                (address_basis.zip = not_published).
            city: City filter; rows that publish no city are kept.
            issued_from: Issued on or after.
            issued_to: Issued on or before.
            type: permit_type, permit_type_raw or permit_category (case-insensitive).
            status: permit_status (case-insensitive).
            matched: Only matched (true) or unmatched (false) permits.
            limit: Page size.
            cursor: next_cursor from the previous page.
        """
        return cast("_t.PermitsSearchResponse", await self._client._request(
            "GET",
            "/api/v1/permits/search",
            query={
                "permit_id": permit_id,
                "permit_number": permit_number,
                "address": address,
                "source": source,
                "state": state,
                "zip": zip,
                "city": city,
                "issued_from": issued_from,
                "issued_to": issued_to,
                "type": type,
                "status": status,
                "matched": matched,
                "limit": limit,
                "cursor": cursor,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def search_iter(
        self,
        *,
        permit_id: Optional[str] = None,
        permit_number: Optional[str] = None,
        address: Optional[str] = None,
        source: Optional[str] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        issued_from: Optional[str] = None,
        issued_to: Optional[str] = None,
        type: Optional[str] = None,
        status: Optional[str] = None,
        matched: Optional[Literal["any", "true", "false"]] = None,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[_t.PermitSearchResult]:
        """Search permits, matched to a parcel or not

        ``GET /api/v1/permits/search``

        Find permits whether or not they are matched to a parcel (#868: about half of the permits
        served are not linked to a parcel, so GET /api/v1/parcels/{id}/permits cannot list them).
        Give one of permit_id (exact), permit_number (punctuation, spaces and case ignored), address
        (house number + street, with state or zip: suffixes, directionals and ordinals are
        normalised and a unit is ignored; a stored unit, city or zip after the street still matches)
        or source (the permit's jurisdiction_id, newest issued first). The other parameters filter;
        a state-only scan is refused (400 search_scope_required). Results are ordered issued_date
        DESC NULLS LAST, permit_id DESC and paged with an opaque keyset cursor (next_cursor). A
        request has a 15 s deadline: past it, 504 search_timeout with Retry-After. ACCOUNT REQUIRED;
        owner_name / applicant_name count as ONE people lookup per response, and at the cap they are
        null and the permits are still returned.

        Auto-paginating iterator over every item (``data``) of :meth:`search`. Passes
        ``cursor=<next_cursor>`` until ``next_cursor`` is null/absent or ``hasMore`` is false.
        ``page_size`` is sent as ``limit``; ``max_items`` caps the number of items yielded.

        Args:
            permit_id: Exact permit_id.
            permit_number: Permit number; punctuation, spaces and case are ignored.
            address: House number and street. Needs state or zip.
            source: The permit's jurisdiction_id (source dataset key).
            state: Two-letter state or 2-digit FIPS.
            zip: ZIP code. With an address and a state, rows that publish no zip are kept
                (address_basis.zip = not_published).
            city: City filter; rows that publish no city are kept.
            issued_from: Issued on or after.
            issued_to: Issued on or before.
            type: permit_type, permit_type_raw or permit_category (case-insensitive).
            status: permit_status (case-insensitive).
            matched: Only matched (true) or unmatched (false) permits.
        """
        async for item in aiterate_cursor(
            lambda _limit, _pos: self.search(permit_id=permit_id, permit_number=permit_number, address=address, source=source, state=state, zip=zip, city=city, issued_from=issued_from, issued_to=issued_to, type=type, status=status, matched=matched, limit=_limit, cursor=_pos, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", next_key="next_cursor", page_size=page_size, max_items=max_items,
        ):
            yield item
