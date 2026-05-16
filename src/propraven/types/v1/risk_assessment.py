# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RiskAssessment", "AirQuality", "Crime", "FloodZone", "Wildfire"]


class AirQuality(BaseModel):
    category: Optional[
        Literal["good", "moderate", "unhealthy_sensitive", "unhealthy", "very_unhealthy", "hazardous"]
    ] = None

    median_aqi: Optional[float] = None
    """Median Air Quality Index value."""


class Crime(BaseModel):
    score: Optional[float] = None
    """Crime score from 0 (low) to 100 (high)."""

    tier: Optional[Literal["very_low", "low", "moderate", "high", "very_high"]] = None

    trend: Optional[Literal["decreasing", "stable", "increasing"]] = None


class FloodZone(BaseModel):
    description: Optional[str] = None

    in_floodplain: Optional[bool] = None

    zone: Optional[str] = None
    """FEMA flood zone designation."""


class Wildfire(BaseModel):
    burn_probability: Optional[float] = None
    """Annual burn probability as a decimal."""

    risk_class: Optional[Literal["low", "moderate", "high", "very_high", "extreme"]] = None


class RiskAssessment(BaseModel):
    air_quality: Optional[AirQuality] = None

    crime: Optional[Crime] = None

    flood_zone: Optional[FloodZone] = None

    wildfire: Optional[Wildfire] = None
