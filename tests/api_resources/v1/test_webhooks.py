# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from propraven import Propraven, AsyncPropraven
from tests.utils import assert_matches_type
from propraven.types.v1 import (
    Webhook,
    WebhookListEndpointsResponse,
    WebhookCreateEndpointResponse,
    WebhookDisableEndpointResponse,
    WebhookRetrieveDeliveriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_endpoint(self, client: Propraven) -> None:
        webhook = client.v1.webhooks.create_endpoint(
            event_types=["parcel.sold"],
            filter_kind="parcel_ids",
            filter_value={"parcel_ids": ["string"]},
            url="https://example.com",
        )
        assert_matches_type(WebhookCreateEndpointResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_endpoint_with_all_params(self, client: Propraven) -> None:
        webhook = client.v1.webhooks.create_endpoint(
            event_types=["parcel.sold"],
            filter_kind="parcel_ids",
            filter_value={"parcel_ids": ["string"]},
            url="https://example.com",
            description="description",
        )
        assert_matches_type(WebhookCreateEndpointResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_endpoint(self, client: Propraven) -> None:
        response = client.v1.webhooks.with_raw_response.create_endpoint(
            event_types=["parcel.sold"],
            filter_kind="parcel_ids",
            filter_value={"parcel_ids": ["string"]},
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookCreateEndpointResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_endpoint(self, client: Propraven) -> None:
        with client.v1.webhooks.with_streaming_response.create_endpoint(
            event_types=["parcel.sold"],
            filter_kind="parcel_ids",
            filter_value={"parcel_ids": ["string"]},
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookCreateEndpointResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disable_endpoint(self, client: Propraven) -> None:
        webhook = client.v1.webhooks.disable_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookDisableEndpointResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disable_endpoint(self, client: Propraven) -> None:
        response = client.v1.webhooks.with_raw_response.disable_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDisableEndpointResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disable_endpoint(self, client: Propraven) -> None:
        with client.v1.webhooks.with_streaming_response.disable_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDisableEndpointResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disable_endpoint(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.webhooks.with_raw_response.disable_endpoint(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_endpoints(self, client: Propraven) -> None:
        webhook = client.v1.webhooks.list_endpoints()
        assert_matches_type(WebhookListEndpointsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_endpoints(self, client: Propraven) -> None:
        response = client.v1.webhooks.with_raw_response.list_endpoints()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListEndpointsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_endpoints(self, client: Propraven) -> None:
        with client.v1.webhooks.with_streaming_response.list_endpoints() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListEndpointsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_deliveries(self, client: Propraven) -> None:
        webhook = client.v1.webhooks.retrieve_deliveries(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookRetrieveDeliveriesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_deliveries(self, client: Propraven) -> None:
        response = client.v1.webhooks.with_raw_response.retrieve_deliveries(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRetrieveDeliveriesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_deliveries(self, client: Propraven) -> None:
        with client.v1.webhooks.with_streaming_response.retrieve_deliveries(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRetrieveDeliveriesResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_deliveries(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.webhooks.with_raw_response.retrieve_deliveries(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_endpoint(self, client: Propraven) -> None:
        webhook = client.v1.webhooks.retrieve_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_endpoint(self, client: Propraven) -> None:
        response = client.v1.webhooks.with_raw_response.retrieve_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_endpoint(self, client: Propraven) -> None:
        with client.v1.webhooks.with_streaming_response.retrieve_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_endpoint(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.webhooks.with_raw_response.retrieve_endpoint(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_endpoint(self, async_client: AsyncPropraven) -> None:
        webhook = await async_client.v1.webhooks.create_endpoint(
            event_types=["parcel.sold"],
            filter_kind="parcel_ids",
            filter_value={"parcel_ids": ["string"]},
            url="https://example.com",
        )
        assert_matches_type(WebhookCreateEndpointResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_endpoint_with_all_params(self, async_client: AsyncPropraven) -> None:
        webhook = await async_client.v1.webhooks.create_endpoint(
            event_types=["parcel.sold"],
            filter_kind="parcel_ids",
            filter_value={"parcel_ids": ["string"]},
            url="https://example.com",
            description="description",
        )
        assert_matches_type(WebhookCreateEndpointResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_endpoint(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.webhooks.with_raw_response.create_endpoint(
            event_types=["parcel.sold"],
            filter_kind="parcel_ids",
            filter_value={"parcel_ids": ["string"]},
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookCreateEndpointResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_endpoint(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.webhooks.with_streaming_response.create_endpoint(
            event_types=["parcel.sold"],
            filter_kind="parcel_ids",
            filter_value={"parcel_ids": ["string"]},
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookCreateEndpointResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disable_endpoint(self, async_client: AsyncPropraven) -> None:
        webhook = await async_client.v1.webhooks.disable_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookDisableEndpointResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disable_endpoint(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.webhooks.with_raw_response.disable_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDisableEndpointResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disable_endpoint(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.webhooks.with_streaming_response.disable_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDisableEndpointResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disable_endpoint(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.webhooks.with_raw_response.disable_endpoint(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_endpoints(self, async_client: AsyncPropraven) -> None:
        webhook = await async_client.v1.webhooks.list_endpoints()
        assert_matches_type(WebhookListEndpointsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_endpoints(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.webhooks.with_raw_response.list_endpoints()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListEndpointsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_endpoints(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.webhooks.with_streaming_response.list_endpoints() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListEndpointsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_deliveries(self, async_client: AsyncPropraven) -> None:
        webhook = await async_client.v1.webhooks.retrieve_deliveries(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookRetrieveDeliveriesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_deliveries(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.webhooks.with_raw_response.retrieve_deliveries(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRetrieveDeliveriesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_deliveries(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.webhooks.with_streaming_response.retrieve_deliveries(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRetrieveDeliveriesResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_deliveries(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.webhooks.with_raw_response.retrieve_deliveries(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_endpoint(self, async_client: AsyncPropraven) -> None:
        webhook = await async_client.v1.webhooks.retrieve_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_endpoint(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.webhooks.with_raw_response.retrieve_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_endpoint(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.webhooks.with_streaming_response.retrieve_endpoint(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_endpoint(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.webhooks.with_raw_response.retrieve_endpoint(
                "",
            )
