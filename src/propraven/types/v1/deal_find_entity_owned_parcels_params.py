# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DealFindEntityOwnedParcelsParams"]


class DealFindEntityOwnedParcelsParams(TypedDict, total=False):
    county_fips: str
    """5-digit county FIPS filter."""

    entity_type: Literal["LLC", "CORP", "TRUST", "LP", "LTD", "ASSOCIATION", "OTHER_ENTITY"]
    """Filter by entity classification."""

    limit: int
    """Page size, max 500."""

    min_value: int
    """Minimum assessed value, USD."""

    offset: int
    """Pagination offset."""

    search: str
    """Owner-name substring search."""

    state_fips: str
    """2-digit state FIPS filter."""

    top: bool
    """
    If true, returns aggregated entity rankings with summary stats instead of
    per-parcel rows.
    """

    zoning: str
    """Zoning substring filter."""
