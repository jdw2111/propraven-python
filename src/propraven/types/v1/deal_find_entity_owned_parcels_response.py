# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "DealFindEntityOwnedParcelsResponse",
    "UnionMember0",
    "UnionMember0Data",
    "UnionMember1",
    "UnionMember1Data",
    "UnionMember1Summary",
]


class UnionMember0Data(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    county_fips: Optional[str] = None

    entity_type: Optional[Literal["LLC", "CORP", "TRUST", "LP", "LTD", "ASSOCIATION", "OTHER_ENTITY"]] = None

    owner_name: Optional[str] = None

    parcel_id: Optional[str] = None

    state: Optional[str] = None

    state_fips: Optional[str] = None

    total_assessed_value: Optional[float] = None

    zip: Optional[str] = None

    zoning: Optional[str] = None


class UnionMember0(BaseModel):
    data: Optional[List[UnionMember0Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None


class UnionMember1Data(BaseModel):
    entity_type: Optional[str] = None

    owner_name: Optional[str] = None

    parcel_count: Optional[int] = None

    states_arr: Optional[List[str]] = None

    total_value: Optional[float] = None


class UnionMember1Summary(BaseModel):
    corp_count: Optional[int] = None

    llc_count: Optional[int] = None

    lp_count: Optional[int] = None

    total_entities: Optional[int] = None

    total_parcels: Optional[int] = None

    trust_count: Optional[int] = None


class UnionMember1(BaseModel):
    data: Optional[List[UnionMember1Data]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    summary: Optional[UnionMember1Summary] = None

    total: Optional[int] = None


DealFindEntityOwnedParcelsResponse: TypeAlias = Union[UnionMember0, UnionMember1]
