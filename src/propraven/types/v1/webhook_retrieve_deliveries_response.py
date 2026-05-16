# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebhookRetrieveDeliveriesResponse", "Delivery"]


class Delivery(BaseModel):
    id: Optional[str] = None

    attempts: Optional[int] = None

    created_at: Optional[datetime] = None

    dead_lettered_at: Optional[datetime] = None

    event_id: Optional[str] = None
    """Deterministic event identifier — sha256(source || pk || event_type).

    Idempotent re-deliveries share this.
    """

    event_occurred_at: Optional[datetime] = None

    event_type: Optional[Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]] = None

    last_attempt_at: Optional[datetime] = None

    last_error: Optional[str] = None

    last_response_body: Optional[str] = None
    """Truncated to ~1KB."""

    last_response_status: Optional[int] = None

    next_attempt_at: Optional[datetime] = None

    status: Optional[Literal["pending", "in_flight", "succeeded", "failed", "dead_lettered"]] = None


class WebhookRetrieveDeliveriesResponse(BaseModel):
    deliveries: Optional[List[Delivery]] = None
