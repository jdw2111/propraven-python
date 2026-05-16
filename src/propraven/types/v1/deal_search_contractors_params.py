# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DealSearchContractorsParams"]


class DealSearchContractorsParams(TypedDict, total=False):
    limit: int
    """Page size, max 500."""

    min_permits: int
    """Minimum permit count to include."""

    min_value: int
    """Minimum total declared permit value, USD."""

    offset: int
    """Pagination offset."""

    search: str
    """Contractor name search (case-insensitive substring)."""

    state: str
    """2-letter state filter."""
