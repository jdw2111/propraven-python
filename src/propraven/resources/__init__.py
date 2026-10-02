# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""Generated resource namespaces and the client mixins that expose them."""

from __future__ import annotations

from functools import cached_property

from .parcels import AsyncParcelsResource, ParcelsResource
from .search import AsyncSearchResource, SearchResource
from .coverage import AsyncCoverageResource, CoverageResource
from .deals import AsyncDealsResource, DealsResource
from .market import AsyncMarketResource, MarketResource
from .owners import AsyncOwnersResource, OwnersResource
from .webhooks import AsyncWebhooksResource, WebhooksResource
from .account import AsyncAccountResource, AccountResource
from .storefront import AsyncStorefrontResource, StorefrontResource
from .leads import AsyncLeadsResource, LeadsResource
from .credits import AsyncCreditsResource, CreditsResource
from .watch import AsyncWatchResource, WatchResource
from .verify import AsyncVerifyResource, VerifyResource
from .cohorts import AsyncCohortsResource, CohortsResource
from .lookup import AsyncLookupResource, LookupResource
from .cmbs import AsyncCmbsResource, CmbsResource
from .freshness import AsyncFreshnessResource, FreshnessResource
from .crime import AsyncCrimeResource, CrimeResource
from .traffic import AsyncTrafficResource, TrafficResource

__all__ = [
    "AccountResource",
    "AsyncAccountResource",
    "AsyncCmbsResource",
    "AsyncCohortsResource",
    "AsyncCoverageResource",
    "AsyncCreditsResource",
    "AsyncCrimeResource",
    "AsyncDealsResource",
    "AsyncFreshnessResource",
    "AsyncLeadsResource",
    "AsyncLookupResource",
    "AsyncMarketResource",
    "AsyncOwnersResource",
    "AsyncParcelsResource",
    "AsyncResourcesMixin",
    "AsyncSearchResource",
    "AsyncStorefrontResource",
    "AsyncTrafficResource",
    "AsyncVerifyResource",
    "AsyncWatchResource",
    "AsyncWebhooksResource",
    "CmbsResource",
    "CohortsResource",
    "CoverageResource",
    "CreditsResource",
    "CrimeResource",
    "DealsResource",
    "FreshnessResource",
    "LeadsResource",
    "LookupResource",
    "MarketResource",
    "OwnersResource",
    "ParcelsResource",
    "SearchResource",
    "StorefrontResource",
    "SyncResourcesMixin",
    "TrafficResource",
    "VerifyResource",
    "WatchResource",
    "WebhooksResource",
]


class SyncResourcesMixin:
    """Adds one attribute per API namespace to the client."""

    @cached_property
    def parcels(self) -> ParcelsResource:
        """``parcels`` namespace (16 operations)."""
        return ParcelsResource(self)

    @cached_property
    def search(self) -> SearchResource:
        """``search`` namespace (4 operations)."""
        return SearchResource(self)

    @cached_property
    def coverage(self) -> CoverageResource:
        """``coverage`` namespace (2 operations)."""
        return CoverageResource(self)

    @cached_property
    def deals(self) -> DealsResource:
        """``deals`` namespace (9 operations)."""
        return DealsResource(self)

    @cached_property
    def market(self) -> MarketResource:
        """``market`` namespace (5 operations)."""
        return MarketResource(self)

    @cached_property
    def owners(self) -> OwnersResource:
        """``owners`` namespace (7 operations)."""
        return OwnersResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """``webhooks`` namespace (6 operations)."""
        return WebhooksResource(self)

    @cached_property
    def account(self) -> AccountResource:
        """``account`` namespace (1 operation)."""
        return AccountResource(self)

    @cached_property
    def storefront(self) -> StorefrontResource:
        """``storefront`` namespace (2 operations)."""
        return StorefrontResource(self)

    @cached_property
    def leads(self) -> LeadsResource:
        """``leads`` namespace (1 operation)."""
        return LeadsResource(self)

    @cached_property
    def credits(self) -> CreditsResource:
        """``credits`` namespace (2 operations)."""
        return CreditsResource(self)

    @cached_property
    def watch(self) -> WatchResource:
        """``watch`` namespace (4 operations)."""
        return WatchResource(self)

    @cached_property
    def verify(self) -> VerifyResource:
        """``verify`` namespace (2 operations)."""
        return VerifyResource(self)

    @cached_property
    def cohorts(self) -> CohortsResource:
        """``cohorts`` namespace (2 operations)."""
        return CohortsResource(self)

    @cached_property
    def lookup(self) -> LookupResource:
        """``lookup`` namespace (2 operations)."""
        return LookupResource(self)

    @cached_property
    def cmbs(self) -> CmbsResource:
        """``cmbs`` namespace (1 operation)."""
        return CmbsResource(self)

    @cached_property
    def freshness(self) -> FreshnessResource:
        """``freshness`` namespace (2 operations)."""
        return FreshnessResource(self)

    @cached_property
    def crime(self) -> CrimeResource:
        """``crime`` namespace (1 operation)."""
        return CrimeResource(self)

    @cached_property
    def traffic(self) -> TrafficResource:
        """``traffic`` namespace (1 operation)."""
        return TrafficResource(self)


