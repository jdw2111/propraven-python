# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["WebhookFilter", "ParcelIDs", "StateFips", "UnionMember2"]


class ParcelIDs(BaseModel):
    parcel_ids: List[str]
    """Composite parcel IDs to subscribe to. 1–1000 IDs."""


class StateFips(BaseModel):
    state_fips: str
    """2-digit state FIPS — subscribe to all parcels in this state."""


class UnionMember2(BaseModel):
    county_fips: str
    """
    3-digit county FIPS (within the state) — subscribe to all parcels in this
    county.
    """

    state_fips: str


WebhookFilter: TypeAlias = Union[ParcelIDs, StateFips, UnionMember2]
