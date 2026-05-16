# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DealFindHighLandRatioResponse", "Data"]


class Data(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    county_fips: Optional[str] = None

    improvement_assessed_value: Optional[float] = None

    land_assessed_value: Optional[float] = None

    land_improvement_ratio: Optional[float] = None
    """land / improvement, higher = more redevelopment potential."""

    owner_name: Optional[str] = None

    parcel_id: Optional[str] = None

    state: Optional[str] = None

    state_fips: Optional[str] = None

    total_assessed_value: Optional[float] = None

    zoning: Optional[str] = None


class DealFindHighLandRatioResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
