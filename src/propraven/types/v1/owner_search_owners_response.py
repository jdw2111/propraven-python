# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .owner import Owner
from ..._models import BaseModel

__all__ = ["OwnerSearchOwnersResponse"]


class OwnerSearchOwnersResponse(BaseModel):
    data: Optional[List[Owner]] = None
