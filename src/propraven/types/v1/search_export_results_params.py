# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SearchExportResultsParams"]


class SearchExportResultsParams(TypedDict, total=False):
    east: float
    """Bounding box: east longitude."""

    limit: int
    """Row cap. Hard max 10,000."""

    north: float
    """Bounding box: north latitude."""

    order: Literal["asc", "desc"]
    """Sort direction."""

    sort: Literal[
        "address",
        "city",
        "state",
        "owner_name",
        "total_assessed_value",
        "zoning",
        "year_built",
        "lot_size_acres",
        "ownership_type",
    ]
    """Sort column."""

    south: float
    """Bounding box: south latitude."""

    west: float
    """Bounding box: west longitude."""

    zoning_categories: Annotated[str, PropertyInfo(alias="zoningCategories")]
    """Comma-delimited zoning categories."""
