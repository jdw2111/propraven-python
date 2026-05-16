# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .webhook_filter import WebhookFilter

__all__ = ["Webhook"]


class Webhook(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    deliveries_attempted: Optional[int] = None

    deliveries_succeeded: Optional[int] = None

    description: Optional[str] = None

    disabled_at: Optional[datetime] = None

    disabled_reason: Optional[str] = None

    event_types: Optional[List[Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]]] = None

    filter_kind: Optional[Literal["parcel_ids", "state_fips", "county_fips"]] = None

    filter_value: Optional[WebhookFilter] = None
    """Shape varies with filter_kind.

    parcel_ids: explicit list. state_fips: all parcels in a state. county_fips: all
    parcels in a county within a state.
    """

    is_active: Optional[bool] = None

    last_delivery_at: Optional[datetime] = None

    last_success_at: Optional[datetime] = None

    secret_prefix: Optional[str] = None
    """First 14 chars of the secret (whsec\\__ + 8 hex).

    Use to identify the webhook in your dashboard; full secret is shown only at
    create time.
    """

    url: Optional[str] = None
    """Customer endpoint. Must be https://."""
