# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .deed import Deed
from .parcel import Parcel
from .permit import Permit
from ..._models import BaseModel
from .risk_assessment import RiskAssessment

__all__ = ["ParcelRetrieveReportResponse", "ComparableSale", "UccLien"]


class ComparableSale(BaseModel):
    comp_baths: Optional[float] = None

    comp_beds: Optional[int] = None

    comp_parcel_id: Optional[str] = None

    comp_sale_date: Optional[date] = None

    comp_sale_price: Optional[float] = None

    comp_sqft: Optional[int] = None

    distance_miles: Optional[float] = None

    similarity_score: Optional[float] = None


class UccLien(BaseModel):
    debtor_name: Optional[str] = None

    filing_date: Optional[date] = None

    filing_id: Optional[str] = None

    filing_status: Optional[str] = None

    lapse_date: Optional[date] = None

    match_confidence: Optional[float] = None

    match_method: Optional[str] = None

    secured_party: Optional[str] = None


class ParcelRetrieveReportResponse(BaseModel):
    """Comprehensive parcel report — every PropRaven data point joined per parcel.

    Subsections are populated on a best-effort basis; missing data is omitted rather than nulled.
    """

    comparable_sales: Optional[List[ComparableSale]] = None

    deeds: Optional[List[Deed]] = None

    parcel: Optional[Parcel] = None

    permits: Optional[List[Permit]] = None

    risk: Optional[RiskAssessment] = None

    ucc_liens: Optional[List[UccLien]] = None
