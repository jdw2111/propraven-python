# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DealFindPortfolioOwnersResponse", "Data"]


class Data(BaseModel):
    avg_assessed_value: Optional[float] = None

    county_count: Optional[int] = None

    owner_name_normalized: Optional[str] = None

    owner_state: Optional[str] = None

    portfolio_rank: Optional[int] = None
    """National rank, 1 = largest portfolio."""

    property_count: Optional[int] = None

    state_count: Optional[int] = None

    states_list: Optional[str] = None

    total_acreage: Optional[float] = None

    total_assessed_value: Optional[float] = None


class DealFindPortfolioOwnersResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
