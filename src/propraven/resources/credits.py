# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""The ``credits`` namespace: ``client.credits``."""

from __future__ import annotations

from typing import Any, Mapping, Optional, Union, cast

import httpx

from .. import types as _t
from .._resource import AsyncAPIResource, SyncAPIResource
from .._transport import NOT_GIVEN, NotGiven

__all__ = ["CreditsResource", "AsyncCreditsResource"]


class CreditsResource(SyncAPIResource):
    """``client.credits`` operations (sync)."""

    def topup(
        self,
        *,
        amount: int,
        credit_token: Optional[str] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CreditsTopupResponse:
        """Fund a prepaid credit balance over x402

        ``GET /api/v1/storefront/credits/topup``

        Pay `amount` USDC once via x402 to fund a prepaid credit balance; receive a credit token
        (pzc_...) to spend on any paid endpoint via the X-CREDIT-TOKEN header — the recurring/volume
        rail, no account, no CDP/Stripe. GET with no payment returns a 402 for `amount`; present an
        existing X-CREDIT-TOKEN to top it up in place. Idempotent on the settlement tx.

        Args:
            amount: Whole USD to fund ($1–$1000).
            credit_token (``X-CREDIT-TOKEN`` header): Optional existing pzc_ token to top up in
                place.
            payment (``X-PAYMENT`` header): Base64 x402 PaymentPayload to fund the balance.
        """
        return cast("_t.CreditsTopupResponse", self._client._request(
            "GET",
            "/api/v1/storefront/credits/topup",
            query={
                "amount": amount,
            },
            headers={"X-CREDIT-TOKEN": credit_token, "X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def balance(
        self,
        *,
        credit_token: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CreditsBalanceResponse:
        """Read a prepaid credit balance + ledger

        ``GET /api/v1/storefront/credits/balance``

        Return the balance and recent ledger for the credit token in the X-CREDIT-TOKEN header. No
        payment; the token is the credential (never a query param).

        Args:
            credit_token (``X-CREDIT-TOKEN`` header): The pzc_ credit token.
        """
        return cast("_t.CreditsBalanceResponse", self._client._request(
            "GET",
            "/api/v1/storefront/credits/balance",
            headers={"X-CREDIT-TOKEN": credit_token},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))


class AsyncCreditsResource(AsyncAPIResource):
    """``client.credits`` operations (async)."""

    async def topup(
        self,
        *,
        amount: int,
        credit_token: Optional[str] = None,
        payment: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CreditsTopupResponse:
        """Fund a prepaid credit balance over x402

        ``GET /api/v1/storefront/credits/topup``

        Pay `amount` USDC once via x402 to fund a prepaid credit balance; receive a credit token
        (pzc_...) to spend on any paid endpoint via the X-CREDIT-TOKEN header — the recurring/volume
        rail, no account, no CDP/Stripe. GET with no payment returns a 402 for `amount`; present an
        existing X-CREDIT-TOKEN to top it up in place. Idempotent on the settlement tx.

        Args:
            amount: Whole USD to fund ($1–$1000).
            credit_token (``X-CREDIT-TOKEN`` header): Optional existing pzc_ token to top up in
                place.
            payment (``X-PAYMENT`` header): Base64 x402 PaymentPayload to fund the balance.
        """
        return cast("_t.CreditsTopupResponse", await self._client._request(
            "GET",
            "/api/v1/storefront/credits/topup",
            query={
                "amount": amount,
            },
            headers={"X-CREDIT-TOKEN": credit_token, "X-PAYMENT": payment},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))

    async def balance(
        self,
        *,
        credit_token: str,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> _t.CreditsBalanceResponse:
        """Read a prepaid credit balance + ledger

        ``GET /api/v1/storefront/credits/balance``

        Return the balance and recent ledger for the credit token in the X-CREDIT-TOKEN header. No
        payment; the token is the credential (never a query param).

        Args:
            credit_token (``X-CREDIT-TOKEN`` header): The pzc_ credit token.
        """
        return cast("_t.CreditsBalanceResponse", await self._client._request(
            "GET",
            "/api/v1/storefront/credits/balance",
            headers={"X-CREDIT-TOKEN": credit_token},
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
            max_retries=max_retries,
        ))
