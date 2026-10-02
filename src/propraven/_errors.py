"""Exception hierarchy for the PropRaven SDK.

The API answers errors with an RFC 7807 problem body (``application/problem+json``):
``{type, title, status, detail, code, errors?, request_id?, ...}``. A 402 may instead
carry an x402 envelope (``{x402Version, error, accepts}``) and older endpoints may answer
``{"error": "..."}``. :func:`make_status_error` understands all three.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List, Mapping, Optional

import httpx

__all__ = [
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
]


class PropRavenError(Exception):
    """Base class of every exception raised by this library."""


class APIError(PropRavenError):
    """The API answered with an error status (>= 400).

    Attributes mirror the RFC 7807 problem body. ``body`` is the parsed JSON body
    (or the raw text when it is not JSON); ``headers`` are the response headers.
    """

    status: int
    type: Optional[str]
    title: Optional[str]
    detail: Optional[str]
    code: Optional[str]
    errors: List[Dict[str, Any]]
    request_id: Optional[str]
    headers: httpx.Headers
    body: Any
    response: Optional[httpx.Response]

    def __init__(
        self,
        message: str,
        *,
        status: int,
        body: Any = None,
        headers: Optional[Mapping[str, str]] = None,
        response: Optional[httpx.Response] = None,
        type: Optional[str] = None,
        title: Optional[str] = None,
        detail: Optional[str] = None,
        code: Optional[str] = None,
        errors: Optional[List[Dict[str, Any]]] = None,
        request_id: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.body = body
        self.headers = httpx.Headers(headers or {})
        self.response = response
        self.type = type
        self.title = title
        self.detail = detail
        self.code = code
        self.errors = list(errors or [])
        self.request_id = request_id

    @property
    def status_code(self) -> int:
        """Alias of :attr:`status`."""
        return self.status

    def __str__(self) -> str:
        return self.message


# Backwards-friendly alias: the Stainless-era client called this APIStatusError.
APIStatusError = APIError


class BadRequestError(APIError):
    """400."""


class AuthenticationError(APIError):
    """401: missing, invalid or revoked API key."""


class PaymentRequiredError(APIError):
    """402: monthly cap reached, or a paid (x402) resource.

    ``accepts`` holds the x402 payment requirements (empty when the body is a
    problem document). The SDK never signs x402 payments.
    """

    accepts: List[Dict[str, Any]]

    def __init__(self, message: str, *, accepts: Optional[List[Dict[str, Any]]] = None, **kwargs: Any) -> None:
        super().__init__(message, **kwargs)
        self.accepts = list(accepts or [])


class PermissionDeniedError(APIError):
    """403."""


class NotFoundError(APIError):
    """404."""


class MethodNotAllowedError(APIError):
    """405."""


class ConflictError(APIError):
    """409."""


class PayloadTooLargeError(APIError):
    """413."""


class UnprocessableEntityError(APIError):
    """422."""


class RateLimitError(APIError):
    """429. ``retry_after`` is the server's requested wait in seconds (or ``None``)."""

    retry_after: Optional[float]

    def __init__(self, message: str, *, retry_after: Optional[float] = None, **kwargs: Any) -> None:
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class InternalServerError(APIError):
    """Any other status >= 500."""


class ServiceUnavailableError(APIError):
    """503."""


class GatewayTimeoutError(APIError):
    """504 (e.g. ``query_timeout``)."""


class APIConnectionError(PropRavenError):
    """The request never produced a response (DNS, TLS, connection reset, ...)."""

    def __init__(self, message: str = "Connection error.", *, request: Optional[httpx.Request] = None) -> None:
        super().__init__(message)
        self.message = message
        self.request = request


class APITimeoutError(APIConnectionError):
    """The request timed out."""

    def __init__(self, message: str = "Request timed out.", *, request: Optional[httpx.Request] = None) -> None:
        super().__init__(message, request=request)


class WebhookVerificationError(PropRavenError):
    """A webhook signature failed verification (bad signature, stale timestamp, malformed header)."""


_STATUS_MAP = {
    400: BadRequestError,
    401: AuthenticationError,
    402: PaymentRequiredError,
    403: PermissionDeniedError,
    404: NotFoundError,
    405: MethodNotAllowedError,
    409: ConflictError,
    413: PayloadTooLargeError,
    422: UnprocessableEntityError,
    429: RateLimitError,
    503: ServiceUnavailableError,
    504: GatewayTimeoutError,
}


def _str_or_none(value: Any) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, str):
        return value
    return str(value)


def parse_body(response: httpx.Response) -> Any:
    """Parse a response body as JSON when possible, else return the text (or ``None`` if empty)."""
    try:
        text = response.text
    except Exception:  # pragma: no cover - undecodable body
        return None
    if not text:
        return None
    try:
        return json.loads(text)
    except ValueError:
        return text


def make_status_error(response: httpx.Response, *, retry_after: Optional[float] = None) -> APIError:
    """Build the right :class:`APIError` subclass for an error response."""
    status = response.status_code
    body = parse_body(response)
    type_ = title = detail = code = request_id = None
    errors: List[Dict[str, Any]] = []
    accepts: List[Dict[str, Any]] = []

    if isinstance(body, dict):
        type_ = _str_or_none(body.get("type"))
        title = _str_or_none(body.get("title"))
        detail = _str_or_none(body.get("detail"))
        code = _str_or_none(body.get("code"))
        request_id = _str_or_none(body.get("request_id"))
        raw_errors = body.get("errors")
        if isinstance(raw_errors, list):
            errors = [e for e in raw_errors if isinstance(e, dict)]
        legacy = body.get("error")
        if detail is None and legacy is not None:
            # Legacy {"error": "..."} body, or the x402 envelope's "error" member.
            detail = legacy if isinstance(legacy, str) else json.dumps(legacy)
        if detail is None and isinstance(body.get("message"), str):
            detail = body["message"]
        raw_accepts = body.get("accepts")
        if isinstance(raw_accepts, list):
            accepts = [a for a in raw_accepts if isinstance(a, dict)]
        if retry_after is None:
            ra = body.get("retry_after")
            if isinstance(ra, (int, float)) and not isinstance(ra, bool):
                retry_after = float(ra)
    elif isinstance(body, str):
        detail = body.strip()[:500] or None

    if request_id is None:
        request_id = response.headers.get("x-request-id") or response.headers.get("x-vercel-id")
    if code is None and status == 402 and accepts:
        code = "payment_required"

    label = code or title or response.reason_phrase or "error"
    message = f"{status} {label}: {detail}" if detail else f"{status} {label}"

    cls = _STATUS_MAP.get(status)
    if cls is None:
        cls = InternalServerError if status >= 500 else APIError

    kwargs: Dict[str, Any] = dict(
        status=status,
        body=body,
        headers=response.headers,
        response=response,
        type=type_,
        title=title,
        detail=detail,
        code=code,
        errors=errors,
        request_id=request_id,
    )
    if cls is PaymentRequiredError:
        return PaymentRequiredError(message, accepts=accepts, **kwargs)
    if cls is RateLimitError:
        return RateLimitError(message, retry_after=retry_after, **kwargs)
    return cls(message, **kwargs)
