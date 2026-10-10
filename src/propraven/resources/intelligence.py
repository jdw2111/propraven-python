# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``intelligence`` namespace: ``client.intelligence``."""

from __future__ import annotations

from typing import Any, Literal, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["IntelligenceResource", "AsyncIntelligenceResource"]


class IntelligenceResource(SyncAPIResource):
    """``client.intelligence`` operations (sync)."""

    def signals(
        self,
        id: _t.IntelligenceParcelId,
        *,
        as_of: Optional[_t.IntelligenceInstant] = None,
        knowledge_cutoff: Optional[_t.IntelligenceInstant] = None,
        use: Optional[Literal["display", "ai"]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.IntelligenceSignalsResponse:
        """Get evidence-backed property signals

        ``GET /api/v1/parcels/{id}/signals``

        Requires API-key or first-party session authentication and a current account in the
        default-off server cohort. Valid current membership does not require a new paid
        subscription. Existing API quotas still apply. Responses are private, no-store. Unknown and
        repeated query parameters are rejected. This contract does not indicate source activation,
        deployment or an SDK release. Retained objects are scoped to the current account and their
        creator; no caller-supplied account/user grant is accepted. Current source rights are
        checked for every read/use, independently of archived grants. Assessment composition, where
        qualified, is not market value. Other groups remain explicitly unavailable without approved
        adapters. Exact values are numerator/denominator strings; historical runs exclude
        later-learned evidence.

        Args:
            id: URL-encoded canonical state_fips:county_fips:parcel_id or legacy county5:parcel_id.
                Bare APNs and UUIDs are not accepted here.
            as_of: Effective-time cutoff; explicit UTC timestamp. Defaults to the service capture
                clock. Future values rejected.
            knowledge_cutoff: Only observations known by this time contribute. Defaults to the same
                capture clock; original knowledge is never backdated from a publication or vintage.
            use: Requested use; checked against current source rights. Agent use is not an external
                send.
        """
        return cast("_t.IntelligenceSignalsResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/signals",
            path_params={"id": id},
            query={
                "as_of": as_of,
                "knowledge_cutoff": knowledge_cutoff,
                "use": use,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def run(
        self,
        run_id: _t.IntelligenceRetainedId,
        *,
        use: Optional[Literal["display", "export", "ai"]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.IntelligenceRunResponse:
        """Read an owned retained run and evidence

        ``GET /api/v1/intelligence/runs/{runId}``

        Requires API-key or first-party session authentication and a current account in the
        default-off server cohort. Valid current membership does not require a new paid
        subscription. Existing API quotas still apply. Responses are private, no-store. Unknown and
        repeated query parameters are rejected. This contract does not indicate source activation,
        deployment or an SDK release. Retained objects are scoped to the current account and their
        creator; no caller-supplied account/user grant is accepted. Current source rights are
        checked for every read/use, independently of archived grants. Withdrawn rights or changed
        source semantics may withhold a saved result; its immutable archived payload is not
        rewritten.

        Args:
            run_id: Retained 64-character lowercase SHA-256 run ID, owned by this account and
                creator.
            use: Requested use; checked against current source rights. Agent use is not an external
                send.
        """
        return cast("_t.IntelligenceRunResponse", self._client._request(
            "GET",
            "/api/v1/intelligence/runs/{runId}",
            path_params={"runId": run_id},
            query={
                "use": use,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def create_scenario(
        self,
        *,
        run_id: str,
        label: Literal["base", "downside", "upside"],
        assumptions: _t.IntelligenceScenarioInputAssumptions,
        parent_revision_id: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.IntelligenceCreateScenarioResponse:
        """Save an explicit named residual scenario

        ``POST /api/v1/intelligence/scenarios``

        Requires API-key or first-party session authentication and a current account in the
        default-off server cohort. Valid current membership does not require a new paid
        subscription. Existing API quotas still apply. Responses are private, no-store. No query
        parameters are used by this operation; its inputs are the strict JSON body. This contract
        does not indicate source activation, deployment or an SDK release. Retained objects are
        scoped to the current account and their creator; no caller-supplied account/user grant is
        accepted. Current source rights are checked for every read/use, independently of archived
        grants. Creates an immutable base/downside/upside revision linked to an owned readable run.
        A parent revision must belong to the same run and creator. Formula uses fixed-dollar profit
        and purchase-independent carry; no live values/default costs are invented. Negative
        residuals remain explicit. The JSON object is strict, bounded to 16,384 bytes, and costs
        must contain each of the five buckets once.
        """
        return cast("_t.IntelligenceCreateScenarioResponse", self._client._request(
            "POST",
            "/api/v1/intelligence/scenarios",
            body={
                "run_id": run_id,
                "label": label,
                "parent_revision_id": parent_revision_id,
                "assumptions": assumptions,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def handoff(
        self,
        run_id: _t.IntelligenceRetainedId,
        *,
        use: Optional[Literal["display", "export", "ai"]] = None,
        scenario_id: Optional[_t.IntelligenceRetainedId] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.IntelligenceHandoffResponse:
        """Prepare an owned structured investigation handoff

        ``GET /api/v1/intelligence/runs/{runId}/handoff``

        Requires API-key or first-party session authentication and a current account in the
        default-off server cohort. Valid current membership does not require a new paid
        subscription. Existing API quotas still apply. Responses are private, no-store. Unknown and
        repeated query parameters are rejected. This contract does not indicate source activation,
        deployment or an SDK release. Retained objects are scoped to the current account and their
        creator; no caller-supplied account/user grant is accepted. Current source rights are
        checked for every read/use, independently of archived grants. Returns the same retained
        calculations, evidence and optional saved scenario, with observations separated from user
        assumptions. The scenario must belong to the same run/creator. Delivery is
        structured_only_not_sent; no agent/model is started.

        Args:
            run_id: Retained 64-character lowercase SHA-256 run ID, owned by this account and
                creator.
            use: Requested use; checked against current source rights. Agent use is not an external
                send.
            scenario_id: Optional saved scenario revision belonging to the same run and creator.
        """
        return cast("_t.IntelligenceHandoffResponse", self._client._request(
            "GET",
            "/api/v1/intelligence/runs/{runId}/handoff",
            path_params={"runId": run_id},
            query={
                "use": use,
                "scenario_id": scenario_id,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncIntelligenceResource(AsyncAPIResource):
    """``client.intelligence`` operations (async)."""

    async def signals(
        self,
        id: _t.IntelligenceParcelId,
        *,
        as_of: Optional[_t.IntelligenceInstant] = None,
        knowledge_cutoff: Optional[_t.IntelligenceInstant] = None,
        use: Optional[Literal["display", "ai"]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.IntelligenceSignalsResponse:
        """Get evidence-backed property signals

        ``GET /api/v1/parcels/{id}/signals``

        Requires API-key or first-party session authentication and a current account in the
        default-off server cohort. Valid current membership does not require a new paid
        subscription. Existing API quotas still apply. Responses are private, no-store. Unknown and
        repeated query parameters are rejected. This contract does not indicate source activation,
        deployment or an SDK release. Retained objects are scoped to the current account and their
        creator; no caller-supplied account/user grant is accepted. Current source rights are
        checked for every read/use, independently of archived grants. Assessment composition, where
        qualified, is not market value. Other groups remain explicitly unavailable without approved
        adapters. Exact values are numerator/denominator strings; historical runs exclude
        later-learned evidence.

        Args:
            id: URL-encoded canonical state_fips:county_fips:parcel_id or legacy county5:parcel_id.
                Bare APNs and UUIDs are not accepted here.
            as_of: Effective-time cutoff; explicit UTC timestamp. Defaults to the service capture
                clock. Future values rejected.
            knowledge_cutoff: Only observations known by this time contribute. Defaults to the same
                capture clock; original knowledge is never backdated from a publication or vintage.
            use: Requested use; checked against current source rights. Agent use is not an external
                send.
        """
        return cast("_t.IntelligenceSignalsResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/signals",
            path_params={"id": id},
            query={
                "as_of": as_of,
                "knowledge_cutoff": knowledge_cutoff,
                "use": use,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def run(
        self,
        run_id: _t.IntelligenceRetainedId,
        *,
        use: Optional[Literal["display", "export", "ai"]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.IntelligenceRunResponse:
        """Read an owned retained run and evidence

        ``GET /api/v1/intelligence/runs/{runId}``

        Requires API-key or first-party session authentication and a current account in the
        default-off server cohort. Valid current membership does not require a new paid
        subscription. Existing API quotas still apply. Responses are private, no-store. Unknown and
        repeated query parameters are rejected. This contract does not indicate source activation,
        deployment or an SDK release. Retained objects are scoped to the current account and their
        creator; no caller-supplied account/user grant is accepted. Current source rights are
        checked for every read/use, independently of archived grants. Withdrawn rights or changed
        source semantics may withhold a saved result; its immutable archived payload is not
        rewritten.

        Args:
            run_id: Retained 64-character lowercase SHA-256 run ID, owned by this account and
                creator.
            use: Requested use; checked against current source rights. Agent use is not an external
                send.
        """
        return cast("_t.IntelligenceRunResponse", await self._client._request(
            "GET",
            "/api/v1/intelligence/runs/{runId}",
            path_params={"runId": run_id},
            query={
                "use": use,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def create_scenario(
        self,
        *,
        run_id: str,
        label: Literal["base", "downside", "upside"],
        assumptions: _t.IntelligenceScenarioInputAssumptions,
        parent_revision_id: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.IntelligenceCreateScenarioResponse:
        """Save an explicit named residual scenario

        ``POST /api/v1/intelligence/scenarios``

        Requires API-key or first-party session authentication and a current account in the
        default-off server cohort. Valid current membership does not require a new paid
        subscription. Existing API quotas still apply. Responses are private, no-store. No query
        parameters are used by this operation; its inputs are the strict JSON body. This contract
        does not indicate source activation, deployment or an SDK release. Retained objects are
        scoped to the current account and their creator; no caller-supplied account/user grant is
        accepted. Current source rights are checked for every read/use, independently of archived
        grants. Creates an immutable base/downside/upside revision linked to an owned readable run.
        A parent revision must belong to the same run and creator. Formula uses fixed-dollar profit
        and purchase-independent carry; no live values/default costs are invented. Negative
        residuals remain explicit. The JSON object is strict, bounded to 16,384 bytes, and costs
        must contain each of the five buckets once.
        """
        return cast("_t.IntelligenceCreateScenarioResponse", await self._client._request(
            "POST",
            "/api/v1/intelligence/scenarios",
            body={
                "run_id": run_id,
                "label": label,
                "parent_revision_id": parent_revision_id,
                "assumptions": assumptions,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def handoff(
        self,
        run_id: _t.IntelligenceRetainedId,
        *,
        use: Optional[Literal["display", "export", "ai"]] = None,
        scenario_id: Optional[_t.IntelligenceRetainedId] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.IntelligenceHandoffResponse:
        """Prepare an owned structured investigation handoff

        ``GET /api/v1/intelligence/runs/{runId}/handoff``

        Requires API-key or first-party session authentication and a current account in the
        default-off server cohort. Valid current membership does not require a new paid
        subscription. Existing API quotas still apply. Responses are private, no-store. Unknown and
        repeated query parameters are rejected. This contract does not indicate source activation,
        deployment or an SDK release. Retained objects are scoped to the current account and their
        creator; no caller-supplied account/user grant is accepted. Current source rights are
        checked for every read/use, independently of archived grants. Returns the same retained
        calculations, evidence and optional saved scenario, with observations separated from user
        assumptions. The scenario must belong to the same run/creator. Delivery is
        structured_only_not_sent; no agent/model is started.

        Args:
            run_id: Retained 64-character lowercase SHA-256 run ID, owned by this account and
                creator.
            use: Requested use; checked against current source rights. Agent use is not an external
                send.
            scenario_id: Optional saved scenario revision belonging to the same run and creator.
        """
        return cast("_t.IntelligenceHandoffResponse", await self._client._request(
            "GET",
            "/api/v1/intelligence/runs/{runId}/handoff",
            path_params={"runId": run_id},
            query={
                "use": use,
                "scenario_id": scenario_id,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
