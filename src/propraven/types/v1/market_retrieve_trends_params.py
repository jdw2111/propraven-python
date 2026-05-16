# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MarketRetrieveTrendsParams"]


class MarketRetrieveTrendsParams(TypedDict, total=False):
    county_fips: str
    """Comma-separated list of county FIPS codes."""

    state_fips: str
    """State FIPS code. Used if county_fips is not provided."""
