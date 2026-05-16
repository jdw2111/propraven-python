# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["DealSearchContractorsResponse", "Data"]


class Data(BaseModel):
    active_years: Optional[float] = None

    avg_permit_value: Optional[float] = None

    contractor_license: Optional[str] = None

    contractor_name_normalized: Optional[str] = None

    contractor_rank: Optional[int] = None
    """National rank, 1 = highest activity."""

    county_count: Optional[int] = None

    first_permit_date: Optional[date] = None

    jurisdiction_count: Optional[int] = None

    last_permit_date: Optional[date] = None

    permit_count: Optional[int] = None

    state_count: Optional[int] = None

    states_list: Optional[str] = None
    """Comma-delimited 2-letter state codes."""

    top_permit_types: Optional[List[str]] = None

    total_permit_value: Optional[float] = None


class DealSearchContractorsResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