class AsyncResourcesMixin:
    """Adds one attribute per API namespace to the client."""

    @cached_property
    def parcels(self) -> AsyncParcelsResource:
        """``parcels`` namespace (16 operations)."""
        return AsyncParcelsResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        """``search`` namespace (4 operations)."""
        return AsyncSearchResource(self)

    @cached_property
    def coverage(self) -> AsyncCoverageResource:
        """``coverage`` namespace (2 operations)."""
        return AsyncCoverageResource(self)

    @cached_property
    def deals(self) -> AsyncDealsResource:
        """``deals`` namespace (9 operations)."""
        return AsyncDealsResource(self)

    @cached_property
    def market(self) -> AsyncMarketResource:
        """``market`` namespace (5 operations)."""
        return AsyncMarketResource(self)

    @cached_property
    def owners(self) -> AsyncOwnersResource:
        """``owners`` namespace (7 operations)."""
        return AsyncOwnersResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """``webhooks`` namespace (6 operations)."""
        return AsyncWebhooksResource(self)

    @cached_property
    def account(self) -> AsyncAccountResource:
        """``account`` namespace (1 operation)."""
        return AsyncAccountResource(self)

    @cached_property
    def storefront(self) -> AsyncStorefrontResource:
        """``storefront`` namespace (2 operations)."""
        return AsyncStorefrontResource(self)

    @cached_property
    def leads(self) -> AsyncLeadsResource:
        """``leads`` namespace (1 operation)."""
        return AsyncLeadsResource(self)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        """``credits`` namespace (2 operations)."""
        return AsyncCreditsResource(self)

    @cached_property
    def watch(self) -> AsyncWatchResource:
        """``watch`` namespace (4 operations)."""
        return AsyncWatchResource(self)

    @cached_property
    def verify(self) -> AsyncVerifyResource:
        """``verify`` namespace (2 operations)."""
        return AsyncVerifyResource(self)

    @cached_property
    def cohorts(self) -> AsyncCohortsResource:
        """``cohorts`` namespace (2 operations)."""
        return AsyncCohortsResource(self)

    @cached_property
    def lookup(self) -> AsyncLookupResource:
        """``lookup`` namespace (2 operations)."""
        return AsyncLookupResource(self)

    @cached_property
    def cmbs(self) -> AsyncCmbsResource:
        """``cmbs`` namespace (1 operation)."""
        return AsyncCmbsResource(self)

    @cached_property
    def freshness(self) -> AsyncFreshnessResource:
        """``freshness`` namespace (2 operations)."""
        return AsyncFreshnessResource(self)

    @cached_property
    def crime(self) -> AsyncCrimeResource:
        """``crime`` namespace (1 operation)."""
        return AsyncCrimeResource(self)

    @cached_property
    def traffic(self) -> AsyncTrafficResource:
        """``traffic`` namespace (1 operation)."""
        return AsyncTrafficResource(self)
