# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V1RetrieveCoverageParams"]


class V1RetrieveCoverageParams(TypedDict, total=False):
    state: str
    """
    State FIPS code or abbreviation to filter coverage to a specific state and
    return county-level breakdown.
    """
