# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DealFindPortfolioOwnersParams"]


class DealFindPortfolioOwnersParams(TypedDict, total=False):
    limit: int
    """Page size, max 500."""

    min_properties: int
    """Minimum properties owned."""

    min_value: int
    """Minimum total portfolio assessed value, USD."""

    offset: int
    """Pagination offset."""

    search: str
    """Owner name substring search."""

    state: str
    """2-letter owner mailing state filter."""
