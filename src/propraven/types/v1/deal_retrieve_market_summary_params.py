# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DealRetrieveMarketSummaryParams"]


class DealRetrieveMarketSummaryParams(TypedDict, total=False):
    county_fips: str
    """5-digit county FIPS filter."""

    limit: int
    """Page size, max 500."""

    offset: int
    """Pagination offset."""

    rating: Literal["AFFORDABLE", "MODERATE", "EXPENSIVE", "VERY_EXPENSIVE"]
    """Affordability-rating filter (only meaningful with view=affordability)."""

    state_fips: str
    """2-digit state FIPS filter."""

    view: Literal["affordability"]
    """Switch to the affordability-index dataset."""

    year: str
    """Year filter."""
