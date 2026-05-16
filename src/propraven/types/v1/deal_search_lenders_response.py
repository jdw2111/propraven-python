# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["DealSearchLendersResponse", "Data"]


class Data(BaseModel):
    avg_mortgage_amount: Optional[float] = None

    county_count: Optional[int] = None

    first_mortgage_date: Optional[date] = None

    last_mortgage_date: Optional[date] = None

    lender_name_normalized: Optional[str] = None

    lender_rank: Optional[int] = None
    """National rank, 1 = highest volume."""

    median_mortgage_amount: Optional[float] = None

    mortgage_count: Optional[int] = None

    state_count: Optional[int] = None

    states_list: Optional[str] = None

    total_mortgage_volume: Optional[float] = None


class DealSearchLendersResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
