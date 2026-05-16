# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DealFindFlipsParams"]


class DealFindFlipsParams(TypedDict, total=False):
    county_fips: str
    """Filter by county FIPS code."""

    flip_tier: Literal["quick", "standard", "long"]
    """Filter by flip speed tier (quick: <6mo, standard: 6-12mo, long: 12-24mo)."""

    limit: int

    min_profit: float
    """Minimum estimated profit."""

    offset: int

    state_fips: str
    """Filter by state FIPS code."""

    view: Literal["flippers"]
    """
    Set to 'flippers' to return a ranked list of top flippers instead of individual
    flips.
    """
