# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountRetrieveUsageResponse", "Period", "RateLimit"]


class Period(BaseModel):
    end: Optional[datetime] = None

    label: Optional[str] = None

    start: Optional[datetime] = None


class RateLimit(BaseModel):
    per_day: Optional[int] = None

    per_minute: Optional[int] = None


class AccountRetrieveUsageResponse(BaseModel):
    calls_included: Optional[int] = None
    """Plan allotment for the current period."""

    calls_remaining: Optional[int] = None

    calls_used: Optional[int] = None

    hard_capped: Optional[bool] = None
    """Whether further calls will be hard-rejected vs allowed-and-billed."""

    period: Optional[Period] = None

    rate_limit: Optional[RateLimit] = None

    tier: Optional[Literal["free", "starter", "pro", "scale", "api_100k"]] = None
