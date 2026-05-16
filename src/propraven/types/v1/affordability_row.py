# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AffordabilityRow"]


class AffordabilityRow(BaseModel):
    affordability_rating: Optional[Literal["AFFORDABLE", "MODERATE", "EXPENSIVE", "VERY_EXPENSIVE"]] = None

    county_fips: Optional[str] = None

    county_name: Optional[str] = None

    median_household_income: Optional[float] = None

    median_sale_price: Optional[float] = None

    monthly_payment_estimate: Optional[float] = None

    pct_income_for_housing: Optional[float] = None

    price_to_income_ratio: Optional[float] = None

    state_fips: Optional[str] = None

    year: Optional[int] = None
