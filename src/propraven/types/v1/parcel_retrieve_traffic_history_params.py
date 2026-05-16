# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ParcelRetrieveTrafficHistoryParams"]


class ParcelRetrieveTrafficHistoryParams(TypedDict, total=False):
    lat: Required[float]
    """Latitude."""

    lng: Required[float]
    """Longitude."""
