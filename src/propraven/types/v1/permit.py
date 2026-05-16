# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Permit"]


class Permit(BaseModel):
    contractor: Optional[str] = None

    description: Optional[str] = None

    estimated_cost: Optional[float] = None

    issued_date: Optional[date] = None

    permit_number: Optional[str] = None

    status: Optional[Literal["issued", "pending", "approved", "expired", "completed", "denied"]] = None

    type: Optional[str] = None
