# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MarketRetrieveFlipActivityParams"]


class MarketRetrieveFlipActivityParams(TypedDict, total=False):
    limit: int
    """Page size, max 500."""

    offset: int
    """Pagination offset."""

    state_fips: str
    """2-digit state FIPS filter."""
