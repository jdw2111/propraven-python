# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["OwnerRetrieveTransactionsResponse", "Data"]


class Data(BaseModel):
    document_number: Optional[str] = None

    document_type: Optional[str] = None
    """Recorded document type (Warranty Deed, Quit Claim, etc.)."""

    grantee_name: Optional[str] = None

    grantor_name: Optional[str] = None

    property_address: Optional[str] = None

    recording_date: Optional[date] = None

    sale_date: Optional[date] = None

    sale_price: Optional[float] = None
    """USD. Null when state is non-disclosure."""


class OwnerRetrieveTransactionsResponse(BaseModel):
    count: Optional[int] = None

    data: Optional[List[Data]] = None
