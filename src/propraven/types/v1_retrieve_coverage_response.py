# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["V1RetrieveCoverageResponse", "Data"]


class Data(BaseModel):
    county_fips: Optional[str] = None

    county_name: Optional[str] = None

    geocoded_pct: Optional[float] = None

    owner_pct: Optional[float] = None

    parcel_count: Optional[int] = None

    state_fips: Optional[str] = None

    state_name: Optional[str] = None

    value_pct: Optional[float] = None


class V1RetrieveCoverageResponse(BaseModel):
    data: Optional[List[Data]] = None

    states_covered: Optional[int] = None

    total_parcels: Optional[int] = None
