# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ParcelRetrieveGeojsonParams"]


class ParcelRetrieveGeojsonParams(TypedDict, total=False):
    bbox: Required[str]
    """Bounding box `west,south,east,north`."""

    zoom: Required[int]
    """Map zoom level. Below 14 returns an empty collection."""
