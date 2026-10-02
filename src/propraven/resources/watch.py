# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``watch`` namespace: ``client.watch``."""

from __future__ import annotations

from typing import Any, Literal, Mapping, Optional, Sequence, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["WatchResource", "AsyncWatchResource"]


class WatchResource(SyncAPIResource):
    """``client.watch`` operations (sync)."""

    def list(
        self,
        *,
        credit_token: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WatchListResponse:
        """List your watches

        ``GET /api/v1/watch``

        List active watches for the X-CREDIT-TOKEN. Free.

        Args:
            credit_token (``X-CREDIT-TOKEN`` header): The pzc_ credit token (identity + wallet).
        """
        return cast("_t.WatchListResponse", self._client._request(
            "GET",
            "/api/v1/watch",
            headers={"X-CREDIT-TOKEN": credit_token},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def create(
        self,
        *,
        credit_token: str,
        filter: _t.WatchCreateParamsFilter,
        name: Optional[str] = None,
        event_types: Optional[Sequence[Literal["parcel.sold", "parcel.owner_changed", "parcel.permit_filed"]]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WatchCreateResponse:
        """Create a watch (free)

        ``POST /api/v1/watch``

        Create a watch tied to your credit token: a filter over parcels/geography + change event
        types. It reports changes going FORWARD; poll it to receive (and pay per delta for) new
        changes. Managing watches is free. Body: { filter, event_types?, name? } where filter is {
        parcel_ids:[...] } | { canonical_ids:[...] } | { state_fips } | { county_fips, state_fips }
        and event_types is a subset of parcel.sold / parcel.owner_changed / parcel.permit_filed
        (default all). Parcel ids (1–500) are canonical `state_fips:county_fips:parcel_id` ids,
        parcel UUIDs, or bare parcel_ids that name exactly ONE served parcel; a bare id that names
        several parcels is refused (422, candidates listed). The watch is stored and matched on
        canonical ids; `parcel_resolution` reports how each input resolved.

        Args:
            credit_token (``X-CREDIT-TOKEN`` header): The pzc_ credit token.
            event_types: Default: all three.
            filter: Exactly one shape: `{parcel_ids: [...]}` / `{canonical_ids: [...]}` (1-500 ids),
                `{state_fips}` or `{state_fips, county_fips}`.
        """
        return cast("_t.WatchCreateResponse", self._client._request(
            "POST",
            "/api/v1/watch",
            headers={"X-CREDIT-TOKEN": credit_token},
            body={
                "name": name,
                "event_types": event_types,
                "filter": filter,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def poll(
        self,
        id: str,
        *,
        credit_token: str,
        preview: Optional[bool] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WatchPollResponse:
        """Poll a watch for new changes (priced per delta)

        ``GET /api/v1/watch/{id}``

        Poll new parcel_deeds / parcel_permits changes matching the watch since its per-source
        cursor. preview=true returns the pending count + exact price + a masked sample (FREE, no
        cursor move). A paid poll debits the credit balance PER DELTA (clamp($0.05 x event-strength,
        $0.02, $0.20), capped $20/poll), advances the cursor, and returns the full deltas. A poll
        with no new changes is free. Insufficient balance -> 402. Parcel watches match on the full
        parcel identity; each delta carries `canonical_id` + `match_basis`. A watch created before
        2026-09-22 whose stored bare ids are ambiguous reports them in `identity_issues` (not
        matched) on every poll. Deed parties (grantor / grantee names and addresses, prior / new
        owner) are people data, delivered to accounts only: a poll paid with a credit token and no
        account (no API key, no signed-in session) receives the deltas with those fields set to null
        and a top-level `people_fields` marker (see PeopleFieldsWithheld). The events themselves
        (what changed, where, when, for how much) are unchanged.

        Args:
            id: The watch id (wat_...).
            preview: FREE count + price + masked sample; no cursor move.
            limit: Max deltas per source (default 50, max 200).
            credit_token (``X-CREDIT-TOKEN`` header): The pzc_ credit token.
        """
        return cast("_t.WatchPollResponse", self._client._request(
            "GET",
            "/api/v1/watch/{id}",
            path_params={"id": id},
            query={
                "preview": preview,
                "limit": limit,
            },
            headers={"X-CREDIT-TOKEN": credit_token},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def delete(
        self,
        id: str,
        *,
        credit_token: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WatchDeleteResponse:
        """Delete a watch

        ``DELETE /api/v1/watch/{id}``

        Deactivate a watch. Free.

        Args:
            id: The watch id.
            credit_token (``X-CREDIT-TOKEN`` header): The pzc_ credit token.
        """
        return cast("_t.WatchDeleteResponse", self._client._request(
            "DELETE",
            "/api/v1/watch/{id}",
            path_params={"id": id},
            headers={"X-CREDIT-TOKEN": credit_token},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncWatchResource(AsyncAPIResource):
    """``client.watch`` operations (async)."""

    async def list(
        self,
        *,
        credit_token: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WatchListResponse:
        """List your watches

        ``GET /api/v1/watch``

        List active watches for the X-CREDIT-TOKEN. Free.

        Args:
            credit_token (``X-CREDIT-TOKEN`` header): The pzc_ credit token (identity + wallet).
        """
        return cast("_t.WatchListResponse", await self._client._request(
            "GET",
            "/api/v1/watch",
            headers={"X-CREDIT-TOKEN": credit_token},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def create(
        self,
        *,
        credit_token: str,
        filter: _t.WatchCreateParamsFilter,
        name: Optional[str] = None,
        event_types: Optional[Sequence[Literal["parcel.sold", "parcel.owner_changed", "parcel.permit_filed"]]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WatchCreateResponse:
        """Create a watch (free)

        ``POST /api/v1/watch``

        Create a watch tied to your credit token: a filter over parcels/geography + change event
        types. It reports changes going FORWARD; poll it to receive (and pay per delta for) new
        changes. Managing watches is free. Body: { filter, event_types?, name? } where filter is {
        parcel_ids:[...] } | { canonical_ids:[...] } | { state_fips } | { county_fips, state_fips }
        and event_types is a subset of parcel.sold / parcel.owner_changed / parcel.permit_filed
        (default all). Parcel ids (1–500) are canonical `state_fips:county_fips:parcel_id` ids,
        parcel UUIDs, or bare parcel_ids that name exactly ONE served parcel; a bare id that names
        several parcels is refused (422, candidates listed). The watch is stored and matched on
        canonical ids; `parcel_resolution` reports how each input resolved.

        Args:
            credit_token (``X-CREDIT-TOKEN`` header): The pzc_ credit token.
            event_types: Default: all three.
            filter: Exactly one shape: `{parcel_ids: [...]}` / `{canonical_ids: [...]}` (1-500 ids),
                `{state_fips}` or `{state_fips, county_fips}`.
        """
        return cast("_t.WatchCreateResponse", await self._client._request(
            "POST",
            "/api/v1/watch",
            headers={"X-CREDIT-TOKEN": credit_token},
            body={
                "name": name,
                "event_types": event_types,
                "filter": filter,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def poll(
        self,
        id: str,
        *,
        credit_token: str,
        preview: Optional[bool] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WatchPollResponse:
        """Poll a watch for new changes (priced per delta)

        ``GET /api/v1/watch/{id}``

        Poll new parcel_deeds / parcel_permits changes matching the watch since its per-source
        cursor. preview=true returns the pending count + exact price + a masked sample (FREE, no
        cursor move). A paid poll debits the credit balance PER DELTA (clamp($0.05 x event-strength,
        $0.02, $0.20), capped $20/poll), advances the cursor, and returns the full deltas. A poll
        with no new changes is free. Insufficient balance -> 402. Parcel watches match on the full
        parcel identity; each delta carries `canonical_id` + `match_basis`. A watch created before
        2026-09-22 whose stored bare ids are ambiguous reports them in `identity_issues` (not
        matched) on every poll. Deed parties (grantor / grantee names and addresses, prior / new
        owner) are people data, delivered to accounts only: a poll paid with a credit token and no
        account (no API key, no signed-in session) receives the deltas with those fields set to null
        and a top-level `people_fields` marker (see PeopleFieldsWithheld). The events themselves
        (what changed, where, when, for how much) are unchanged.

        Args:
            id: The watch id (wat_...).
            preview: FREE count + price + masked sample; no cursor move.
            limit: Max deltas per source (default 50, max 200).
            credit_token (``X-CREDIT-TOKEN`` header): The pzc_ credit token.
        """
        return cast("_t.WatchPollResponse", await self._client._request(
            "GET",
            "/api/v1/watch/{id}",
            path_params={"id": id},
            query={
                "preview": preview,
                "limit": limit,
            },
            headers={"X-CREDIT-TOKEN": credit_token},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def delete(
        self,
        id: str,
        *,
        credit_token: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.WatchDeleteResponse:
        """Delete a watch

        ``DELETE /api/v1/watch/{id}``

        Deactivate a watch. Free.

        Args:
            id: The watch id.
            credit_token (``X-CREDIT-TOKEN`` header): The pzc_ credit token.
        """
        return cast("_t.WatchDeleteResponse", await self._client._request(
            "DELETE",
            "/api/v1/watch/{id}",
            path_params={"id": id},
            headers={"X-CREDIT-TOKEN": credit_token},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
