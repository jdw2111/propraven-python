# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["CountyRetrieveStatisticsResponse", "Data"]


class Data(BaseModel):
    avg_days_on_market: Optional[int] = None

    avg_price: Optional[float] = None

    county_fips: Optional[str] = None

    county_name: Optional[str] = None

    median_price: Optional[float] = None

    quarter: Optional[str] = None

    sale_count: Optional[int] = None

    state_abbr: Optional[str] = None

    state_fips: Optional[str] = None

    yoy_change: Optional[float] = None
    """Year-over-year median price change as a decimal (e.g., 0.05 = 5%)."""


class CountyRetrieveStatisticsResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
