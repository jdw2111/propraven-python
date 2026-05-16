# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from propraven import Propraven, AsyncPropraven
from tests.utils import assert_matches_type
from propraven.types.v1 import (
    SearchFullSearchResponse,
    SearchAutocompleteResponse,
    SearchParcelSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete(self, client: Propraven) -> None:
        search = client.v1.search.autocomplete(
            q="xx",
        )
        assert_matches_type(SearchAutocompleteResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_autocomplete(self, client: Propraven) -> None:
        response = client.v1.search.with_raw_response.autocomplete(
            q="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchAutocompleteResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_autocomplete(self, client: Propraven) -> None:
        with client.v1.search.with_streaming_response.autocomplete(
            q="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchAutocompleteResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_results(self, client: Propraven) -> None:
        search = client.v1.search.export_results()
        assert_matches_type(str, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_results_with_all_params(self, client: Propraven) -> None:
        search = client.v1.search.export_results(
            east=0,
            limit=1,
            north=0,
            order="asc",
            sort="address",
            south=0,
            west=0,
            zoning_categories="zoningCategories",
        )
        assert_matches_type(str, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_export_results(self, client: Propraven) -> None:
        response = client.v1.search.with_raw_response.export_results()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(str, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_export_results(self, client: Propraven) -> None:
        with client.v1.search.with_streaming_response.export_results() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(str, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_full_search(self, client: Propraven) -> None:
        search = client.v1.search.full_search(
            q="xx",
        )
        assert_matches_type(SearchFullSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_full_search_with_all_params(self, client: Propraven) -> None:
        search = client.v1.search.full_search(
            q="xx",
            city="city",
            dir="asc",
            field="all",
            limit=1,
            page=1,
            sort="address",
            state="xx",
        )
        assert_matches_type(SearchFullSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_full_search(self, client: Propraven) -> None:
        response = client.v1.search.with_raw_response.full_search(
            q="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchFullSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_full_search(self, client: Propraven) -> None:
        with client.v1.search.with_streaming_response.full_search(
            q="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchFullSearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_parcel_search(self, client: Propraven) -> None:
        search = client.v1.search.parcel_search(
            bounds={
                "east": -78.55,
                "north": 35.85,
                "south": 35.75,
                "west": -78.7,
            },
        )
        assert_matches_type(SearchParcelSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_parcel_search_with_all_params(self, client: Propraven) -> None:
        search = client.v1.search.parcel_search(
            bounds={
                "east": -78.55,
                "north": 35.85,
                "south": 35.75,
                "west": -78.7,
            },
            filters={
                "absentee_only": True,
                "acreage_range": {
                    "max": 10,
                    "min": 0.5,
                },
                "owner_types": ["individual"],
                "value_range": {
                    "max": 500000,
                    "min": 100000,
                },
                "year_built_range": {
                    "max": 2024,
                    "min": 1990,
                },
                "zoning_categories": ["residential", "commercial"],
            },
            limit=1,
            offset=0,
            order="asc",
            sort="assessed_value",
        )
        assert_matches_type(SearchParcelSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_parcel_search(self, client: Propraven) -> None:
        response = client.v1.search.with_raw_response.parcel_search(
            bounds={
                "east": -78.55,
                "north": 35.85,
                "south": 35.75,
                "west": -78.7,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchParcelSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_parcel_search(self, client: Propraven) -> None:
        with client.v1.search.with_streaming_response.parcel_search(
            bounds={
                "east": -78.55,
                "north": 35.85,
                "south": 35.75,
                "west": -78.7,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchParcelSearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete(self, async_client: AsyncPropraven) -> None:
        search = await async_client.v1.search.autocomplete(
            q="xx",
        )
        assert_matches_type(SearchAutocompleteResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_autocomplete(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.search.with_raw_response.autocomplete(
            q="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchAutocompleteResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_autocomplete(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.search.with_streaming_response.autocomplete(
            q="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchAutocompleteResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_results(self, async_client: AsyncPropraven) -> None:
        search = await async_client.v1.search.export_results()
        assert_matches_type(str, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_results_with_all_params(self, async_client: AsyncPropraven) -> None:
        search = await async_client.v1.search.export_results(
            east=0,
            limit=1,
            north=0,
            order="asc",
            sort="address",
            south=0,
            west=0,
            zoning_categories="zoningCategories",
        )
        assert_matches_type(str, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_export_results(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.search.with_raw_response.export_results()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(str, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_export_results(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.search.with_streaming_response.export_results() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(str, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_full_search(self, async_client: AsyncPropraven) -> None:
        search = await async_client.v1.search.full_search(
            q="xx",
        )
        assert_matches_type(SearchFullSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_full_search_with_all_params(self, async_client: AsyncPropraven) -> None:
        search = await async_client.v1.search.full_search(
            q="xx",
            city="city",
            dir="asc",
            field="all",
            limit=1,
            page=1,
            sort="address",
            state="xx",
        )
        assert_matches_type(SearchFullSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_full_search(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.search.with_raw_response.full_search(
            q="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchFullSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_full_search(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.search.with_streaming_response.full_search(
            q="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchFullSearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_parcel_search(self, async_client: AsyncPropraven) -> None:
        search = await async_client.v1.search.parcel_search(
            bounds={
                "east": -78.55,
                "north": 35.85,
                "south": 35.75,
                "west": -78.7,
            },
        )
        assert_matches_type(SearchParcelSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_parcel_search_with_all_params(self, async_client: AsyncPropraven) -> None:
        search = await async_client.v1.search.parcel_search(
            bounds={
                "east": -78.55,
                "north": 35.85,
                "south": 35.75,
                "west": -78.7,
            },
            filters={
                "absentee_only": True,
                "acreage_range": {
                    "max": 10,
                    "min": 0.5,
                },
                "owner_types": ["individual"],
                "value_range": {
                    "max": 500000,
                    "min": 100000,
                },
                "year_built_range": {
                    "max": 2024,
                    "min": 1990,
                },
                "zoning_categories": ["residential", "commercial"],
            },
            limit=1,
            offset=0,
            order="asc",
            sort="assessed_value",
        )
        assert_matches_type(SearchParcelSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_parcel_search(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.search.with_raw_response.parcel_search(
            bounds={
                "east": -78.55,
                "north": 35.85,
                "south": 35.75,
                "west": -78.7,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchParcelSearchResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_parcel_search(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.search.with_streaming_response.parcel_search(
            bounds={
                "east": -78.55,
                "north": 35.85,
                "south": 35.75,
                "west": -78.7,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchParcelSearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
