# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ParcelRetrieveTrafficHistoryResponse", "History", "Station"]


class History(BaseModel):
    aadt: Optional[int] = None

    year: Optional[int] = None


class Station(BaseModel):
    id: Optional[str] = None

    aadt_current: Optional[int] = None
    """Most recent AADT count."""

    aadt_year: Optional[int] = None

    cagr_3yr: Optional[float] = None

    cagr_5yr: Optional[float] = None

    cagr_7yr: Optional[float] = None

    functional_class: Optional[str] = None

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    route_name: Optional[str] = None

    station_id: Optional[str] = None


class ParcelRetrieveTrafficHistoryResponse(BaseModel):
    history: Optional[List[History]] = None
    """Year-keyed historical counts (newest last)."""

    station: Optional[Station] = None
