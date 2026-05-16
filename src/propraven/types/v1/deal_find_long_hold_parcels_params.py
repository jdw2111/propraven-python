# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DealFindLongHoldParcelsParams"]


class DealFindLongHoldParcelsParams(TypedDict, total=False):
    county_fips: str
    """5-digit county FIPS filter."""

    hold_tier: Literal["10-15yr", "15-20yr", "20-30yr", "30yr+"]
    """Filter by hold-period tier."""

    limit: int
    """Page size, max 500."""

    min_value: int
    """Minimum assessed value, USD."""

    min_years: int
    """Minimum years held."""

    offset: int
    """Pagination offset."""

    state_fips: str
    """2-digit state FIPS filter."""
