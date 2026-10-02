"""The PropRaven clients: :class:`PropRaven` (sync) and :class:`AsyncPropRaven` (async).

The per-namespace methods (``client.parcels.get(...)`` etc.) are generated from
``openapi.json`` into :mod:`propraven.resources`; this module holds the hand-written
transport: auth, retries, errors and rate-limit bookkeeping.
"""

from __future__ import annotations

import asyncio
import json
import os
import time
import warnings
from typing import Any, Collection, Dict, Mapping, Optional, Union

import httpx

from ._errors import APIConnectionError, APITimeoutError, make_status_error
from ._transport import (
    DEFAULT_BASE_URL,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
    NOT_GIVEN,
    NotGiven,
    RateLimit,
    TimeoutTypes,
    backoff_delay,
    clean_body,
    clean_headers,
    decode_response,
    encode_query,
    parse_rate_limit,
    parse_retry_after,
    render_path,
    retry_delay,
    should_retry_status,
    to_httpx_timeout,
)
from ._version import __version__
from .resources import AsyncResourcesMixin, SyncResourcesMixin

__all__ = ["PropRaven", "AsyncPropRaven", "Propraven", "AsyncPropraven"]

USER_AGENT = f"propraven-python/{__version__}"


def _sleep(seconds: float) -> None:
    time.sleep(seconds)


async def _asleep(seconds: float) -> None:
    await asyncio.sleep(seconds)


class _BaseClient:
    api_key: Optional[str]
    base_url: str
    timeout: TimeoutTypes
    max_retries: int
    last_rate_limit: Optional[RateLimit]

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: TimeoutTypes = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        if api_key is None:
            api_key = os.environ.get("PROPRAVEN_API_KEY") or None
        if api_key is not None and not api_key.startswith("pz_"):
            warnings.warn(
                "PropRaven API keys start with 'pz_'; the key you supplied does not. Requests will be sent anyway.",
                UserWarning,
                stacklevel=3,
            )
        if base_url is None:
            base_url = os.environ.get("PROPRAVEN_BASE_URL") or DEFAULT_BASE_URL
        if max_retries < 0:
            raise ValueError("max_retries must be >= 0")
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self._default_headers: Dict[str, str] = dict(default_headers or {})
        self.last_rate_limit = None

    def __repr__(self) -> str:
        return f"{type(self).__name__}(base_url={self.base_url!r})"

    # -- request building -------------------------------------------------

    def _headers(self, accept: Optional[str], has_body: bool) -> Dict[str, str]:
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": accept or "application/json",
        }
        if has_body:
            headers["Content-Type"] = "application/json"
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        headers.update(self._default_headers)
        return headers

    def _build_request(
        self,
        http: Union[httpx.Client, httpx.AsyncClient],
        method: str,
        path: str,
        *,
        path_params: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        explode: Collection[str] = (),
        accept: Optional[str] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        timeout: Union[TimeoutTypes, NotGiven] = NOT_GIVEN,
    ) -> httpx.Request:
        url = self.base_url + render_path(path, path_params)
        params = encode_query(query, explode)
        if extra_query:
            override = set(extra_query)
            params = [p for p in params if p[0] not in override] + encode_query(extra_query)

        content: Optional[bytes] = None
        if isinstance(body, Mapping):
            payload: Any = clean_body(body)
            if extra_body:
                payload.update(extra_body)
            content = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        elif body is not None:
            content = json.dumps(body, separators=(",", ":")).encode("utf-8")
        elif extra_body:
            content = json.dumps(dict(extra_body), separators=(",", ":")).encode("utf-8")

        all_headers = self._headers(accept, content is not None)
        all_headers.update(clean_headers(headers))
        if extra_headers:
            all_headers.update(extra_headers)

        effective_timeout = self.timeout if isinstance(timeout, NotGiven) else timeout
        return http.build_request(
            method.upper(),
            url,
            params=tuple(params),
            headers=all_headers,
            content=content,
            timeout=to_httpx_timeout(effective_timeout),
        )

    def _retries(self, max_retries: Union[int, NotGiven]) -> int:
        return self.max_retries if isinstance(max_retries, NotGiven) else max_retries

    def _record(self, response: httpx.Response) -> None:
        self.last_rate_limit = parse_rate_limit(response.headers)


