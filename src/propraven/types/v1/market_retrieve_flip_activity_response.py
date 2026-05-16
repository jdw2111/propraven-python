# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MarketRetrieveFlipActivityResponse", "Data"]


class Data(BaseModel):
    avg_hold_days: Optional[float] = None

    avg_roi: Optional[float] = None
    """Average profit percentage (e.g. 0.18 = 18%)."""

    county_fips: Optional[str] = None

    flip_count: Optional[int] = None

    total_profit: Optional[float] = None


class MarketRetrieveFlipActivityResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
