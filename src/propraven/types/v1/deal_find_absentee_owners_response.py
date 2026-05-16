# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .parcel import Parcel
from ..._models import BaseModel

__all__ = ["DealFindAbsenteeOwnersResponse"]


class DealFindAbsenteeOwnersResponse(BaseModel):
    data: Optional[List[Parcel]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
