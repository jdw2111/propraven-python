# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MarketRetrieveTrendsResponse", "Data", "DataQuarter"]


class DataQuarter(BaseModel):
    avg_price: Optional[float] = None

    median_price: Optional[float] = None

    quarter: Optional[str] = None

    sale_count: Optional[int] = None

    yoy_change: Optional[float] = None


class Data(BaseModel):
    county_fips: Optional[str] = None

    county_name: Optional[str] = None

    quarters: Optional[List[DataQuarter]] = None


class MarketRetrieveTrendsResponse(BaseModel):
    data: Optional[List[Data]] = None
