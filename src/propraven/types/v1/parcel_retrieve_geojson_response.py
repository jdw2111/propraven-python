# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ParcelRetrieveGeojsonResponse", "Feature", "FeatureGeometry", "FeatureProperties"]


class FeatureGeometry(BaseModel):
    coordinates: Optional[List[List[List[float]]]] = None
    """GeoJSON polygon coordinate rings: outer ring first, then any inner rings."""

    type: Optional[Literal["Polygon"]] = None


class FeatureProperties(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    county_fips: Optional[str] = None

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    owner_name: Optional[str] = None

    parcel_id: Optional[str] = None

    property_type: Optional[str] = None

    state: Optional[str] = None

    total_assessed_value: Optional[float] = None

    year_built: Optional[int] = None


class Feature(BaseModel):
    geometry: Optional[FeatureGeometry] = None

    properties: Optional[FeatureProperties] = None

    type: Optional[Literal["Feature"]] = None


class ParcelRetrieveGeojsonResponse(BaseModel):
    """GeoJSON FeatureCollection of parcel polygons.

    Each feature's properties carry the basic parcel summary for popup rendering.
    """

    features: Optional[List[Feature]] = None

    type: Optional[Literal["FeatureCollection"]] = None
