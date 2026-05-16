# V1

Types:

```python
from propraven.types import V1RetrieveCoverageResponse
```

Methods:

- <code title="get /api/v1/coverage">client.v1.<a href="./src/propraven/resources/v1/v1.py">retrieve_coverage</a>(\*\*<a href="src/propraven/types/v1_retrieve_coverage_params.py">params</a>) -> <a href="./src/propraven/types/v1_retrieve_coverage_response.py">V1RetrieveCoverageResponse</a></code>

## Parcels

Types:

```python
from propraven.types.v1 import (
    Deed,
    Parcel,
    Permit,
    RiskAssessment,
    ParcelRetrieveDeedsResponse,
    ParcelRetrieveGeojsonResponse,
    ParcelRetrieveOwnerResponse,
    ParcelRetrievePermitsResponse,
    ParcelRetrieveReportResponse,
    ParcelRetrieveTrafficHistoryResponse,
)
```

Methods:

- <code title="get /api/v1/parcels/{id}">client.v1.parcels.<a href="./src/propraven/resources/v1/parcels.py">retrieve</a>(id) -> <a href="./src/propraven/types/v1/parcel.py">Parcel</a></code>
- <code title="get /api/v1/parcels/{id}/deeds">client.v1.parcels.<a href="./src/propraven/resources/v1/parcels.py">retrieve_deeds</a>(id) -> <a href="./src/propraven/types/v1/parcel_retrieve_deeds_response.py">ParcelRetrieveDeedsResponse</a></code>
- <code title="get /api/v1/parcels/geojson">client.v1.parcels.<a href="./src/propraven/resources/v1/parcels.py">retrieve_geojson</a>(\*\*<a href="src/propraven/types/v1/parcel_retrieve_geojson_params.py">params</a>) -> <a href="./src/propraven/types/v1/parcel_retrieve_geojson_response.py">ParcelRetrieveGeojsonResponse</a></code>
- <code title="get /api/v1/parcels/{id}/owner">client.v1.parcels.<a href="./src/propraven/resources/v1/parcels.py">retrieve_owner</a>(id) -> <a href="./src/propraven/types/v1/parcel_retrieve_owner_response.py">ParcelRetrieveOwnerResponse</a></code>
- <code title="get /api/v1/parcels/{id}/permits">client.v1.parcels.<a href="./src/propraven/resources/v1/parcels.py">retrieve_permits</a>(id) -> <a href="./src/propraven/types/v1/parcel_retrieve_permits_response.py">ParcelRetrievePermitsResponse</a></code>
- <code title="get /api/v1/parcels/{id}/report">client.v1.parcels.<a href="./src/propraven/resources/v1/parcels.py">retrieve_report</a>(id, \*\*<a href="src/propraven/types/v1/parcel_retrieve_report_params.py">params</a>) -> <a href="./src/propraven/types/v1/parcel_retrieve_report_response.py">ParcelRetrieveReportResponse</a></code>
- <code title="get /api/v1/parcels/{id}/risks">client.v1.parcels.<a href="./src/propraven/resources/v1/parcels.py">retrieve_risks</a>(id) -> <a href="./src/propraven/types/v1/risk_assessment.py">RiskAssessment</a></code>
- <code title="get /api/v1/parcels/{id}/traffic-history">client.v1.parcels.<a href="./src/propraven/resources/v1/parcels.py">retrieve_traffic_history</a>(id, \*\*<a href="src/propraven/types/v1/parcel_retrieve_traffic_history_params.py">params</a>) -> <a href="./src/propraven/types/v1/parcel_retrieve_traffic_history_response.py">ParcelRetrieveTrafficHistoryResponse</a></code>

## Search

Types:

```python
from propraven.types.v1 import (
    SearchAutocompleteResponse,
    SearchExportResultsResponse,
    SearchFullSearchResponse,
    SearchParcelSearchResponse,
)
```

Methods:

- <code title="get /api/v1/search/autocomplete">client.v1.search.<a href="./src/propraven/resources/v1/search.py">autocomplete</a>(\*\*<a href="src/propraven/types/v1/search_autocomplete_params.py">params</a>) -> <a href="./src/propraven/types/v1/search_autocomplete_response.py">SearchAutocompleteResponse</a></code>
- <code title="get /api/v1/search/export">client.v1.search.<a href="./src/propraven/resources/v1/search.py">export_results</a>(\*\*<a href="src/propraven/types/v1/search_export_results_params.py">params</a>) -> str</code>
- <code title="get /api/v1/search/full">client.v1.search.<a href="./src/propraven/resources/v1/search.py">full_search</a>(\*\*<a href="src/propraven/types/v1/search_full_search_params.py">params</a>) -> <a href="./src/propraven/types/v1/search_full_search_response.py">SearchFullSearchResponse</a></code>
- <code title="post /api/v1/search">client.v1.search.<a href="./src/propraven/resources/v1/search.py">parcel_search</a>(\*\*<a href="src/propraven/types/v1/search_parcel_search_params.py">params</a>) -> <a href="./src/propraven/types/v1/search_parcel_search_response.py">SearchParcelSearchResponse</a></code>

