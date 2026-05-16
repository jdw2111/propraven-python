# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .parcel import Parcel
from ..._models import BaseModel

__all__ = ["ParcelRetrieveOwnerResponse", "PortfolioSummary"]


class PortfolioSummary(BaseModel):
    property_count: Optional[int] = None

    states: Optional[List[str]] = None

    total_assessed_value: Optional[float] = None


class ParcelRetrieveOwnerResponse(BaseModel):
    entity_type: Optional[Literal["individual", "corporation", "llc", "trust", "government", "other"]] = None

    mailing_address: Optional[str] = None

    owner_name: Optional[str] = None

    portfolio_summary: Optional[PortfolioSummary] = None

    properties: Optional[List[Parcel]] = None
