# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from propraven import Propraven, AsyncPropraven
from tests.utils import assert_matches_type
from propraven.types.v1 import (
    MarketRetrieveTrendsResponse,
    MarketRetrieveFlipActivityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarket:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_flip_activity(self, client: Propraven) -> None:
        market = client.v1.market.retrieve_flip_activity()
        assert_matches_type(MarketRetrieveFlipActivityResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_flip_activity_with_all_params(self, client: Propraven) -> None:
        market = client.v1.market.retrieve_flip_activity(
            limit=1,
            offset=0,
            state_fips="37",
        )
        assert_matches_type(MarketRetrieveFlipActivityResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_flip_activity(self, client: Propraven) -> None:
        response = client.v1.market.with_raw_response.retrieve_flip_activity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(MarketRetrieveFlipActivityResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_flip_activity(self, client: Propraven) -> None:
        with client.v1.market.with_streaming_response.retrieve_flip_activity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(MarketRetrieveFlipActivityResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_trends(self, client: Propraven) -> None:
        market = client.v1.market.retrieve_trends()
        assert_matches_type(MarketRetrieveTrendsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_trends_with_all_params(self, client: Propraven) -> None:
        market = client.v1.market.retrieve_trends(
            county_fips="37183,37063",
            state_fips="37",
        )
        assert_matches_type(MarketRetrieveTrendsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_trends(self, client: Propraven) -> None:
        response = client.v1.market.with_raw_response.retrieve_trends()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(MarketRetrieveTrendsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_trends(self, client: Propraven) -> None:
        with client.v1.market.with_streaming_response.retrieve_trends() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(MarketRetrieveTrendsResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarket:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_flip_activity(self, async_client: AsyncPropraven) -> None:
        market = await async_client.v1.market.retrieve_flip_activity()
        assert_matches_type(MarketRetrieveFlipActivityResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_flip_activity_with_all_params(self, async_client: AsyncPropraven) -> None:
        market = await async_client.v1.market.retrieve_flip_activity(
            limit=1,
            offset=0,
            state_fips="37",
        )
        assert_matches_type(MarketRetrieveFlipActivityResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_flip_activity(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.market.with_raw_response.retrieve_flip_activity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(MarketRetrieveFlipActivityResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_flip_activity(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.market.with_streaming_response.retrieve_flip_activity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(MarketRetrieveFlipActivityResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_trends(self, async_client: AsyncPropraven) -> None:
        market = await async_client.v1.market.retrieve_trends()
        assert_matches_type(MarketRetrieveTrendsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_trends_with_all_params(self, async_client: AsyncPropraven) -> None:
        market = await async_client.v1.market.retrieve_trends(
            county_fips="37183,37063",
            state_fips="37",
        )
        assert_matches_type(MarketRetrieveTrendsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_trends(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.market.with_raw_response.retrieve_trends()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(MarketRetrieveTrendsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_trends(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.market.with_streaming_response.retrieve_trends() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(MarketRetrieveTrendsResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True
