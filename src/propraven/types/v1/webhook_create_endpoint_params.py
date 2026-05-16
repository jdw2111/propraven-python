# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .webhook_filter_param import WebhookFilterParam

__all__ = ["WebhookCreateEndpointParams"]


class WebhookCreateEndpointParams(TypedDict, total=False):
    event_types: Required[List[Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]]]
    """Event types to subscribe to.

    NOTE: only parcel.sold is live in v1.0; others 501.
    """

    filter_kind: Required[Literal["parcel_ids", "state_fips", "county_fips"]]

    filter_value: Required[WebhookFilterParam]
    """Shape varies with filter_kind.

    parcel_ids: explicit list. state_fips: all parcels in a state. county_fips: all
    parcels in a county within a state.
    """

    url: Required[str]
    """Customer endpoint. https:// only."""

    description: str
    """Optional human-readable label for your dashboard."""
