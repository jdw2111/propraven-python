# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DealFindHighLandRatioParams"]


class DealFindHighLandRatioParams(TypedDict, total=False):
    county_fips: str
    """5-digit county FIPS filter."""

    limit: int
    """Page size, max 500."""

    min_ratio: float
    """Minimum land/improvement ratio."""

    min_value: int
    """Minimum land assessed value, USD."""

    offset: int
    """Pagination offset."""

    state_fips: str
    """2-digit state FIPS filter."""

    zoning: str
    """Zoning substring filter."""
