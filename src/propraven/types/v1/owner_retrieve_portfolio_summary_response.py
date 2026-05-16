# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .parcel import Parcel
from ..._models import BaseModel

__all__ = ["OwnerRetrievePortfolioSummaryResponse", "Summary"]


class Summary(BaseModel):
    avg_assessed_value: Optional[float] = None

    counties: Optional[int] = None

    property_count: Optional[int] = None

    states: Optional[List[str]] = None

    total_assessed_value: Optional[float] = None

    zoning_breakdown: Optional[Dict[str, int]] = None


class OwnerRetrievePortfolioSummaryResponse(BaseModel):
    entity_type: Optional[Literal["individual", "corporation", "llc", "trust", "government", "other"]] = None

    owner_name: Optional[str] = None

    properties: Optional[List[Parcel]] = None

    summary: Optional[Summary] = None
