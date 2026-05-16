# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DealFindFlipsResponse", "Data"]


class Data(BaseModel):
    address: Optional[str] = None

    buy_date: Optional[date] = None

    buy_price: Optional[float] = None

    buyer_name: Optional[str] = None

    county_fips: Optional[str] = None

    flip_tier: Optional[Literal["quick", "standard", "long"]] = None

    hold_days: Optional[int] = None

    parcel_id: Optional[str] = None

    profit: Optional[float] = None

    sell_date: Optional[date] = None

    sell_price: Optional[float] = None

    seller_name: Optional[str] = None


class DealFindFlipsResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
