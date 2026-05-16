# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["WebhookFilterParam", "ParcelIDs", "StateFips", "UnionMember2"]


class ParcelIDs(TypedDict, total=False):
    parcel_ids: Required[SequenceNotStr[str]]
    """Composite parcel IDs to subscribe to. 1–1000 IDs."""


class StateFips(TypedDict, total=False):
    state_fips: Required[str]
    """2-digit state FIPS — subscribe to all parcels in this state."""


class UnionMember2(TypedDict, total=False):
    county_fips: Required[str]
    """
    3-digit county FIPS (within the state) — subscribe to all parcels in this
    county.
    """

    state_fips: Required[str]


WebhookFilterParam: TypeAlias = Union[ParcelIDs, StateFips, UnionMember2]
