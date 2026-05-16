# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OwnerSearchOwnersParams"]


class OwnerSearchOwnersParams(TypedDict, total=False):
    q: Required[str]
    """Search query for owner name."""

    limit: int

    min_properties: int
    """Minimum number of properties owned."""
