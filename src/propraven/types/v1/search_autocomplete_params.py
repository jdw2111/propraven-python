# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchAutocompleteParams"]


class SearchAutocompleteParams(TypedDict, total=False):
    q: Required[str]
    """Search prefix. Minimum 2 chars."""