class SyncAPIClient(_BaseClient):
    """Hand-written synchronous core. Use :class:`PropRaven`."""

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: TimeoutTypes = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Optional[Mapping[str, str]] = None,
        http_client: Optional[httpx.Client] = None,
    ) -> None:
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
        )
        self._owns_http = http_client is None
        self._http = http_client if http_client is not None else httpx.Client(follow_redirects=True)

    def close(self) -> None:
        """Close the underlying HTTP client (only if this client created it)."""
        if self._owns_http:
            self._http.close()

    def __enter__(self) -> SyncAPIClient:
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def _request(
        self,
        method: str,
        path: str,
        *,
        kind: str = "json",
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        **kwargs: Any,
    ) -> Any:
        request = self._build_request(self._http, method, path, **kwargs)
        retries = self._retries(max_retries)
        attempt = 0
        while True:
            try:
                response = self._http.send(request)
            except httpx.TimeoutException as exc:
                if attempt < retries:
                    _sleep(backoff_delay(attempt))
                    attempt += 1
                    continue
                raise APITimeoutError(request=request) from exc
            except httpx.TransportError as exc:
                if attempt < retries:
                    _sleep(backoff_delay(attempt))
                    attempt += 1
                    continue
                raise APIConnectionError(f"Connection error: {exc}", request=request) from exc

            self._record(response)
            if response.status_code < 400:
                return decode_response(response, kind)
            if attempt < retries and should_retry_status(method, response.status_code):
                delay = retry_delay(response.headers, attempt)
                if delay is not None:
                    response.close()
                    _sleep(delay)
                    attempt += 1
                    continue
            raise make_status_error(response, retry_after=parse_retry_after(response.headers))

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: Union[TimeoutTypes, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Any:
        """Call any endpoint directly, e.g. ``client.request("GET", "/api/v1/freshness")``.

        Uses the same auth, retries and error mapping as the generated methods.
        """
        return self._request(
            method,
            path,
            query=query,
            body=body,
            extra_headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            kind="json",
        )


class AsyncAPIClient(_BaseClient):
    """Hand-written asynchronous core. Use :class:`AsyncPropRaven`."""

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: TimeoutTypes = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Optional[Mapping[str, str]] = None,
        http_client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
        )
        self._owns_http = http_client is None
        self._http = http_client if http_client is not None else httpx.AsyncClient(follow_redirects=True)

    async def close(self) -> None:
        """Close the underlying HTTP client (only if this client created it)."""
        if self._owns_http:
            await self._http.aclose()

    async def __aenter__(self) -> AsyncAPIClient:
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.close()

    async def _request(
        self,
        method: str,
        path: str,
        *,
        kind: str = "json",
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        **kwargs: Any,
    ) -> Any:
        request = self._build_request(self._http, method, path, **kwargs)
        retries = self._retries(max_retries)
        attempt = 0
        while True:
            try:
                response = await self._http.send(request)
            except httpx.TimeoutException as exc:
                if attempt < retries:
                    await _asleep(backoff_delay(attempt))
                    attempt += 1
                    continue
                raise APITimeoutError(request=request) from exc
            except httpx.TransportError as exc:
                if attempt < retries:
                    await _asleep(backoff_delay(attempt))
                    attempt += 1
                    continue
                raise APIConnectionError(f"Connection error: {exc}", request=request) from exc

            self._record(response)
            if response.status_code < 400:
                return decode_response(response, kind)
            if attempt < retries and should_retry_status(method, response.status_code):
                delay = retry_delay(response.headers, attempt)
                if delay is not None:
                    await response.aclose()
                    await _asleep(delay)
                    attempt += 1
                    continue
            raise make_status_error(response, retry_after=parse_retry_after(response.headers))

    async def request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: Union[TimeoutTypes, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
    ) -> Any:
        """Call any endpoint directly, e.g. ``await client.request("GET", "/api/v1/freshness")``."""
        return await self._request(
            method,
            path,
            query=query,
            body=body,
            extra_headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            kind="json",
        )


class PropRaven(SyncResourcesMixin, SyncAPIClient):
    """Synchronous PropRaven API client.

    Args:
        api_key: API key (``pz_...``). Defaults to the ``PROPRAVEN_API_KEY`` env var.
            Optional: key-optional endpoints work anonymously.
        base_url: Defaults to ``PROPRAVEN_BASE_URL`` or ``https://propraven.com``.
        timeout: Seconds (or an ``httpx.Timeout``) per request; default 60.
        max_retries: Retries for 429/503/504, network errors and (for GET/HEAD/DELETE/OPTIONS) other 5xx; default 2.
        default_headers: Extra headers sent with every request.
        http_client: Bring your own ``httpx.Client`` (proxies, transports, ...).

    Server-side only: the API key is a secret and the REST API sends no CORS headers.
    """

    def __enter__(self) -> PropRaven:
        return self


class AsyncPropRaven(AsyncResourcesMixin, AsyncAPIClient):
    """Asynchronous PropRaven API client. Same options as :class:`PropRaven`
    (``http_client`` is an ``httpx.AsyncClient``)."""

    async def __aenter__(self) -> AsyncPropRaven:
        return self


#: Stainless-era spellings, kept as aliases.
Propraven = PropRaven
AsyncPropraven = AsyncPropRaven
