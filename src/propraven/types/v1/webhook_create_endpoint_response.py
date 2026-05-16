# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .webhook import Webhook

__all__ = ["WebhookCreateEndpointResponse"]


class WebhookCreateEndpointResponse(Webhook):
    hint: str
    """Signature-verification reminder."""

    secret: str
    """**Shown once.** Copy and store server-side immediately.

    Used to sign every outgoing delivery.
    """
