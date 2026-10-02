"""Transport helpers shared by the sync and async clients: request encoding,
retry policy, rate-limit parsing and response decoding."""

from __future__ import annotations

import json
import math
import random
import time
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from typing import Any, Collection, Dict, List, Mapping, Optional, Tuple, Union
from urllib.parse import quote

import httpx

__all__ = [
    "NOT_GIVEN",
    "NotGiven",
    "RateLimit",
    "MAX_RETRY_WAIT",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_BASE_URL",
]

DEFAULT_BASE_URL = "https://propraven.com"
DEFAULT_TIMEOUT = 60.0
DEFAULT_MAX_RETRIES = 2
#: Longest single wait (seconds) the client will sleep before a retry. If the server
#: asks for longer (e.g. a monthly cap's Retry-After in days) the error is raised instead.
MAX_RETRY_WAIT = 60.0

_IDEMPOTENT = frozenset({"GET", "HEAD", "DELETE", "OPTIONS"})


class NotGiven:
    """Sentinel for "argument not supplied" where ``None`` is meaningful (e.g. ``timeout=None``)."""

    _instance: Optional[NotGiven] = None

    def __new__(cls) -> NotGiven:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()

TimeoutTypes = Union[float, int, httpx.Timeout, None]


@dataclass(frozen=True)
class RateLimit:
    """Rate-limit headers of the most recent response.

    ``reset`` is a Unix epoch in seconds. Any member may be ``None`` when the
    corresponding header was absent.
    """

    limit: Optional[int]
    remaining: Optional[int]
    reset: Optional[int]


def _to_int(value: Optional[str]) -> Optional[int]:
    if value is None:
        return None
    try:
        return int(float(value.strip()))
    except (ValueError, AttributeError):
        return None


def parse_rate_limit(headers: httpx.Headers) -> Optional[RateLimit]:
    limit = headers.get("x-ratelimit-limit")
    remaining = headers.get("x-ratelimit-remaining")
    reset = headers.get("x-ratelimit-reset")
    if limit is None and remaining is None and reset is None:
        return None
    return RateLimit(limit=_to_int(limit), remaining=_to_int(remaining), reset=_to_int(reset))


def parse_retry_after(headers: httpx.Headers, now: Optional[float] = None) -> Optional[float]:
    """``Retry-After`` in seconds (delta-seconds or an HTTP date), or ``None``."""
    raw = headers.get("retry-after")
    if raw is None:
        return None
    raw = raw.strip()
    try:
        seconds = float(raw)
        if math.isnan(seconds) or math.isinf(seconds):
            return None
        return max(0.0, seconds)
    except ValueError:
        pass
    try:
        when = parsedate_to_datetime(raw)
    except (TypeError, ValueError, IndexError):
        return None
    if when is None:  # pragma: no cover - older Pythons return None for junk
        return None
    current = time.time() if now is None else now
    return max(0.0, when.timestamp() - current)


def should_retry_status(method: str, status: int) -> bool:
    if status in (429, 503, 504):
        return True
    if status >= 500 and status != 501:
        return method.upper() in _IDEMPOTENT
    return False


def backoff_delay(attempt: int) -> float:
    """Exponential backoff ``0.5 * 2**attempt`` seconds with +/-25% jitter, capped at 60 s."""
    base = 0.5 * float(2**attempt)
    jitter = base * random.uniform(-0.25, 0.25)
    return min(MAX_RETRY_WAIT, max(0.0, base + jitter))


def retry_delay(headers: httpx.Headers, attempt: int, now: Optional[float] = None) -> Optional[float]:
    """Seconds to wait before retrying a failed response, or ``None`` when the server
    asks for longer than :data:`MAX_RETRY_WAIT` (the caller must then raise)."""
    current = time.time() if now is None else now
    delay = parse_retry_after(headers, now=current)
    if delay is None:
        remaining = _to_int(headers.get("x-ratelimit-remaining"))
        reset = _to_int(headers.get("x-ratelimit-reset"))
        if remaining == 0 and reset is not None:
            delay = max(0.0, reset - current)
    if delay is None:
        return backoff_delay(attempt)
    if delay > MAX_RETRY_WAIT:
        return None
    return delay


def _encode_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, separators=(",", ":"))
    return str(value)


def encode_query(query: Optional[Mapping[str, Any]], explode: Collection[str] = ()) -> List[Tuple[str, str]]:
    """Encode query params: booleans as ``true``/``false``, sequences comma-joined
    (repeated keys for names in ``explode``), ``None`` omitted."""
    out: List[Tuple[str, str]] = []
    if not query:
        return out
    for key, value in query.items():
        if value is None or isinstance(value, NotGiven):
            continue
        if isinstance(value, (list, tuple, set, frozenset)):
            items = [v for v in value if v is not None]
            if key in explode:
                out.extend((key, _encode_scalar(v)) for v in items)
            else:
                out.append((key, ",".join(_encode_scalar(v) for v in items)))
            continue
        out.append((key, _encode_scalar(value)))
    return out


def render_path(template: str, params: Optional[Mapping[str, Any]]) -> str:
    """Substitute ``{name}`` placeholders with URL-encoded values (one segment each)."""
    if not params:
        return template
    path = template
    for name, value in params.items():
        if value is None or (isinstance(value, str) and value == ""):
            raise ValueError(f"Expected a non-empty value for path parameter {name!r}, got {value!r}")
        path = path.replace("{" + name + "}", quote(str(value), safe=""))
    return path


def clean_headers(headers: Optional[Mapping[str, Any]]) -> Dict[str, str]:
    if not headers:
        return {}
    return {k: _encode_scalar(v) for k, v in headers.items() if v is not None and not isinstance(v, NotGiven)}


def clean_body(body: Optional[Mapping[str, Any]]) -> Dict[str, Any]:
    """Drop top-level ``None`` values (``None`` means "not set" for keyword arguments)."""
    if not body:
        return {}
    return {k: v for k, v in body.items() if v is not None and not isinstance(v, NotGiven)}


def decode_response(response: httpx.Response, kind: str) -> Any:
    """Decode a successful response. ``kind`` is ``"json"`` or ``"text"`` (from the spec);
    the response's Content-Type wins when it says JSON."""
    if response.status_code == 204 or not response.content:
        return None
    ctype = response.headers.get("content-type", "").lower()
    if "json" in ctype:
        return response.json()
    if kind == "json":
        try:
            return json.loads(response.text)
        except ValueError:
            return response.text
    return response.text


def to_httpx_timeout(value: TimeoutTypes) -> httpx.Timeout:
    if isinstance(value, httpx.Timeout):
        return value
    return httpx.Timeout(value)
