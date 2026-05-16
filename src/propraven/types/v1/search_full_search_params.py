# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchFullSearchParams"]


class SearchFullSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query. Min 2 chars."""

    city: str
    """City filter."""

    dir: Literal["asc", "desc"]
    """Sort direction."""

    field: Literal["all", "address", "owner_name", "city"]
    """Field to match against."""

    limit: int
    """Page size, max 200."""

    page: int
    """1-indexed page number."""

    sort: Literal["address", "city", "state", "owner_name", "total_value", "year_built"]
    """Sort column."""

    state: str
    """2-letter state filter."""
