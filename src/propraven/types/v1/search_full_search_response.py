# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .parcel import Parcel
from ..._models import BaseModel

__all__ = ["SearchFullSearchResponse"]


class SearchFullSearchResponse(BaseModel):
    page: Optional[int] = None

    pages: Optional[int] = None

    results: Optional[List[Parcel]] = None

    total: Optional[int] = None
