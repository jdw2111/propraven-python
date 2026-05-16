# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from propraven import Propraven, AsyncPropraven
from tests.utils import assert_matches_type
from propraven.types.v1 import (
    DealFindFlipsResponse,
    DealSearchLendersResponse,
    DealFindHighLandRatioResponse,
    DealSearchContractorsResponse,
    DealFindAbsenteeOwnersResponse,
    DealFindLongHoldParcelsResponse,
    DealFindPortfolioOwnersResponse,
    DealRetrieveMarketSummaryResponse,
    DealFindEntityOwnedParcelsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_absentee_owners(self, client: Propraven) -> None:
        deal = client.v1.deals.find_absentee_owners()
        assert_matches_type(DealFindAbsenteeOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_absentee_owners_with_all_params(self, client: Propraven) -> None:
        deal = client.v1.deals.find_absentee_owners(
            county_fips="37183",
            limit=1,
            min_value=50000,
            offset=0,
            out_of_state=True,
            state_fips="37",
        )
        assert_matches_type(DealFindAbsenteeOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_absentee_owners(self, client: Propraven) -> None:
        response = client.v1.deals.with_raw_response.find_absentee_owners()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(DealFindAbsenteeOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_absentee_owners(self, client: Propraven) -> None:
        with client.v1.deals.with_streaming_response.find_absentee_owners() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(DealFindAbsenteeOwnersResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_entity_owned_parcels(self, client: Propraven) -> None:
        deal = client.v1.deals.find_entity_owned_parcels()
        assert_matches_type(DealFindEntityOwnedParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_entity_owned_parcels_with_all_params(self, client: Propraven) -> None:
        deal = client.v1.deals.find_entity_owned_parcels(
            county_fips="37183",
            entity_type="LLC",
            limit=1,
            min_value=0,
            offset=0,
            search="BLACKSTONE",
            state_fips="37",
            top=True,
            zoning="zoning",
        )
        assert_matches_type(DealFindEntityOwnedParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_entity_owned_parcels(self, client: Propraven) -> None:
        response = client.v1.deals.with_raw_response.find_entity_owned_parcels()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(DealFindEntityOwnedParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_entity_owned_parcels(self, client: Propraven) -> None:
        with client.v1.deals.with_streaming_response.find_entity_owned_parcels() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(DealFindEntityOwnedParcelsResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_flips(self, client: Propraven) -> None:
        deal = client.v1.deals.find_flips()
        assert_matches_type(DealFindFlipsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_flips_with_all_params(self, client: Propraven) -> None:
        deal = client.v1.deals.find_flips(
            county_fips="37183",
            flip_tier="quick",
            limit=1,
            min_profit=25000,
            offset=0,
            state_fips="37",
            view="flippers",
        )
        assert_matches_type(DealFindFlipsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_flips(self, client: Propraven) -> None:
        response = client.v1.deals.with_raw_response.find_flips()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(DealFindFlipsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_flips(self, client: Propraven) -> None:
        with client.v1.deals.with_streaming_response.find_flips() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(DealFindFlipsResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_high_land_ratio(self, client: Propraven) -> None:
        deal = client.v1.deals.find_high_land_ratio()
        assert_matches_type(DealFindHighLandRatioResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_high_land_ratio_with_all_params(self, client: Propraven) -> None:
        deal = client.v1.deals.find_high_land_ratio(
            county_fips="county_fips",
            limit=1,
            min_ratio=1,
            min_value=0,
            offset=0,
            state_fips="state_fips",
            zoning="zoning",
        )
        assert_matches_type(DealFindHighLandRatioResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_high_land_ratio(self, client: Propraven) -> None:
        response = client.v1.deals.with_raw_response.find_high_land_ratio()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(DealFindHighLandRatioResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_high_land_ratio(self, client: Propraven) -> None:
        with client.v1.deals.with_streaming_response.find_high_land_ratio() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(DealFindHighLandRatioResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_long_hold_parcels(self, client: Propraven) -> None:
        deal = client.v1.deals.find_long_hold_parcels()
        assert_matches_type(DealFindLongHoldParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_long_hold_parcels_with_all_params(self, client: Propraven) -> None:
        deal = client.v1.deals.find_long_hold_parcels(
            county_fips="county_fips",
            hold_tier="10-15yr",
            limit=1,
            min_value=0,
            min_years=0,
            offset=0,
            state_fips="state_fips",
        )
        assert_matches_type(DealFindLongHoldParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_long_hold_parcels(self, client: Propraven) -> None:
        response = client.v1.deals.with_raw_response.find_long_hold_parcels()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(DealFindLongHoldParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_long_hold_parcels(self, client: Propraven) -> None:
        with client.v1.deals.with_streaming_response.find_long_hold_parcels() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(DealFindLongHoldParcelsResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_portfolio_owners(self, client: Propraven) -> None:
        deal = client.v1.deals.find_portfolio_owners()
        assert_matches_type(DealFindPortfolioOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_portfolio_owners_with_all_params(self, client: Propraven) -> None:
        deal = client.v1.deals.find_portfolio_owners(
            limit=1,
            min_properties=0,
            min_value=0,
            offset=0,
            search="search",
            state="NC",
        )
        assert_matches_type(DealFindPortfolioOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_portfolio_owners(self, client: Propraven) -> None:
        response = client.v1.deals.with_raw_response.find_portfolio_owners()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(DealFindPortfolioOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_portfolio_owners(self, client: Propraven) -> None:
        with client.v1.deals.with_streaming_response.find_portfolio_owners() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(DealFindPortfolioOwnersResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_market_summary(self, client: Propraven) -> None:
        deal = client.v1.deals.retrieve_market_summary()
        assert_matches_type(DealRetrieveMarketSummaryResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_market_summary_with_all_params(self, client: Propraven) -> None:
        deal = client.v1.deals.retrieve_market_summary(
            county_fips="county_fips",
            limit=1,
            offset=0,
            rating="AFFORDABLE",
            state_fips="state_fips",
            view="affordability",
            year="2024",
        )
        assert_matches_type(DealRetrieveMarketSummaryResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_market_summary(self, client: Propraven) -> None:
        response = client.v1.deals.with_raw_response.retrieve_market_summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(DealRetrieveMarketSummaryResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_market_summary(self, client: Propraven) -> None:
        with client.v1.deals.with_streaming_response.retrieve_market_summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(DealRetrieveMarketSummaryResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_contractors(self, client: Propraven) -> None:
        deal = client.v1.deals.search_contractors()
        assert_matches_type(DealSearchContractorsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_contractors_with_all_params(self, client: Propraven) -> None:
        deal = client.v1.deals.search_contractors(
            limit=1,
            min_permits=1,
            min_value=0,
            offset=0,
            search="SMITH CONSTRUCTION",
            state="NC",
        )
        assert_matches_type(DealSearchContractorsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_contractors(self, client: Propraven) -> None:
        response = client.v1.deals.with_raw_response.search_contractors()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(DealSearchContractorsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_contractors(self, client: Propraven) -> None:
        with client.v1.deals.with_streaming_response.search_contractors() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(DealSearchContractorsResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_lenders(self, client: Propraven) -> None:
        deal = client.v1.deals.search_lenders()
        assert_matches_type(DealSearchLendersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_lenders_with_all_params(self, client: Propraven) -> None:
        deal = client.v1.deals.search_lenders(
            limit=1,
            min_mortgages=0,
            offset=0,
            search="WELLS FARGO",
            state="NC",
        )
        assert_matches_type(DealSearchLendersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_lenders(self, client: Propraven) -> None:
        response = client.v1.deals.with_raw_response.search_lenders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(DealSearchLendersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_lenders(self, client: Propraven) -> None:
        with client.v1.deals.with_streaming_response.search_lenders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(DealSearchLendersResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_absentee_owners(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_absentee_owners()
        assert_matches_type(DealFindAbsenteeOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_absentee_owners_with_all_params(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_absentee_owners(
            county_fips="37183",
            limit=1,
            min_value=50000,
            offset=0,
            out_of_state=True,
            state_fips="37",
        )
        assert_matches_type(DealFindAbsenteeOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_absentee_owners(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.deals.with_raw_response.find_absentee_owners()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(DealFindAbsenteeOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_absentee_owners(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.deals.with_streaming_response.find_absentee_owners() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(DealFindAbsenteeOwnersResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_entity_owned_parcels(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_entity_owned_parcels()
        assert_matches_type(DealFindEntityOwnedParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_entity_owned_parcels_with_all_params(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_entity_owned_parcels(
            county_fips="37183",
            entity_type="LLC",
            limit=1,
            min_value=0,
            offset=0,
            search="BLACKSTONE",
            state_fips="37",
            top=True,
            zoning="zoning",
        )
        assert_matches_type(DealFindEntityOwnedParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_entity_owned_parcels(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.deals.with_raw_response.find_entity_owned_parcels()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(DealFindEntityOwnedParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_entity_owned_parcels(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.deals.with_streaming_response.find_entity_owned_parcels() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(DealFindEntityOwnedParcelsResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_flips(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_flips()
        assert_matches_type(DealFindFlipsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_flips_with_all_params(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_flips(
            county_fips="37183",
            flip_tier="quick",
            limit=1,
            min_profit=25000,
            offset=0,
            state_fips="37",
            view="flippers",
        )
        assert_matches_type(DealFindFlipsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_flips(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.deals.with_raw_response.find_flips()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(DealFindFlipsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_flips(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.deals.with_streaming_response.find_flips() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(DealFindFlipsResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_high_land_ratio(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_high_land_ratio()
        assert_matches_type(DealFindHighLandRatioResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_high_land_ratio_with_all_params(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_high_land_ratio(
            county_fips="county_fips",
            limit=1,
            min_ratio=1,
            min_value=0,
            offset=0,
            state_fips="state_fips",
            zoning="zoning",
        )
        assert_matches_type(DealFindHighLandRatioResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_high_land_ratio(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.deals.with_raw_response.find_high_land_ratio()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(DealFindHighLandRatioResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_high_land_ratio(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.deals.with_streaming_response.find_high_land_ratio() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(DealFindHighLandRatioResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_long_hold_parcels(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_long_hold_parcels()
        assert_matches_type(DealFindLongHoldParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_long_hold_parcels_with_all_params(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_long_hold_parcels(
            county_fips="county_fips",
            hold_tier="10-15yr",
            limit=1,
            min_value=0,
            min_years=0,
            offset=0,
            state_fips="state_fips",
        )
        assert_matches_type(DealFindLongHoldParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_long_hold_parcels(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.deals.with_raw_response.find_long_hold_parcels()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(DealFindLongHoldParcelsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_long_hold_parcels(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.deals.with_streaming_response.find_long_hold_parcels() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(DealFindLongHoldParcelsResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_portfolio_owners(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_portfolio_owners()
        assert_matches_type(DealFindPortfolioOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_portfolio_owners_with_all_params(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.find_portfolio_owners(
            limit=1,
            min_properties=0,
            min_value=0,
            offset=0,
            search="search",
            state="NC",
        )
        assert_matches_type(DealFindPortfolioOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_portfolio_owners(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.deals.with_raw_response.find_portfolio_owners()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(DealFindPortfolioOwnersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_portfolio_owners(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.deals.with_streaming_response.find_portfolio_owners() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(DealFindPortfolioOwnersResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_market_summary(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.retrieve_market_summary()
        assert_matches_type(DealRetrieveMarketSummaryResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_market_summary_with_all_params(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.retrieve_market_summary(
            county_fips="county_fips",
            limit=1,
            offset=0,
            rating="AFFORDABLE",
            state_fips="state_fips",
            view="affordability",
            year="2024",
        )
        assert_matches_type(DealRetrieveMarketSummaryResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_market_summary(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.deals.with_raw_response.retrieve_market_summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(DealRetrieveMarketSummaryResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_market_summary(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.deals.with_streaming_response.retrieve_market_summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(DealRetrieveMarketSummaryResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_contractors(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.search_contractors()
        assert_matches_type(DealSearchContractorsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_contractors_with_all_params(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.search_contractors(
            limit=1,
            min_permits=1,
            min_value=0,
            offset=0,
            search="SMITH CONSTRUCTION",
            state="NC",
        )
        assert_matches_type(DealSearchContractorsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_contractors(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.deals.with_raw_response.search_contractors()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(DealSearchContractorsResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_contractors(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.deals.with_streaming_response.search_contractors() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(DealSearchContractorsResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_lenders(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.search_lenders()
        assert_matches_type(DealSearchLendersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_lenders_with_all_params(self, async_client: AsyncPropraven) -> None:
        deal = await async_client.v1.deals.search_lenders(
            limit=1,
            min_mortgages=0,
            offset=0,
            search="WELLS FARGO",
            state="NC",
        )
        assert_matches_type(DealSearchLendersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_lenders(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.deals.with_raw_response.search_lenders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(DealSearchLendersResponse, deal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_lenders(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.deals.with_streaming_response.search_lenders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(DealSearchLendersResponse, deal, path=["response"])

        assert cast(Any, response.is_closed) is True
