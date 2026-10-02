# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``leads`` namespace: ``client.leads``."""

from __future__ import annotations

from typing import Any, Literal, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["LeadsResource", "AsyncLeadsResource"]


class LeadsResource(SyncAPIResource):
    """``client.leads`` operations (sync)."""

    def find(
        self,
        *,
        signal: Literal["absentee", "long_hold", "entity_owned", "portfolio_owner", "high_land_ratio", "flip", "distressed"],
        state: str,
        county: Optional[str] = None,
        zip: Optional[str] = None,
        value_min: Optional[int] = None,
        value_max: Optional[int] = None,
        limit: Optional[int] = None,
        preview: Optional[bool] = None,
        mail_ready: Optional[bool] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.LeadsFindResponse:
        """Lead feed (paid, priced per lead) — with a FREE preview

        ``GET /api/v1/leads/find``

        The Machine Storefront's lead feed: the qualified target list for one SIGNAL in one STATE,
        delivered as lead records and priced PER LEAD.

        Each lead carries its canonical_id (state:county:APN), owner, assessed value, that signal's
        own strength fields (years held, land/improvement ratio, flip profit, portfolio size, ...),
        a deterministic lead_score (1-100) and provenance {as_of, source}.

        PRICE: per_lead = clamp($0.25 x S(signal strength) x V(asset-value tier), $0.05, $1.00);
        total = min(count x per_lead, $20). You pay for the leads DELIVERED -- min(matching rows,
        limit) -- and an empty result is never charged for. The exact total is advertised in the
        402's accepts[0].maxAmountRequired (USDC atomic units, 6 decimals).

        FREE PREVIEW: add preview=true for the exact count, the exact quote and up to three MASKED
        sample leads (APN truncated to state:county, house number stripped, owner name and every
        other people field withheld). No payment, no API key required; anonymous callers are
        IP-throttled at the free tier. The anonymous security alternative (`{}`) applies to the
        preview ONLY.

        ACCOUNT REQUIRED FOR DELIVERY: a lead is an owner's name and mailing address by area --
        people data, delivered to PropRaven ACCOUNTS only. A paid (non-preview) pull must carry an
        API key (`Authorization: Bearer pz_...`), an MCP OAuth token or a signed-in session on EVERY
        rail. Payment alone (an x402 `X-PAYMENT` header or a prepaid `X-CREDIT-TOKEN`) is not an
        account: without one the call is refused with HTTP 401 `code: "account_required"`, `reason:
        "people_data_requires_account"`, before any payment is verified or any credit drawn.

        PAID ACCESS (preview omitted), for an account, requires ONE of: (a) x402 pay-per-call --
        send a base64 signed x402 PaymentPayload in the `X-PAYMENT` header together with your
        credentials; on a successful build the leads are returned and the on-chain settlement
        receipt is in the `X-PAYMENT-RESPONSE` response header. (b) A prepaid `X-CREDIT-TOKEN`
        balance. (c) A genuine PAID PropRaven subscription entitlement (lead feeds are included).
        Being merely authenticated is NOT sufficient. (d) Anything else -> HTTP 402 whose `accepts`
        array carries the exact payment requirements for this pull.

        OWNER CONTACT: each delivered lead carries `owner_contact` -- the owner's best mailing
        address, read from ONE address column family of the record with its ZIP, flagged mail_ready.
        `mail_ready=true` narrows the pull to parcels whose record carries a complete one-family
        mailing address (parcel-grain signals only). Each delivery is recorded in PropRaven's
        people-data access log before it is returned; if the log is unavailable the delivery is
        refused (503) and nothing is charged.

        BOUNDED READS: every read carries a statement timeout (10 s with `mail_ready`, 25 s
        otherwise). A pull too broad to finish returns 503 `code: "lead_read_timeout"` telling you
        to narrow it (add `county`); nothing is charged.

        NOTE on `distressed`: an assessment-derived cohort (a structure on the books assessed at a
        nominal value, on land that carries real value). It is NOT a pre-foreclosure, tax-lien or
        lis-pendens feed.

        Args:
            signal: Which qualified cohort to pull from. Priced by strength: absentee (1.0x, widest)
                < long_hold (1.1x) < entity_owned (1.15x) < portfolio_owner (1.25x) <
                high_land_ratio (1.4x) < flip (1.6x) < distressed (1.9x).
            state: REQUIRED 2-letter USPS state code. Every pull is pruned to one state partition.
            county: 3-digit within-state code ("183") or 5-digit state+county ("37183").
            zip: 5-digit ZIP. Supported only on the long_hold and entity_owned cohorts (the other
                source relations carry no ZIP column) -- a zip on any other signal returns 400.
            value_min: Minimum assessed value (sell price for the flip cohort), USD.
            value_max: Maximum assessed value (sell price for the flip cohort), USD.
            limit: How many leads to buy. Default 25, max 200. You pay for min(matching rows,
                limit).
            preview: true -> the FREE preview (count + quote + up to three masked sample leads, no
                payment). Omit or false -> the paid call.
            mail_ready: true -> only parcels whose record carries a complete mailing address
                (street, city, state, 5-digit ZIP) in ONE column family. Parcel-grain signals only
                (400 on portfolio_owner). Each delivered lead's `owner_contact.mail_ready` is the
                final word. Narrow with `county` in large states: the filter checks every candidate.
            payment (``X-PAYMENT`` header): x402 payment, sent TOGETHER with your account
                credentials (Authorization: Bearer pz_...) -- a payment alone is not an account and
                is refused with 401 before it is verified: a base64-encoded signed x402
                PaymentPayload (EIP-3009 transferWithAuthorization over USDC on Base). The signed
                amount must equal this pull's quoted maxAmountRequired (see the 402 body, or call
                with preview=true first). Ignored on a preview call, which is free.
        """
        return cast("_t.LeadsFindResponse", self._client._request(
            "GET",
            "/api/v1/leads/find",
            query={
                "signal": signal,
                "state": state,
                "county": county,
                "zip": zip,
                "value_min": value_min,
                "value_max": value_max,
                "limit": limit,
                "preview": preview,
                "mail_ready": mail_ready,
            },
            headers={"X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncLeadsResource(AsyncAPIResource):
    """``client.leads`` operations (async)."""

    async def find(
        self,
        *,
        signal: Literal["absentee", "long_hold", "entity_owned", "portfolio_owner", "high_land_ratio", "flip", "distressed"],
        state: str,
        county: Optional[str] = None,
        zip: Optional[str] = None,
        value_min: Optional[int] = None,
        value_max: Optional[int] = None,
        limit: Optional[int] = None,
        preview: Optional[bool] = None,
        mail_ready: Optional[bool] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.LeadsFindResponse:
        """Lead feed (paid, priced per lead) — with a FREE preview

        ``GET /api/v1/leads/find``

        The Machine Storefront's lead feed: the qualified target list for one SIGNAL in one STATE,
        delivered as lead records and priced PER LEAD.

        Each lead carries its canonical_id (state:county:APN), owner, assessed value, that signal's
        own strength fields (years held, land/improvement ratio, flip profit, portfolio size, ...),
        a deterministic lead_score (1-100) and provenance {as_of, source}.

        PRICE: per_lead = clamp($0.25 x S(signal strength) x V(asset-value tier), $0.05, $1.00);
        total = min(count x per_lead, $20). You pay for the leads DELIVERED -- min(matching rows,
        limit) -- and an empty result is never charged for. The exact total is advertised in the
        402's accepts[0].maxAmountRequired (USDC atomic units, 6 decimals).

        FREE PREVIEW: add preview=true for the exact count, the exact quote and up to three MASKED
        sample leads (APN truncated to state:county, house number stripped, owner name and every
        other people field withheld). No payment, no API key required; anonymous callers are
        IP-throttled at the free tier. The anonymous security alternative (`{}`) applies to the
        preview ONLY.

        ACCOUNT REQUIRED FOR DELIVERY: a lead is an owner's name and mailing address by area --
        people data, delivered to PropRaven ACCOUNTS only. A paid (non-preview) pull must carry an
        API key (`Authorization: Bearer pz_...`), an MCP OAuth token or a signed-in session on EVERY
        rail. Payment alone (an x402 `X-PAYMENT` header or a prepaid `X-CREDIT-TOKEN`) is not an
        account: without one the call is refused with HTTP 401 `code: "account_required"`, `reason:
        "people_data_requires_account"`, before any payment is verified or any credit drawn.

        PAID ACCESS (preview omitted), for an account, requires ONE of: (a) x402 pay-per-call --
        send a base64 signed x402 PaymentPayload in the `X-PAYMENT` header together with your
        credentials; on a successful build the leads are returned and the on-chain settlement
        receipt is in the `X-PAYMENT-RESPONSE` response header. (b) A prepaid `X-CREDIT-TOKEN`
        balance. (c) A genuine PAID PropRaven subscription entitlement (lead feeds are included).
        Being merely authenticated is NOT sufficient. (d) Anything else -> HTTP 402 whose `accepts`
        array carries the exact payment requirements for this pull.

        OWNER CONTACT: each delivered lead carries `owner_contact` -- the owner's best mailing
        address, read from ONE address column family of the record with its ZIP, flagged mail_ready.
        `mail_ready=true` narrows the pull to parcels whose record carries a complete one-family
        mailing address (parcel-grain signals only). Each delivery is recorded in PropRaven's
        people-data access log before it is returned; if the log is unavailable the delivery is
        refused (503) and nothing is charged.

        BOUNDED READS: every read carries a statement timeout (10 s with `mail_ready`, 25 s
        otherwise). A pull too broad to finish returns 503 `code: "lead_read_timeout"` telling you
        to narrow it (add `county`); nothing is charged.

        NOTE on `distressed`: an assessment-derived cohort (a structure on the books assessed at a
        nominal value, on land that carries real value). It is NOT a pre-foreclosure, tax-lien or
        lis-pendens feed.

        Args:
            signal: Which qualified cohort to pull from. Priced by strength: absentee (1.0x, widest)
                < long_hold (1.1x) < entity_owned (1.15x) < portfolio_owner (1.25x) <
                high_land_ratio (1.4x) < flip (1.6x) < distressed (1.9x).
            state: REQUIRED 2-letter USPS state code. Every pull is pruned to one state partition.
            county: 3-digit within-state code ("183") or 5-digit state+county ("37183").
            zip: 5-digit ZIP. Supported only on the long_hold and entity_owned cohorts (the other
                source relations carry no ZIP column) -- a zip on any other signal returns 400.
            value_min: Minimum assessed value (sell price for the flip cohort), USD.
            value_max: Maximum assessed value (sell price for the flip cohort), USD.
            limit: How many leads to buy. Default 25, max 200. You pay for min(matching rows,
                limit).
            preview: true -> the FREE preview (count + quote + up to three masked sample leads, no
                payment). Omit or false -> the paid call.
            mail_ready: true -> only parcels whose record carries a complete mailing address
                (street, city, state, 5-digit ZIP) in ONE column family. Parcel-grain signals only
                (400 on portfolio_owner). Each delivered lead's `owner_contact.mail_ready` is the
                final word. Narrow with `county` in large states: the filter checks every candidate.
            payment (``X-PAYMENT`` header): x402 payment, sent TOGETHER with your account
                credentials (Authorization: Bearer pz_...) -- a payment alone is not an account and
                is refused with 401 before it is verified: a base64-encoded signed x402
                PaymentPayload (EIP-3009 transferWithAuthorization over USDC on Base). The signed
                amount must equal this pull's quoted maxAmountRequired (see the 402 body, or call
                with preview=true first). Ignored on a preview call, which is free.
        """
        return cast("_t.LeadsFindResponse", await self._client._request(
            "GET",
            "/api/v1/leads/find",
            query={
                "signal": signal,
                "state": state,
                "county": county,
                "zip": zip,
                "value_min": value_min,
                "value_max": value_max,
                "limit": limit,
                "preview": preview,
                "mail_ready": mail_ready,
            },
            headers={"X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
