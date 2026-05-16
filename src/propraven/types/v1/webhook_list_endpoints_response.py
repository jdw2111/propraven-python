# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .webhook import Webhook
from ..._models import BaseModel

__all__ = ["WebhookListEndpointsResponse", "Quota"]


class Quota(BaseModel):
    max_endpoints: Optional[int] = FieldInfo(alias="maxEndpoints", default=None)
    """Max simultaneous active webhook endpoints on this tier."""

    max_events_per_day: Optional[int] = FieldInfo(alias="maxEventsPerDay", default=None)
    """Max event deliveries per UTC day on this tier."""


class WebhookListEndpointsResponse(BaseModel):
    quota: Optional[Quota] = None

    tier: Optional[Literal["free", "starter", "pro", "scale", "api_100k"]] = None

    webhooks: Optional[List[Webhook]] = None
