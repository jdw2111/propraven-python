# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from propraven import Propraven, AsyncPropraven
from tests.utils import assert_matches_type
from propraven.types.v1 import (
    Parcel,
    RiskAssessment,
    ParcelRetrieveDeedsResponse,
    ParcelRetrieveOwnerResponse,
    ParcelRetrieveReportResponse,
    ParcelRetrieveGeojsonResponse,
    ParcelRetrievePermitsResponse,
    ParcelRetrieveTrafficHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParcels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Propraven) -> None:
        parcel = client.v1.parcels.retrieve(
            "37183:0012345",
        )
        assert_matches_type(Parcel, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Propraven) -> None:
        response = client.v1.parcels.with_raw_response.retrieve(
            "37183:0012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = response.parse()
        assert_matches_type(Parcel, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Propraven) -> None:
        with client.v1.parcels.with_streaming_response.retrieve(
            "37183:0012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = response.parse()
            assert_matches_type(Parcel, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.parcels.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_deeds(self, client: Propraven) -> None:
        parcel = client.v1.parcels.retrieve_deeds(
            "37183:0012345",
        )
        assert_matches_type(ParcelRetrieveDeedsResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_deeds(self, client: Propraven) -> None:
        response = client.v1.parcels.with_raw_response.retrieve_deeds(
            "37183:0012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = response.parse()
        assert_matches_type(ParcelRetrieveDeedsResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_deeds(self, client: Propraven) -> None:
        with client.v1.parcels.with_streaming_response.retrieve_deeds(
            "37183:0012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = response.parse()
            assert_matches_type(ParcelRetrieveDeedsResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_deeds(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.parcels.with_raw_response.retrieve_deeds(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_geojson(self, client: Propraven) -> None:
        parcel = client.v1.parcels.retrieve_geojson(
            bbox="-.6...,.1........6,....,-108.6",
            zoom=0,
        )
        assert_matches_type(ParcelRetrieveGeojsonResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_geojson(self, client: Propraven) -> None:
        response = client.v1.parcels.with_raw_response.retrieve_geojson(
            bbox="-.6...,.1........6,....,-108.6",
            zoom=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = response.parse()
        assert_matches_type(ParcelRetrieveGeojsonResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_geojson(self, client: Propraven) -> None:
        with client.v1.parcels.with_streaming_response.retrieve_geojson(
            bbox="-.6...,.1........6,....,-108.6",
            zoom=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = response.parse()
            assert_matches_type(ParcelRetrieveGeojsonResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_owner(self, client: Propraven) -> None:
        parcel = client.v1.parcels.retrieve_owner(
            "37183:0012345",
        )
        assert_matches_type(ParcelRetrieveOwnerResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_owner(self, client: Propraven) -> None:
        response = client.v1.parcels.with_raw_response.retrieve_owner(
            "37183:0012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = response.parse()
        assert_matches_type(ParcelRetrieveOwnerResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_owner(self, client: Propraven) -> None:
        with client.v1.parcels.with_streaming_response.retrieve_owner(
            "37183:0012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = response.parse()
            assert_matches_type(ParcelRetrieveOwnerResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_owner(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.parcels.with_raw_response.retrieve_owner(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_permits(self, client: Propraven) -> None:
        parcel = client.v1.parcels.retrieve_permits(
            "37183:0012345",
        )
        assert_matches_type(ParcelRetrievePermitsResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_permits(self, client: Propraven) -> None:
        response = client.v1.parcels.with_raw_response.retrieve_permits(
            "37183:0012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = response.parse()
        assert_matches_type(ParcelRetrievePermitsResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_permits(self, client: Propraven) -> None:
        with client.v1.parcels.with_streaming_response.retrieve_permits(
            "37183:0012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = response.parse()
            assert_matches_type(ParcelRetrievePermitsResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_permits(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.parcels.with_raw_response.retrieve_permits(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_report(self, client: Propraven) -> None:
        parcel = client.v1.parcels.retrieve_report(
            id="id",
        )
        assert_matches_type(ParcelRetrieveReportResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_report_with_all_params(self, client: Propraven) -> None:
        parcel = client.v1.parcels.retrieve_report(
            id="id",
            county_fips="37183",
        )
        assert_matches_type(ParcelRetrieveReportResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_report(self, client: Propraven) -> None:
        response = client.v1.parcels.with_raw_response.retrieve_report(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = response.parse()
        assert_matches_type(ParcelRetrieveReportResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_report(self, client: Propraven) -> None:
        with client.v1.parcels.with_streaming_response.retrieve_report(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = response.parse()
            assert_matches_type(ParcelRetrieveReportResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_report(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.parcels.with_raw_response.retrieve_report(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_risks(self, client: Propraven) -> None:
        parcel = client.v1.parcels.retrieve_risks(
            "37183:0012345",
        )
        assert_matches_type(RiskAssessment, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_risks(self, client: Propraven) -> None:
        response = client.v1.parcels.with_raw_response.retrieve_risks(
            "37183:0012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = response.parse()
        assert_matches_type(RiskAssessment, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_risks(self, client: Propraven) -> None:
        with client.v1.parcels.with_streaming_response.retrieve_risks(
            "37183:0012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = response.parse()
            assert_matches_type(RiskAssessment, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_risks(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.parcels.with_raw_response.retrieve_risks(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_traffic_history(self, client: Propraven) -> None:
        parcel = client.v1.parcels.retrieve_traffic_history(
            id="id",
            lat=0,
            lng=0,
        )
        assert_matches_type(ParcelRetrieveTrafficHistoryResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_traffic_history(self, client: Propraven) -> None:
        response = client.v1.parcels.with_raw_response.retrieve_traffic_history(
            id="id",
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = response.parse()
        assert_matches_type(ParcelRetrieveTrafficHistoryResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_traffic_history(self, client: Propraven) -> None:
        with client.v1.parcels.with_streaming_response.retrieve_traffic_history(
            id="id",
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = response.parse()
            assert_matches_type(ParcelRetrieveTrafficHistoryResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_traffic_history(self, client: Propraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.parcels.with_raw_response.retrieve_traffic_history(
                id="",
                lat=0,
                lng=0,
            )


class TestAsyncParcels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPropraven) -> None:
        parcel = await async_client.v1.parcels.retrieve(
            "37183:0012345",
        )
        assert_matches_type(Parcel, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.parcels.with_raw_response.retrieve(
            "37183:0012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = await response.parse()
        assert_matches_type(Parcel, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.parcels.with_streaming_response.retrieve(
            "37183:0012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = await response.parse()
            assert_matches_type(Parcel, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.parcels.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_deeds(self, async_client: AsyncPropraven) -> None:
        parcel = await async_client.v1.parcels.retrieve_deeds(
            "37183:0012345",
        )
        assert_matches_type(ParcelRetrieveDeedsResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_deeds(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.parcels.with_raw_response.retrieve_deeds(
            "37183:0012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = await response.parse()
        assert_matches_type(ParcelRetrieveDeedsResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_deeds(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.parcels.with_streaming_response.retrieve_deeds(
            "37183:0012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = await response.parse()
            assert_matches_type(ParcelRetrieveDeedsResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_deeds(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.parcels.with_raw_response.retrieve_deeds(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_geojson(self, async_client: AsyncPropraven) -> None:
        parcel = await async_client.v1.parcels.retrieve_geojson(
            bbox="-.6...,.1........6,....,-108.6",
            zoom=0,
        )
        assert_matches_type(ParcelRetrieveGeojsonResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_geojson(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.parcels.with_raw_response.retrieve_geojson(
            bbox="-.6...,.1........6,....,-108.6",
            zoom=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = await response.parse()
        assert_matches_type(ParcelRetrieveGeojsonResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_geojson(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.parcels.with_streaming_response.retrieve_geojson(
            bbox="-.6...,.1........6,....,-108.6",
            zoom=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = await response.parse()
            assert_matches_type(ParcelRetrieveGeojsonResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_owner(self, async_client: AsyncPropraven) -> None:
        parcel = await async_client.v1.parcels.retrieve_owner(
            "37183:0012345",
        )
        assert_matches_type(ParcelRetrieveOwnerResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_owner(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.parcels.with_raw_response.retrieve_owner(
            "37183:0012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = await response.parse()
        assert_matches_type(ParcelRetrieveOwnerResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_owner(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.parcels.with_streaming_response.retrieve_owner(
            "37183:0012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = await response.parse()
            assert_matches_type(ParcelRetrieveOwnerResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_owner(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.parcels.with_raw_response.retrieve_owner(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_permits(self, async_client: AsyncPropraven) -> None:
        parcel = await async_client.v1.parcels.retrieve_permits(
            "37183:0012345",
        )
        assert_matches_type(ParcelRetrievePermitsResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_permits(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.parcels.with_raw_response.retrieve_permits(
            "37183:0012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = await response.parse()
        assert_matches_type(ParcelRetrievePermitsResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_permits(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.parcels.with_streaming_response.retrieve_permits(
            "37183:0012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = await response.parse()
            assert_matches_type(ParcelRetrievePermitsResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_permits(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.parcels.with_raw_response.retrieve_permits(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_report(self, async_client: AsyncPropraven) -> None:
        parcel = await async_client.v1.parcels.retrieve_report(
            id="id",
        )
        assert_matches_type(ParcelRetrieveReportResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_report_with_all_params(self, async_client: AsyncPropraven) -> None:
        parcel = await async_client.v1.parcels.retrieve_report(
            id="id",
            county_fips="37183",
        )
        assert_matches_type(ParcelRetrieveReportResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_report(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.parcels.with_raw_response.retrieve_report(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = await response.parse()
        assert_matches_type(ParcelRetrieveReportResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_report(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.parcels.with_streaming_response.retrieve_report(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = await response.parse()
            assert_matches_type(ParcelRetrieveReportResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_report(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.parcels.with_raw_response.retrieve_report(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_risks(self, async_client: AsyncPropraven) -> None:
        parcel = await async_client.v1.parcels.retrieve_risks(
            "37183:0012345",
        )
        assert_matches_type(RiskAssessment, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_risks(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.parcels.with_raw_response.retrieve_risks(
            "37183:0012345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = await response.parse()
        assert_matches_type(RiskAssessment, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_risks(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.parcels.with_streaming_response.retrieve_risks(
            "37183:0012345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = await response.parse()
            assert_matches_type(RiskAssessment, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_risks(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.parcels.with_raw_response.retrieve_risks(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_traffic_history(self, async_client: AsyncPropraven) -> None:
        parcel = await async_client.v1.parcels.retrieve_traffic_history(
            id="id",
            lat=0,
            lng=0,
        )
        assert_matches_type(ParcelRetrieveTrafficHistoryResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_traffic_history(self, async_client: AsyncPropraven) -> None:
        response = await async_client.v1.parcels.with_raw_response.retrieve_traffic_history(
            id="id",
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcel = await response.parse()
        assert_matches_type(ParcelRetrieveTrafficHistoryResponse, parcel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_traffic_history(self, async_client: AsyncPropraven) -> None:
        async with async_client.v1.parcels.with_streaming_response.retrieve_traffic_history(
            id="id",
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcel = await response.parse()
            assert_matches_type(ParcelRetrieveTrafficHistoryResponse, parcel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_traffic_history(self, async_client: AsyncPropraven) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.parcels.with_raw_response.retrieve_traffic_history(
                id="",
                lat=0,
                lng=0,
            )
