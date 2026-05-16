# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from propraven import Propraven, AsyncPropraven
from tests.utils import assert_matches_type
from propraven.types.v1.market import (
    CountyRetrieveDetailResponse,
    CountyRetrieveStatisticsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCounties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_detail(self, client: Propraven) -> None:
        county = client.v1.market.counties.retrieve_detail(
            "21029",
        )
        assert_matches_type(CountyRetrieveDetailResponse, county, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_detail(self, client: Propraven) -> None:
        response = client.v1.market.counties.with_raw_response.retrieve_detail(
            "21029",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        county = response.parse()
        assert_matches_type(CountyRetrieveDetailResponse, county, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_detail(self, client: Propraven) -> None:
        with client.v1.market.counties.with_streaming_response.retrieve_detail(
            "21029",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            county = response.parse()
            assert_matches_type(CountyRetrieveDetailResponse, county, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_detail(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fips` but received ''"):
            client.v1.market.counties.with_raw_response.retrieve_detail(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_statistics(self, client: Propraven) -> None:
        county = client.v1.market.counties.retrieve_statistics()
        assert_matches_type(CountyRetrieveStatisticsResponse, county, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_statistics_with_all_params(self, client: Propraven) -> None:
        county = client.v1.market.counties.retrieve_statistics(
            limit=1,
            min_sales=50,
            offset=0,
            order="asc",
            quarter="2025Q4",
            sort="sale_count",
            state_fips="37",
        )
        assert_matches_type(CountyRetrieveStatisticsResponse, county, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_statistics(self, client: Propraven) -> None:
        response = client.v1.market.counties.with_raw_response.retrieve_statistics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        county = response.parse()
        assert_matches_type(CountyRetrieveStatisticsResponse, county, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_statistics(self, client: Propraven) -> None:
        with client.v1.market.counties.with_streaming_response.retrieve_statistics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            county = response.parse()
            assert_matches_type(CountyRetrieveStatisticsResponse, county, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCounties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_detail(self, async_client: AsyncPropraven) -> None:
        county = await async_client.v1.market.counties.retrieve_detail(
            "21029",
        )
        assert_matches_type(CountyRetrieveDetailResponse, county, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_detail(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.market.counties.with_raw_response.retrieve_detail(
            "21029",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        county = await response.parse()
        assert_matches_type(CountyRetrieveDetailResponse, county, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_detail(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.market.counties.with_streaming_response.retrieve_detail(
            "21029",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            county = await response.parse()
            assert_matches_type(CountyRetrieveDetailResponse, county, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_detail(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fips` but received ''"):
            await async_client.v1.market.counties.with_raw_response.retrieve_detail(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_statistics(self, async_client: AsyncPropraven) -> None:
        county = await async_client.v1.market.counties.retrieve_statistics()
        assert_matches_type(CountyRetrieveStatisticsResponse, county, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_statistics_with_all_params(self, async_client: AsyncPropraven) -> None:
        county = await async_client.v1.market.counties.retrieve_statistics(
            limit=1,
            min_sales=50,
            offset=0,
            order="asc",
            quarter="2025Q4",
            sort="sale_count",
            state_fips="37",
        )
        assert_matches_type(CountyRetrieveStatisticsResponse, county, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_statistics(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.market.counties.with_raw_response.retrieve_statistics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        county = await response.parse()
        assert_matches_type(CountyRetrieveStatisticsResponse, county, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_statistics(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.market.counties.with_streaming_response.retrieve_statistics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            county = await response.parse()
            assert_matches_type(CountyRetrieveStatisticsResponse, county, path=["response"])

        assert cast(Any, response.is_closed) is True
