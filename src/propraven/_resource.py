"""Base classes for the generated resource namespaces."""

from __future__ import annotations

from typing import Any

__all__ = ["SyncAPIResource", "AsyncAPIResource"]


class SyncAPIResource:
    def __init__(self, client: Any) -> None:
        self._client = client

    def __repr__(self) -> str:
        return f"<{type(self).__name__}>"


class AsyncAPIResource:
    def __init__(self, client: Any) -> None:
        self._client = client

    def __repr__(self) -> str:
        return f"<{type(self).__name__}>"
