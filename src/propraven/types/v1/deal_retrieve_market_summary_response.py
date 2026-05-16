# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .affordability_row import AffordabilityRow

__all__ = ["DealRetrieveMarketSummaryResponse", "UnionMember0", "UnionMember0Data", "UnionMember1"]


class UnionMember0Data(BaseModel):
    avg_sale_price: Optional[float] = None

    county_fips: Optional[str] = None

    county_name: Optional[str] = None

    median_sale_price: Optional[float] = None

    sale_count: Optional[int] = None

    state_fips: Optional[str] = None

    year: Optional[int] = None


class UnionMember0(BaseModel):
    data: Optional[List[UnionMember0Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None


class UnionMember1(BaseModel):
    data: Optional[List[AffordabilityRow]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None


DealRetrieveMarketSummaryResponse: TypeAlias = Union[UnionMember0, UnionMember1]
