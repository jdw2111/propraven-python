# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ParcelRetrieveReportParams"]


class ParcelRetrieveReportParams(TypedDict, total=False):
    county_fips: str
    """5-digit county FIPS. Strongly recommended when passing a county-local id."""
