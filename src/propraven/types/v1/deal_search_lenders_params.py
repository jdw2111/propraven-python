# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DealSearchLendersParams"]


class DealSearchLendersParams(TypedDict, total=False):
    limit: int
    """Page size, max 500."""

    min_mortgages: int
    """Minimum mortgage count."""

    offset: int
    """Pagination offset."""

    search: str
    """Lender name substring search."""

    state: str
    """2-letter state filter."""
