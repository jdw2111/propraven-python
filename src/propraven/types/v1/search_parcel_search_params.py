# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "SearchParcelSearchParams",
    "Bounds",
    "Filters",
    "FiltersAcreageRange",
    "FiltersValueRange",
    "FiltersYearBuiltRange",
]


class SearchParcelSearchParams(TypedDict, total=False):
    bounds: Required[Bounds]

    filters: Filters

    limit: int
    """Number of results to return."""

    offset: int
    """Number of results to skip for pagination."""

    order: Literal["asc", "desc"]

    sort: Literal["assessed_value", "sale_price", "acreage", "year_built", "deal_score"]
    """Sort field."""


class Bounds(TypedDict, total=False):
    east: Required[float]

    north: Required[float]

    south: Required[float]

    west: Required[float]


class FiltersAcreageRange(TypedDict, total=False):
    """Filter by acreage range."""

    max: float

    min: float


class FiltersValueRange(TypedDict, total=False):
    """Filter by assessed value range."""

    max: float

    min: float


class FiltersYearBuiltRange(TypedDict, total=False):
    """Filter by year built range."""

    max: int

    min: int


class Filters(TypedDict, total=False):
    absentee_only: Annotated[bool, PropertyInfo(alias="absenteeOnly")]
    """Only return parcels with absentee owners."""

    acreage_range: Annotated[FiltersAcreageRange, PropertyInfo(alias="acreageRange")]
    """Filter by acreage range."""

    owner_types: Annotated[
        List[Literal["individual", "corporation", "llc", "trust", "government", "other"]],
        PropertyInfo(alias="ownerTypes"),
    ]
    """Filter by owner entity type."""

    value_range: Annotated[FiltersValueRange, PropertyInfo(alias="valueRange")]
    """Filter by assessed value range."""

    year_built_range: Annotated[FiltersYearBuiltRange, PropertyInfo(alias="yearBuiltRange")]
    """Filter by year built range."""

    zoning_categories: Annotated[SequenceNotStr[str], PropertyInfo(alias="zoningCategories")]
    """Filter by zoning category (e.g., residential, commercial, industrial)."""
