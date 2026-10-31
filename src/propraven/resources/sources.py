# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``sources`` namespace: ``client.sources``."""

from __future__ import annotations

from typing import Any, AsyncIterator, Dict, Iterator, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._pagination import aiterate_cursor, iterate_cursor
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["SourcesResource", "AsyncSourcesResource"]


class SourcesResource(SyncAPIResource):
    """``client.sources`` operations (sync)."""

    def observations(
        self,
        source_id: str,
        *,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.SourcesObservationsResponse:
        """Read full-fidelity observations from a published source

        ``GET /api/v1/sources/{sourceId}/observations``

        Account and existing people verification/meter required. Original source fields and native
        geometry remain beside versioned normalization, provenance, flags and separate area/parcel
        links. Parcel-unmatched observations remain searchable by source. Private acquisition paths
        are not served. Existing confidentiality and live opt-out rules affect served copies;
        canonical originals stay private. Source issue/inspection dates are reported separately from
        pull time; unpublished/unqualified source returns503. Precision-sensitive integers/decimals
        use tagged exact text rather than lossy JSON numbers.

        Args:
            source_id: Published source identifier, for example billings-mt-permits.
            cursor: Exact source-specific next_cursor from the prior page; native public provenance
                cursors reject stale publication/run bindings.
        """
        return cast("_t.SourcesObservationsResponse", self._client._request(
            "GET",
            "/api/v1/sources/{sourceId}/observations",
            path_params={"sourceId": source_id},
            query={
                "cursor": cursor,
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def observations_iter(
        self,
        source_id: str,
        *,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Iterator[Dict[str, Any]]:
        """Read full-fidelity observations from a published source

        ``GET /api/v1/sources/{sourceId}/observations``

        Account and existing people verification/meter required. Original source fields and native
        geometry remain beside versioned normalization, provenance, flags and separate area/parcel
        links. Parcel-unmatched observations remain searchable by source. Private acquisition paths
        are not served. Existing confidentiality and live opt-out rules affect served copies;
        canonical originals stay private. Source issue/inspection dates are reported separately from
        pull time; unpublished/unqualified source returns503. Precision-sensitive integers/decimals
        use tagged exact text rather than lossy JSON numbers.

        Auto-paginating iterator over every item (``data``) of :meth:`observations`. Passes
        ``cursor=<next_cursor>`` until ``next_cursor`` is null/absent or ``hasMore`` is false.
        ``page_size`` is sent as ``limit``; ``max_items`` caps the number of items yielded.

        Args:
            source_id: Published source identifier, for example billings-mt-permits.
        """
        return iterate_cursor(
            lambda _limit, _pos: self.observations(source_id, cursor=_pos, limit=_limit, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", next_key="next_cursor", page_size=page_size, max_items=max_items,
        )


class AsyncSourcesResource(AsyncAPIResource):
    """``client.sources`` operations (async)."""

    async def observations(
        self,
        source_id: str,
        *,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.SourcesObservationsResponse:
        """Read full-fidelity observations from a published source

        ``GET /api/v1/sources/{sourceId}/observations``

        Account and existing people verification/meter required. Original source fields and native
        geometry remain beside versioned normalization, provenance, flags and separate area/parcel
        links. Parcel-unmatched observations remain searchable by source. Private acquisition paths
        are not served. Existing confidentiality and live opt-out rules affect served copies;
        canonical originals stay private. Source issue/inspection dates are reported separately from
        pull time; unpublished/unqualified source returns503. Precision-sensitive integers/decimals
        use tagged exact text rather than lossy JSON numbers.

        Args:
            source_id: Published source identifier, for example billings-mt-permits.
            cursor: Exact source-specific next_cursor from the prior page; native public provenance
                cursors reject stale publication/run bindings.
        """
        return cast("_t.SourcesObservationsResponse", await self._client._request(
            "GET",
            "/api/v1/sources/{sourceId}/observations",
            path_params={"sourceId": source_id},
            query={
                "cursor": cursor,
                "limit": limit,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def observations_iter(
        self,
        source_id: str,
        *,
        page_size: Optional[int] = None,
        max_items: Optional[int] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> AsyncIterator[Dict[str, Any]]:
        """Read full-fidelity observations from a published source

        ``GET /api/v1/sources/{sourceId}/observations``

        Account and existing people verification/meter required. Original source fields and native
        geometry remain beside versioned normalization, provenance, flags and separate area/parcel
        links. Parcel-unmatched observations remain searchable by source. Private acquisition paths
        are not served. Existing confidentiality and live opt-out rules affect served copies;
        canonical originals stay private. Source issue/inspection dates are reported separately from
        pull time; unpublished/unqualified source returns503. Precision-sensitive integers/decimals
        use tagged exact text rather than lossy JSON numbers.

        Auto-paginating iterator over every item (``data``) of :meth:`observations`. Passes
        ``cursor=<next_cursor>`` until ``next_cursor`` is null/absent or ``hasMore`` is false.
        ``page_size`` is sent as ``limit``; ``max_items`` caps the number of items yielded.

        Args:
            source_id: Published source identifier, for example billings-mt-permits.
        """
        async for item in aiterate_cursor(
            lambda _limit, _pos: self.observations(source_id, cursor=_pos, limit=_limit, extra_headers=extra_headers, extra_query=extra_query, timeout=timeout, max_retries=max_retries),
            items="data", next_key="next_cursor", page_size=page_size, max_items=max_items,
        ):
            yield item
