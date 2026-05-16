# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DealFindAbsenteeOwnersParams"]


class DealFindAbsenteeOwnersParams(TypedDict, total=False):
    county_fips: str
    """Filter by county FIPS code."""

    limit: int

    min_value: float
    """Minimum assessed value."""

    offset: int

    out_of_state: bool
    """Only return owners whose mailing address is in a different state."""

    state_fips: str
    """Filter by state FIPS code."""
