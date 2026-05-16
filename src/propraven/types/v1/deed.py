# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["Deed"]


class Deed(BaseModel):
    deed_type: Optional[str] = None

    document_number: Optional[str] = None

    grantee_name: Optional[str] = None

    grantor_name: Optional[str] = None

    recording_date: Optional[date] = None

    sale_date: Optional[date] = None

    sale_price: Optional[float] = None
