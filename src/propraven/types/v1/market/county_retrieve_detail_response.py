# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ..affordability_row import AffordabilityRow

__all__ = ["CountyRetrieveDetailResponse", "FlipSummary", "MarketStat", "ParcelSummary"]


class FlipSummary(BaseModel):
    avg_hold_days: Optional[float] = None

    avg_roi: Optional[float] = None

    flip_count: Optional[int] = None

    total_profit: Optional[float] = None


class MarketStat(BaseModel):
    avg_dom: Optional[float] = None
    """Average days on market."""

    avg_sale_price: Optional[float] = None

    county_fips: Optional[str] = None

    median_sale_price: Optional[float] = None

    price_yoy_pct: Optional[float] = None

    quarter: Optional[str] = None

    sale_count: Optional[int] = None

    state_fips: Optional[str] = None

    total_volume: Optional[float] = None


class ParcelSummary(BaseModel):
    avg_assessed_value: Optional[float] = None

    parcel_count: Optional[int] = None


class CountyRetrieveDetailResponse(BaseModel):
    affordability: Optional[List[AffordabilityRow]] = None

    flip_summary: Optional[FlipSummary] = None

    market_stats: Optional[List[MarketStat]] = None

    parcel_summary: Optional[ParcelSummary] = None
