# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from propraven import Propraven, AsyncPropraven
from tests.utils import assert_matches_type
from propraven.types.v1 import (
    Owner,
    OwnerSearchOwnersResponse,
    OwnerRetrievePropertiesResponse,
    OwnerRetrieveTransactionsResponse,
    OwnerRetrievePortfolioSummaryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOwners:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_portfolio_summary(self, client: Propraven) -> None:
        owner = client.v1.owners.retrieve_portfolio_summary(
            "BLACKROCK FUND ADVISORS",
        )
        assert_matches_type(OwnerRetrievePortfolioSummaryResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_portfolio_summary(self, client: Propraven) -> None:
        response = client.v1.owners.with_raw_response.retrieve_portfolio_summary(
            "BLACKROCK FUND ADVISORS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        owner = response.parse()
        assert_matches_type(OwnerRetrievePortfolioSummaryResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_portfolio_summary(self, client: Propraven) -> None:
        with client.v1.owners.with_streaming_response.retrieve_portfolio_summary(
            "BLACKROCK FUND ADVISORS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            owner = response.parse()
            assert_matches_type(OwnerRetrievePortfolioSummaryResponse, owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_portfolio_summary(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.v1.owners.with_raw_response.retrieve_portfolio_summary(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_profile(self, client: Propraven) -> None:
        owner = client.v1.owners.retrieve_profile(
            "BLACKROCK FUND ADVISORS",
        )
        assert_matches_type(Owner, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_profile(self, client: Propraven) -> None:
        response = client.v1.owners.with_raw_response.retrieve_profile(
            "BLACKROCK FUND ADVISORS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        owner = response.parse()
        assert_matches_type(Owner, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_profile(self, client: Propraven) -> None:
        with client.v1.owners.with_streaming_response.retrieve_profile(
            "BLACKROCK FUND ADVISORS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            owner = response.parse()
            assert_matches_type(Owner, owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_profile(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.v1.owners.with_raw_response.retrieve_profile(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_properties(self, client: Propraven) -> None:
        owner = client.v1.owners.retrieve_properties(
            name="BLACKROCK FUND ADVISORS",
        )
        assert_matches_type(OwnerRetrievePropertiesResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_properties_with_all_params(self, client: Propraven) -> None:
        owner = client.v1.owners.retrieve_properties(
            name="BLACKROCK FUND ADVISORS",
            limit=1,
            offset=0,
        )
        assert_matches_type(OwnerRetrievePropertiesResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_properties(self, client: Propraven) -> None:
        response = client.v1.owners.with_raw_response.retrieve_properties(
            name="BLACKROCK FUND ADVISORS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        owner = response.parse()
        assert_matches_type(OwnerRetrievePropertiesResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_properties(self, client: Propraven) -> None:
        with client.v1.owners.with_streaming_response.retrieve_properties(
            name="BLACKROCK FUND ADVISORS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            owner = response.parse()
            assert_matches_type(OwnerRetrievePropertiesResponse, owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_properties(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.v1.owners.with_raw_response.retrieve_properties(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_transactions(self, client: Propraven) -> None:
        owner = client.v1.owners.retrieve_transactions(
            "BLACKROCK FUND ADVISORS",
        )
        assert_matches_type(OwnerRetrieveTransactionsResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_transactions(self, client: Propraven) -> None:
        response = client.v1.owners.with_raw_response.retrieve_transactions(
            "BLACKROCK FUND ADVISORS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        owner = response.parse()
        assert_matches_type(OwnerRetrieveTransactionsResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_transactions(self, client: Propraven) -> None:
        with client.v1.owners.with_streaming_response.retrieve_transactions(
            "BLACKROCK FUND ADVISORS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            owner = response.parse()
            assert_matches_type(OwnerRetrieveTransactionsResponse, owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_transactions(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.v1.owners.with_raw_response.retrieve_transactions(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_owners(self, client: Propraven) -> None:
        owner = client.v1.owners.search_owners(
            q="BLACKROCK",
        )
        assert_matches_type(OwnerSearchOwnersResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_owners_with_all_params(self, client: Propraven) -> None:
        owner = client.v1.owners.search_owners(
            q="BLACKROCK",
            limit=1,
            min_properties=5,
        )
        assert_matches_type(OwnerSearchOwnersResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_owners(self, client: Propraven) -> None:
        response = client.v1.owners.with_raw_response.search_owners(
            q="BLACKROCK",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        owner = response.parse()
        assert_matches_type(OwnerSearchOwnersResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_owners(self, client: Propraven) -> None:
        with client.v1.owners.with_streaming_response.search_owners(
            q="BLACKROCK",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            owner = response.parse()
            assert_matches_type(OwnerSearchOwnersResponse, owner, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOwners:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_portfolio_summary(self, async_client: AsyncPropraven) -> None:
        owner = await async_client.v1.owners.retrieve_portfolio_summary(
            "BLACKROCK FUND ADVISORS",
        )
        assert_matches_type(OwnerRetrievePortfolioSummaryResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_portfolio_summary(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.owners.with_raw_response.retrieve_portfolio_summary(
            "BLACKROCK FUND ADVISORS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        owner = await response.parse()
        assert_matches_type(OwnerRetrievePortfolioSummaryResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_portfolio_summary(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.owners.with_streaming_response.retrieve_portfolio_summary(
            "BLACKROCK FUND ADVISORS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            owner = await response.parse()
            assert_matches_type(OwnerRetrievePortfolioSummaryResponse, owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_portfolio_summary(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.v1.owners.with_raw_response.retrieve_portfolio_summary(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_profile(self, async_client: AsyncPropraven) -> None:
        owner = await async_client.v1.owners.retrieve_profile(
            "BLACKROCK FUND ADVISORS",
        )
        assert_matches_type(Owner, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_profile(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.owners.with_raw_response.retrieve_profile(
            "BLACKROCK FUND ADVISORS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        owner = await response.parse()
        assert_matches_type(Owner, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_profile(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.owners.with_streaming_response.retrieve_profile(
            "BLACKROCK FUND ADVISORS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            owner = await response.parse()
            assert_matches_type(Owner, owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_profile(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.v1.owners.with_raw_response.retrieve_profile(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_properties(self, async_client: AsyncPropraven) -> None:
        owner = await async_client.v1.owners.retrieve_properties(
            name="BLACKROCK FUND ADVISORS",
        )
        assert_matches_type(OwnerRetrievePropertiesResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_properties_with_all_params(self, async_client: AsyncPropraven) -> None:
        owner = await async_client.v1.owners.retrieve_properties(
            name="BLACKROCK FUND ADVISORS",
            limit=1,
            offset=0,
        )
        assert_matches_type(OwnerRetrievePropertiesResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_properties(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.owners.with_raw_response.retrieve_properties(
            name="BLACKROCK FUND ADVISORS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        owner = await response.parse()
        assert_matches_type(OwnerRetrievePropertiesResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_properties(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.owners.with_streaming_response.retrieve_properties(
            name="BLACKROCK FUND ADVISORS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            owner = await response.parse()
            assert_matches_type(OwnerRetrievePropertiesResponse, owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_properties(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.v1.owners.with_raw_response.retrieve_properties(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_transactions(self, async_client: AsyncPropraven) -> None:
        owner = await async_client.v1.owners.retrieve_transactions(
            "BLACKROCK FUND ADVISORS",
        )
        assert_matches_type(OwnerRetrieveTransactionsResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_transactions(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.owners.with_raw_response.retrieve_transactions(
            "BLACKROCK FUND ADVISORS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        owner = await response.parse()
        assert_matches_type(OwnerRetrieveTransactionsResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_transactions(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.owners.with_streaming_response.retrieve_transactions(
            "BLACKROCK FUND ADVISORS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            owner = await response.parse()
            assert_matches_type(OwnerRetrieveTransactionsResponse, owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_transactions(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.v1.owners.with_raw_response.retrieve_transactions(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_owners(self, async_client: AsyncPropraven) -> None:
        owner = await async_client.v1.owners.search_owners(
            q="BLACKROCK",
        )
        assert_matches_type(OwnerSearchOwnersResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_owners_with_all_params(self, async_client: AsyncPropraven) -> None:
        owner = await async_client.v1.owners.search_owners(
            q="BLACKROCK",
            limit=1,
            min_properties=5,
        )
        assert_matches_type(OwnerSearchOwnersResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_owners(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.owners.with_raw_response.search_owners(
            q="BLACKROCK",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        owner = await response.parse()
        assert_matches_type(OwnerSearchOwnersResponse, owner, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_owners(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.owners.with_streaming_response.search_owners(
            q="BLACKROCK",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            owner = await response.parse()
            assert_matches_type(OwnerSearchOwnersResponse, owner, path=["response"])

        assert cast(Any, response.is_closed) is True
