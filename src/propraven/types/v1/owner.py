# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Owner"]


class Owner(BaseModel):
    entity_type: Optional[Literal["individual", "corporation", "llc", "trust", "government", "other"]] = None

    owner_name: Optional[str] = None

    property_count: Optional[int] = None

    states: Optional[List[str]] = None

    total_assessed_value: Optional[float] = None
