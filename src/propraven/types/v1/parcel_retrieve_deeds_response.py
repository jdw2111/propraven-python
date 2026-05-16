# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .deed import Deed
from ..._models import BaseModel

__all__ = ["ParcelRetrieveDeedsResponse"]


class ParcelRetrieveDeedsResponse(BaseModel):
    data: Optional[List[Deed]] = None
