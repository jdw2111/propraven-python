"""Official Python SDK for the PropRaven property-intelligence API.

Quick start::

    from propraven import PropRaven

    client = PropRaven()  # reads PROPRAVEN_API_KEY
    parcel = client.parcels.get("37:119:12104406")
"""

from . import types, webhooks
from ._client import AsyncPropRaven, AsyncPropraven, PropRaven, Propraven
from ._errors import (
    APIConnectionError,
    APIError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    GatewayTimeoutError,
    InternalServerError,
    MethodNotAllowedError,
    NotFoundError,
    PayloadTooLargeError,
    PaymentRequiredError,
    PermissionDeniedError,
    PropRavenError,
    RateLimitError,
    ServiceUnavailableError,
    UnprocessableEntityError,
    WebhookVerificationError,
)
from ._transport import DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT, NOT_GIVEN, NotGiven, RateLimit
from ._version import __title__, __version__
from .webhooks import verify as verify_webhook

__all__ = [
    "PropRaven",
    "AsyncPropRaven",
    "Propraven",
    "AsyncPropraven",
    "PropRavenError",
    "APIError",
    "APIStatusError",
    "BadRequestError",
    "AuthenticationError",
    "PaymentRequiredError",
    "PermissionDeniedError",
    "NotFoundError",
    "MethodNotAllowedError",
    "ConflictError",
    "PayloadTooLargeError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "ServiceUnavailableError",
    "GatewayTimeoutError",
    "APIConnectionError",
    "APITimeoutError",
    "WebhookVerificationError",
    "RateLimit",
    "NOT_GIVEN",
    "NotGiven",
    "DEFAULT_BASE_URL",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "verify_webhook",
    "webhooks",
    "types",
    "__version__",
    "__title__",
]
