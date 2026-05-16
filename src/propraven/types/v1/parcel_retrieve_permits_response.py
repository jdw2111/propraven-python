# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .permit import Permit
from ..._models import BaseModel

__all__ = ["ParcelRetrievePermitsResponse"]


class ParcelRetrievePermitsResponse(BaseModel):
    data: Optional[List[Permit]] = None