## Deals

Types:

```python
from propraven.types.v1 import (
    AffordabilityRow,
    DealFindAbsenteeOwnersResponse,
    DealFindEntityOwnedParcelsResponse,
    DealFindFlipsResponse,
    DealFindHighLandRatioResponse,
    DealFindLongHoldParcelsResponse,
    DealFindPortfolioOwnersResponse,
    DealRetrieveMarketSummaryResponse,
    DealSearchContractorsResponse,
    DealSearchLendersResponse,
)
```

Methods:

- <code title="get /api/v1/deals/absentee">client.v1.deals.<a href="./src/propraven/resources/v1/deals.py">find_absentee_owners</a>(\*\*<a href="src/propraven/types/v1/deal_find_absentee_owners_params.py">params</a>) -> <a href="./src/propraven/types/v1/deal_find_absentee_owners_response.py">DealFindAbsenteeOwnersResponse</a></code>
- <code title="get /api/v1/deals/entities">client.v1.deals.<a href="./src/propraven/resources/v1/deals.py">find_entity_owned_parcels</a>(\*\*<a href="src/propraven/types/v1/deal_find_entity_owned_parcels_params.py">params</a>) -> <a href="./src/propraven/types/v1/deal_find_entity_owned_parcels_response.py">DealFindEntityOwnedParcelsResponse</a></code>
- <code title="get /api/v1/deals/flips">client.v1.deals.<a href="./src/propraven/resources/v1/deals.py">find_flips</a>(\*\*<a href="src/propraven/types/v1/deal_find_flips_params.py">params</a>) -> <a href="./src/propraven/types/v1/deal_find_flips_response.py">DealFindFlipsResponse</a></code>
- <code title="get /api/v1/deals/high-land-ratio">client.v1.deals.<a href="./src/propraven/resources/v1/deals.py">find_high_land_ratio</a>(\*\*<a href="src/propraven/types/v1/deal_find_high_land_ratio_params.py">params</a>) -> <a href="./src/propraven/types/v1/deal_find_high_land_ratio_response.py">DealFindHighLandRatioResponse</a></code>
- <code title="get /api/v1/deals/long-hold">client.v1.deals.<a href="./src/propraven/resources/v1/deals.py">find_long_hold_parcels</a>(\*\*<a href="src/propraven/types/v1/deal_find_long_hold_parcels_params.py">params</a>) -> <a href="./src/propraven/types/v1/deal_find_long_hold_parcels_response.py">DealFindLongHoldParcelsResponse</a></code>
- <code title="get /api/v1/deals/portfolio-owners">client.v1.deals.<a href="./src/propraven/resources/v1/deals.py">find_portfolio_owners</a>(\*\*<a href="src/propraven/types/v1/deal_find_portfolio_owners_params.py">params</a>) -> <a href="./src/propraven/types/v1/deal_find_portfolio_owners_response.py">DealFindPortfolioOwnersResponse</a></code>
- <code title="get /api/v1/deals/market">client.v1.deals.<a href="./src/propraven/resources/v1/deals.py">retrieve_market_summary</a>(\*\*<a href="src/propraven/types/v1/deal_retrieve_market_summary_params.py">params</a>) -> <a href="./src/propraven/types/v1/deal_retrieve_market_summary_response.py">DealRetrieveMarketSummaryResponse</a></code>
- <code title="get /api/v1/deals/contractors">client.v1.deals.<a href="./src/propraven/resources/v1/deals.py">search_contractors</a>(\*\*<a href="src/propraven/types/v1/deal_search_contractors_params.py">params</a>) -> <a href="./src/propraven/types/v1/deal_search_contractors_response.py">DealSearchContractorsResponse</a></code>
- <code title="get /api/v1/deals/lenders">client.v1.deals.<a href="./src/propraven/resources/v1/deals.py">search_lenders</a>(\*\*<a href="src/propraven/types/v1/deal_search_lenders_params.py">params</a>) -> <a href="./src/propraven/types/v1/deal_search_lenders_response.py">DealSearchLendersResponse</a></code>

## Market

Types:

```python
from propraven.types.v1 import MarketRetrieveFlipActivityResponse, MarketRetrieveTrendsResponse
```

Methods:

- <code title="get /api/v1/market/flips">client.v1.market.<a href="./src/propraven/resources/v1/market/market.py">retrieve_flip_activity</a>(\*\*<a href="src/propraven/types/v1/market_retrieve_flip_activity_params.py">params</a>) -> <a href="./src/propraven/types/v1/market_retrieve_flip_activity_response.py">MarketRetrieveFlipActivityResponse</a></code>
- <code title="get /api/v1/market/trends">client.v1.market.<a href="./src/propraven/resources/v1/market/market.py">retrieve_trends</a>(\*\*<a href="src/propraven/types/v1/market_retrieve_trends_params.py">params</a>) -> <a href="./src/propraven/types/v1/market_retrieve_trends_response.py">MarketRetrieveTrendsResponse</a></code>

### Counties

Types:

