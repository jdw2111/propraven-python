# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SearchAutocompleteResponse", "Address", "Location", "Parcel"]


class Address(BaseModel):
    """Mapbox-geocoded address suggestion.

    Use to disambiguate user input before calling /api/v1/lookup or /api/v1/parcels/{id}.
    """

    lat: Optional[float] = None

    lng: Optional[float] = None

    name: Optional[str] = None

    type: Optional[Literal["address"]] = None


class Location(BaseModel):
    city: Optional[str] = None

    lat: Optional[float] = None

    lng: Optional[float] = None

    name: Optional[str] = None

    parcel_count: Optional[int] = None

    state: Optional[str] = None

    type: Optional[Literal["city"]] = None


class Parcel(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    county_fips: Optional[str] = None

    parcel_id: Optional[str] = None

    state: Optional[str] = None

    type: Optional[Literal["parcel"]] = None


class SearchAutocompleteResponse(BaseModel):
    addresses: Optional[List[Address]] = None

    locations: Optional[List[Location]] = None

    parcels: Optional[List[Parcel]] = None
