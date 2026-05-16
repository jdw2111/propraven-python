# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Parcel"]


class Parcel(BaseModel):
    absentee_owner: Optional[bool] = None

    acreage: Optional[float] = None

    address: Optional[str] = None

    assessed_value: Optional[float] = None

    city: Optional[str] = None

    county_fips: Optional[str] = None
    """5-digit county FIPS code."""

    county_name: Optional[str] = None

    crime_score: Optional[float] = None
    """Crime score from 0 (low) to 100 (high)."""

    deal_score: Optional[float] = None
    """Composite deal opportunity score from 0 to 100."""

    improvement_value: Optional[float] = None

    land_use: Optional[str] = None

    land_value: Optional[float] = None

    last_sale_date: Optional[date] = None

    last_sale_price: Optional[float] = None

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    mailing_address: Optional[str] = None

    market_value: Optional[float] = None

    owner_name: Optional[str] = None

    owner_type: Optional[Literal["individual", "corporation", "llc", "trust", "government", "other"]] = None

    parcel_id: Optional[str] = None
    """County-assigned parcel identifier."""

    state_abbr: Optional[str] = None

    state_fips: Optional[str] = None

    year_built: Optional[int] = None

    zip: Optional[str] = None

    zoning: Optional[str] = None

    zoning_category: Optional[Literal["residential", "commercial", "industrial", "agricultural", "mixed", "other"]] = (
        None
    )