```python
from propraven.types.v1.market import CountyRetrieveDetailResponse, CountyRetrieveStatisticsResponse
```

Methods:

- <code title="get /api/v1/market/counties/{fips}">client.v1.market.counties.<a href="./src/propraven/resources/v1/market/counties.py">retrieve_detail</a>(fips) -> <a href="./src/propraven/types/v1/market/county_retrieve_detail_response.py">CountyRetrieveDetailResponse</a></code>
- <code title="get /api/v1/market/counties">client.v1.market.counties.<a href="./src/propraven/resources/v1/market/counties.py">retrieve_statistics</a>(\*\*<a href="src/propraven/types/v1/market/county_retrieve_statistics_params.py">params</a>) -> <a href="./src/propraven/types/v1/market/county_retrieve_statistics_response.py">CountyRetrieveStatisticsResponse</a></code>

## Owners

Types:

```python
from propraven.types.v1 import (
    Owner,
    OwnerRetrievePortfolioSummaryResponse,
    OwnerRetrievePropertiesResponse,
    OwnerRetrieveTransactionsResponse,
    OwnerSearchOwnersResponse,
)
```

Methods:

- <code title="get /api/v1/owners/{name}/portfolio">client.v1.owners.<a href="./src/propraven/resources/v1/owners.py">retrieve_portfolio_summary</a>(name) -> <a href="./src/propraven/types/v1/owner_retrieve_portfolio_summary_response.py">OwnerRetrievePortfolioSummaryResponse</a></code>
- <code title="get /api/v1/owners/{name}">client.v1.owners.<a href="./src/propraven/resources/v1/owners.py">retrieve_profile</a>(name) -> <a href="./src/propraven/types/v1/owner.py">Owner</a></code>
- <code title="get /api/v1/owners/{name}/properties">client.v1.owners.<a href="./src/propraven/resources/v1/owners.py">retrieve_properties</a>(name, \*\*<a href="src/propraven/types/v1/owner_retrieve_properties_params.py">params</a>) -> <a href="./src/propraven/types/v1/owner_retrieve_properties_response.py">OwnerRetrievePropertiesResponse</a></code>
- <code title="get /api/v1/owners/{name}/transactions">client.v1.owners.<a href="./src/propraven/resources/v1/owners.py">retrieve_transactions</a>(name) -> <a href="./src/propraven/types/v1/owner_retrieve_transactions_response.py">OwnerRetrieveTransactionsResponse</a></code>
- <code title="get /api/v1/owners/search">client.v1.owners.<a href="./src/propraven/resources/v1/owners.py">search_owners</a>(\*\*<a href="src/propraven/types/v1/owner_search_owners_params.py">params</a>) -> <a href="./src/propraven/types/v1/owner_search_owners_response.py">OwnerSearchOwnersResponse</a></code>

## Webhooks

Types:

```python
from propraven.types.v1 import (
    Webhook,
    WebhookFilter,
    WebhookCreateEndpointResponse,
    WebhookDisableEndpointResponse,
    WebhookListEndpointsResponse,
    WebhookRetrieveDeliveriesResponse,
)
```

Methods:

- <code title="post /api/v1/webhooks">client.v1.webhooks.<a href="./src/propraven/resources/v1/webhooks.py">create_endpoint</a>(\*\*<a href="src/propraven/types/v1/webhook_create_endpoint_params.py">params</a>) -> <a href="./src/propraven/types/v1/webhook_create_endpoint_response.py">WebhookCreateEndpointResponse</a></code>
- <code title="delete /api/v1/webhooks/{id}">client.v1.webhooks.<a href="./src/propraven/resources/v1/webhooks.py">disable_endpoint</a>(id) -> <a href="./src/propraven/types/v1/webhook_disable_endpoint_response.py">WebhookDisableEndpointResponse</a></code>
- <code title="get /api/v1/webhooks">client.v1.webhooks.<a href="./src/propraven/resources/v1/webhooks.py">list_endpoints</a>() -> <a href="./src/propraven/types/v1/webhook_list_endpoints_response.py">WebhookListEndpointsResponse</a></code>
- <code title="get /api/v1/webhooks/{id}/deliveries">client.v1.webhooks.<a href="./src/propraven/resources/v1/webhooks.py">retrieve_deliveries</a>(id) -> <a href="./src/propraven/types/v1/webhook_retrieve_deliveries_response.py">WebhookRetrieveDeliveriesResponse</a></code>
- <code title="get /api/v1/webhooks/{id}">client.v1.webhooks.<a href="./src/propraven/resources/v1/webhooks.py">retrieve_endpoint</a>(id) -> <a href="./src/propraven/types/v1/webhook.py">Webhook</a></code>

## Account

Types:

```python
from propraven.types.v1 import AccountRetrieveUsageResponse
```

Methods:

- <code title="get /api/v1/account/usage">client.v1.account.<a href="./src/propraven/resources/v1/account.py">retrieve_usage</a>() -> <a href="./src/propraven/types/v1/account_retrieve_usage_response.py">AccountRetrieveUsageResponse</a></code>
