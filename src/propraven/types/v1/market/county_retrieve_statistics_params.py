# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CountyRetrieveStatisticsParams"]


class CountyRetrieveStatisticsParams(TypedDict, total=False):
    limit: int

    min_sales: int
    """Minimum number of sales in the period to include a county."""

    offset: int

    order: Literal["asc", "desc"]

    quarter: str
    """Specific quarter to retrieve (e.g., 2025Q4). Defaults to latest available."""

    sort: Literal["sale_count", "median_price", "yoy_change", "county_name"]
    """Sort field."""

    state_fips: str
    """Filter by state FIPS code."""
