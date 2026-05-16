# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DealFindLongHoldParcelsResponse", "Data"]


class Data(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    county_fips: Optional[str] = None

    hold_tier: Optional[Literal["10-15yr", "15-20yr", "20-30yr", "30yr+"]] = None

    last_sale_date: Optional[date] = None

    owner_name: Optional[str] = None

    parcel_id: Optional[str] = None

    state: Optional[str] = None

    state_fips: Optional[str] = None

    total_assessed_value: Optional[float] = None

    years_held: Optional[float] = None

    zip: Optional[str] = None


class DealFindLongHoldParcelsResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
