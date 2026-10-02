# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``parcels`` namespace: ``client.parcels``."""

from __future__ import annotations

from typing import Any, Literal, Mapping, Optional, Sequence, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["ParcelsResource", "AsyncParcelsResource"]


class ParcelsResource(SyncAPIResource):
    """``client.parcels`` operations (sync)."""

    def assessment_history(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsAssessmentHistoryResponse:
        """Get recorded annual assessment history

        ``GET /api/v1/parcels/{id}/assessment-history``

        Returns source-backed historical assessment observations from published county history. Uses
        exact national parcel identity. Never substitutes the current parcel snapshot. Unknown
        assessment years remain null; vintage years and tax years are distinct. Missing years are
        not interpolated. County coverage can be partial by town and year. Unpublished coverage and
        failed reads return 503, not an empty history. Requires normal API or first-party session
        authentication.

        Args:
            id: Canonical state_fips:county_fips:parcel_id, legacy county5:parcel_id, or parcel
                UUID.
        """
        return cast("_t.ParcelsAssessmentHistoryResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/assessment-history",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def get(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsGetResponse:
        """Get parcel by ID

        ``GET /api/v1/parcels/{id}``

        Retrieve a single parcel by its composite ID (county_fips:parcel_id).

        Args:
            id: Composite parcel identifier in the format county_fips:parcel_id (e.g.,
                37:119:12104406).
        """
        return cast("_t.ParcelsGetResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def owner(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsOwnerResponse:
        """Get parcel owner details and portfolio

        ``GET /api/v1/parcels/{id}/owner``

        Retrieve the owner of a parcel along with their portfolio summary and list of properties.

        Args:
            id: Composite parcel identifier (county_fips:parcel_id).
        """
        return cast("_t.ParcelsOwnerResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/owner",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def permits(
        self,
        id: str,
        *,
        shape: Optional[Literal["envelope"]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsPermitsResponse:
        """Get parcel permits

        ``GET /api/v1/parcels/{id}/permits``

        Retrieve building and construction permits associated with a parcel.

        Args:
            id: Composite parcel identifier (county_fips:parcel_id).
            shape: Body shape. Omit for the default bare array of up to 100 permit rows (newest
                first); `envelope` returns `{ data, permit_count, permit_count_basis, truncated,
                row_cap }`, where `permit_count` is the parcel's true count when
                `permit_count_basis` is `exact` and the size of the capped window (a floor) when
                `capped`, and `truncated` is true when the parcel has more permits than `data`
                carries.
        """
        return cast("_t.ParcelsPermitsResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/permits",
            path_params={"id": id},
            query={
                "shape": shape,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def deeds(
        self,
        id: str,
        *,
        shape: Optional[Literal["envelope"]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsDeedsResponse:
        """Get parcel deed history

        ``GET /api/v1/parcels/{id}/deeds``

        Retrieve deed transactions and transfer history for a parcel.

        Args:
            id: Composite parcel identifier (county_fips:parcel_id).
            shape: Body shape. Omit for the default bare array of deed rows; `envelope` returns the
                typed envelope with a `status` header and the frozen `known_deed_count`.
        """
        return cast("_t.ParcelsDeedsResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/deeds",
            path_params={"id": id},
            query={
                "shape": shape,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def risks(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsRisksResponse:
        """Get parcel risk assessment

        ``GET /api/v1/parcels/{id}/risks``

        Retrieve flood, wildfire, air quality, and crime risk data for a parcel.

        Args:
            id: Composite parcel identifier (county_fips:parcel_id).
        """
        return cast("_t.ParcelsRisksResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/risks",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def geojson(
        self,
        *,
        bbox: str,
        zoom: int,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsGeojsonResponse:
        """Parcel polygons as GeoJSON for a bounding box

        ``GET /api/v1/parcels/geojson``

        Returns parcel polygons inside a bounding box as a GeoJSON FeatureCollection. Only served at
        zoom ≥ 14 to limit data volume — coarser bbox returns an empty collection. Each feature's
        properties include parcel_id, county_fips, owner_name, assessed value, and basic attributes
        for rendering popups.

        Args:
            bbox: Bounding box `west,south,east,north`.
            zoom: Map zoom level. Below 14 returns an empty collection.
        """
        return cast("_t.ParcelsGeojsonResponse", self._client._request(
            "GET",
            "/api/v1/parcels/geojson",
            query={
                "bbox": bbox,
                "zoom": zoom,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def report(
        self,
        id: str,
        *,
        county_fips: Optional[str] = None,
        sections: Optional[str] = None,
        fields: Optional[str] = None,
        include_provenance: Optional[bool] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsReportResponse:
        """Parcel dossier (paid, provenance-first)

        ``GET /api/v1/parcels/{id}/report``

        The Machine Storefront's per-parcel dossier: a single provenance-first JSON payload carrying
        every POPULATED field for the parcel as `{name, value}` (by default: no `sections`/`fields`
        params delivers everything the quote was priced on), plus the real deeds / comparable-sales
        / permits sub-tables. The per-field receipts (source, as_of, confidence, coverage tier) are
        opt-in: `?include_provenance=true` adds a `provenance` map keyed by field name. `?sections=`
        (identity, valuation, owner, hazard, permits, deeds, market, demographics, `core`, `all`)
        and `?fields=` narrow the delivered field list; anything narrowed out is NAMED in
        `meta.projection.omitted_fields`, and the price never changes with the projection. A ~50 KB
        soft cap applies to the `fields` portion only. The GeoJSON boundary is held out as a
        separately-priced add-on the base payload omits.

        PRICE (value-tiered, per parcel): price = clamp($5 x V(asset value) x R(data richness) x
        F(freshness), $2, $20). The exact amount for a given parcel is quoted, before payment, by
        GET /api/v1/storefront/availability?parcel_id=... and is what the 402 advertises in
        accepts[0].maxAmountRequired (USDC atomic units, 6 decimals).

        ACCESS requires ONE of: (a) x402 pay-per-call -- send a base64 signed x402 PaymentPayload in
        the `X-PAYMENT` header; on a successful build the dossier is returned and the on-chain
        settlement receipt is in the `X-PAYMENT-RESPONSE` response header. No account is needed for
        the parcel record, but PEOPLE DATA (owner names, owner mailing addresses, entity principals,
        deed and sale party names and addresses) is delivered to accounts only: a wallet-only or
        credit-token buyer receives the dossier with those fields set to null and a top-level
        `people_fields` marker (see PeopleFieldsWithheld), and the price is computed on exactly that
        body, so it never counts a field the buyer does not receive. Send your API key with the
        payment to receive them. (b) A genuine PAID PropRaven subscription entitlement -- the
        dossier is served on the subscription invoice. Being merely authenticated is NOT sufficient:
        a free-tier key, or a self-service first-party key with no paid plan, receives a 402. (c)
        Anything else -> HTTP 402 whose `accepts` array carries the exact x402 payment requirements
        for this parcel.

        Args:
            id: Parcel ID. Composite `county_fips:parcel_id` or county-local id when `county_fips`
                query param is provided.
            county_fips: 5-digit county FIPS. Strongly recommended when passing a county-local id.
            sections: Comma-separated report sections to deliver in `fields`: identity, valuation,
                owner, hazard, permits, deeds, market, demographics, `core` (the first four) or
                `all`. Omit (with no `fields`) for `all` — every populated field the quote was
                priced on. The compact core is delivered only on an explicit `core`.
            fields: Comma-separated parcels_serving column names to deliver on top of `sections`.
            include_provenance: `true` attaches the per-field receipts map (`provenance`, keyed by
                field name: source, as_of, confidence, coverage, tier). Off by default — the
                receipts are epoch catalog metadata and roughly triple the payload.
            payment (``X-PAYMENT`` header): x402 payment: a base64-encoded signed x402
                PaymentPayload (EIP-3009 transferWithAuthorization over USDC on Base). Present it to
                pay per call with no API key; the signed amount must equal this parcel's quoted
                maxAmountRequired (see the 402 body or /storefront/availability?parcel_id=). Omit it
                to be served only if your key holds a paid subscription entitlement; otherwise you
                receive a 402 carrying the payment requirements.
        """
        return cast("_t.ParcelsReportResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/report",
            path_params={"id": id},
            query={
                "county_fips": county_fips,
                "sections": sections,
                "fields": fields,
                "include_provenance": include_provenance,
            },
            headers={"X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def comp_pack(
        self,
        id: str,
        *,
        n: Optional[int] = None,
        radius: Optional[float] = None,
        preview: Optional[bool] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsCompPackResponse:
        """Comp pack (paid, priced per pack) — with a FREE preview

        ``GET /api/v1/parcels/{id}/comp-pack``

        The Machine Storefront's comp pack: a subject valuation INDICATED BY comparable sales,
        wrapped with the comps that prove it. Answers the underwriting question "what is this worth,
        and which sales prove it?".

        The comps are the SAME precomputed comparable_sales the free GET /api/v1/parcels/{id}/comps
        route serves; the subject's valuation fields come from parcels_serving. The indicated value
        is derived transparently (median comp $/sqft x subject sqft when both are known, else the
        median comp sale price) with an interquartile range, and is reconstructable from the comps
        in the same payload -- never a black-box AVM.

        PRICE: per pack = clamp($2 x V(subject value) x Q(comp support), $1, $20). Q ramps on the
        comp count with a small bonus for high median similarity. A subject with ZERO precomputed
        comps has no evidence to support a number and is returned free, never charged. The exact
        price is advertised in the 402's accepts[0].maxAmountRequired (USDC atomic units, 6
        decimals).

        FREE PREVIEW: add preview=true for the subject summary, the comp count + median similarity,
        the exact price, and up to three MASKED comps (parcel/APN withheld, sale price rounded, date
        to the year). The precise indicated value and the unmasked comps are the paid product.

        PAID ACCESS (preview omitted) requires ONE of: (a) x402 pay-per-call via a base64 signed
        x402 PaymentPayload in the `X-PAYMENT` header (receipt in `X-PAYMENT-RESPONSE`); (b) a
        genuine PAID PropRaven subscription entitlement; (c) anything else -> HTTP 402 whose
        `accepts` carries the exact requirements.

        Args:
            id: Parcel id: canonical state:county:parcel, 5-digit-county:parcel, or a parcel UUID.
            n: How many comps back the pack.
            radius: Optional post-filter: keep only precomputed comps within this many miles.
            preview: FREE try-before-buy: subject summary, comp count, exact price and three masked
                comps. No payment.
            payment (``X-PAYMENT`` header): Base64-encoded x402 PaymentPayload (EIP-3009 signed).
                Present it to pay per call for the full pack.
        """
        return cast("_t.ParcelsCompPackResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/comp-pack",
            path_params={"id": id},
            query={
                "n": n,
                "radius": radius,
                "preview": preview,
            },
            headers={"X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def risk_score(
        self,
        id: str,
        *,
        preview: Optional[bool] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsRiskScoreResponse:
        """Risk score (paid, priced per assessment) — with a FREE preview

        ``GET /api/v1/parcels/{id}/risk-score``

        The Machine Storefront's risk score: a multi-hazard risk assessment for one parcel, anchored
        on FEMA's National Risk Index COMPOSITE (nri_risk_score 0-100 + rating) with the flood /
        seismic / windstorm / wildfire / air-quality / crime breakdown that supports it. Answers
        "what could go wrong with this asset?". The headline is FEMA's own methodology, not an
        invented weighting.

        Reuses the SAME panel the free GET /api/v1/parcels/{id}/risks route serves
        (getParcelRisksData) plus the NRI composite + flood detail from parcels_serving.

        PRICE: per assessment = clamp($0.60 x V(asset value) x C(hazard coverage), $0.20, $20). C
        ramps on how many independent hazard layers resolved. A parcel with ZERO layers is returned
        free, never charged. The cheapest paid SKU. The exact price is in the 402's
        accepts[0].maxAmountRequired (USDC atomic units).

        FREE PREVIEW: add preview=true for the subject, WHICH hazard layers resolved, and the exact
        price. The precise NRI score and the hazard breakdown are the paid product.

        PAID ACCESS: (a) x402 via a base64 signed PaymentPayload in `X-PAYMENT` (receipt in
        `X-PAYMENT-RESPONSE`); (b) a genuine PAID subscription entitlement; (c) else HTTP 402 with
        the exact requirements.

        Args:
            id: Parcel id: canonical state:county:parcel, 5-digit-county:parcel, or a parcel UUID.
            preview: FREE try-before-buy: subject, resolved hazard layers, and the exact price. No
                payment.
            payment (``X-PAYMENT`` header): Base64-encoded x402 PaymentPayload (EIP-3009 signed).
                Present it to pay per call.
        """
        return cast("_t.ParcelsRiskScoreResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/risk-score",
            path_params={"id": id},
            query={
                "preview": preview,
            },
            headers={"X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def traffic_history(
        self,
        id: str,
        *,
        lat: float,
        lng: float,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsTrafficHistoryResponse:
        """Nearest traffic station + AADT history

        ``GET /api/v1/parcels/{id}/traffic-history``

        Finds the AADT (annual average daily traffic) station nearest to the given coordinates and
        returns its historical time series plus 3/5/7-year CAGRs. Useful for retail / CRE site
        selection. Search radius ~2 miles; returns empty data if no station is in range.

        Args:
            id: Parcel ID (used for context only; the actual nearest-station search is by lat/lng).
            lat: Latitude.
            lng: Longitude.
        """
        return cast("_t.ParcelsTrafficHistoryResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/traffic-history",
            path_params={"id": id},
            query={
                "lat": lat,
                "lng": lng,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def batch(
        self,
        *,
        tuples: Sequence[_t.ParcelsBatchParamsTuplesItem],
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsBatchResponse:
        """Fetch up to 100 parcels by (state, county, parcel) tuple

        ``POST /api/v1/parcels/batch``

        Card-projection rows for up to 100 unique `(state_fips, county_fips, parcel_id)` tuples.
        `county_fips` is the 3-digit within-state code (a 5-digit value is refused with a 400 naming
        the fix). Tuples with no match are listed in `missing`.
        """
        return cast("_t.ParcelsBatchResponse", self._client._request(
            "POST",
            "/api/v1/parcels/batch",
            body={
                "tuples": tuples,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def comps(
        self,
        id: str,
        *,
        n: Optional[int] = None,
        radius: Optional[float] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsCompsResponse:
        """Comparable sales for a parcel

        ``GET /api/v1/parcels/{id}/comps``

        Precomputed comparable sales near the parcel (`tier` names the comp source).

        Args:
            id: Parcel identifier: the canonical `state_fips:county_fips:parcel_id` form (e.g.
                `37:119:12104406`), the legacy 5-digit `county_fips5:parcel_id` form, or a PropRaven
                parcel UUID. URL-encode it.
            n: Number of comps (1-25).
            radius: Search radius in miles.
        """
        return cast("_t.ParcelsCompsResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/comps",
            path_params={"id": id},
            query={
                "n": n,
                "radius": radius,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def occupants(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsOccupantsResponse:
        """Business occupants of a parcel

        ``GET /api/v1/parcels/{id}/occupants``

        Businesses matched to the parcel (names, brands, categories, match confidence), primary
        occupant first. At most 100 rows; `truncated` says when more exist.

        Args:
            id: Parcel identifier: the canonical `state_fips:county_fips:parcel_id` form (e.g.
                `37:119:12104406`), the legacy 5-digit `county_fips5:parcel_id` form, or a PropRaven
                parcel UUID. URL-encode it.
        """
        return cast("_t.ParcelsOccupantsResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/occupants",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def violations(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsViolationsResponse:
        """Code violations on a parcel

        ``GET /api/v1/parcels/{id}/violations``

        Municipal code-enforcement cases matched to the parcel, with the source coverage that says
        whether an empty list means 'none recorded' or 'not collected here'.

        Args:
            id: Parcel identifier: the canonical `state_fips:county_fips:parcel_id` form (e.g.
                `37:119:12104406`), the legacy 5-digit `county_fips5:parcel_id` form, or a PropRaven
                parcel UUID. URL-encode it.
        """
        return cast("_t.ParcelsViolationsResponse", self._client._request(
            "GET",
            "/api/v1/parcels/{id}/violations",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def pois(
        self,
        *,
        bbox: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsPoisResponse:
        """Business parcels in a small bounding box

        ``GET /api/v1/parcels/poi``

        Up to 250 parcels with a recorded business type inside `bbox`, highest assessed value first.
        Boxes larger than 0.03 square degrees return an empty list.

        Args:
            bbox: `west,south,east,north` in decimal degrees.
        """
        return cast("_t.ParcelsPoisResponse", self._client._request(
            "GET",
            "/api/v1/parcels/poi",
            query={
                "bbox": bbox,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncParcelsResource(AsyncAPIResource):
    """``client.parcels`` operations (async)."""

    async def assessment_history(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsAssessmentHistoryResponse:
        """Get recorded annual assessment history

        ``GET /api/v1/parcels/{id}/assessment-history``

        Returns source-backed historical assessment observations from published county history. Uses
        exact national parcel identity. Never substitutes the current parcel snapshot. Unknown
        assessment years remain null; vintage years and tax years are distinct. Missing years are
        not interpolated. County coverage can be partial by town and year. Unpublished coverage and
        failed reads return 503, not an empty history. Requires normal API or first-party session
        authentication.

        Args:
            id: Canonical state_fips:county_fips:parcel_id, legacy county5:parcel_id, or parcel
                UUID.
        """
        return cast("_t.ParcelsAssessmentHistoryResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/assessment-history",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def get(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsGetResponse:
        """Get parcel by ID

        ``GET /api/v1/parcels/{id}``

        Retrieve a single parcel by its composite ID (county_fips:parcel_id).

        Args:
            id: Composite parcel identifier in the format county_fips:parcel_id (e.g.,
                37:119:12104406).
        """
        return cast("_t.ParcelsGetResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def owner(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsOwnerResponse:
        """Get parcel owner details and portfolio

        ``GET /api/v1/parcels/{id}/owner``

        Retrieve the owner of a parcel along with their portfolio summary and list of properties.

        Args:
            id: Composite parcel identifier (county_fips:parcel_id).
        """
        return cast("_t.ParcelsOwnerResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/owner",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def permits(
        self,
        id: str,
        *,
        shape: Optional[Literal["envelope"]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsPermitsResponse:
        """Get parcel permits

        ``GET /api/v1/parcels/{id}/permits``

        Retrieve building and construction permits associated with a parcel.

        Args:
            id: Composite parcel identifier (county_fips:parcel_id).
            shape: Body shape. Omit for the default bare array of up to 100 permit rows (newest
                first); `envelope` returns `{ data, permit_count, permit_count_basis, truncated,
                row_cap }`, where `permit_count` is the parcel's true count when
                `permit_count_basis` is `exact` and the size of the capped window (a floor) when
                `capped`, and `truncated` is true when the parcel has more permits than `data`
                carries.
        """
        return cast("_t.ParcelsPermitsResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/permits",
            path_params={"id": id},
            query={
                "shape": shape,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def deeds(
        self,
        id: str,
        *,
        shape: Optional[Literal["envelope"]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsDeedsResponse:
        """Get parcel deed history

        ``GET /api/v1/parcels/{id}/deeds``

        Retrieve deed transactions and transfer history for a parcel.

        Args:
            id: Composite parcel identifier (county_fips:parcel_id).
            shape: Body shape. Omit for the default bare array of deed rows; `envelope` returns the
                typed envelope with a `status` header and the frozen `known_deed_count`.
        """
        return cast("_t.ParcelsDeedsResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/deeds",
            path_params={"id": id},
            query={
                "shape": shape,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def risks(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsRisksResponse:
        """Get parcel risk assessment

        ``GET /api/v1/parcels/{id}/risks``

        Retrieve flood, wildfire, air quality, and crime risk data for a parcel.

        Args:
            id: Composite parcel identifier (county_fips:parcel_id).
        """
        return cast("_t.ParcelsRisksResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/risks",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def geojson(
        self,
        *,
        bbox: str,
        zoom: int,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsGeojsonResponse:
        """Parcel polygons as GeoJSON for a bounding box

        ``GET /api/v1/parcels/geojson``

        Returns parcel polygons inside a bounding box as a GeoJSON FeatureCollection. Only served at
        zoom ≥ 14 to limit data volume — coarser bbox returns an empty collection. Each feature's
        properties include parcel_id, county_fips, owner_name, assessed value, and basic attributes
        for rendering popups.

        Args:
            bbox: Bounding box `west,south,east,north`.
            zoom: Map zoom level. Below 14 returns an empty collection.
        """
        return cast("_t.ParcelsGeojsonResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/geojson",
            query={
                "bbox": bbox,
                "zoom": zoom,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def report(
        self,
        id: str,
        *,
        county_fips: Optional[str] = None,
        sections: Optional[str] = None,
        fields: Optional[str] = None,
        include_provenance: Optional[bool] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsReportResponse:
        """Parcel dossier (paid, provenance-first)

        ``GET /api/v1/parcels/{id}/report``

        The Machine Storefront's per-parcel dossier: a single provenance-first JSON payload carrying
        every POPULATED field for the parcel as `{name, value}` (by default: no `sections`/`fields`
        params delivers everything the quote was priced on), plus the real deeds / comparable-sales
        / permits sub-tables. The per-field receipts (source, as_of, confidence, coverage tier) are
        opt-in: `?include_provenance=true` adds a `provenance` map keyed by field name. `?sections=`
        (identity, valuation, owner, hazard, permits, deeds, market, demographics, `core`, `all`)
        and `?fields=` narrow the delivered field list; anything narrowed out is NAMED in
        `meta.projection.omitted_fields`, and the price never changes with the projection. A ~50 KB
        soft cap applies to the `fields` portion only. The GeoJSON boundary is held out as a
        separately-priced add-on the base payload omits.

        PRICE (value-tiered, per parcel): price = clamp($5 x V(asset value) x R(data richness) x
        F(freshness), $2, $20). The exact amount for a given parcel is quoted, before payment, by
        GET /api/v1/storefront/availability?parcel_id=... and is what the 402 advertises in
        accepts[0].maxAmountRequired (USDC atomic units, 6 decimals).

        ACCESS requires ONE of: (a) x402 pay-per-call -- send a base64 signed x402 PaymentPayload in
        the `X-PAYMENT` header; on a successful build the dossier is returned and the on-chain
        settlement receipt is in the `X-PAYMENT-RESPONSE` response header. No account is needed for
        the parcel record, but PEOPLE DATA (owner names, owner mailing addresses, entity principals,
        deed and sale party names and addresses) is delivered to accounts only: a wallet-only or
        credit-token buyer receives the dossier with those fields set to null and a top-level
        `people_fields` marker (see PeopleFieldsWithheld), and the price is computed on exactly that
        body, so it never counts a field the buyer does not receive. Send your API key with the
        payment to receive them. (b) A genuine PAID PropRaven subscription entitlement -- the
        dossier is served on the subscription invoice. Being merely authenticated is NOT sufficient:
        a free-tier key, or a self-service first-party key with no paid plan, receives a 402. (c)
        Anything else -> HTTP 402 whose `accepts` array carries the exact x402 payment requirements
        for this parcel.

        Args:
            id: Parcel ID. Composite `county_fips:parcel_id` or county-local id when `county_fips`
                query param is provided.
            county_fips: 5-digit county FIPS. Strongly recommended when passing a county-local id.
            sections: Comma-separated report sections to deliver in `fields`: identity, valuation,
                owner, hazard, permits, deeds, market, demographics, `core` (the first four) or
                `all`. Omit (with no `fields`) for `all` — every populated field the quote was
                priced on. The compact core is delivered only on an explicit `core`.
            fields: Comma-separated parcels_serving column names to deliver on top of `sections`.
            include_provenance: `true` attaches the per-field receipts map (`provenance`, keyed by
                field name: source, as_of, confidence, coverage, tier). Off by default — the
                receipts are epoch catalog metadata and roughly triple the payload.
            payment (``X-PAYMENT`` header): x402 payment: a base64-encoded signed x402
                PaymentPayload (EIP-3009 transferWithAuthorization over USDC on Base). Present it to
                pay per call with no API key; the signed amount must equal this parcel's quoted
                maxAmountRequired (see the 402 body or /storefront/availability?parcel_id=). Omit it
                to be served only if your key holds a paid subscription entitlement; otherwise you
                receive a 402 carrying the payment requirements.
        """
        return cast("_t.ParcelsReportResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/report",
            path_params={"id": id},
            query={
                "county_fips": county_fips,
                "sections": sections,
                "fields": fields,
                "include_provenance": include_provenance,
            },
            headers={"X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def comp_pack(
        self,
        id: str,
        *,
        n: Optional[int] = None,
        radius: Optional[float] = None,
        preview: Optional[bool] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsCompPackResponse:
        """Comp pack (paid, priced per pack) — with a FREE preview

        ``GET /api/v1/parcels/{id}/comp-pack``

        The Machine Storefront's comp pack: a subject valuation INDICATED BY comparable sales,
        wrapped with the comps that prove it. Answers the underwriting question "what is this worth,
        and which sales prove it?".

        The comps are the SAME precomputed comparable_sales the free GET /api/v1/parcels/{id}/comps
        route serves; the subject's valuation fields come from parcels_serving. The indicated value
        is derived transparently (median comp $/sqft x subject sqft when both are known, else the
        median comp sale price) with an interquartile range, and is reconstructable from the comps
        in the same payload -- never a black-box AVM.

        PRICE: per pack = clamp($2 x V(subject value) x Q(comp support), $1, $20). Q ramps on the
        comp count with a small bonus for high median similarity. A subject with ZERO precomputed
        comps has no evidence to support a number and is returned free, never charged. The exact
        price is advertised in the 402's accepts[0].maxAmountRequired (USDC atomic units, 6
        decimals).

        FREE PREVIEW: add preview=true for the subject summary, the comp count + median similarity,
        the exact price, and up to three MASKED comps (parcel/APN withheld, sale price rounded, date
        to the year). The precise indicated value and the unmasked comps are the paid product.

        PAID ACCESS (preview omitted) requires ONE of: (a) x402 pay-per-call via a base64 signed
        x402 PaymentPayload in the `X-PAYMENT` header (receipt in `X-PAYMENT-RESPONSE`); (b) a
        genuine PAID PropRaven subscription entitlement; (c) anything else -> HTTP 402 whose
        `accepts` carries the exact requirements.

        Args:
            id: Parcel id: canonical state:county:parcel, 5-digit-county:parcel, or a parcel UUID.
            n: How many comps back the pack.
            radius: Optional post-filter: keep only precomputed comps within this many miles.
            preview: FREE try-before-buy: subject summary, comp count, exact price and three masked
                comps. No payment.
            payment (``X-PAYMENT`` header): Base64-encoded x402 PaymentPayload (EIP-3009 signed).
                Present it to pay per call for the full pack.
        """
        return cast("_t.ParcelsCompPackResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/comp-pack",
            path_params={"id": id},
            query={
                "n": n,
                "radius": radius,
                "preview": preview,
            },
            headers={"X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def risk_score(
        self,
        id: str,
        *,
        preview: Optional[bool] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsRiskScoreResponse:
        """Risk score (paid, priced per assessment) — with a FREE preview

        ``GET /api/v1/parcels/{id}/risk-score``

        The Machine Storefront's risk score: a multi-hazard risk assessment for one parcel, anchored
        on FEMA's National Risk Index COMPOSITE (nri_risk_score 0-100 + rating) with the flood /
        seismic / windstorm / wildfire / air-quality / crime breakdown that supports it. Answers
        "what could go wrong with this asset?". The headline is FEMA's own methodology, not an
        invented weighting.

        Reuses the SAME panel the free GET /api/v1/parcels/{id}/risks route serves
        (getParcelRisksData) plus the NRI composite + flood detail from parcels_serving.

        PRICE: per assessment = clamp($0.60 x V(asset value) x C(hazard coverage), $0.20, $20). C
        ramps on how many independent hazard layers resolved. A parcel with ZERO layers is returned
        free, never charged. The cheapest paid SKU. The exact price is in the 402's
        accepts[0].maxAmountRequired (USDC atomic units).

        FREE PREVIEW: add preview=true for the subject, WHICH hazard layers resolved, and the exact
        price. The precise NRI score and the hazard breakdown are the paid product.

        PAID ACCESS: (a) x402 via a base64 signed PaymentPayload in `X-PAYMENT` (receipt in
        `X-PAYMENT-RESPONSE`); (b) a genuine PAID subscription entitlement; (c) else HTTP 402 with
        the exact requirements.

        Args:
            id: Parcel id: canonical state:county:parcel, 5-digit-county:parcel, or a parcel UUID.
            preview: FREE try-before-buy: subject, resolved hazard layers, and the exact price. No
                payment.
            payment (``X-PAYMENT`` header): Base64-encoded x402 PaymentPayload (EIP-3009 signed).
                Present it to pay per call.
        """
        return cast("_t.ParcelsRiskScoreResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/risk-score",
            path_params={"id": id},
            query={
                "preview": preview,
            },
            headers={"X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def traffic_history(
        self,
        id: str,
        *,
        lat: float,
        lng: float,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsTrafficHistoryResponse:
        """Nearest traffic station + AADT history

        ``GET /api/v1/parcels/{id}/traffic-history``

        Finds the AADT (annual average daily traffic) station nearest to the given coordinates and
        returns its historical time series plus 3/5/7-year CAGRs. Useful for retail / CRE site
        selection. Search radius ~2 miles; returns empty data if no station is in range.

        Args:
            id: Parcel ID (used for context only; the actual nearest-station search is by lat/lng).
            lat: Latitude.
            lng: Longitude.
        """
        return cast("_t.ParcelsTrafficHistoryResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/traffic-history",
            path_params={"id": id},
            query={
                "lat": lat,
                "lng": lng,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def batch(
        self,
        *,
        tuples: Sequence[_t.ParcelsBatchParamsTuplesItem],
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsBatchResponse:
        """Fetch up to 100 parcels by (state, county, parcel) tuple

        ``POST /api/v1/parcels/batch``

        Card-projection rows for up to 100 unique `(state_fips, county_fips, parcel_id)` tuples.
        `county_fips` is the 3-digit within-state code (a 5-digit value is refused with a 400 naming
        the fix). Tuples with no match are listed in `missing`.
        """
        return cast("_t.ParcelsBatchResponse", await self._client._request(
            "POST",
            "/api/v1/parcels/batch",
            body={
                "tuples": tuples,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def comps(
        self,
        id: str,
        *,
        n: Optional[int] = None,
        radius: Optional[float] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsCompsResponse:
        """Comparable sales for a parcel

        ``GET /api/v1/parcels/{id}/comps``

        Precomputed comparable sales near the parcel (`tier` names the comp source).

        Args:
            id: Parcel identifier: the canonical `state_fips:county_fips:parcel_id` form (e.g.
                `37:119:12104406`), the legacy 5-digit `county_fips5:parcel_id` form, or a PropRaven
                parcel UUID. URL-encode it.
            n: Number of comps (1-25).
            radius: Search radius in miles.
        """
        return cast("_t.ParcelsCompsResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/comps",
            path_params={"id": id},
            query={
                "n": n,
                "radius": radius,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def occupants(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsOccupantsResponse:
        """Business occupants of a parcel

        ``GET /api/v1/parcels/{id}/occupants``

        Businesses matched to the parcel (names, brands, categories, match confidence), primary
        occupant first. At most 100 rows; `truncated` says when more exist.

        Args:
            id: Parcel identifier: the canonical `state_fips:county_fips:parcel_id` form (e.g.
                `37:119:12104406`), the legacy 5-digit `county_fips5:parcel_id` form, or a PropRaven
                parcel UUID. URL-encode it.
        """
        return cast("_t.ParcelsOccupantsResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/occupants",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def violations(
        self,
        id: str,
        *,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsViolationsResponse:
        """Code violations on a parcel

        ``GET /api/v1/parcels/{id}/violations``

        Municipal code-enforcement cases matched to the parcel, with the source coverage that says
        whether an empty list means 'none recorded' or 'not collected here'.

        Args:
            id: Parcel identifier: the canonical `state_fips:county_fips:parcel_id` form (e.g.
                `37:119:12104406`), the legacy 5-digit `county_fips5:parcel_id` form, or a PropRaven
                parcel UUID. URL-encode it.
        """
        return cast("_t.ParcelsViolationsResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/{id}/violations",
            path_params={"id": id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def pois(
        self,
        *,
        bbox: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.ParcelsPoisResponse:
        """Business parcels in a small bounding box

        ``GET /api/v1/parcels/poi``

        Up to 250 parcels with a recorded business type inside `bbox`, highest assessed value first.
        Boxes larger than 0.03 square degrees return an empty list.

        Args:
            bbox: `west,south,east,north` in decimal degrees.
        """
        return cast("_t.ParcelsPoisResponse", await self._client._request(
            "GET",
            "/api/v1/parcels/poi",
            query={
                "bbox": bbox,
            },
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
