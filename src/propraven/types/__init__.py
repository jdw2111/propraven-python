# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.
"""Response and request types generated from openapi.json.

Every type is a ``TypedDict`` (a plain ``dict`` at runtime; no validation).
"""

from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, TypedDict, Union

__all__ = [
    "AccountUsage",
    "AccountUsageRateLimit",
    "AccountUsageResponse",
    "AffordabilityRow",
    "AutocompleteAddress",
    "AutocompleteLocation",
    "AutocompleteParcel",
    "AutocompleteResult",
    "AutocompleteResultOwnerNameSearch",
    "AutocompleteResultPeopleFields",
    "CmbsExposureResponse",
    "CmbsExposureResponseCoverage",
    "CmbsExposureResponseCoverageEdgarRoster",
    "CmbsExposureResponseCoverageExcluded",
    "CmbsExposureResponseDataAsOf",
    "CmbsExposureResponseFieldStatus",
    "CmbsExposureResponseFieldStatusProperties",
    "CmbsExposureResponseSubject",
    "CoOwner",
    "CohortsExportResponse",
    "CohortsListResponse",
    "CohortsListResponseCohortsItem",
    "ComparableSale",
    "ContactSource",
    "Contractor",
    "CountyDetail",
    "CountyDetailDataProvenance",
    "CountyDetailDataProvenanceAffordability",
    "CountyDetailDataProvenanceAffordabilityIncomeMeasure",
    "CountyDetailDataProvenanceMarket",
    "CountyDetailFlipSummary",
    "CountyDetailMarketStatsItem",
    "CountyDetailParcelSummary",
    "CoverageGetResponse",
    "CoverageGetResponseDataItem",
    "CoverageGetResponseNationalCounts",
    "CoverageGetResponseNationalCountsParcelCountDefinitions",
    "CoverageMapResponse",
    "CoverageMapResponseCountiesItem",
    "CoverageMapResponseMeta",
    "CoverageMapResponseMetaTotals",
    "CreditsBalanceResponse",
    "CreditsTopupResponse",
    "CrimeLookupResponse",
    "CrimeLookupResponseCrime",
    "DealsAbsenteeResponse",
    "DealsAbsenteeResponseDataItem",
    "DealsContractorsResponse",
    "DealsContractorsResponseSourceQuality",
    "DealsEntitiesResponse",
    "DealsEntitiesResponseVariant1",
    "DealsEntitiesResponseVariant2",
    "DealsFlipsResponse",
    "DealsFlipsResponseDataItem",
    "DealsHighLandRatioResponse",
    "DealsLendersResponse",
    "DealsLongHoldResponse",
    "DealsMarketResponse",
    "DealsMarketResponseVariant1",
    "DealsMarketResponseVariant1DataProvenance",
    "DealsMarketResponseVariant2",
    "DealsPortfolioOwnersResponse",
    "Deed",
    "DossierSubSection",
    "EntityAggregate",
    "EntityOwnedParcel",
    "EntitySummary",
    "Error",
    "FreshnessDatasetsResponse",
    "FreshnessDatasetsResponseDatasetsItem",
    "FreshnessDatasetsResponseDatasetsItemCoverage",
    "FreshnessDatasetsResponseDatasetsItemRecordActivity",
    "FreshnessDatasetsResponseDatasetsItemRefresh",
    "FreshnessGetResponse",
    "FullSearchResult",
    "FullSearchResultResultsItem",
    "FullSearchResultWarningsItem",
    "HighLandRatioParcel",
    "Lead",
    "LeadFeed",
    "LeadFeedGeo",
    "LeadFeedPreview",
    "LeadFeedPreviewGeo",
    "LeadOwnerContact",
    "LeadProvenance",
    "LeadProvenanceCatalogReference",
    "LeadProvenanceCatalogReferenceCatalogSeal",
    "LeadsFindResponse",
    "LeadsQuote",
    "LeadsQuoteBreakdown",
    "Lender",
    "LongHoldParcel",
    "LookupBatchResponse",
    "LookupBatchResponseItemsItem",
    "LookupBatchResponseItemsItemParcel",
    "LookupBatchResponseItemsItemParcelLastSale",
    "LookupGetResponse",
    "LookupGetResponseParcel",
    "MailingAddress",
    "MarketCountiesResponse",
    "MarketCountiesResponseDataItem",
    "MarketCountiesResponseSummary",
    "MarketCountyResponse",
    "MarketFlipsResponse",
    "MarketFlipsRow",
    "MarketSnapshotResponse",
    "MarketSnapshotResponseDemographics",
    "MarketSnapshotResponseDemographicsDemographicsBasisGrain",
    "MarketSnapshotResponseEconomy",
    "MarketSnapshotResponseEconomyEconomyBasisGrain",
    "MarketSnapshotResponseGeo",
    "MarketSnapshotResponseHazard",
    "MarketSnapshotResponseHazardHazardBasisGrain",
    "MarketSnapshotResponseHealthcare",
    "MarketSnapshotResponseHealthcareHealthcareBasisGrain",
    "MarketSnapshotResponseHousing",
    "MarketSnapshotResponseHousingHousingBasisGrain",
    "MarketSnapshotResponseLending",
    "MarketSnapshotResponseLendingLendingBasisGrain",
    "MarketSnapshotResponseMarketProvenance",
    "MarketSummary",
    "MarketTrendsResponse",
    "MarketTrendsResponseDataItem",
    "MarketTrendsResponseDataItemQuartersItem",
    "Money",
    "Owner",
    "OwnerCard",
    "OwnerCardContact",
    "OwnerCardContactEntity",
    "OwnerCardContactEntitySource",
    "OwnerCardContactOtherAddressesItem",
    "OwnerCardContactOtherAddressesItemAddress",
    "OwnerCardContactOtherAddressesItemCitedByItem",
    "OwnerCardContactOtherAddressesItemSource",
    "OwnerCardContactOtherAddressesScope",
    "OwnerCardContactOtherAddressesScopeEvidenceProvidersItem",
    "OwnerCardContactOwnerNameProvenance",
    "OwnerCardContactOwnerNameProvenanceSource",
    "OwnerCardOwner",
    "OwnerCardSubject",
    "OwnerTransaction",
    "OwnersCardResponse",
    "OwnersGetResponse",
    "OwnersPortfolioResponse",
    "OwnersPortfolioResponseMatch",
    "OwnersPortfolioResponseMatchBasisCounts",
    "OwnersPortfolioResponsePropertiesItem",
    "OwnersPortfolioResponseSummary",
    "OwnersPortfolioResponseSummaryByStateItem",
    "OwnersPropertiesResponse",
    "OwnersPropertiesResponseDataItem",
    "OwnersReportResponse",
    "OwnersReportResponseFilter",
    "OwnersReportResponseOwner",
    "OwnersReportResponseOwnerMatch",
    "OwnersReportResponseOwnerMatchBasisCounts",
    "OwnersReportResponseQuote",
    "OwnersReportResponseQuoteBreakdown",
    "OwnersReportResponseQuotePrice",
    "OwnersReportResponseSampleItem",
    "OwnersReportResponseSummary",
    "OwnersReportResponseSummaryByStateItem",
    "OwnersSearchResponse",
    "OwnersTransactionsResponse",
    "Parcel",
    "ParcelDerivedGate",
    "ParcelDossier",
    "ParcelDossierBoundary",
    "ParcelDossierFieldsItem",
    "ParcelDossierMeta",
    "ParcelDossierMetaEntitlement",
    "ParcelDossierParcel",
    "ParcelDossierSections",
    "ParcelGeoFeature",
    "ParcelGeoFeatureGeometry",
    "ParcelGeoFeatureProperties",
    "ParcelGeoJSON",
    "ParcelIdentityGate",
    "ParcelOwnerChangedEvent",
    "ParcelPermitFiledEvent",
    "ParcelRentGate",
    "ParcelSiteGate",
    "ParcelSoldEvent",
    "ParcelsBatchParamsTuplesItem",
    "ParcelsBatchResponse",
    "ParcelsBatchResponseRowsItem",
    "ParcelsCompPackResponse",
    "ParcelsCompPackResponseQuote",
    "ParcelsCompPackResponseQuoteBreakdown",
    "ParcelsCompPackResponseQuotePrice",
    "ParcelsCompPackResponseSampleItem",
    "ParcelsCompPackResponseSubject",
    "ParcelsCompsResponse",
    "ParcelsCompsResponseCompsItem",
    "ParcelsCompsResponseProvenanceGate",
    "ParcelsCompsResponseProvenanceGateScope",
    "ParcelsCompsResponseSubject",
    "ParcelsDeedsResponse",
    "ParcelsDeedsResponseVariant2",
    "ParcelsGeojsonResponse",
    "ParcelsGetResponse",
    "ParcelsOccupantsResponse",
    "ParcelsOccupantsResponseOccupantsItem",
    "ParcelsOwnerResponse",
    "ParcelsOwnerResponseContact",
    "ParcelsOwnerResponseContactEntity",
    "ParcelsOwnerResponseContactEntitySource",
    "ParcelsOwnerResponseContactMailing",
    "ParcelsOwnerResponseContactMailingSource",
    "ParcelsOwnerResponseContactOtherAddressesItem",
    "ParcelsOwnerResponseContactOtherAddressesItemAddress",
    "ParcelsOwnerResponseContactOtherAddressesItemCitedByItem",
    "ParcelsOwnerResponseContactOtherAddressesItemSource",
    "ParcelsOwnerResponseContactOtherAddressesScope",
    "ParcelsOwnerResponseContactOtherAddressesScopeEvidenceProvidersItem",
    "ParcelsOwnerResponseContactOwnerNameProvenance",
    "ParcelsOwnerResponseContactOwnerNameProvenanceSource",
    "ParcelsOwnerResponseOwner",
    "ParcelsOwnerResponsePortfolio",
    "ParcelsOwnerResponsePortfolioSummary",
    "ParcelsOwnerResponsePropertiesItem",
    "ParcelsPermitsResponse",
    "ParcelsPermitsResponseVariant2",
    "ParcelsPoisResponse",
    "ParcelsReportResponse",
    "ParcelsRiskScoreResponse",
    "ParcelsRiskScoreResponseQuote",
    "ParcelsRiskScoreResponseQuoteBreakdown",
    "ParcelsRiskScoreResponseQuotePrice",
    "ParcelsRiskScoreResponseSubject",
    "ParcelsRisksResponse",
    "ParcelsTrafficHistoryResponse",
    "ParcelsViolationsResponse",
    "ParcelsViolationsResponseCoveredJurisdictionsItem",
    "ParcelsViolationsResponsePlace",
    "ParcelsViolationsResponseSummary",
    "ParcelsViolationsResponseWithheld",
    "PeopleFieldsWithheld",
    "Permit",
    "PortfolioOwner",
    "Problem",
    "ProblemErrorsItem",
    "RiskAssessment",
    "RiskAssessmentAirQuality",
    "RiskAssessmentCrime",
    "RiskAssessmentIdentityGate",
    "RiskAssessmentSeismic",
    "RiskAssessmentWildfire",
    "RiskAssessmentWindstorm",
    "RiskAssessmentWithholdGate",
    "RiskAssessmentWithholdGateReasons",
    "SearchAutocompleteResponse",
    "SearchExportResponse",
    "SearchFullResponse",
    "SearchParcelsParamsBounds",
    "SearchParcelsParamsFilters",
    "SearchParcelsParamsFiltersAcreageRange",
    "SearchParcelsParamsFiltersValueRange",
    "SearchParcelsParamsFiltersYearBuiltRange",
    "SearchParcelsResponse",
    "SearchParcelsResponseDataItem",
    "SearchParcelsResponseWithholdGate",
    "SearchParcelsResponseWithholdGateReasons",
    "ServiceUnavailable",
    "StorefrontAvailabilityResponse",
    "StorefrontAvailabilityResponseCounties",
    "StorefrontAvailabilityResponseCountiesRowsItem",
    "StorefrontAvailabilityResponseCountiesRowsItemCoverage",
    "StorefrontAvailabilityResponseCoverage",
    "StorefrontAvailabilityResponseCoverageHeadlineFacts",
    "StorefrontAvailabilityResponseCoverageNational",
    "StorefrontAvailabilityResponseCoverageNationalParcelCountDefinitions",
    "StorefrontAvailabilityResponseDisclosures",
    "StorefrontAvailabilityResponseDisclosuresFieldAdvisoriesItem",
    "StorefrontAvailabilityResponseDisclosuresReferenceCatalog",
    "StorefrontAvailabilityResponseDisclosuresWithheldFieldsItem",
    "StorefrontAvailabilityResponseDossierQuote",
    "StorefrontAvailabilityResponseDossierQuoteBand",
    "StorefrontAvailabilityResponseDossierQuoteBreakdown",
    "StorefrontAvailabilityResponseDossierQuoteGeometryAddOn",
    "StorefrontAvailabilityResponseDossierQuoteGeometryAddOnPrice",
    "StorefrontAvailabilityResponseDossierQuoteSignals",
    "StorefrontAvailabilityResponseFields",
    "StorefrontAvailabilityResponseFieldsNational",
    "StorefrontAvailabilityResponseFieldsNationalAtOrAbove",
    "StorefrontAvailabilityResponseFieldsNationalTiers",
    "StorefrontAvailabilityResponseJurisdiction",
    "StorefrontAvailabilityResponseParcel",
    "StorefrontAvailabilityResponseQuote",
    "StorefrontAvailabilityResponseQuoteAddOnsItem",
    "StorefrontAvailabilityResponseQuoteAddOnsItemPrice",
    "StorefrontAvailabilityResponseQuotePrice",
    "StorefrontAvailabilityResponseSeal",
    "StorefrontAvailabilityResponseWartsItem",
    "StorefrontAvailabilityResponseWorstGapsItem",
    "StorefrontCatalogResponse",
    "StorefrontCatalogResponseAdvisoriesItem",
    "StorefrontCatalogResponseAdvisoriesItemWorstAffectedItem",
    "StorefrontCatalogResponseCounts",
    "StorefrontCatalogResponseCountsByGrain",
    "StorefrontCatalogResponseCountsCumulativeAt",
    "StorefrontCatalogResponseDisclosures",
    "StorefrontCatalogResponseDisclosuresFieldAdvisoriesItem",
    "StorefrontCatalogResponseDisclosuresReferenceCatalog",
    "StorefrontCatalogResponseDisclosuresWithheldFieldsItem",
    "StorefrontCatalogResponseFieldsItem",
    "StorefrontCatalogResponseFreshnessItem",
    "StorefrontCatalogResponseHeadline",
    "StorefrontCatalogResponseMeasuredFrom",
    "StorefrontCatalogResponseMeasuredFromBaseline",
    "StorefrontCatalogResponseMeasuredFromParcelCountDefinitions",
    "StorefrontCatalogResponsePricing",
    "StorefrontCatalogResponsePricingAddOnsItem",
    "StorefrontCatalogResponsePricingAddOnsItemPrice",
    "StorefrontCatalogResponsePricingDossier",
    "StorefrontCatalogResponseQuote",
    "StorefrontCatalogResponseQuoteAddOnsItem",
    "StorefrontCatalogResponseQuoteAddOnsItemPrice",
    "StorefrontCatalogResponseQuotePrice",
    "StorefrontCatalogResponseSeal",
    "StorefrontCatalogResponseSections",
    "StorefrontCatalogResponseSectionsComps",
    "StorefrontCatalogResponseSectionsDeeds",
    "StorefrontCatalogResponseSectionsGeometry",
    "StorefrontCatalogResponseSectionsParcel",
    "StorefrontCatalogResponseSectionsPermits",
    "StorefrontCatalogResponseState",
    "StorefrontCatalogResponseStateCoverage",
    "StorefrontCatalogResponseStateWorstGapsItem",
    "StorefrontCatalogResponseTiers",
    "StorefrontCatalogResponseWartsItem",
    "TrafficStationHistory",
    "TrafficStationHistoryHistoryItem",
    "TrafficStationHistoryPointsItem",
    "TrafficStationHistoryStation",
    "TrafficStationHistoryTimeSeriesItem",
    "TrafficStationHistoryWithholdGate",
    "TrafficStationHistoryWithholdGateReasons",
    "TrafficStationsResponse",
    "TrafficStationsResponseDataItem",
    "UccLien",
    "VerifyBatchParamsLookupsItem",
    "VerifyBatchResponse",
    "VerifyBatchResponseProvenance",
    "VerifyBatchResponseProvenanceCatalogReference",
    "VerifyBatchResponseProvenanceCatalogReferenceCatalogSeal",
    "VerifyBatchResponseQuote",
    "VerifyBatchResponseQuoteBreakdown",
    "VerifyBatchResponseQuotePerLookup",
    "VerifyBatchResponseQuoteTotal",
    "VerifyGetResponse",
    "VerifyGetResponseProvenance",
    "VerifyGetResponseProvenanceCatalogReference",
    "VerifyGetResponseProvenanceCatalogReferenceCatalogSeal",
    "VerifyGetResponseQuote",
    "VerifyGetResponseQuoteBreakdown",
    "VerifyGetResponseQuotePerLookup",
    "VerifyGetResponseQuoteTotal",
    "WatchCreateParamsFilter",
    "WatchCreateResponse",
    "WatchDeleteResponse",
    "WatchListResponse",
    "WatchPollResponse",
    "Webhook",
    "WebhookCreate",
    "WebhookCreated",
    "WebhookDelivery",
    "WebhookFilter",
    "WebhookFilterVariant1",
    "WebhookFilterVariant2",
    "WebhookFilterVariant3",
    "WebhookQuota",
    "WebhooksCreateResponse",
    "WebhooksDeleteResponse",
    "WebhooksDeliveriesResponse",
    "WebhooksGetResponse",
    "WebhooksListResponse",
    "WebhooksRetryDeliveryResponse",
    "X402PaymentRequired",
    "X402PaymentRequiredAcceptsItem",
    "X402PaymentRequiredAcceptsItemExtra",
]


class ParcelIdentityGate(TypedDict):
    applied: Optional[bool]
    suppressed: List[Optional[str]]
    reason: Optional[str]
    join_key_basis: str
    twins_in_other_counties: Optional[int]
    coords_basis: str
    unmeasured: List[Optional[str]]
    served_under_doubt: List[Optional[str]]
    note: Optional[str]


class ParcelSiteGate(TypedDict):
    applied: Optional[bool]
    suppressed: List[Optional[str]]
    reason: Optional[str]
    labelled: List[Optional[str]]
    mailing_basis: str
    note: Optional[str]


class ParcelDerivedGate(TypedDict):
    applied: Optional[bool]
    suppressed: List[Optional[str]]
    recomputed: List[Optional[str]]
    unevaluated: List[Any]
    reason: Optional[str]
    note: Optional[str]


class ParcelRentGate(TypedDict):
    applied: Optional[bool]
    suppressed: List[Optional[str]]
    reason: Optional[str]
    rental_confidence: Optional[str]
    note: Optional[str]


class _ParcelRequired(TypedDict):
    id: str
    county_fips: str
    """5-digit county FIPS code."""
    state_fips: str
    parcel_id: str
    """County-assigned parcel identifier."""
    address: Optional[str]
    normalized_address: Optional[str]
    city: Optional[str]
    state: Optional[float]
    zip: Optional[str]
    zip5: Optional[str]
    zip_plus4: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    land_use_code: Optional[str]
    land_use_desc: Optional[str]
    total_assessed_value: Optional[float]
    land_assessed_value: Optional[float]
    improvement_assessed_value: Optional[float]
    last_sale_price: Optional[float]
    last_sale_date: Optional[str]
    market_value: Optional[float]
    avm_value: Optional[float]
    avm_confidence: Optional[str]
    avm_method: Optional[str]
    tax_amount: Optional[float]
    tax_year: Optional[int]
    deal_score: Optional[float]
    """Composite deal opportunity score from 0 to 100."""
    price_per_sqft: Optional[float]
    comp_sale_price: Optional[float]
    comp_sale_date: Optional[str]
    comp_similarity_score: Optional[float]
    estimated_monthly_rent: Optional[float]
    estimated_annual_rent: Optional[float]
    rent_yield_pct: Optional[float]
    rental_confidence: Optional[str]
    gross_rent_multiplier: Optional[float]
    land_improvement_ratio: Optional[float]
    improvement_to_land_ratio: Optional[float]
    is_redevelopment_candidate: Optional[bool]
    building_sqft: Optional[float]
    year_built: Optional[int]
    lot_size_acres: Optional[float]
    lot_size_sqft: Optional[float]
    bedrooms: Optional[int]
    bathrooms: Optional[float]
    stories: Optional[float]
    units: Optional[int]
    unit_count: Optional[int]
    construction_type: Optional[str]
    owner_name: Optional[str]
    owner_address: Optional[str]
    owner_city: Optional[str]
    owner_state: Optional[str]
    owner_zip: Optional[str]
    ownership_type: Optional[str]
    owner_entity_type: Optional[str]
    entity_type: Optional[str]
    is_entity_owned: Optional[bool]
    is_absentee: Optional[bool]
    is_pe_aggregator: Optional[bool]
    owner_occupied_flag: Optional[bool]
    data_quality_score: Optional[float]
    flood_zone: Optional[str]
    is_sfha: Optional[bool]
    is_opportunity_zone: Optional[bool]
    is_justice40: Optional[bool]
    is_flip: Optional[bool]
    deed_count: Optional[int]
    permit_count: Optional[int]
    permit_count_12mo: Optional[int]
    zoning: Optional[str]
    county_name: Optional[str]
    property_type: Optional[str]
    _guards: List[str]
    is_flip_basis: str
    land_improvement_ratio_stored: Optional[float]
    land_improvement_ratio_basis: str
    improvement_to_land_ratio_basis: str
    is_absentee_basis: str
    owner_state_norm: Optional[str]
    is_out_of_state: Optional[bool]
    identity_gate: ParcelIdentityGate
    site_gate: ParcelSiteGate
    derived_gate: ParcelDerivedGate
    rent_gate: ParcelRentGate
    county_name_basis: str
    avm_method_family: Optional[str]
    avm_method_basis: str


class Parcel(_ParcelRequired, total=False):
    is_flip_dominant_share_pct: Optional[float]
    price_per_sqft_basis: str


class _OwnerRequired(TypedDict):
    owner_name_normalized: Optional[str]
    property_count: Optional[int]
    state_count: Optional[int]
    county_count: Optional[int]
    total_assessed_value: Optional[float]
    avg_assessed_value: Optional[float]
    total_acreage: Optional[float]
    states_list: Optional[Union[float, str]]
    portfolio_rank: Optional[int]


class Owner(_OwnerRequired, total=False):
    entity_type: Optional[str]
    """Observed values include: CORP."""
    is_pe_aggregator: Optional[bool]
    is_entity_owned: Optional[bool]
    pe_parent_group: Optional[str]
    pe_sponsor: Optional[str]
    pe_confidence: Optional[float]
    owner_entity_type: Optional[str]
    is_absentee: Optional[bool]
    contact_card: Optional[str]
    owner_name: str
    states: List[str]


class _PermitRequired(TypedDict):
    permit_number: Optional[str]
    permit_type: Optional[str]
    permit_status: Optional[str]
    description: Optional[str]
    work_class: Optional[str]
    issued_date: Optional[str]
    completed_date: Optional[str]
    estimated_cost: Optional[float]
    fee_amount: Optional[float]
    contractor_name: Optional[str]
    contractor_license: Optional[str]
    site_address: Optional[str]
    city: Optional[str]


class Permit(_PermitRequired, total=False):
    type: str
    status: Literal["issued", "pending", "approved", "expired", "completed", "denied"]
    contractor: Optional[str]


class _DeedRequired(TypedDict):
    document_number: Optional[str]
    recording_date: Optional[str]
    sale_date: Optional[str]
    document_type: Optional[str]
    sale_price: Optional[float]
    consideration: Optional[float]
    grantor_name: Optional[str]
    grantee_name: Optional[str]
    grantor_name_2: Optional[str]
    grantee_name_2: Optional[str]
    grantor_address: Optional[str]
    grantee_address: Optional[str]
    grantor_type: Optional[str]
    grantee_type: Optional[str]
    book: Optional[str]
    page: Optional[str]
    instrument_number: Optional[str]
    transfer_tax: Optional[float]
    excise_tax: Optional[float]
    sale_type: Optional[str]
    is_arm_length: Optional[bool]
    legal_description: Optional[str]
    lot: Optional[str]
    block: Optional[str]
    subdivision: Optional[str]
    source_url: Optional[str]
    property_address: Optional[str]
    property_city: Optional[str]
    property_state: Optional[str]


class Deed(_DeedRequired, total=False):
    deed_type: Optional[str]


class RiskAssessmentSeismic(TypedDict):
    ss: Optional[float]
    s1: Optional[float]
    sds: Optional[float]
    sd1: Optional[float]
    sdc: Optional[str]
    pga_g: Optional[float]
    nri_earthquake_rating: Optional[str]


class RiskAssessmentWindstorm(TypedDict):
    hurricane_rating: Optional[str]
    tornado_rating: Optional[str]
    power_wind_mw: Optional[float]
    storm_score: Optional[float]
    storm_top_event: Optional[str]
    storm_event_count_30y: Optional[int]
    storm_tornado_count_30y: Optional[int]
    storm_hurricane_count_30y: Optional[int]
    storm_hail_count_30y: Optional[int]
    storm_property_dmg_usd_30y: Optional[float]
    storm_deaths_30y: Optional[float]


class _RiskAssessmentWildfireRequired(TypedDict):
    county_name: Optional[str]
    risk_national_rank: Optional[float]
    bp_national_rank: Optional[float]
    risk_state_rank: Optional[float]
    bp_state_rank: Optional[float]


class RiskAssessmentWildfire(_RiskAssessmentWildfireRequired, total=False):
    risk_class: Optional[Literal["low", "moderate", "high", "very_high", "extreme"]]
    burn_probability: Optional[float]
    """Annual burn probability as a decimal."""


class _RiskAssessmentAirQualityRequired(TypedDict):
    year: Optional[int]
    median_aqi: Optional[float]
    """Median Air Quality Index value."""
    max_aqi: Optional[float]
    good_days: Optional[int]
    moderate_days: Optional[int]
    unhealthy_days: Optional[int]


class RiskAssessmentAirQuality(_RiskAssessmentAirQualityRequired, total=False):
    category: Optional[Literal["good", "moderate", "unhealthy_sensitive", "unhealthy", "very_unhealthy", "hazardous"]]


class RiskAssessmentCrime(TypedDict):
    score: Optional[float]
    """Crime score from 0 (low) to 100 (high)."""
    tier: Optional[float]
    """Observed values include: 3."""
    tier_label: Optional[str]
    trend: Optional[str]
    """Observed values include: improving."""
    violent_crime_rate: Optional[float]
    property_crime_rate: Optional[float]


class RiskAssessmentWithholdGateReasons(TypedDict):
    power_wind_mw: Optional[str]
    storm_hurricane_count_30y: Optional[str]


class RiskAssessmentWithholdGate(TypedDict):
    applied: Optional[bool]
    suppressed: List[Optional[str]]
    reason: Optional[str]
    reasons: RiskAssessmentWithholdGateReasons
    withheld_on: Optional[str]
    note: Optional[str]


class RiskAssessmentIdentityGate(TypedDict):
    applied: Optional[bool]
    suppressed: List[Any]
    reason: Optional[str]
    join_key_basis: str
    twins_in_other_counties: Optional[int]
    coords_basis: Optional[str]
    unmeasured: List[Any]
    served_under_doubt: List[Any]
    note: Optional[str]


class RiskAssessment(TypedDict):
    flood_zone: Optional[str]
    is_sfha: Optional[bool]
    is_sfha_basis: str
    seismic: RiskAssessmentSeismic
    windstorm: RiskAssessmentWindstorm
    wildfire: RiskAssessmentWildfire
    air_quality: RiskAssessmentAirQuality
    crime: RiskAssessmentCrime
    withhold_gate: RiskAssessmentWithholdGate
    identity_gate: RiskAssessmentIdentityGate


class Contractor(TypedDict):
    contractor_name_normalized: Optional[str]
    contractor_license: Optional[str]
    permit_count: Optional[int]
    jurisdiction_count: Optional[int]
    state_count: Optional[int]
    county_count: Optional[int]
    total_permit_value: Optional[int]
    avg_permit_value: Optional[float]
    first_permit_date: Optional[str]
    last_permit_date: Optional[str]
    active_years: Optional[int]
    top_permit_types: Optional[str]
    states_list: Optional[str]
    """Comma-delimited 2-letter state codes."""
    contractor_rank: Optional[int]
    """National rank, 1 = highest activity."""


class EntityOwnedParcel(TypedDict):
    county_fips: str
    state_fips: str
    parcel_id: str
    owner_name: Optional[str]
    entity_type: Optional[Literal["LLC", "CORP", "TRUST", "LP", "LTD", "ASSOCIATION", "OTHER_ENTITY"]]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    total_assessed_value: Optional[int]
    lot_size_acres: Optional[float]
    year_built: Optional[int]
    zoning: Optional[str]
    land_use_desc: Optional[str]
    owner_address: Optional[str]
    owner_city: Optional[str]
    owner_state: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]


class EntityAggregate(TypedDict, total=False):
    owner_name: str
    entity_type: str
    parcel_count: int
    total_value: Optional[float]
    states_arr: List[str]


class EntitySummary(TypedDict, total=False):
    total_entities: int
    total_parcels: int
    llc_count: int
    corp_count: int
    trust_count: int
    lp_count: int


class HighLandRatioParcel(TypedDict):
    county_fips: str
    state_fips: str
    parcel_id: str
    owner_name: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    land_assessed_value: Optional[float]
    improvement_assessed_value: Optional[float]
    total_assessed_value: Optional[int]
    land_improvement_ratio: Optional[float]
    """land / improvement, higher = more redevelopment potential."""
    lot_size_acres: Optional[float]
    year_built: Optional[int]
    zoning: Optional[str]
    land_use_desc: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]


class Lender(TypedDict, total=False):
    lender_name_normalized: str
    mortgage_count: int
    total_mortgage_volume: Optional[float]
    avg_mortgage_amount: Optional[float]
    median_mortgage_amount: Optional[float]
    county_count: int
    state_count: int
    states_list: Optional[str]
    first_mortgage_date: Optional[str]
    last_mortgage_date: Optional[str]
    lender_rank: int
    """National rank, 1 = highest volume."""


class LongHoldParcel(TypedDict):
    county_fips: str
    state_fips: str
    parcel_id: str
    owner_name: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    total_assessed_value: Optional[int]
    last_sale_date: Optional[str]
    last_sale_price: Optional[float]
    years_held: Optional[float]
    year_built: Optional[int]
    building_age: Optional[int]
    lot_size_acres: Optional[float]
    hold_tier: Optional[Literal["10-15yr", "15-20yr", "20-30yr", "30yr+"]]
    land_use_desc: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]


class _MarketSummaryRequired(TypedDict):
    county_fips: str
    year: Optional[int]
    quarter: Optional[int]
    transaction_count: Optional[int]
    median_price: Optional[float]
    avg_price: Optional[float]
    total_volume: Optional[int]
    cash_sale_count: Optional[int]
    cash_sale_pct: Optional[float]
    median_consideration: Optional[float]
    unique_buyers: Optional[float]
    unique_sellers: Optional[float]
    refreshed_at: Optional[str]
    state_fips: str
    county_name: Optional[str]
    state: Optional[str]


class MarketSummary(_MarketSummaryRequired, total=False):
    sale_count: int
    median_sale_price: Optional[float]
    avg_sale_price: Optional[float]


class _AffordabilityRowRequired(TypedDict):
    county_fips: str
    median_household_income: Optional[float]
    median_sale_price: Optional[float]
    price_to_income_ratio: Optional[float]
    affordability_rating: Optional[Literal["AFFORDABLE", "MODERATE", "EXPENSIVE", "VERY_EXPENSIVE"]]
    year: Optional[int]
    refreshed_at: Optional[str]


class AffordabilityRow(_AffordabilityRowRequired, total=False):
    state_fips: str
    county_name: Optional[str]
    monthly_payment_estimate: Optional[float]
    pct_income_for_housing: Optional[float]


class PortfolioOwner(TypedDict):
    owner_name_normalized: Optional[str]
    owner_state: Optional[str]
    property_count: Optional[int]
    state_count: Optional[int]
    county_count: Optional[int]
    total_assessed_value: Optional[int]
    avg_assessed_value: Optional[float]
    total_acreage: Optional[float]
    states_list: Optional[str]
    portfolio_rank: Optional[int]
    """National rank, 1 = largest portfolio."""


class Webhook(TypedDict, total=False):
    id: str
    url: str
    """Customer endpoint. Must be https://."""
    secret_prefix: str
    """First 14 chars of the secret (whsec_ + 8 hex). Use to identify the webhook in your dashboard;
    full secret is shown only at create time.
    """
    event_types: List[Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]]
    filter_kind: Literal["parcel_ids", "state_fips", "county_fips"]
    filter_value: WebhookFilter
    description: Optional[str]
    is_active: bool
    created_at: str
    disabled_at: Optional[str]
    disabled_reason: Optional[str]
    deliveries_attempted: int
    deliveries_succeeded: int
    last_delivery_at: Optional[str]
    last_success_at: Optional[str]


class WebhookFilterVariant1(TypedDict):
    parcel_ids: List[str]
    """Parcels to subscribe to, 1–1000: canonical ids `state_fips:county_fips:parcel_id` (preferred;
    the `canonical_id` other endpoints return), legacy `SSCCC:parcel_id`, parcel UUIDs, or a bare
    parcel_id that names exactly ONE served parcel. parcel_id is county-scoped, so a bare id that
    names several parcels is refused with 422 `parcel_identity_unresolved` listing the candidate
    canonical ids. Stored and matched on the full identity; deliveries carry `canonical_id`.
    """


class WebhookFilterVariant2(TypedDict):
    state_fips: str
    """2-digit state FIPS — subscribe to all parcels in this state."""


class WebhookFilterVariant3(TypedDict):
    state_fips: str
    county_fips: str
    """3-digit county FIPS (within the state) — subscribe to all parcels in this county."""


class _WebhookCreateRequired(TypedDict):
    url: str
    """Customer endpoint. https:// only."""
    event_types: List[Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]]
    """Event types to subscribe to. NOTE: only parcel.sold is live in v1.0; others 501."""
    filter_kind: Literal["parcel_ids", "state_fips", "county_fips"]
    filter_value: WebhookFilter


class WebhookCreate(_WebhookCreateRequired, total=False):
    description: Optional[str]
    """Optional human-readable label for your dashboard."""


class _WebhookCreatedRequired(TypedDict):
    secret: str
    """**Shown once.** Copy and store server-side immediately. Used to sign every outgoing delivery."""
    hint: str
    """Signature-verification reminder."""


class WebhookCreated(_WebhookCreatedRequired, total=False):
    id: str
    url: str
    """Customer endpoint. Must be https://."""
    secret_prefix: str
    """First 14 chars of the secret (whsec_ + 8 hex). Use to identify the webhook in your dashboard;
    full secret is shown only at create time.
    """
    event_types: List[Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]]
    filter_kind: Literal["parcel_ids", "state_fips", "county_fips"]
    filter_value: WebhookFilter
    description: Optional[str]
    is_active: bool
    created_at: str
    disabled_at: Optional[str]
    disabled_reason: Optional[str]
    deliveries_attempted: int
    deliveries_succeeded: int
    last_delivery_at: Optional[str]
    last_success_at: Optional[str]


class WebhookQuota(TypedDict):
    maxEndpoints: float
    """Max simultaneous active webhook endpoints on this tier."""
    maxEventsPerDay: float
    """Max event deliveries per UTC day on this tier."""


class WebhookDelivery(TypedDict, total=False):
    id: str
    event_id: str
    """Deterministic event identifier — sha256(source || pk || event_type). Idempotent re-deliveries
    share this.
    """
    event_type: Literal["parcel.sold", "parcel.permit_filed", "parcel.owner_changed"]
    event_occurred_at: str
    status: Literal["pending", "in_flight", "succeeded", "failed", "dead_lettered"]
    attempts: int
    last_attempt_at: Optional[str]
    next_attempt_at: Optional[str]
    last_response_status: Optional[int]
    last_response_body: Optional[str]
    """Truncated to ~1KB."""
    last_error: Optional[str]
    dead_lettered_at: Optional[str]
    created_at: str


class _ParcelSoldEventRequired(TypedDict):
    event_type: Literal["parcel.sold"]
    event_id: str
    """Deterministic. Use for idempotency."""
    occurred_at: str
    delivery_attempt: int
    """Starts at 1; increments on retry."""
    parcel_id: str
    """Composite county_fips:parcel_id."""
    state_fips: str
    county_fips: str


class ParcelSoldEvent(_ParcelSoldEventRequired, total=False):
    sale_date: Optional[str]
    sale_price_usd: Optional[float]
    """May be null in non-disclosure states (KS, MS, TX, UT, WY, etc.)."""
    grantor: Optional[str]
    grantee: Optional[str]
    recorded_date: Optional[str]
    source_run_id: Optional[str]
    """PropRaven ingest run that surfaced this event."""


class AutocompleteResultOwnerNameSearch(TypedDict):
    status: str
    code: str
    reason: str
    note: str


class AutocompleteResultPeopleFields(TypedDict):
    status: str
    code: str
    reason: str
    note: str


class _AutocompleteResultRequired(TypedDict):
    locations: List[AutocompleteLocation]
    parcels: List[AutocompleteParcel]
    addresses: List[AutocompleteAddress]
    degraded: bool


class AutocompleteResult(_AutocompleteResultRequired, total=False):
    owner_name_search: AutocompleteResultOwnerNameSearch
    people_fields: AutocompleteResultPeopleFields


class AutocompleteLocation(TypedDict, total=False):
    name: str
    type: Literal["city"]
    state: str
    city: str
    lat: Optional[float]
    lng: Optional[float]
    parcel_count: int


class _AutocompleteParcelRequired(TypedDict):
    parcel_id: str
    address: Optional[str]
    city: Optional[str]
    state_fips: str
    state: Optional[str]
    county_fips: str
    owner_name: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    total_assessed_value: Optional[int]


class AutocompleteParcel(_AutocompleteParcelRequired, total=False):
    type: Literal["parcel"]


class AutocompleteAddress(TypedDict):
    """Mapbox-geocoded address suggestion. Use to disambiguate user input before calling /api/v1/lookup
    or /api/v1/parcels/{id}.
    """
    name: Optional[str]
    type: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    south: Optional[float]
    north: Optional[float]
    west: Optional[float]
    east: Optional[float]


class FullSearchResultResultsItem(TypedDict):
    parcel_id: str
    apn: Optional[str]
    county_fips: str
    state_fips: str
    site_address: Optional[str]
    city: Optional[str]
    zip5: Optional[str]
    owner_name: Optional[str]
    total_value: Optional[int]
    latitude: Optional[float]
    longitude: Optional[float]


class FullSearchResultWarningsItem(TypedDict):
    code: Optional[str]
    param: Optional[str]
    message: Optional[str]


class _FullSearchResultRequired(TypedDict):
    results: List[FullSearchResultResultsItem]
    total: int
    totalCapped: bool
    page: int
    pages: int
    hasMore: bool
    nextCursor: Optional[str]


class FullSearchResult(_FullSearchResultRequired, total=False):
    warnings: List[FullSearchResultWarningsItem]
    total_is_capped: bool


class ParcelGeoJSON(TypedDict):
    """GeoJSON FeatureCollection of parcel polygons. Each feature's properties carry the basic parcel
    summary for popup rendering.
    """
    type: str
    features: List[ParcelGeoFeature]


class ParcelGeoFeatureGeometry(TypedDict):
    type: Optional[str]
    coordinates: List[List[List[Optional[float]]]]
    """GeoJSON polygon coordinate rings: outer ring first, then any inner rings."""


class _ParcelGeoFeaturePropertiesRequired(TypedDict):
    id: str
    county_fips: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    owner: Optional[str]
    value: Optional[float]
    type: Optional[str]
    year_built: Optional[int]


class ParcelGeoFeatureProperties(_ParcelGeoFeaturePropertiesRequired, total=False):
    parcel_id: str
    owner_name: Optional[str]
    total_assessed_value: Optional[float]
    property_type: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]


class ParcelGeoFeature(TypedDict):
    type: Optional[str]
    geometry: ParcelGeoFeatureGeometry
    properties: ParcelGeoFeatureProperties


class Money(TypedDict):
    """A money amount as a decimal string plus its currency code."""
    amount: str
    currency: str


class DossierSubSection(TypedDict, total=False):
    """One real sub-table (deeds, comps, or permits) in a dossier, with the exact serving relation it
    came from and that relation's own watermark (each is NOT pinned to the parcels epoch).
    """
    relation: str
    """The serving relation the rows came from."""
    as_of: Optional[str]
    """Watermark for this relation."""
    status: Literal["ok", "empty"]
    row_count: int
    note: str
    rows: List[Dict[str, Any]]


class ParcelDossierParcel(TypedDict, total=False):
    """Parcel identity."""
    canonical_id: str
    """state_fips:county_fips:parcel_id."""
    id: Optional[str]
    """PropRaven row UUID when the serving row carried one."""
    state_fips: str
    county_fips: str
    """3-digit within-state county code (the parcels_serving convention)."""
    county_fips_3: str
    """Same as county_fips, named for its width."""
    county_fips_5: str
    parcel_id: str
    state: Optional[str]
    address: Optional[str]


class ParcelDossierFieldsItem(TypedDict, total=False):
    name: str
    value: Any
    """The field value (any JSON type)."""
    source: str
    """Field-level source label from the sealed catalog."""
    as_of: Optional[str]
    confidence: Optional[float]
    """0..1 FIELD-LEVEL coverage (this parcel's state, else national); null when uncatalogued. Not a
    per-cell probability -- see confidence_basis.
    """
    confidence_basis: str
    national_coverage: Optional[float]
    state_coverage: Optional[float]
    tier: Optional[str]
    """prime|strong|good|partial|sparse|trace, re-derived from the applicable (state, else national)
    coverage.
    """
    grain: Optional[str]
    section: Optional[str]
    flags: List[str]
    catalogued: bool
    """False when the column is absent from the sealed catalog (source unknown)."""


class ParcelDossierSections(TypedDict, total=False):
    """Real sub-tables from the serving relations."""
    deeds: DossierSubSection
    comps: DossierSubSection
    permits: DossierSubSection


class ParcelDossierBoundary(TypedDict, total=False):
    """The GeoJSON boundary add-on. In the base dossier included=false and geometry is absent; a
    phase-2 add-on purchase populates geometry.
    """
    code: str
    price: Money
    included: bool
    purchasable: bool
    available: Optional[bool]
    relation: str
    note: str
    geometry: Any
    """GeoJSON geometry, present only for an entitled add-on purchase."""


class ParcelDossierMetaEntitlement(TypedDict, total=False):
    gated: bool
    method: str
    note: str


class ParcelDossierMeta(TypedDict, total=False):
    """Dossier-level provenance and pricing."""
    catalog_version: str
    catalog_seal: str
    contract_version: float
    snapshot_as_of: Optional[str]
    generated_at: str
    price: Money
    """The dossier product's contract price. The amount actually charged is the value-tiered per-parcel
    quote settled via x402 (or billed on a paid subscription) -- see the 402 accepts and
    /storefront/availability?parcel_id=.
    """
    currency: str
    field_count: float
    """Populated fields actually emitted."""
    catalog_sellable_fields: float
    catalog_total_columns: float
    sections_included: List[str]
    geometry_included: bool
    confidence_basis: str
    provenance_note: str
    license: str
    """The data license that governs this dossier's data (the Data license section of the Terms of
    Use).
    """
    entitlement: ParcelDossierMetaEntitlement


class ParcelDossier(TypedDict, total=False):
    """The paid, provenance-first parcel dossier returned by GET /parcels/{id}/report. Every populated
    field is delivered as `{name, value}`; the receipts (source, as_of, confidence, coverage) come
    as the opt-in `provenance` map (`include_provenance=true`), keyed by field name. The
    deeds/comps/permits sub-tables carry real rows; the GeoJSON boundary is a separately-priced
    add-on omitted from the base payload. Nulls/empties are dropped (see meta.field_count), not
    returned as null; columns a `sections`/`fields` projection leaves out are named in
    `meta.projection.omitted_fields`.
    """
    parcel: ParcelDossierParcel
    """Parcel identity."""
    fields: List[ParcelDossierFieldsItem]
    """Every populated field the delivery kept, as {name, value}. The receipt properties below are
    present only on the pure assembler's unprojected output; on a delivered dossier they live in the
    `provenance` map when `include_provenance=true` was requested.
    """
    sections: ParcelDossierSections
    """Real sub-tables from the serving relations."""
    boundary: ParcelDossierBoundary
    """The GeoJSON boundary add-on. In the base dossier included=false and geometry is absent; a
    phase-2 add-on purchase populates geometry.
    """
    meta: ParcelDossierMeta
    """Dossier-level provenance and pricing."""
    people_fields: PeopleFieldsWithheld
    """Present only when the buyer has no account (wallet-only x402 or credit token): the people fields
    in this dossier were withheld.
    """


class UccLien(TypedDict, total=False):
    filing_id: str
    debtor_name: Optional[str]
    secured_party: Optional[str]
    filing_date: Optional[str]
    lapse_date: Optional[str]
    filing_status: Optional[str]
    match_method: Optional[str]
    match_confidence: Optional[float]


class ComparableSale(TypedDict, total=False):
    comp_parcel_id: str
    comp_sale_price: Optional[float]
    comp_sale_date: Optional[str]
    comp_sqft: Optional[int]
    comp_beds: Optional[int]
    comp_baths: Optional[float]
    similarity_score: Optional[float]
    distance_miles: Optional[float]


class TrafficStationHistoryWithholdGateReasons(TypedDict):
    direct_vpd: Optional[str]
    nearby_vpd: Optional[str]
    vpd_visibility_score: Optional[str]


class TrafficStationHistoryWithholdGate(TypedDict):
    applied: Optional[bool]
    suppressed: List[Optional[str]]
    reason: Optional[str]
    reasons: TrafficStationHistoryWithholdGateReasons
    withheld_on: Optional[str]
    note: Optional[str]


class TrafficStationHistoryPointsItem(TypedDict):
    date: Optional[str]
    vpd: Optional[float]


class TrafficStationHistoryStation(TypedDict):
    id: str
    station_id: Optional[str]
    route_name: Optional[str]
    functional_class: Optional[str]
    aadt_current: Optional[float]
    """Most recent AADT count."""
    aadt_year: Optional[int]
    cagr_3yr: Optional[float]
    cagr_5yr: Optional[float]
    cagr_7yr: Optional[float]
    latitude: Optional[float]
    longitude: Optional[float]


class TrafficStationHistoryTimeSeriesItem(TypedDict):
    year: Optional[int]
    aadt: Optional[float]


class TrafficStationHistoryHistoryItem(TypedDict, total=False):
    year: int
    aadt: Optional[int]


class _TrafficStationHistoryRequired(TypedDict):
    direct_vpd: Optional[float]
    nearby_vpd: Optional[float]
    vpd_visibility_score: Optional[float]
    withhold_gate: TrafficStationHistoryWithholdGate
    points: List[TrafficStationHistoryPointsItem]
    station: TrafficStationHistoryStation
    time_series: List[TrafficStationHistoryTimeSeriesItem]


class TrafficStationHistory(_TrafficStationHistoryRequired, total=False):
    history: List[TrafficStationHistoryHistoryItem]
    """Year-keyed historical counts (newest last)."""


class CountyDetailMarketStatsItem(TypedDict):
    county_fips: str
    state_fips: str
    quarter: Optional[str]
    sale_count: Optional[int]
    median_sale_price: Optional[float]
    avg_sale_price: Optional[float]
    total_volume: Optional[int]
    price_yoy_pct: Optional[float]
    avg_dom: Optional[float]
    """Average days on market."""
    refreshed_at: Optional[str]


class CountyDetailDataProvenanceMarket(TypedDict):
    dataset: Optional[str]
    period_upper_bound: Optional[str]
    returned_records: Optional[float]
    oldest_record_refresh: Optional[str]
    newest_record_refresh: Optional[str]
    records_without_refresh: Optional[float]
    source_vintage: Optional[str]
    basis: Optional[str]


class CountyDetailDataProvenanceAffordabilityIncomeMeasure(TypedDict):
    stored_field: Optional[str]
    interpretation: Optional[str]
    source_tax_year: Optional[str]
    source_lineage_verified: Optional[bool]
    limitations: Optional[str]


class CountyDetailDataProvenanceAffordability(TypedDict):
    dataset: Optional[str]
    period_upper_bound: Optional[float]
    returned_records: Optional[float]
    oldest_record_refresh: Optional[str]
    newest_record_refresh: Optional[str]
    records_without_refresh: Optional[float]
    source_vintage: Optional[str]
    income_measure: CountyDetailDataProvenanceAffordabilityIncomeMeasure
    basis: Optional[str]


class CountyDetailDataProvenance(TypedDict):
    market: CountyDetailDataProvenanceMarket
    affordability: CountyDetailDataProvenanceAffordability


class CountyDetailParcelSummary(TypedDict):
    parcel_count: Optional[int]
    avg_assessed_value: Optional[float]


class CountyDetailFlipSummary(TypedDict):
    flip_count: Optional[int]
    avg_roi: Optional[float]
    avg_hold_days: Optional[float]
    total_profit: Optional[float]


class CountyDetail(TypedDict):
    county_fips: str
    market_stats: List[CountyDetailMarketStatsItem]
    affordability: List[AffordabilityRow]
    data_provenance: CountyDetailDataProvenance
    parcel_summary: CountyDetailParcelSummary
    flip_summary: CountyDetailFlipSummary


class MarketFlipsRow(TypedDict):
    county_fips: str
    flip_count: Optional[int]
    avg_roi: Optional[float]
    """Average profit percentage (e.g. 0.18 = 18%)."""
    avg_hold_days: Optional[float]
    total_profit: Optional[int]


class OwnerTransaction(TypedDict, total=False):
    document_number: str
    recording_date: Optional[str]
    sale_date: Optional[str]
    document_type: Optional[str]
    """Recorded document type (Warranty Deed, Quit Claim, etc.)."""
    sale_price: Optional[float]
    """USD. Null when state is non-disclosure."""
    grantor_name: Optional[str]
    grantee_name: Optional[str]
    property_address: Optional[str]


class AccountUsageRateLimit(TypedDict):
    per_minute: float
    per_day: float


class _AccountUsageRequired(TypedDict):
    tier: Literal["free", "starter", "pro", "scale", "api_100k"]
    period: str
    period_start: str
    period_end: str
    calls_used: int
    calls_included: int
    """Plan allotment for the current period."""
    calls_remaining: int
    rate_limit: AccountUsageRateLimit
    hard_cap_enabled: bool
    auth_source: str


class AccountUsage(_AccountUsageRequired, total=False):
    hard_capped: bool
    """Whether further calls will be hard-rejected vs allowed-and-billed."""


class _ParcelOwnerChangedEventRequired(TypedDict):
    event_type: Literal["parcel.owner_changed"]
    event_id: str
    """Deterministic. Use for idempotency."""
    occurred_at: str
    delivery_attempt: int
    """Starts at 1; increments on retry."""
    parcel_id: str
    """Composite county_fips:parcel_id."""
    state_fips: str
    county_fips: str


class ParcelOwnerChangedEvent(_ParcelOwnerChangedEventRequired, total=False):
    recorded_date: Optional[str]
    document_type: Optional[str]
    """Deed/document classification (e.g., Warranty Deed, Quitclaim Deed, Trust Transfer)."""
    document_number: Optional[str]
    prior_owner: Optional[str]
    """Grantor on the recorded deed."""
    new_owner: Optional[str]
    """Grantee on the recorded deed."""
    is_sale: Optional[bool]
    """True when the transfer is a real sale (price > 0, arm's-length). When true, subscribers to
    parcel.sold ALSO receive that event.
    """
    source_run_id: Optional[str]
    """PropRaven ingest run that surfaced this event."""


class _ParcelPermitFiledEventRequired(TypedDict):
    event_type: Literal["parcel.permit_filed"]
    event_id: str
    """Deterministic. Use for idempotency."""
    occurred_at: str
    delivery_attempt: int
    """Starts at 1; increments on retry."""
    parcel_id: str
    """Composite county_fips:parcel_id."""
    state_fips: str
    county_fips: str
    permit_id: str
    """PropRaven internal permit id (stable across re-ingests)."""


class ParcelPermitFiledEvent(_ParcelPermitFiledEventRequired, total=False):
    permit_number: Optional[str]
    """Jurisdiction-issued permit number."""
    permit_type: Optional[str]
    """Building, electrical, roofing, demolition, etc."""
    permit_status: Optional[str]
    """Filed, issued, in_review, final, expired, withdrawn."""
    filed_date: Optional[str]
    issued_date: Optional[str]
    description: Optional[str]
    estimated_cost: Optional[float]
    """Declared job cost in USD."""
    contractor_name: Optional[str]
    contractor_license: Optional[str]
    applicant_name: Optional[str]
    jurisdiction_id: Optional[str]
    """PropRaven jurisdiction id; join to /v1/jurisdictions."""
    source_run_id: Optional[str]
    """PropRaven ingest run that surfaced this event."""


class X402PaymentRequiredAcceptsItemExtra(TypedDict, total=False):
    """The asset's EIP-712 domain { name, version } (USDC = { name: 'USDC', version: '2' }) -- required
    by the exact EVM scheme so the facilitator can reconstruct the domain separator and verify the
    transferWithAuthorization signature.
    """
    name: str
    version: str


class X402PaymentRequiredAcceptsItem(TypedDict, total=False):
    scheme: str
    network: str
    """base-sepolia (testnet default) or base (mainnet)."""
    maxAmountRequired: str
    """The DYNAMIC price in the asset's atomic units (USDC, 6 decimals). Dossier: clamp($5 x V x R x F,
    $2, $20) per parcel. Lead feed: min(count x clamp($0.25 x S x V, $0.05, $1.00), $20) per pull.
    2000000 = $2.00, 6250000 = $6.25, 20000000 = the $20 cap. Sign for exactly this amount.
    """
    resource: str
    """The absolute URL being paid for."""
    description: str
    mimeType: str
    payTo: str
    """Receiving wallet address."""
    maxTimeoutSeconds: int
    """How long the quote is valid before the client must re-fetch it."""
    asset: str
    """ERC-20 asset contract address (USDC on the given network)."""
    extra: X402PaymentRequiredAcceptsItemExtra
    """The asset's EIP-712 domain { name, version } (USDC = { name: 'USDC', version: '2' }) -- required
    by the exact EVM scheme so the facilitator can reconstruct the domain separator and verify the
    transferWithAuthorization signature.
    """


class X402PaymentRequired(TypedDict, total=False):
    """x402 (HTTP 402) payment-required body (x402 protocol v1). `accepts` lists the payment
    requirements a wallet-bearing agent signs to pay per call. Returned by both paid products: the
    per-parcel dossier (GET /api/v1/parcels/{id}/report) and the per-lead feed (GET
    /api/v1/leads/find). Flow: sign an EIP-3009 transferWithAuthorization for
    accepts[0].maxAmountRequired, base64 the PaymentPayload into the `X-PAYMENT` request header, and
    retry. The response also carries `Link: <https://propraven.com/terms#data-license>;
    rel="license"`, the data license that governs what the payment buys.
    """
    x402Version: int
    """x402 protocol version advertised (1 = the base exact scheme with maxAmountRequired)."""
    error: str
    """Human-readable reason payment is required or was rejected."""
    accepts: List[X402PaymentRequiredAcceptsItem]
    """The payment requirements to satisfy (one entry: the dossier, or the lead pull)."""


class LeadsQuoteBreakdown(TypedDict):
    """The dials, so the price is auditable."""
    base_per_lead: float
    S: float
    """Signal-strength multiplier (absentee 1.0 ... distressed 1.9)."""
    V: float
    """Asset-value tier multiplier (low 0.7, mid 1.0, high 1.5, premium 2.2)."""
    per_lead_raw: float
    """Per-lead price BEFORE the [$0.05, $1.00] clamp."""
    total_raw: float
    """count x per_lead BEFORE the $20 per-call cap."""
    capped: bool
    """True when the $20 cap bound -- volume beyond it was free."""


class LeadsQuote(TypedDict):
    """The per-lead price quote. IDENTICAL in the free preview and in the 402/charge -- the previewed
    price is the paid price.
    """
    per_lead: Money
    per_lead_usd: float
    """Unit price to 4dp: clamp($0.25 x S x V, $0.05, $1.00)."""
    total: Money
    total_usd: float
    """The amount actually charged: min(count x per_lead, $20)."""
    total_atomic_usdc: str
    """total_usd in USDC atomic units (6dp) -- what the 402 advertises as maxAmountRequired."""
    asset: str
    count: int
    """Leads priced = leads delivered."""
    signal: str
    tier: Literal["low", "mid", "high", "premium"]
    """Asset-value tier, from the median assessed value of the delivered set."""
    tier_label: str
    breakdown: LeadsQuoteBreakdown
    """The dials, so the price is auditable."""
    pay: List[Optional[str]]
    note: str


class LeadProvenanceCatalogReferenceCatalogSeal(TypedDict):
    algorithm: Optional[str]
    value: Optional[str]
    covers: Optional[str]


class LeadProvenanceCatalogReference(TypedDict):
    catalog_version: Optional[str]
    catalog_generated_at: Optional[str]
    catalog_seal: LeadProvenanceCatalogReferenceCatalogSeal


class LeadProvenance(TypedDict):
    source: Optional[str]
    source_datasets: List[Optional[str]]
    as_of: Optional[str]
    """The serving epoch's generated_at."""
    as_of_basis: Optional[str]
    serving_epoch: Optional[str]
    freshness_status: Optional[str]
    catalog_reference: LeadProvenanceCatalogReference
    note: Optional[str]


class _LeadRequired(TypedDict):
    canonical_id: str
    """state_fips:county_fips3:parcel_id (the assessor APN, never a PropRaven UUID). Null on the
    owner-grain portfolio_owner cohort. MASKED to "37:183:..." in the free preview.
    """
    address: Optional[str]
    """Situs address. House number stripped in the free preview."""
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    assessed_value: Optional[float]
    """Total assessed value (sell price on the flip cohort)."""
    lead_score: Optional[float]
    """Deterministic 1-100: the signal's base intent plus a bounded bonus from that signal's own
    strength column. Re-derivable, never random.
    """
    owner_address: Optional[str]
    owner_city: Optional[str]
    owner_state: Optional[str]
    is_out_of_state: Optional[bool]
    last_sale_date: Optional[str]
    last_sale_price: Optional[float]
    owner_name: Optional[str]
    """Withheld (null) in the free preview. Delivered leads go to accounts only."""
    masked: Optional[bool]
    """Present and true ONLY on free-preview sample leads."""
    provenance: LeadProvenance


class Lead(_LeadRequired, total=False):
    """One delivered lead. Signal-specific strength fields are flattened alongside the common keys
    (e.g. years_held + hold_tier for long_hold; profit + profit_pct + flip_tier for flip;
    land_improvement_ratio for high_land_ratio/distressed; property_count + states_list for
    portfolio_owner).
    """
    owner_contact: LeadOwnerContact
    """Delivered leads only: the owner's best mailing address (ONE column family, with its ZIP),
    flagged mail_ready. Absent from the free preview.
    """


class LeadFeedPreviewGeo(TypedDict):
    """The resolved request geography and filters."""
    state: str
    state_fips: str
    county_fips: Optional[str]
    zip: Optional[str]
    value_min: Optional[int]
    value_max: Optional[int]
    mail_ready: bool
    limit: int


class _LeadFeedPreviewRequired(TypedDict):
    signal: str
    geo: LeadFeedPreviewGeo
    """The resolved request geography and filters."""
    count: int
    """Leads that will be / were delivered: min(matching rows, limit). This is the priced quantity."""
    count_capped_at_limit: bool
    """True when the count stopped at `limit` -- more leads exist beyond this pull."""
    quote: LeadsQuote
    preview: Literal[True]
    sample: List[Lead]
    """Up to three MASKED leads: APN truncated to state:county, house number stripped, owner name
    withheld. Enough to judge the set, not enough to work it.
    """
    note: str


class LeadFeedPreview(_LeadFeedPreviewRequired, total=False):
    """The FREE preview (preview=true). `count` and `quote` are exactly what a paid call would deliver
    and charge.
    """
    coverage_note: str
    """Present only when a known data gap explains an empty result (e.g. the owner-portfolio rollup's
    unpopulated state columns). Nothing is charged in that case.
    """


class LeadFeedGeo(TypedDict, total=False):
    """The resolved request geography and filters."""
    state: str
    state_fips: Optional[str]
    county_fips: Optional[str]
    zip: Optional[str]
    value_min: Optional[int]
    value_max: Optional[int]
    limit: int
    mail_ready: bool


class LeadFeed(TypedDict, total=False):
    """The delivered lead set (paid), or an honest empty result when nothing matched (count 0, quote
    total $0, no payment taken).
    """
    signal: str
    geo: LeadFeedGeo
    """The resolved request geography and filters."""
    count: int
    """Leads that will be / were delivered: min(matching rows, limit). This is the priced quantity."""
    count_capped_at_limit: bool
    """True when the count stopped at `limit` -- more leads exist beyond this pull."""
    quote: LeadsQuote
    coverage_note: str
    """Present only when a known data gap explains an empty result (e.g. the owner-portfolio rollup's
    unpopulated state columns). Nothing is charged in that case.
    """
    note: str
    paid_via: Literal["x402", "credits", "subscription"]
    """Absent on an unpaid empty result (count 0)."""
    leads: List[Lead]
    """The delivered, UNMASKED leads."""


class ProblemErrorsItem(TypedDict):
    param: str
    message: str


class _ProblemRequired(TypedDict):
    type: str
    title: str
    status: int
    detail: str
    code: str
    """Stable machine-readable code."""


class Problem(_ProblemRequired, total=False):
    """THE error body of every /api/v1 endpoint (RFC 7807 problem details, served as
    `application/problem+json`). `code` is the stable machine-readable identifier (e.g.
    invalid_parameter, authentication_required, account_required, monthly_cap_reached,
    query_timeout, not_found, method_not_allowed); `detail` is human-readable and never contains
    database or driver text. Validation failures add `errors: [{param, message}]`. `request_id`
    identifies the request for support. Per-code members (e.g. `reason`, `retry_after`, `used` /
    `limit` / `plan` / `upgrade`, `allow`) sit beside the core members. Exception: an x402 `402
    Payment Required` keeps the x402 protocol envelope (`x402Version`, `accepts`).
    """
    reason: str
    """Finer reason for `code`, e.g. people_data_requires_account."""
    errors: List[ProblemErrorsItem]
    """Per-parameter validation failures (400 invalid_parameter)."""
    request_id: str
    """Support handle for this request."""


class ServiceUnavailable(TypedDict):
    """A refusal that took nothing: the work was not done and nothing was charged. Retry after
    `Retry-After`.
    """
    error: str


class PeopleFieldsWithheld(TypedDict):
    """Additive marker on a record (or list) whose people fields were withheld because the caller has
    no PropRaven account. People fields are owner names, owner mailing / owner-address columns,
    entity principals, recorded-document party names and addresses (grantor/grantee, buyer/seller,
    prior/new owner), permit applicant names and the resolved `owner_contact` block. Withheld keys
    are kept and set to null (lists of people records become []), so the record's shape does not
    change. Payment alone (an x402 `X-PAYMENT` header or a prepaid `X-CREDIT-TOKEN`) is not an
    account: send an API key (`Authorization: Bearer pz_...`) or call from a signed-in session.
    """
    status: Literal["withheld"]
    code: Literal["account_required"]
    reason: Literal["people_data_requires_account"]
    note: str


class ContactSource(TypedDict):
    authority: str
    """Who published the value, e.g. the county assessor."""
    dataset: str
    url: Optional[str]


class CoOwner(TypedDict, total=False):
    """A co-owner of record: another owner the SAME assessor record names beside the owner (OWNER2,
    ownname2, ADD_OWNER ...), as the county published it. Same source and as-of date as the owner
    name. Account required, like every people field.
    """
    name: str
    basis: Literal["assessor_co_owner"]
    source: ContactSource
    as_of: Optional[str]
    as_of_basis: Optional[Literal["roll_year", "release_vintage"]]
    grade: Literal["A", "B", "C", "D"]


class MailingAddress(TypedDict):
    """One mailing address, read from ONE address column family of the record (owner_mailing_* or
    owner_*), never a street from one family and a ZIP from the other.
    """
    basis: str
    """Where the address came from, e.g. owner_mailing, owner_address, deed_grantee."""
    line1: str
    city: str
    state: str
    zip5: str
    zip4: Optional[str]
    mail_ready: bool
    """Street, city, state and a 5-digit ZIP are all present and consistent."""
    po_box: bool
    equals_situs: bool
    """The mailing address is the property itself (owner-occupied)."""
    zip_conflict: bool
    parcels_citing: float
    """Owner (name) cards only: how many of the owner's parcels carry this address."""
    parcels_citing_basis: str
    label: str
    """The address as one mailing label."""
    source: ContactSource
    as_of: str
    as_of_basis: str
    grade: Literal["A", "B", "C", "D"]
    """A = the authority's own complete record; D = contradictory (hidden unless
    include_low_confidence=true).
    """


class LeadOwnerContact(TypedDict, total=False):
    """The owner's best mailing address on a delivered lead (account holders only). Lead pulls do not
    run the per-parcel permit phone lookup (`phone_status` is always not_checked); call GET
    /api/v1/owners/card for the full card.
    """
    status: Literal["resolved", "not_found", "unavailable"]
    """unavailable = the contact read failed for this delivery (never a silently missing block)."""
    mailing: Optional[MailingAddress]
    mail_ready: bool
    phone_status: Literal["not_checked"]
    hidden_low_confidence: int


class OwnerCardSubject(TypedDict):
    """{ kind: "parcel", canonical_id } or { kind: "owner", parcels_considered, parcels_capped }."""
    kind: str
    canonical_id: str


class OwnerCardOwner(TypedDict):
    name: str
    name_status: Literal["present", "missing", "placeholder", "confidential"]
    entity_type: str
    roles: List[Any]


class OwnerCardContactOwnerNameProvenanceSource(TypedDict):
    authority: str
    dataset: str
    url: Optional[str]


class OwnerCardContactOwnerNameProvenance(TypedDict):
    source: OwnerCardContactOwnerNameProvenanceSource
    as_of: str
    as_of_basis: str
    grade: str


class OwnerCardContactEntitySource(TypedDict):
    authority: str
    dataset: str
    url: Optional[str]


class OwnerCardContactEntity(TypedDict):
    """Secretary of State principals (entity type, status, registered agent, officers) when the owner
    is an entity.
    """
    entity_type: str
    status: Optional[str]
    state_of_formation: Optional[str]
    formation_date: Optional[str]
    registered_agent: Optional[str]
    officers: List[Any]
    source: OwnerCardContactEntitySource
    as_of: Optional[str]
    as_of_basis: Optional[str]
    grade: str


class OwnerCardContactOtherAddressesItemAddress(TypedDict):
    line1: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip5: Optional[str]
    zip4: Optional[str]
    label: Optional[str]
    mail_ready: Optional[bool]
    po_box: Optional[bool]


class OwnerCardContactOtherAddressesItemCitedByItem(TypedDict):
    parcel_id: str
    state: Optional[str]
    county: Optional[str]


class OwnerCardContactOtherAddressesItemSource(TypedDict):
    authority: Optional[str]
    dataset: Optional[str]
    url: Optional[str]


class OwnerCardContactOtherAddressesItem(TypedDict):
    parcel_id: str
    state: Optional[str]
    county: Optional[str]
    kind: Optional[str]
    address: OwnerCardContactOtherAddressesItemAddress
    same_as: Optional[str]
    grade: Optional[str]
    link: Optional[str]
    basis: Optional[str]
    label_note: Optional[str]
    evidence: List[Any]
    mail_merge: Optional[bool]
    owner_name_on_record: Optional[str]
    owner_roles: List[Any]
    cited_by: List[OwnerCardContactOtherAddressesItemCitedByItem]
    parcels_citing: Optional[float]
    source: OwnerCardContactOtherAddressesItemSource
    as_of: Optional[str]
    as_of_basis: str


class OwnerCardContactOtherAddressesScopeEvidenceProvidersItem(TypedDict):
    id: str
    status: Optional[str]


class OwnerCardContactOtherAddressesScope(TypedDict):
    name_basis: str
    spellings: float
    parcels_read: float
    capped: bool
    copies_skipped: float
    parcels_linked: float
    possible_found: float
    possible_listed: float
    possible_cap: float
    possible_withheld_reason: Optional[str]
    listed_capped: bool
    evidence_providers: List[OwnerCardContactOtherAddressesScopeEvidenceProvidersItem]
    co_owner_link: str


class _OwnerCardContactRequired(TypedDict):
    owner_name: str
    owner_name_status: str
    owner_roles: List[Any]
    owner_name_provenance: OwnerCardContactOwnerNameProvenance
    co_owners: List[CoOwner]
    """The other owners the same assessor record names, in the record's order; never the owner again.
    Name mode: across the side-read parcels, distinct by name.
    """
    co_owner_status: Literal["listed", "none_listed", "not_checked"]
    """none_listed is claimed only for a record whose state's co-owners were loaded from the release
    that serves it; not_checked when the lookup could not run, the state is not loaded yet, or the
    loaded row was read beside a different owner.
    """
    mailing: MailingAddress
    mailing_alternates: List[MailingAddress]
    """Parcel mode: a latest-deed grantee address naming the same owner, when it differs."""
    entity: OwnerCardContactEntity
    """Secretary of State principals (entity type, status, registered agent, officers) when the owner
    is an entity.
    """
    phones: List[Dict[str, Any]]
    """OWNER phones (owner role only) published on a building permit filed in the current owner's era
    and naming them (grade C): { e164, display, ext, phone_raw, role_basis, permit_ref, source,
    as_of, as_of_basis, grade }.
    """
    phone_status: Literal["published", "none_published", "not_checked"]
    """none_published is claimed only after the permit lookup ran; not_checked when it could not
    (timeout, no acquisition date, no owner name).
    """
    emails: List[Dict[str, Any]]
    none_published: List[Optional[Literal["phone", "email"]]]
    hidden_low_confidence: float
    people_on_permits: List[Dict[str, Any]]
    """Applicant and contractor phones on the parcel's permits (name mode: across the side-read
    parcels), newest first, one per (role, number), at most 10: { role: applicant|contractor,
    role_basis, name, e164, display, ext, phone_raw, permit_ref, era:
    current_owner|prior_owner|unknown, source, as_of, as_of_basis, grade }. Never the owner's phone.
    """
    people_on_permits_status: Literal["listed", "none_published", "not_checked"]
    """none_published only after the parcel's permits were read in full; not_checked when the read did
    not run or stopped at its cap.
    """
    other_addresses: List[OwnerCardContactOtherAddressesItem]
    other_addresses_status: str
    other_addresses_scope: OwnerCardContactOtherAddressesScope


class OwnerCardContact(_OwnerCardContactRequired, total=False):
    co_owner_scope: Dict[str, Any]
    """Name mode: { parcels_checked, parcels_considered }."""
    mailing_addresses: List[MailingAddress]
    """Name mode: the owner's distinct mailing addresses, most-cited first."""
    phone_scope: Dict[str, Any]
    """Name mode: { parcels_checked, parcels_considered }."""


class OwnerCard(TypedDict):
    """The owner card: the owner of record and how to reach them by mail, from what the publishing
    authorities released.
    """
    subject: OwnerCardSubject
    """{ kind: "parcel", canonical_id } or { kind: "owner", parcels_considered, parcels_capped }."""
    owner: OwnerCardOwner
    contact: OwnerCardContact
    note: str


class ParcelsOwnerResponseOwner(TypedDict):
    owner_name: Optional[str]
    owner_address: Optional[str]
    owner_city: Optional[str]
    owner_state: Optional[str]


class ParcelsOwnerResponseContactOwnerNameProvenanceSource(TypedDict):
    authority: Optional[str]
    dataset: Optional[str]
    url: Optional[str]


class ParcelsOwnerResponseContactOwnerNameProvenance(TypedDict):
    source: ParcelsOwnerResponseContactOwnerNameProvenanceSource
    as_of: Optional[str]
    as_of_basis: str
    grade: Optional[str]


class ParcelsOwnerResponseContactMailingSource(TypedDict):
    authority: Optional[str]
    dataset: Optional[str]
    url: Optional[str]


class ParcelsOwnerResponseContactMailing(TypedDict):
    basis: Optional[str]
    line1: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip5: Optional[str]
    zip4: Optional[str]
    mail_ready: Optional[bool]
    po_box: Optional[bool]
    equals_situs: Optional[bool]
    zip_conflict: Optional[bool]
    parcels_citing: Optional[float]
    parcels_citing_basis: str
    label: Optional[str]
    source: ParcelsOwnerResponseContactMailingSource
    as_of: Optional[str]
    as_of_basis: str
    grade: Optional[str]


class ParcelsOwnerResponseContactEntitySource(TypedDict):
    authority: Optional[str]
    dataset: Optional[str]
    url: Optional[str]


class ParcelsOwnerResponseContactEntity(TypedDict):
    entity_type: Optional[str]
    status: Optional[str]
    state_of_formation: Optional[str]
    formation_date: Optional[str]
    registered_agent: Optional[str]
    officers: List[Any]
    source: ParcelsOwnerResponseContactEntitySource
    as_of: Optional[str]
    as_of_basis: Optional[str]
    grade: Optional[str]


class ParcelsOwnerResponseContactOtherAddressesItemAddress(TypedDict):
    line1: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip5: Optional[str]
    zip4: Optional[str]
    label: Optional[str]
    mail_ready: Optional[bool]
    po_box: Optional[bool]


class ParcelsOwnerResponseContactOtherAddressesItemCitedByItem(TypedDict):
    parcel_id: str
    state: Optional[str]
    county: Optional[str]


class ParcelsOwnerResponseContactOtherAddressesItemSource(TypedDict):
    authority: Optional[str]
    dataset: Optional[str]
    url: Optional[str]


class ParcelsOwnerResponseContactOtherAddressesItem(TypedDict):
    parcel_id: str
    state: Optional[str]
    county: Optional[str]
    kind: Optional[str]
    address: ParcelsOwnerResponseContactOtherAddressesItemAddress
    same_as: Optional[str]
    grade: Optional[str]
    link: Optional[str]
    basis: Optional[str]
    label_note: Optional[str]
    evidence: List[Any]
    mail_merge: Optional[bool]
    owner_name_on_record: Optional[str]
    owner_roles: List[Any]
    cited_by: List[ParcelsOwnerResponseContactOtherAddressesItemCitedByItem]
    parcels_citing: Optional[float]
    source: ParcelsOwnerResponseContactOtherAddressesItemSource
    as_of: Optional[str]
    as_of_basis: str


class ParcelsOwnerResponseContactOtherAddressesScopeEvidenceProvidersItem(TypedDict):
    id: str
    status: Optional[str]


class ParcelsOwnerResponseContactOtherAddressesScope(TypedDict):
    name_basis: str
    spellings: Optional[float]
    parcels_read: Optional[float]
    capped: Optional[bool]
    copies_skipped: Optional[float]
    parcels_linked: Optional[float]
    possible_found: Optional[float]
    possible_listed: Optional[float]
    possible_cap: Optional[float]
    possible_withheld_reason: Optional[str]
    listed_capped: Optional[bool]
    evidence_providers: List[ParcelsOwnerResponseContactOtherAddressesScopeEvidenceProvidersItem]
    co_owner_link: Optional[str]


class ParcelsOwnerResponseContact(TypedDict):
    owner_name: Optional[str]
    owner_name_status: Optional[str]
    owner_roles: List[Any]
    owner_name_provenance: ParcelsOwnerResponseContactOwnerNameProvenance
    co_owners: List[Any]
    co_owner_status: Optional[str]
    mailing: ParcelsOwnerResponseContactMailing
    mailing_alternates: List[Any]
    entity: ParcelsOwnerResponseContactEntity
    phones: List[Any]
    phone_status: Optional[str]
    emails: List[Any]
    none_published: List[Optional[str]]
    hidden_low_confidence: Optional[float]
    people_on_permits: List[Any]
    people_on_permits_status: Optional[str]
    other_addresses: List[ParcelsOwnerResponseContactOtherAddressesItem]
    other_addresses_status: Optional[str]
    other_addresses_scope: ParcelsOwnerResponseContactOtherAddressesScope


class _ParcelsOwnerResponsePortfolioRequired(TypedDict):
    property_count: Optional[int]
    state_count: Optional[int]
    total_assessed_value: Optional[int]
    total_acreage: Optional[float]
    states_list: Optional[str]


class ParcelsOwnerResponsePortfolio(_ParcelsOwnerResponsePortfolioRequired, total=False):
    county_count: Optional[int]
    portfolio_rank: Optional[int]


class ParcelsOwnerResponsePropertiesItem(TypedDict):
    parcel_id: str
    county_fips: str
    state_fips: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    total_assessed_value: Optional[float]
    last_sale_price: Optional[float]
    last_sale_date: Optional[str]
    property_type: Optional[str]
    building_sqft: Optional[float]
    lot_size_acres: Optional[float]
    year_built: Optional[int]


class ParcelsOwnerResponsePortfolioSummary(TypedDict, total=False):
    property_count: int
    total_assessed_value: float
    states: List[str]


class _ParcelsOwnerResponseRequired(TypedDict):
    owner: ParcelsOwnerResponseOwner
    contact: ParcelsOwnerResponseContact
    entity_type: Optional[str]
    """Observed values include: CORP."""
    portfolio: ParcelsOwnerResponsePortfolio
    properties: List[ParcelsOwnerResponsePropertiesItem]


class ParcelsOwnerResponse(_ParcelsOwnerResponseRequired, total=False):
    owner_name: str
    mailing_address: str
    portfolio_summary: ParcelsOwnerResponsePortfolioSummary


class ParcelsPermitsResponseVariant2(TypedDict):
    data: List[Permit]
    permit_count: int
    """The parcel's permit count (exact) or the capped window size (a floor) — see permit_count_basis."""
    permit_count_basis: Literal["exact", "capped"]
    truncated: bool
    """True when the parcel has more permits than `data` carries."""
    row_cap: int
    """The row cap `data` is bounded by (100)."""


class _ParcelsDeedsResponseVariant2Required(TypedDict):
    data: List[Deed]
    status: Literal["per_deed", "rollup_events", "summary_only", "none"]
    known_deed_count: Optional[int]
    """parcels_serving.deed_count when the parcel carries one; NOT a count of the returned rows."""
    known_deed_count_basis: Optional[str]
    """Where known_deed_count comes from: the frozen 2026-04 weld, or the identity gate's reason when
    the parcel_id collides across counties — parcel_id_collides_bare_id_joined (rollup withheld,
    count null), parcel_id_collides_unmeasured (served with the doubt visible),
    collision_check_unavailable (withheld under DQ_IDENTITY_GATE_FAIL_CLOSED=1).
    """


class ParcelsDeedsResponseVariant2(_ParcelsDeedsResponseVariant2Required, total=False):
    """Returned only when `shape=envelope`."""
    note: str
    join_key_basis: Literal["state_county_parcel_id", "parcel_id_collides", "unchecked"]
    """The identity probe's verdict on the rollup (present on rollup-derived envelopes; absent on the
    county-scoped per_deed branch).
    """
    rollup_probe: Literal["deeds_relation"]
    """Present when the rollup was withheld on the deeds-relation probe: the parcel_id is unique in
    parcels_serving (join_key_basis state_county_parcel_id) but parcel_deeds carries rows for it
    under another (state, county), so the frozen rollup was welded on the bare id from another
    parcel's deeds.
    """


class SearchParcelsParamsBounds(TypedDict):
    """Viewport in WGS84 degrees. north > south. west > east is an antimeridian-crossing box."""
    north: float
    south: float
    east: float
    west: float


class SearchParcelsParamsFiltersValueRange(TypedDict, total=False):
    """Assessed value range."""
    min: Optional[float]
    max: Optional[float]


class SearchParcelsParamsFiltersYearBuiltRange(TypedDict, total=False):
    """Year built range."""
    min: Optional[int]
    max: Optional[int]


class SearchParcelsParamsFiltersAcreageRange(TypedDict, total=False):
    """Lot size range in acres."""
    min: Optional[float]
    max: Optional[float]


class SearchParcelsParamsFilters(TypedDict, total=False):
    """All optional; null means not set. Unknown members are a 400."""
    zoningCategories: List[str]
    """Zoning categories (Residential, Commercial, Industrial, Mixed-Use, Agricultural, …).
    Unrecognised labels are reported in `zoning_categories_unrecognized`.
    """
    ownerTypes: List[Literal["individual", "llc", "trust", "corporation", "government", "religious", "partnership", "association", "financial"]]
    """Owner entity type (case-insensitive)."""
    propertyType: List[str]
    """Property type group, e.g. Commercial, Residential."""
    businessTypes: List[str]
    """Business / use type, e.g. car_wash."""
    absenteeOnly: bool
    """Only parcels whose owner state differs from the parcel state."""
    soldWithin: Literal["6mo", "1yr", "3yr", "never"]
    floodZone: str
    valueRange: SearchParcelsParamsFiltersValueRange
    """Assessed value range."""
    yearBuiltRange: SearchParcelsParamsFiltersYearBuiltRange
    """Year built range."""
    acreageRange: SearchParcelsParamsFiltersAcreageRange
    """Lot size range in acres."""
    minYearsOwned: float
    minCrimeScore: float
    maxCrimeScore: float
    crimeTrend: str
    minVpd: float
    """WITHHELD — refused with 400 filter_withheld until traffic counts are verified."""
    maxVpd: float
    """WITHHELD — refused with 400 filter_withheld."""
    minVisibilityScore: float
    """WITHHELD — refused with 400 filter_withheld."""


class SearchParcelsResponseDataItem(TypedDict):
    parcel_id: str
    state_fips: str
    county_fips: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    owner_name: Optional[str]
    total_assessed_value: Optional[float]
    zoning: Optional[str]
    zoning_code_raw: Optional[str]
    year_built: Optional[int]
    lot_size_acres: Optional[float]
    ownership_type: Optional[str]
    land_use_desc: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    direct_vpd: Optional[float]
    nearby_vpd: Optional[float]
    vpd_visibility_score: Optional[float]
    crime_score: Optional[float]
    crime_tier: Optional[float]
    crime_trend: Optional[str]
    _guards: List[str]


class SearchParcelsResponseWithholdGateReasons(TypedDict):
    direct_vpd: str
    nearby_vpd: str
    vpd_visibility_score: str


class SearchParcelsResponseWithholdGate(TypedDict):
    """Present when withheld columns (traffic counts) are in the rows; they are null."""
    applied: bool
    suppressed: List[Optional[str]]
    reason: str
    reasons: SearchParcelsResponseWithholdGateReasons
    withheld_on: str
    note: str


class _SearchParcelsResponseRequired(TypedDict):
    data: List[SearchParcelsResponseDataItem]
    total: int
    """Exact matching count up to 10,000; 10,000 when capped; null when the count timed out."""
    total_is_estimate: bool
    """True only when `total` is capped (a lower bound)."""
    total_is_lower_bound: bool
    has_more: bool
    limit: int
    offset: int
    sort_applied: bool
    """False when `bounds` was given (sort is not applied to bounded queries) or no sort was requested."""
    withhold_gate: SearchParcelsResponseWithholdGate
    """Present when withheld columns (traffic counts) are in the rows; they are null."""


class SearchParcelsResponse(_SearchParcelsResponseRequired, total=False):
    total_status: Literal["timed_out"]
    """Present when the count did not finish."""
    zoning_categories_applied: List[str]
    zoning_categories_unrecognized: List[str]
    zoning_unknown_estimate: Optional[int]
    zoning_unknown_is_estimate: bool
    zoning_filter_note: str


class _CoverageGetResponseDataItemRequired(TypedDict):
    state_fips: str
    parcel_count: Optional[int]
    with_address: Optional[float]
    with_geocode: Optional[float]
    with_owner: Optional[float]
    with_value: Optional[float]
    last_updated: Optional[str]
    with_geometry: Optional[float]


class CoverageGetResponseDataItem(_CoverageGetResponseDataItemRequired, total=False):
    county_fips: str
    county_name: Optional[str]
    population: Optional[float]
    state_abbr: Optional[str]
    county_count: Optional[int]
    total_counties: Optional[int]
    total_population: Optional[int]
    covered_population: Optional[float]
    population_coverage_pct: Optional[float]
    state_name: str
    geocoded_pct: float
    owner_pct: float
    value_pct: float


class CoverageGetResponseNationalCountsParcelCountDefinitions(TypedDict):
    parcels: str
    mapped_locations: str
    geocoded_parcels: str
    rows: str


class CoverageGetResponseNationalCounts(TypedDict):
    parcel_counts_epoch: str
    parcels: float
    mapped_locations: float
    geocoded_parcels: float
    rows: float
    parcel_count_definitions: CoverageGetResponseNationalCountsParcelCountDefinitions


class _CoverageGetResponseRequired(TypedDict):
    data: List[CoverageGetResponseDataItem]


class CoverageGetResponse(_CoverageGetResponseRequired, total=False):
    state: str
    total_counties: int
    total_counties_us: int
    total_population_us: int
    covered_population_us: float
    population_coverage_pct: float
    national_counts: CoverageGetResponseNationalCounts
    total_parcels: int
    states_covered: int


class DealsAbsenteeResponseDataItem(TypedDict):
    county_fips: str
    state_fips: str
    parcel_id: str
    owner_name: Optional[str]
    property_address: Optional[str]
    property_city: Optional[str]
    property_state: Optional[str]
    owner_address: Optional[str]
    owner_city: Optional[str]
    owner_state: Optional[str]
    total_assessed_value: Optional[int]
    last_sale_date: Optional[str]
    last_sale_price: Optional[float]
    is_out_of_state: Optional[bool]


class DealsAbsenteeResponse(TypedDict):
    data: List[DealsAbsenteeResponseDataItem]
    total: int
    limit: int
    offset: int


class DealsFlipsResponseDataItem(TypedDict):
    county_fips: str
    state_fips: str
    parcel_id: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    buy_date: Optional[str]
    buy_price: Optional[float]
    buyer_name: Optional[str]
    sell_date: Optional[str]
    sell_price: Optional[float]
    seller_name: Optional[str]
    hold_days: Optional[int]
    profit: Optional[float]
    profit_pct: Optional[float]
    flip_tier: Optional[Literal["QUICK_FLIP", "SHORT_HOLD", "MEDIUM_HOLD"]]


class DealsFlipsResponse(TypedDict):
    data: List[DealsFlipsResponseDataItem]
    total: int
    limit: int
    offset: int


class _MarketCountiesResponseDataItemRequired(TypedDict):
    county_fips: str
    state_fips: str
    county_name: Optional[str]
    state: Optional[str]
    refreshed_at: Optional[str]
    quarter: Optional[str]
    sale_count: Optional[int]
    median_sale_price: Optional[float]
    avg_sale_price: Optional[float]
    total_volume: Optional[int]
    price_yoy_pct: Optional[float]
    avg_dom: Optional[float]


class MarketCountiesResponseDataItem(_MarketCountiesResponseDataItemRequired, total=False):
    state_abbr: str
    median_price: float
    avg_price: float
    yoy_change: float
    """Year-over-year median price change as a decimal (e.g., 0.05 = 5%)."""
    avg_days_on_market: int


class MarketCountiesResponseSummary(TypedDict):
    total_counties: int
    total_sales: int
    overall_median_price: float
    total_volume: int
    avg_yoy_pct: float


class MarketCountiesResponse(TypedDict):
    data: List[MarketCountiesResponseDataItem]
    summary: MarketCountiesResponseSummary
    total: int
    limit: int
    offset: int


class MarketTrendsResponseDataItemQuartersItem(TypedDict, total=False):
    quarter: str
    sale_count: int
    median_price: float
    avg_price: float
    yoy_change: float


class _MarketTrendsResponseDataItemRequired(TypedDict):
    quarter: Optional[str]
    total_sales: Optional[int]
    median_price: Optional[float]
    total_volume: Optional[int]
    avg_dom: Optional[float]


class MarketTrendsResponseDataItem(_MarketTrendsResponseDataItemRequired, total=False):
    county_fips: str
    county_name: str
    quarters: List[MarketTrendsResponseDataItemQuartersItem]


class MarketTrendsResponse(TypedDict):
    data: List[MarketTrendsResponseDataItem]
    mode: str


class OwnersSearchResponse(TypedDict):
    data: List[Owner]
    count: int


class OwnersPropertiesResponseDataItem(TypedDict):
    state_fips: str
    county_fips: str
    parcel_id: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    total_assessed_value: Optional[float]
    land_value: Optional[float]
    improvement_value: Optional[float]
    lot_size_acres: Optional[float]
    zoning: Optional[str]
    zoning_code_raw: Optional[str]
    land_use_desc: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    year_built: Optional[int]


class OwnersPropertiesResponse(TypedDict):
    data: List[OwnersPropertiesResponseDataItem]
    total: int
    limit: int
    offset: int


class OwnersPortfolioResponsePropertiesItem(TypedDict):
    parcel_id: str
    county_fips: str
    state_fips: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    owner_name: Optional[str]
    total_assessed_value: Optional[float]
    land_assessed_value: Optional[float]
    improvement_assessed_value: Optional[float]
    lot_size_acres: Optional[float]
    building_sqft: Optional[float]
    year_built: Optional[int]
    zoning: Optional[str]
    zoning_code_raw: Optional[str]
    last_sale_date: Optional[str]
    last_sale_price: Optional[float]
    property_type: Optional[str]
    match_basis: str
    match_confidence: Optional[str]
    owner_roles: List[Any]


class OwnersPortfolioResponseSummaryByStateItem(TypedDict):
    state: Optional[str]
    state_fips: str
    abbr: Optional[str]
    count: Optional[int]
    total_value: Optional[int]
    total_acreage: Optional[float]


class _OwnersPortfolioResponseSummaryRequired(TypedDict):
    count: int
    returned: float
    limit: int
    offset: int
    truncated: bool
    total_value: int
    total_acreage: float
    states: List[Optional[float]]
    by_state: List[OwnersPortfolioResponseSummaryByStateItem]


class OwnersPortfolioResponseSummary(_OwnersPortfolioResponseSummaryRequired, total=False):
    property_count: int
    total_assessed_value: float
    avg_assessed_value: float
    counties: int
    zoning_breakdown: Dict[str, int]


class OwnersPortfolioResponseMatchBasisCounts(TypedDict):
    exact_spelling: float
    variant: float
    ticker_curated: float


class OwnersPortfolioResponseMatch(TypedDict):
    method: str
    confidence: str
    verified_corporate_link: bool
    basis_counts: OwnersPortfolioResponseMatchBasisCounts
    basis_counts_scope: str
    note: str


class _OwnersPortfolioResponseRequired(TypedDict):
    owner_name: str
    properties: List[OwnersPortfolioResponsePropertiesItem]
    summary: OwnersPortfolioResponseSummary
    match: OwnersPortfolioResponseMatch


class OwnersPortfolioResponse(_OwnersPortfolioResponseRequired, total=False):
    entity_type: Literal["individual", "corporation", "llc", "trust", "government", "other"]


class OwnersReportResponseOwnerMatchBasisCounts(TypedDict):
    exact_spelling: float
    variant: float
    ticker_curated: float


class OwnersReportResponseOwnerMatch(TypedDict):
    method: str
    confidence: str
    verified_corporate_link: bool
    basis_counts: OwnersReportResponseOwnerMatchBasisCounts
    basis_counts_scope: str
    note: str


class OwnersReportResponseOwner(TypedDict):
    query_name: str
    ticker: Optional[str]
    entity_type: str
    resolved_variants: List[Optional[str]]
    match: OwnersReportResponseOwnerMatch


class OwnersReportResponseFilter(TypedDict):
    state_fips: Optional[str]


class OwnersReportResponseSummaryByStateItem(TypedDict):
    state: Optional[str]
    state_fips: str
    abbr: Optional[str]
    count: Optional[int]
    total_value: Optional[int]
    total_acreage: Optional[float]


class OwnersReportResponseSummary(TypedDict):
    count: int
    total_assessed_value: int
    total_acreage: float
    states: List[Optional[float]]
    by_state: List[OwnersReportResponseSummaryByStateItem]


class OwnersReportResponseQuotePrice(TypedDict):
    amount: str
    currency: str


class OwnersReportResponseQuoteBreakdown(TypedDict):
    base: float
    P: float
    V: float
    price_raw: float
    capped: bool


class OwnersReportResponseQuote(TypedDict):
    price: OwnersReportResponseQuotePrice
    price_usd: float
    price_atomic_usdc: str
    asset: str
    parcel_count: int
    band: str
    band_label: str
    breakdown: OwnersReportResponseQuoteBreakdown
    pay: List[Optional[str]]
    note: str


class OwnersReportResponseSampleItem(TypedDict):
    canonical_id: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    total_assessed_value: Optional[float]
    property_type: Optional[str]
    match_basis: str
    match_confidence: Optional[str]


class OwnersReportResponse(TypedDict):
    owner: OwnersReportResponseOwner
    filter: OwnersReportResponseFilter
    summary: OwnersReportResponseSummary
    quote: OwnersReportResponseQuote
    preview: bool
    sample: List[OwnersReportResponseSampleItem]
    note: str


class DealsContractorsResponseSourceQuality(TypedDict):
    geography_status: str
    profile_refresh_observed_at: str
    quality_checked_at: str
    scope: str
    reason: str


class DealsContractorsResponse(TypedDict):
    data: List[Contractor]
    total: int
    limit: int
    offset: int
    source_quality: DealsContractorsResponseSourceQuality


class DealsEntitiesResponseVariant1(TypedDict):
    data: List[EntityOwnedParcel]
    total: int
    limit: int
    offset: int


class DealsEntitiesResponseVariant2(TypedDict, total=False):
    data: List[EntityAggregate]
    summary: EntitySummary
    total: int
    limit: int
    offset: int


class DealsHighLandRatioResponse(TypedDict):
    data: List[HighLandRatioParcel]
    total: int
    limit: int
    offset: int


class DealsLendersResponse(TypedDict, total=False):
    data: List[Lender]
    total: int
    limit: int
    offset: int


class DealsLongHoldResponse(TypedDict):
    data: List[LongHoldParcel]
    total: int
    limit: int
    offset: int


class DealsMarketResponseVariant1DataProvenance(TypedDict):
    dataset: str
    period_upper_bound: str
    returned_records: float
    oldest_record_refresh: Optional[str]
    newest_record_refresh: Optional[str]
    records_without_refresh: float
    source_vintage: Optional[str]
    basis: str


class DealsMarketResponseVariant1(TypedDict):
    data: List[MarketSummary]
    data_provenance: DealsMarketResponseVariant1DataProvenance
    total: int
    limit: int
    offset: int


class DealsMarketResponseVariant2(TypedDict, total=False):
    data: List[AffordabilityRow]
    total: int
    limit: int
    offset: int


class DealsPortfolioOwnersResponse(TypedDict):
    data: List[PortfolioOwner]
    total: int
    limit: int
    offset: int


class WebhooksListResponse(TypedDict):
    webhooks: List[Webhook]
    quota: WebhookQuota
    tier: Literal["free", "starter", "pro", "scale", "api_100k"]


class WebhooksDeleteResponse(TypedDict, total=False):
    deleted: str


class WebhooksDeliveriesResponse(TypedDict, total=False):
    deliveries: List[WebhookDelivery]


class ParcelsCompPackResponseSubject(TypedDict):
    canonical_id: str
    parcel_id: str
    state_fips: str
    county_fips: str
    total_assessed_value: int
    market_value: float
    building_sqft: Optional[float]
    property_type: str
    last_sale_price: Optional[float]
    last_sale_date: str


class ParcelsCompPackResponseQuotePrice(TypedDict):
    amount: str
    currency: str


class ParcelsCompPackResponseQuoteBreakdown(TypedDict):
    base: float
    V: float
    Q: float
    price_raw: float
    capped: bool


class ParcelsCompPackResponseQuote(TypedDict):
    price: ParcelsCompPackResponseQuotePrice
    price_usd: float
    price_atomic_usdc: str
    asset: str
    comp_count: int
    breakdown: ParcelsCompPackResponseQuoteBreakdown
    pay: List[Optional[str]]
    note: str


class ParcelsCompPackResponseSampleItem(TypedDict):
    comp_parcel_id: Optional[str]
    comp_apn: Optional[str]
    comp_address: Optional[str]
    comp_sale_price_approx: Optional[float]
    comp_sale_year: Optional[int]
    comp_sqft: Optional[float]
    comp_year_built: Optional[int]
    similarity_score: Optional[float]
    distance_miles: Optional[float]
    rank: Optional[int]


class ParcelsCompPackResponse(TypedDict):
    subject: ParcelsCompPackResponseSubject
    comp_count: int
    radius_miles: Optional[float]
    quote: ParcelsCompPackResponseQuote
    preview: bool
    sample: List[ParcelsCompPackResponseSampleItem]
    note: str


class ParcelsRiskScoreResponseSubject(TypedDict):
    canonical_id: str
    parcel_id: str
    state_fips: str
    county_fips: str
    total_assessed_value: int


class ParcelsRiskScoreResponseQuotePrice(TypedDict):
    amount: str
    currency: str


class ParcelsRiskScoreResponseQuoteBreakdown(TypedDict):
    base: float
    V: float
    C: float
    price_raw: float
    capped: bool


class ParcelsRiskScoreResponseQuote(TypedDict):
    price: ParcelsRiskScoreResponseQuotePrice
    price_usd: float
    price_atomic_usdc: str
    asset: str
    hazard_layers: float
    breakdown: ParcelsRiskScoreResponseQuoteBreakdown
    pay: List[Optional[str]]
    note: str


class ParcelsRiskScoreResponse(TypedDict):
    subject: ParcelsRiskScoreResponseSubject
    hazard_layers: List[Optional[str]]
    hazard_layer_count: int
    quote: ParcelsRiskScoreResponseQuote
    preview: bool
    note: str


class MarketFlipsResponse(TypedDict):
    data: List[MarketFlipsRow]
    total: int
    limit: int
    offset: int


class OwnersTransactionsResponse(TypedDict, total=False):
    data: List[OwnerTransaction]
    count: int


class StorefrontCatalogResponseSeal(TypedDict):
    """Content hash: two callers under the same seal get byte-identical numbers."""
    algorithm: str
    value: str
    covers: str


class StorefrontCatalogResponseDisclosuresWithheldFieldsItem(TypedDict):
    field: Optional[str]
    reason: Optional[str]
    withheld_on: Optional[str]
    note: Optional[str]


class StorefrontCatalogResponseDisclosuresReferenceCatalog(TypedDict):
    version: str
    seal: str


class StorefrontCatalogResponseDisclosuresFieldAdvisoriesItem(TypedDict):
    field: Optional[str]
    documented_at: Optional[str]
    evidence_source: Optional[str]
    evidence_scope: Optional[str]
    reference_catalog_version: Optional[str]
    reference_catalog_seal: Optional[str]
    reference_catalog_matches: Optional[bool]
    current_value_verified: Optional[bool]
    code: Optional[str]
    note: Optional[str]


class StorefrontCatalogResponseDisclosures(TypedDict):
    annotation_version: str
    seal_scope: str
    withheld_fields: List[StorefrontCatalogResponseDisclosuresWithheldFieldsItem]
    annotation_basis: str
    reference_catalog: StorefrontCatalogResponseDisclosuresReferenceCatalog
    reference_catalog_matches: bool
    catalog_published_at: str
    catalog_generated_at: str
    serving_epoch_match: str
    current_source_vintage: str
    freshness_scope: str
    coverage_scope: str
    pricing_scope: str
    applicability: str
    field_advisories: List[StorefrontCatalogResponseDisclosuresFieldAdvisoriesItem]


class StorefrontCatalogResponseMeasuredFromBaseline(TypedDict):
    source: str
    last_analyze: str
    note: str


class StorefrontCatalogResponseMeasuredFromParcelCountDefinitions(TypedDict):
    parcels: str
    mapped_locations: str
    geocoded_parcels: str
    rows: str


class StorefrontCatalogResponseMeasuredFrom(TypedDict):
    """National counts (distinct parcels, rows, mapped locations, geocoded parcels) each with the
    definition it was measured under.
    """
    relation: str
    schema: str
    parent: str
    parcels: float
    states: float
    method: str
    weight_source: str
    weights_reconcile_to_snapshot: bool
    manifest: str
    snapshot_watermark: str
    snapshot_swapped_at: str
    parity_status: str
    partition_analyze_min: str
    partition_analyze_max: str
    geocode_coverage: float
    sampling: str
    baseline: StorefrontCatalogResponseMeasuredFromBaseline
    parcel_counts_epoch: str
    mapped_locations: float
    geocoded_parcels: float
    rows: float
    parcel_count_definitions: StorefrontCatalogResponseMeasuredFromParcelCountDefinitions
    geocode_coverage_basis: str


class StorefrontCatalogResponseCountsByGrain(TypedDict):
    county: int
    parcel: float
    tract: float
    unknown: float
    zip: float


StorefrontCatalogResponseCountsCumulativeAt = TypedDict("StorefrontCatalogResponseCountsCumulativeAt", {"0.95": "float", "0.80": "float", "0.60": "float", "0.30": "float"}, total=False)


class StorefrontCatalogResponseCounts(TypedDict):
    columns: float
    sellable: float
    plumbing: float
    headline_parcel_grain_at_80: float
    red_cells: float
    epoch_regressions: float
    curation_review_required: float
    by_grain: StorefrontCatalogResponseCountsByGrain
    cumulative_at: StorefrontCatalogResponseCountsCumulativeAt
    withheld: float


class StorefrontCatalogResponseTiers(TypedDict):
    prime: float
    strong: float
    good: float
    partial: float
    sparse: float
    trace: float


class StorefrontCatalogResponseHeadline(TypedDict):
    floor: float
    parcel_grain_fields: float
    all_sellable_fields: float
    claim: str


class StorefrontCatalogResponseSectionsParcel(TypedDict):
    relation: str
    rows: float


class StorefrontCatalogResponseSectionsPermits(TypedDict):
    relation: str
    rows: float
    national_share: float


class StorefrontCatalogResponseSectionsDeeds(TypedDict):
    relation: str
    rows: float
    national_share: float


class StorefrontCatalogResponseSectionsComps(TypedDict):
    relation: str
    rows: float
    national_share: float


class StorefrontCatalogResponseSectionsGeometry(TypedDict):
    relation: str
    rows: float
    national_share: float


class StorefrontCatalogResponseSections(TypedDict):
    parcel: StorefrontCatalogResponseSectionsParcel
    permits: StorefrontCatalogResponseSectionsPermits
    deeds: StorefrontCatalogResponseSectionsDeeds
    comps: StorefrontCatalogResponseSectionsComps
    geometry: StorefrontCatalogResponseSectionsGeometry


class StorefrontCatalogResponsePricingDossier(TypedDict):
    amount: str
    currency: str


class StorefrontCatalogResponsePricingAddOnsItemPrice(TypedDict):
    amount: Optional[str]
    currency: Optional[str]


class StorefrontCatalogResponsePricingAddOnsItem(TypedDict):
    code: Optional[str]
    label: Optional[str]
    price: StorefrontCatalogResponsePricingAddOnsItemPrice
    purchasable: Optional[bool]
    note: Optional[str]


class StorefrontCatalogResponsePricing(TypedDict):
    """The dossier pricing model (base price, floor/cap, add-ons)."""
    dossier: StorefrontCatalogResponsePricingDossier
    add_ons: List[StorefrontCatalogResponsePricingAddOnsItem]
    catalog: str
    availability: str
    purchase_flow: str


class StorefrontCatalogResponseQuotePrice(TypedDict):
    amount: str
    currency: str


class StorefrontCatalogResponseQuoteAddOnsItemPrice(TypedDict):
    amount: Optional[str]
    currency: Optional[str]


class StorefrontCatalogResponseQuoteAddOnsItem(TypedDict):
    code: Optional[str]
    label: Optional[str]
    price: StorefrontCatalogResponseQuoteAddOnsItemPrice
    available: Optional[bool]
    purchasable: Optional[bool]
    note: Optional[str]


class StorefrontCatalogResponseQuote(TypedDict):
    """The base dossier quote derived from the pricing model. The per-parcel, value-tiered price is
    quoted by /storefront/availability?parcel_id=.
    """
    price: StorefrontCatalogResponseQuotePrice
    currency: str
    add_ons: List[StorefrontCatalogResponseQuoteAddOnsItem]
    pay: List[Any]
    purchase_flow: str


class StorefrontCatalogResponseWartsItem(TypedDict):
    dataset: Optional[str]
    surface: Optional[str]
    status: Optional[str]
    observed_max_date: Optional[str]
    age_days: Optional[float]
    max_age_days: Optional[int]
    probed_at: Optional[str]
    reason: Optional[str]


class StorefrontCatalogResponseFreshnessItem(TypedDict):
    dataset: Optional[str]
    surface: Optional[str]
    status: Optional[str]
    observed_max_date: Optional[str]
    age_days: Optional[float]
    max_age_days: Optional[int]
    probed_at: Optional[str]
    reason: Optional[str]


class StorefrontCatalogResponseAdvisoriesItemWorstAffectedItem(TypedDict):
    name: Optional[str]
    coverage: Optional[float]
    baseline_coverage: Optional[float]
    delta: Optional[float]


class _StorefrontCatalogResponseAdvisoriesItemRequired(TypedDict):
    code: Optional[str]
    severity: Optional[str]
    headline: Optional[str]
    cause: Optional[str]
    effect: Optional[str]
    remedy: Optional[str]


class StorefrontCatalogResponseAdvisoriesItem(_StorefrontCatalogResponseAdvisoriesItemRequired, total=False):
    worst_affected: List[StorefrontCatalogResponseAdvisoriesItemWorstAffectedItem]


class StorefrontCatalogResponseStateCoverage(TypedDict):
    address: float
    geocode: float
    owner: float
    value: float
    geometry: float


class StorefrontCatalogResponseStateWorstGapsItem(TypedDict):
    name: Optional[str]
    label: Optional[str]
    national: Optional[float]
    state: Optional[float]
    section: Optional[str]


class StorefrontCatalogResponseState(TypedDict):
    state_fips: str
    state: str
    counties: int
    parcels: float
    rollup_parcels: float
    share_of_national: float
    coverage: StorefrontCatalogResponseStateCoverage
    last_analyze: str
    worst_gaps: List[StorefrontCatalogResponseStateWorstGapsItem]


class StorefrontCatalogResponseFieldsItem(TypedDict):
    name: Optional[str]
    type: Optional[str]
    section: Optional[str]
    grain: Optional[str]
    category: Optional[str]
    sellable: Optional[bool]
    label: Optional[str]
    description: Optional[str]
    source: Optional[str]
    curated: Optional[bool]
    coverage: Optional[float]
    tier: Optional[str]
    baseline_coverage: Optional[float]
    coverage_delta: Optional[float]
    states_measured: Optional[float]
    states_with_any_coverage: Optional[float]
    n_distinct: Optional[float]
    flags: List[Optional[str]]
    red_cell: Optional[bool]
    headline_eligible: Optional[bool]
    curation_review_required: Optional[bool]
    source_as_of: Optional[str]
    source_as_of_basis: str
    catalog_published_at: Optional[str]
    catalog_generated_at: Optional[str]
    source_label_basis: str
    grain_basis: str
    catalog_description: Optional[str]
    historical_advisories: List[Any]
    state_coverage: Optional[float]


class StorefrontCatalogResponse(TypedDict):
    """The sealed field catalog. Additional top-level blocks (headline, sections, tiers, freshness,
    advisories, state_index, and an optional per-state `state` block) are present; the load-bearing
    ones are documented here.
    """
    contract_version: float
    catalog_version: str
    """The serving epoch this catalog was built for."""
    generated_at: str
    seal: StorefrontCatalogResponseSeal
    """Content hash: two callers under the same seal get byte-identical numbers."""
    disclosures: StorefrontCatalogResponseDisclosures
    measured_from: StorefrontCatalogResponseMeasuredFrom
    """National counts (distinct parcels, rows, mapped locations, geocoded parcels) each with the
    definition it was measured under.
    """
    counts: StorefrontCatalogResponseCounts
    tiers: StorefrontCatalogResponseTiers
    headline: StorefrontCatalogResponseHeadline
    sections: StorefrontCatalogResponseSections
    pricing: StorefrontCatalogResponsePricing
    """The dossier pricing model (base price, floor/cap, add-ons)."""
    quote: StorefrontCatalogResponseQuote
    """The base dossier quote derived from the pricing model. The per-parcel, value-tiered price is
    quoted by /storefront/availability?parcel_id=.
    """
    warts: List[StorefrontCatalogResponseWartsItem]
    """Every non-ok freshness probe, shipped rather than hidden (the honesty layer)."""
    freshness: List[StorefrontCatalogResponseFreshnessItem]
    advisories: List[StorefrontCatalogResponseAdvisoriesItem]
    state_index: List[Optional[Union[float, str]]]
    state: StorefrontCatalogResponseState
    field_count: int
    """Number of field entries returned after filters."""
    fields: List[StorefrontCatalogResponseFieldsItem]
    """The field dictionary: one entry per serving column with name, label, section, grain, tier,
    national (and optional per-state) coverage, and honesty flags.
    """


class StorefrontAvailabilityResponseSeal(TypedDict):
    algorithm: str
    value: str
    covers: str


class StorefrontAvailabilityResponseDisclosuresWithheldFieldsItem(TypedDict):
    field: Optional[str]
    reason: Optional[str]
    withheld_on: Optional[str]
    note: Optional[str]


class StorefrontAvailabilityResponseDisclosuresReferenceCatalog(TypedDict):
    version: str
    seal: str


class StorefrontAvailabilityResponseDisclosuresFieldAdvisoriesItem(TypedDict):
    field: Optional[str]
    documented_at: Optional[str]
    evidence_source: Optional[str]
    evidence_scope: Optional[str]
    reference_catalog_version: Optional[str]
    reference_catalog_seal: Optional[str]
    reference_catalog_matches: Optional[bool]
    current_value_verified: Optional[bool]
    code: Optional[str]
    note: Optional[str]


class StorefrontAvailabilityResponseDisclosures(TypedDict):
    annotation_version: str
    seal_scope: str
    withheld_fields: List[StorefrontAvailabilityResponseDisclosuresWithheldFieldsItem]
    annotation_basis: str
    reference_catalog: StorefrontAvailabilityResponseDisclosuresReferenceCatalog
    reference_catalog_matches: bool
    catalog_published_at: str
    catalog_generated_at: str
    serving_epoch_match: str
    current_source_vintage: str
    freshness_scope: str
    coverage_scope: str
    pricing_scope: str
    applicability: str
    field_advisories: List[StorefrontAvailabilityResponseDisclosuresFieldAdvisoriesItem]


class StorefrontAvailabilityResponseJurisdiction(TypedDict):
    """JURISDICTION mode: the state/county being described."""
    level: str
    state: str
    state_fips: str
    county_fips: str
    county_name: str
    parcels: float
    share_of_national: float
    counties: int
    last_analyze: str


class StorefrontAvailabilityResponseCoverageHeadlineFacts(TypedDict):
    address: float
    geocode: float
    owner: float
    value: float
    geometry: float


class StorefrontAvailabilityResponseCoverageNationalParcelCountDefinitions(TypedDict):
    parcels: str
    mapped_locations: str
    geocoded_parcels: str
    rows: str


class StorefrontAvailabilityResponseCoverageNational(TypedDict):
    parcel_counts_epoch: str
    parcels: float
    mapped_locations: float
    geocoded_parcels: float
    rows: float
    parcel_count_definitions: StorefrontAvailabilityResponseCoverageNationalParcelCountDefinitions


class StorefrontAvailabilityResponseCoverage(TypedDict):
    """JURISDICTION mode: headline coverage facts and parcel counts."""
    headline_facts: StorefrontAvailabilityResponseCoverageHeadlineFacts
    headline_facts_scope: str
    state_rollup_parcels: float
    state_ratified_parcels: float
    state_parcel_counts_unit: str
    national: StorefrontAvailabilityResponseCoverageNational
    national_parcels: float


StorefrontAvailabilityResponseFieldsNationalAtOrAbove = TypedDict("StorefrontAvailabilityResponseFieldsNationalAtOrAbove", {"0.95": "float", "0.80": "float", "0.60": "float", "0.30": "float"}, total=False)


class StorefrontAvailabilityResponseFieldsNationalTiers(TypedDict):
    prime: float
    strong: float
    good: float
    partial: float
    sparse: float
    trace: float


class StorefrontAvailabilityResponseFieldsNational(TypedDict):
    measured_fields: float
    unmeasured_fields: float
    at_or_above: StorefrontAvailabilityResponseFieldsNationalAtOrAbove
    tiers: StorefrontAvailabilityResponseFieldsNationalTiers
    red_cells: float
    red_cell_rule: str


class StorefrontAvailabilityResponseFields(TypedDict):
    """JURISDICTION mode: national vs in-jurisdiction field-coverage summaries."""
    sellable: float
    national: StorefrontAvailabilityResponseFieldsNational
    in_jurisdiction: Any
    """(Only null in observed responses.)"""
    county_field_resolution: str


class StorefrontAvailabilityResponseWorstGapsItem(TypedDict):
    name: Optional[str]
    label: Optional[str]
    national: Optional[float]
    state: Optional[float]
    section: Optional[str]


class StorefrontAvailabilityResponseQuotePrice(TypedDict):
    amount: str
    currency: str


class StorefrontAvailabilityResponseQuoteAddOnsItemPrice(TypedDict):
    amount: Optional[str]
    currency: Optional[str]


class StorefrontAvailabilityResponseQuoteAddOnsItem(TypedDict):
    code: Optional[str]
    label: Optional[str]
    price: StorefrontAvailabilityResponseQuoteAddOnsItemPrice
    available: Optional[bool]
    purchasable: Optional[bool]
    note: Optional[str]


class StorefrontAvailabilityResponseQuote(TypedDict):
    """JURISDICTION mode: the base dossier quote."""
    price: StorefrontAvailabilityResponseQuotePrice
    currency: str
    add_ons: List[StorefrontAvailabilityResponseQuoteAddOnsItem]
    pay: List[Any]
    purchase_flow: str


class StorefrontAvailabilityResponseWartsItem(TypedDict):
    dataset: Optional[str]
    surface: Optional[str]
    status: Optional[str]
    observed_max_date: Optional[str]
    age_days: Optional[float]
    max_age_days: Optional[int]
    probed_at: Optional[str]
    reason: Optional[str]


class StorefrontAvailabilityResponseCountiesRowsItemCoverage(TypedDict):
    address: Optional[float]
    geocode: Optional[float]
    owner: Optional[float]
    value: Optional[float]
    geometry: Optional[float]


class StorefrontAvailabilityResponseCountiesRowsItem(TypedDict):
    state_fips: str
    county_fips: str
    state: Optional[str]
    name: Optional[str]
    parcels: Optional[float]
    coverage: StorefrontAvailabilityResponseCountiesRowsItemCoverage


class StorefrontAvailabilityResponseCounties(TypedDict):
    """JURISDICTION mode: the state's counties by parcel count."""
    total: int
    returned: float
    rows: List[StorefrontAvailabilityResponseCountiesRowsItem]


class StorefrontAvailabilityResponseParcel(TypedDict):
    """PARCEL mode: the resolved parcel identity."""
    canonical_id: str
    state_fips: str
    county_fips: str
    county_fips_5: str
    parcel_id: str


class StorefrontAvailabilityResponseDossierQuoteBand(TypedDict):
    """Asset-class band (residential|multifamily|premium) derived from assessed value."""
    key: str
    label: str
    range: str


class StorefrontAvailabilityResponseDossierQuoteBreakdown(TypedDict):
    """The auditable multipliers: base, V (asset value), R (data richness), F (freshness)."""
    base: float
    V: float
    R: float
    F: float


class StorefrontAvailabilityResponseDossierQuoteSignals(TypedDict):
    """The cheap signals the multipliers were derived from."""
    assessed_value: float
    populated_fields: float
    has_deeds: bool
    has_permits: bool
    freshness: str


class StorefrontAvailabilityResponseDossierQuoteGeometryAddOnPrice(TypedDict):
    amount: str
    currency: str


class StorefrontAvailabilityResponseDossierQuoteGeometryAddOn(TypedDict):
    code: str
    label: str
    price: StorefrontAvailabilityResponseDossierQuoteGeometryAddOnPrice
    purchasable: bool


class StorefrontAvailabilityResponseDossierQuote(TypedDict):
    """PARCEL mode: the value-tiered quote for this parcel."""
    basis: str
    price: Money
    price_usd: float
    price_atomic_usdc: str
    """What the x402 402 advertises as maxAmountRequired (USDC atomic, 6dp)."""
    asset: str
    band: StorefrontAvailabilityResponseDossierQuoteBand
    """Asset-class band (residential|multifamily|premium) derived from assessed value."""
    breakdown: StorefrontAvailabilityResponseDossierQuoteBreakdown
    """The auditable multipliers: base, V (asset value), R (data richness), F (freshness)."""
    signals: StorefrontAvailabilityResponseDossierQuoteSignals
    """The cheap signals the multipliers were derived from."""
    geometry_add_on: StorefrontAvailabilityResponseDossierQuoteGeometryAddOn
    pay: List[Optional[str]]
    note: str


class _StorefrontAvailabilityResponseRequired(TypedDict):
    contract_version: float
    catalog_version: str
    generated_at: str
    seal: StorefrontAvailabilityResponseSeal
    disclosures: StorefrontAvailabilityResponseDisclosures


class StorefrontAvailabilityResponse(_StorefrontAvailabilityResponseRequired, total=False):
    """Shape depends on mode. Both carry contract_version, catalog_version, generated_at and seal.
    PARCEL mode adds mode='parcel', a `parcel` identity block, and `dossier_quote`; JURISDICTION
    mode adds `jurisdiction`, `coverage`, `fields`, `worst_gaps`, `quote`, `warts` and `counties`.
    """
    jurisdiction: StorefrontAvailabilityResponseJurisdiction
    """JURISDICTION mode: the state/county being described."""
    coverage: StorefrontAvailabilityResponseCoverage
    """JURISDICTION mode: headline coverage facts and parcel counts."""
    fields: StorefrontAvailabilityResponseFields
    """JURISDICTION mode: national vs in-jurisdiction field-coverage summaries."""
    worst_gaps: List[StorefrontAvailabilityResponseWorstGapsItem]
    quote: StorefrontAvailabilityResponseQuote
    """JURISDICTION mode: the base dossier quote."""
    warts: List[StorefrontAvailabilityResponseWartsItem]
    counties: StorefrontAvailabilityResponseCounties
    """JURISDICTION mode: the state's counties by parcel count."""
    mode: Literal["parcel"]
    """'parcel' in PARCEL mode; absent in JURISDICTION mode."""
    parcel: StorefrontAvailabilityResponseParcel
    """PARCEL mode: the resolved parcel identity."""
    dossier_quote: StorefrontAvailabilityResponseDossierQuote
    """PARCEL mode: the value-tiered quote for this parcel."""


class WatchCreateParamsFilter(TypedDict, total=False):
    """Exactly one shape: `{parcel_ids: [...]}` / `{canonical_ids: [...]}` (1-500 ids), `{state_fips}`
    or `{state_fips, county_fips}`.
    """
    parcel_ids: List[str]
    canonical_ids: List[str]
    state_fips: str
    county_fips: str


class WatchPollResponse(TypedDict, total=False):
    deltas: List[Dict[str, Any]]
    people_fields: PeopleFieldsWithheld


class VerifyGetResponseQuotePerLookup(TypedDict):
    amount: str
    currency: str


class VerifyGetResponseQuoteTotal(TypedDict):
    amount: str
    currency: str


class VerifyGetResponseQuoteBreakdown(TypedDict):
    per_lookup_usd: float
    total_raw: float
    capped: bool


class VerifyGetResponseQuote(TypedDict):
    per_lookup: VerifyGetResponseQuotePerLookup
    total: VerifyGetResponseQuoteTotal
    total_usd: float
    total_atomic_usdc: str
    asset: str
    lookup_count: int
    breakdown: VerifyGetResponseQuoteBreakdown
    pay: List[Optional[str]]
    note: str


class VerifyGetResponseProvenanceCatalogReferenceCatalogSeal(TypedDict):
    algorithm: str
    value: str
    covers: str


class VerifyGetResponseProvenanceCatalogReference(TypedDict):
    catalog_version: str
    catalog_generated_at: str
    catalog_seal: VerifyGetResponseProvenanceCatalogReferenceCatalogSeal


class VerifyGetResponseProvenance(TypedDict):
    source: str
    source_datasets: List[Optional[str]]
    as_of: Optional[str]
    as_of_basis: Optional[str]
    serving_epoch: Optional[str]
    freshness_status: str
    catalog_reference: VerifyGetResponseProvenanceCatalogReference
    note: str


class VerifyGetResponse(TypedDict):
    lookup_count: int
    parcel_count: int
    quote: VerifyGetResponseQuote
    provenance: VerifyGetResponseProvenance
    preview: bool
    note: str


class VerifyBatchParamsLookupsItem(TypedDict):
    parcel_id: str
    fields: List[str]


class VerifyBatchResponseQuotePerLookup(TypedDict):
    amount: str
    currency: str


class VerifyBatchResponseQuoteTotal(TypedDict):
    amount: str
    currency: str


class VerifyBatchResponseQuoteBreakdown(TypedDict):
    per_lookup_usd: float
    total_raw: float
    capped: bool


class VerifyBatchResponseQuote(TypedDict):
    per_lookup: VerifyBatchResponseQuotePerLookup
    total: VerifyBatchResponseQuoteTotal
    total_usd: float
    total_atomic_usdc: str
    asset: str
    lookup_count: int
    breakdown: VerifyBatchResponseQuoteBreakdown
    pay: List[Optional[str]]
    note: str


class VerifyBatchResponseProvenanceCatalogReferenceCatalogSeal(TypedDict):
    algorithm: str
    value: str
    covers: str


class VerifyBatchResponseProvenanceCatalogReference(TypedDict):
    catalog_version: str
    catalog_generated_at: str
    catalog_seal: VerifyBatchResponseProvenanceCatalogReferenceCatalogSeal


class VerifyBatchResponseProvenance(TypedDict):
    source: str
    source_datasets: List[Optional[str]]
    as_of: Optional[str]
    as_of_basis: Optional[str]
    serving_epoch: Optional[str]
    freshness_status: str
    catalog_reference: VerifyBatchResponseProvenanceCatalogReference
    note: str


class VerifyBatchResponse(TypedDict):
    lookup_count: int
    parcel_count: int
    quote: VerifyBatchResponseQuote
    provenance: VerifyBatchResponseProvenance
    preview: bool
    note: str


class LookupGetResponseParcel(TypedDict):
    id: str
    apn: Optional[str]
    county_fips: str
    state_fips: str
    address: Optional[str]
    city: Optional[str]
    zip: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    total_assessed_value: Optional[int]
    last_sale_price: Optional[float]
    land_use_code: Optional[str]
    owner_name: Optional[str]


class LookupGetResponse(TypedDict):
    found: Optional[bool]
    query: Optional[str]
    parcel: LookupGetResponseParcel


class LookupBatchResponseItemsItemParcelLastSale(TypedDict):
    date: Optional[str]
    price: Optional[float]


class LookupBatchResponseItemsItemParcel(TypedDict):
    id: str
    apn: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    county_fips: str
    state_fips: str
    owner_name: Optional[str]
    land_value: Optional[float]
    improvement_value: Optional[float]
    total_assessed_value: Optional[int]
    last_sale: LookupBatchResponseItemsItemParcelLastSale
    permits: Any
    """(Only null in observed responses.)"""
    hazard_score: Optional[float]
    latitude: Optional[float]
    longitude: Optional[float]
    has_geometry: Optional[bool]


class LookupBatchResponseItemsItem(TypedDict):
    query: Optional[str]
    match_type: Optional[str]
    parcel: Optional[LookupBatchResponseItemsItemParcel]


class LookupBatchResponse(TypedDict):
    items: List[LookupBatchResponseItemsItem]
    lookups_charged: float
    unavailable_fields: List[Optional[str]]
    tier: str
    notice: str


class ParcelsBatchParamsTuplesItem(TypedDict):
    state_fips: str
    county_fips: str
    parcel_id: str


class ParcelsBatchResponseRowsItem(TypedDict):
    id: str
    county_fips: str
    state_fips: str
    parcel_id: str
    address: Optional[str]
    normalized_address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    zip5: Optional[str]
    zip_plus4: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    land_use_code: Optional[str]
    land_use_desc: Optional[str]
    total_assessed_value: Optional[float]
    land_assessed_value: Optional[float]
    improvement_assessed_value: Optional[float]
    last_sale_price: Optional[float]
    last_sale_date: Optional[str]
    market_value: Optional[float]
    avm_value: Optional[float]
    avm_confidence: Optional[str]
    avm_method: Optional[str]
    tax_amount: Optional[float]
    tax_year: Optional[int]
    deal_score: Optional[float]
    price_per_sqft: Optional[float]
    building_sqft: Optional[float]
    year_built: Optional[int]
    lot_size_acres: Optional[float]
    lot_size_sqft: Optional[float]
    bedrooms: Optional[int]
    bathrooms: Optional[float]
    stories: Optional[float]
    units: Optional[int]
    unit_count: Optional[int]
    construction_type: Optional[str]
    owner_name: Optional[str]
    owner_address: Optional[str]
    owner_city: Optional[str]
    owner_state: Optional[str]
    owner_zip: Optional[str]
    ownership_type: Optional[str]
    owner_entity_type: Optional[str]
    entity_type: Optional[str]
    is_entity_owned: Optional[bool]
    is_absentee: Optional[bool]
    is_pe_aggregator: Optional[bool]
    owner_occupied_flag: Optional[bool]
    data_quality_score: Optional[float]
    flood_zone: Optional[str]
    is_sfha: Optional[bool]
    is_opportunity_zone: Optional[bool]
    is_justice40: Optional[bool]
    is_flip: Optional[bool]
    crime_score: Optional[float]
    crime_tier: Optional[float]
    deed_count: Optional[int]
    permit_count: Optional[int]
    permit_count_12mo: Optional[int]
    zoning: Optional[str]
    zoning_code_raw: Optional[str]
    county_name: Optional[str]
    property_type: Optional[str]


class ParcelsBatchResponse(TypedDict):
    rows: List[ParcelsBatchResponseRowsItem]
    missing: List[Any]


class ParcelsCompsResponseSubject(TypedDict):
    canonical_id: str
    parcel_id: str
    state_fips: str
    county_fips: str


class ParcelsCompsResponseCompsItem(TypedDict):
    comp_parcel_id: Optional[str]
    comp_apn: Optional[str]
    comp_sale_price: Optional[float]
    comp_sale_date: Optional[str]
    comp_address: Optional[str]
    comp_sqft: Optional[float]
    comp_year_built: Optional[int]
    comp_beds: Optional[float]
    comp_baths: Optional[float]
    similarity_score: Optional[float]
    distance_miles: Optional[float]
    rank: Optional[int]
    sale_price_reconciled: Optional[bool]


class ParcelsCompsResponseProvenanceGateScope(TypedDict):
    state_fips: str
    county_fips: str


class ParcelsCompsResponseProvenanceGate(TypedDict):
    applied: bool
    rule: str
    scope: ParcelsCompsResponseProvenanceGateScope
    comps_reconciled: float
    reason: Optional[str]
    note: Optional[str]


class ParcelsCompsResponse(TypedDict):
    subject: ParcelsCompsResponseSubject
    tier: str
    radius_miles: Optional[float]
    count: int
    comps: List[ParcelsCompsResponseCompsItem]
    provenance_gate: ParcelsCompsResponseProvenanceGate


class ParcelsOccupantsResponseOccupantsItem(TypedDict):
    occupant_id: Optional[str]
    name_raw: Optional[str]
    name_norm: Optional[str]
    brand_name: Optional[str]
    brand_wikidata: Optional[str]
    category_fsq: Optional[str]
    naics: Optional[str]
    confidence: Optional[float]
    status: Optional[str]
    is_primary: Optional[bool]
    match_method: Optional[str]
    match_distance_m: Optional[float]
    source_count: Optional[int]
    first_seen: Optional[str]
    last_seen: Optional[str]
    occupant_lat: Optional[float]
    occupant_lon: Optional[float]
    lu_class: Optional[str]


class ParcelsOccupantsResponse(TypedDict):
    parcel_id: str
    occupant_count: int
    occupants: List[ParcelsOccupantsResponseOccupantsItem]
    truncated: bool


class ParcelsViolationsResponsePlace(TypedDict):
    place_geoid: Optional[str]
    place_name: Optional[str]


class ParcelsViolationsResponseSummary(TypedDict):
    open_count: int
    closed_count: int
    other_count: int
    unknown_status_count: int
    unmapped_status_count: int
    latest_issued_date: Optional[str]
    latest_status: Optional[str]
    oldest_open_issued_date: Optional[str]
    has_open_code_violation: Optional[bool]


class ParcelsViolationsResponseWithheld(TypedDict):
    outside_publisher_area: float
    account_only_fields: List[Any]


class ParcelsViolationsResponseCoveredJurisdictionsItem(TypedDict):
    source_id: Optional[str]
    state_fips: str
    county_fips: str
    place_geoid: Optional[str]
    place_name: Optional[str]
    publisher: Optional[str]


class ParcelsViolationsResponse(TypedDict):
    data: List[Any]
    violation_count: int
    violation_count_basis: str
    truncated: bool
    row_cap: int
    coverage: str
    coverage_reason: str
    place: ParcelsViolationsResponsePlace
    sources: List[Any]
    summary: ParcelsViolationsResponseSummary
    withheld: ParcelsViolationsResponseWithheld
    covered_jurisdictions: List[ParcelsViolationsResponseCoveredJurisdictionsItem]
    notes: List[Optional[str]]


class ParcelsPoisResponse(TypedDict):
    data: List[Any]


class MarketSnapshotResponseGeo(TypedDict):
    scope: Optional[str]
    value: Optional[float]
    state_fips: str
    county_fips: str
    county_name: Optional[str]
    state: Optional[str]
    cbsa_code: Optional[str]
    census_tract: Optional[str]
    zip5: Optional[str]
    geo_basis: str
    geo_basis_withheld: List[Optional[str]]


class MarketSnapshotResponseDemographicsDemographicsBasisGrain(TypedDict):
    acs_median_hh_income: Optional[str]
    acs_median_home_value: Optional[str]
    acs_median_rent: Optional[str]
    acs_median_year_built: Optional[str]
    acs_bachelors_plus_pct: Optional[str]
    acs_owner_occupied_pct: Optional[str]
    acs_poverty_pct: Optional[str]
    acs_vacant_housing_pct: Optional[str]
    acs_age_65plus_pct: Optional[str]
    acs_broadband_pct: Optional[str]
    acs_mean_commute_minutes: Optional[str]
    acs_long_commute_pct: Optional[str]
    tract_population: Optional[str]
    tract_median_home_value: Optional[str]
    tract_median_rent: Optional[str]
    tract_owner_occupied_pct: Optional[str]
    tract_vacancy_rate: Optional[str]
    tract_poverty_rate: Optional[str]
    tract_college_educated_pct: Optional[str]
    tract_avg_income: Optional[str]


class MarketSnapshotResponseDemographics(TypedDict):
    acs_median_hh_income: Optional[float]
    acs_median_home_value: Optional[float]
    acs_median_rent: Optional[float]
    acs_median_year_built: Optional[float]
    acs_bachelors_plus_pct: Optional[float]
    acs_owner_occupied_pct: Optional[float]
    acs_poverty_pct: Optional[float]
    acs_vacant_housing_pct: Optional[float]
    acs_age_65plus_pct: Optional[float]
    acs_broadband_pct: Optional[float]
    acs_mean_commute_minutes: Optional[float]
    acs_long_commute_pct: Optional[float]
    tract_population: Optional[str]
    tract_median_home_value: Optional[str]
    tract_median_rent: Optional[str]
    tract_owner_occupied_pct: Optional[str]
    tract_vacancy_rate: Optional[str]
    tract_poverty_rate: Optional[str]
    tract_college_educated_pct: Optional[str]
    tract_avg_income: Optional[str]
    demographics_basis: str
    demographics_basis_withheld: List[Optional[str]]
    demographics_basis_grain: MarketSnapshotResponseDemographicsDemographicsBasisGrain


class MarketSnapshotResponseEconomyEconomyBasisGrain(TypedDict):
    county_employment: Optional[str]
    county_unemployment_rate: Optional[str]
    county_total_employees: Optional[str]
    county_total_establishments: Optional[str]
    lodes_jobs_total: Optional[str]
    lodes_jobs_high_wage: Optional[str]
    lodes_jobs_mid_wage: Optional[str]
    lodes_jobs_low_wage: Optional[str]
    lodes_jobs_healthcare: Optional[str]
    lodes_jobs_manufacturing: Optional[str]
    lodes_jobs_retail: Optional[str]
    lodes_jobs_education: Optional[str]
    lodes_jobs_hospitality: Optional[str]
    tract_total_jobs: Optional[str]
    tract_jobs_density_per_sqmi: Optional[str]
    tract_high_wage_pct: Optional[str]
    tract_healthcare_jobs_pct: Optional[str]


class MarketSnapshotResponseEconomy(TypedDict):
    bea_gdp_2024_thousands: Optional[float]
    bea_gdp_2023_thousands: Optional[float]
    bea_gdp_5y_growth_pct: Optional[float]
    bea_gdp_10y_growth_pct: Optional[float]
    bea_gdp_20y_growth_pct: Optional[float]
    bea_pcpi_2024: Optional[float]
    bea_pcpi_5y_growth_pct: Optional[float]
    bea_personal_income_thousands_2024: Optional[float]
    bea_population_2024: Optional[float]
    county_employment: Optional[float]
    county_unemployment_rate: Optional[float]
    county_total_employees: Optional[float]
    county_total_establishments: Optional[float]
    county_median_income_irs: Optional[int]
    county_affordability_ratio: Optional[float]
    county_affordability_rating: Optional[str]
    lodes_jobs_total: Optional[float]
    lodes_jobs_high_wage: Optional[float]
    lodes_jobs_mid_wage: Optional[float]
    lodes_jobs_low_wage: Optional[float]
    lodes_jobs_healthcare: Optional[float]
    lodes_jobs_manufacturing: Optional[float]
    lodes_jobs_retail: Optional[float]
    lodes_jobs_education: Optional[float]
    lodes_jobs_hospitality: Optional[float]
    tract_total_jobs: Optional[str]
    tract_jobs_density_per_sqmi: Optional[str]
    tract_high_wage_pct: Optional[str]
    tract_healthcare_jobs_pct: Optional[str]
    economy_basis: str
    economy_basis_withheld: List[Optional[str]]
    economy_basis_grain: MarketSnapshotResponseEconomyEconomyBasisGrain


class MarketSnapshotResponseHousingHousingBasisGrain(TypedDict):
    fhfa_hpi_latest: Optional[str]
    fhfa_hpi_year: Optional[str]
    fhfa_hpi_1y_change_pct: Optional[str]
    fhfa_hpi_5y_change_pct: Optional[str]
    fhfa_hpi_10y_change_pct: Optional[str]
    fhfa_hpi_20y_change_pct: Optional[str]


class MarketSnapshotResponseHousing(TypedDict):
    bps_total_units_2024: Optional[float]
    bps_total_units_2023: Optional[float]
    bps_total_value_2024: Optional[float]
    bps_sf_units_2024: Optional[float]
    bps_sf_value_2024: Optional[float]
    bps_mf_units_2024: Optional[float]
    bps_mf_value_2024: Optional[float]
    bps_yoy_unit_growth_pct: Optional[float]
    fhfa_hpi_latest: Optional[float]
    fhfa_hpi_year: Optional[int]
    fhfa_hpi_1y_change_pct: Optional[float]
    fhfa_hpi_5y_change_pct: Optional[float]
    fhfa_hpi_10y_change_pct: Optional[float]
    fhfa_hpi_20y_change_pct: Optional[float]
    housing_basis: str
    housing_basis_withheld: List[Optional[str]]
    housing_basis_grain: MarketSnapshotResponseHousingHousingBasisGrain


class MarketSnapshotResponseLendingLendingBasisGrain(TypedDict):
    hmda_orig_count: Optional[str]
    hmda_orig_volume_thousands: Optional[str]
    hmda_avg_loan_amount_thousands: Optional[str]
    hmda_avg_interest_rate: Optional[str]
    hmda_avg_ltv: Optional[str]
    hmda_conv_count: Optional[str]
    hmda_fha_count: Optional[str]
    hmda_va_count: Optional[str]
    hmda_usda_count: Optional[str]
    tract_loan_originations: Optional[str]
    tract_avg_loan_amount: Optional[str]
    tract_avg_interest_rate: Optional[str]
    tract_fha_pct: Optional[str]
    tract_investor_pct: Optional[str]
    tract_credit_risk_tier: Optional[str]
    tract_flood_claims: Optional[str]
    tract_flood_loss_ratio: Optional[str]


class MarketSnapshotResponseLending(TypedDict):
    hmda_orig_count: Optional[float]
    hmda_orig_volume_thousands: Optional[float]
    hmda_avg_loan_amount_thousands: Optional[float]
    hmda_avg_interest_rate: Optional[float]
    hmda_avg_ltv: Optional[float]
    hmda_conv_count: Optional[float]
    hmda_fha_count: Optional[float]
    hmda_va_count: Optional[float]
    hmda_usda_count: Optional[float]
    tract_loan_originations: Optional[str]
    tract_avg_loan_amount: Optional[str]
    tract_avg_interest_rate: Optional[str]
    tract_fha_pct: Optional[str]
    tract_investor_pct: Optional[str]
    tract_credit_risk_tier: Optional[str]
    tract_flood_claims: Optional[str]
    tract_flood_loss_ratio: Optional[str]
    lending_basis: str
    lending_basis_withheld: List[Optional[str]]
    lending_basis_grain: MarketSnapshotResponseLendingLendingBasisGrain


class MarketSnapshotResponseHazardHazardBasisGrain(TypedDict):
    fema_policy_count: Optional[str]
    county_violent_crime_rate: Optional[str]
    county_property_crime_rate: Optional[str]


class MarketSnapshotResponseHazard(TypedDict):
    fema_disaster_count: Optional[int]
    fema_disaster_count_10y: Optional[int]
    fema_flood_count: Optional[int]
    fema_fire_count: Optional[int]
    fema_hurricane_count: Optional[int]
    fema_tornado_count: Optional[int]
    fema_earthquake_count: Optional[int]
    fema_sev_storm_count: Optional[int]
    fema_biological_count: Optional[int]
    fema_ia_declarations: Optional[float]
    fema_pa_declarations: Optional[float]
    fema_policy_count: Optional[float]
    fema_top_incident_type: Optional[str]
    fema_latest_declaration_date: Optional[str]
    county_violent_crime_rate: Optional[float]
    county_property_crime_rate: Optional[float]
    hazard_basis: str
    hazard_basis_withheld: List[Optional[str]]
    hazard_basis_grain: MarketSnapshotResponseHazardHazardBasisGrain


class MarketSnapshotResponseHealthcareHealthcareBasisGrain(TypedDict):
    cms_hosp_count: Optional[str]
    cms_hosp_avg_stars: Optional[str]
    cms_hosp_4_5_star: Optional[str]
    cms_hosp_with_er: Optional[str]
    cms_nh_count: Optional[str]
    cms_nh_beds: Optional[str]
    cms_nh_avg_stars: Optional[str]
    cms_nh_4_5_star: Optional[str]
    cms_nh_1_2_star: Optional[str]
    cms_hospice_count: Optional[str]
    cms_hh_count: Optional[str]


class MarketSnapshotResponseHealthcare(TypedDict):
    cms_hosp_count: Optional[float]
    cms_hosp_avg_stars: Optional[float]
    cms_hosp_4_5_star: Optional[float]
    cms_hosp_with_er: Optional[float]
    cms_nh_count: Optional[float]
    cms_nh_beds: Optional[float]
    cms_nh_avg_stars: Optional[float]
    cms_nh_4_5_star: Optional[float]
    cms_nh_1_2_star: Optional[float]
    cms_hospice_count: Optional[float]
    cms_hh_count: Optional[float]
    healthcare_basis: str
    healthcare_basis_withheld: List[Optional[str]]
    healthcare_basis_grain: MarketSnapshotResponseHealthcareHealthcareBasisGrain


class MarketSnapshotResponseMarketProvenance(TypedDict):
    dataset: Optional[str]
    period_upper_bound: Optional[str]
    returned_records: Optional[float]
    oldest_record_refresh: Optional[str]
    newest_record_refresh: Optional[str]
    records_without_refresh: Optional[float]
    source_vintage: Optional[str]
    basis: Optional[str]


class MarketSnapshotResponse(TypedDict):
    geo: MarketSnapshotResponseGeo
    demographics: MarketSnapshotResponseDemographics
    economy: MarketSnapshotResponseEconomy
    housing: MarketSnapshotResponseHousing
    lending: MarketSnapshotResponseLending
    hazard: MarketSnapshotResponseHazard
    healthcare: MarketSnapshotResponseHealthcare
    market: Optional[Dict[str, Any]]
    market_history: List[Any]
    market_provenance: MarketSnapshotResponseMarketProvenance
    generated_at: Optional[str]
    _guards: List[str]


class CmbsExposureResponseSubject(TypedDict):
    canonical_id: str
    parcel_id: str
    state_fips: str
    county_fips: str


class CmbsExposureResponseDataAsOf(TypedDict):
    snapshot_assembled: Optional[str]
    figures_as_of: Optional[str]
    refreshed_since: Optional[bool]
    statement: Optional[str]
    source: Optional[str]


class CmbsExposureResponseCoverageEdgarRoster(TypedDict):
    reporting_month: Optional[str]
    cmbs_trusts_filing_abs_ee: Optional[float]
    of_which_served: Optional[float]
    measured_on: Optional[str]


class CmbsExposureResponseCoverageExcluded(TypedDict):
    non_cmbs_trusts: Optional[float]
    non_cmbs_note: Optional[str]
    depositor_ciks: Optional[float]
    depositor_note: Optional[str]
    property_rows_stored_as_loans: Optional[float]
    unverified_ciks: Optional[float]


class CmbsExposureResponseCoverage(TypedDict):
    scope: Optional[str]
    trusts: Optional[float]
    loans: Optional[float]
    properties: Optional[float]
    counts_source: Optional[str]
    edgar_roster: CmbsExposureResponseCoverageEdgarRoster
    excluded: CmbsExposureResponseCoverageExcluded
    not_covered: List[Optional[str]]


class CmbsExposureResponseFieldStatusProperties(TypedDict):
    loan_id: Optional[str]
    appraised_value: Optional[str]
    allocated_loan_amount: Optional[str]
    current_noi: Optional[str]
    current_occupancy: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    matched_parcel_id: Optional[str]


class CmbsExposureResponseFieldStatus(TypedDict):
    is_specially_serviced: Optional[str]
    is_on_watchlist: Optional[str]
    is_interest_only: Optional[str]
    borrower_name: Optional[str]
    sponsor_name: Optional[str]
    loan_type: Optional[str]
    payment_status: Optional[str]
    note_rate: Optional[str]
    current_balance: Optional[str]
    uw_dscr: Optional[str]
    uw_ltv: Optional[str]
    uw_occupancy: Optional[str]
    uw_noi: Optional[str]
    appraised_value: Optional[str]
    current_dscr: Optional[str]
    current_ltv: Optional[str]
    current_occupancy: Optional[str]
    current_noi: Optional[str]
    current_debt_yield: Optional[str]
    properties: CmbsExposureResponseFieldStatusProperties


class CmbsExposureResponse(TypedDict):
    mode: Optional[str]
    matched: Optional[bool]
    reason: Optional[str]
    subject: CmbsExposureResponseSubject
    note: Optional[str]
    loans: List[Any]
    properties: List[Any]
    data_as_of: CmbsExposureResponseDataAsOf
    coverage: CmbsExposureResponseCoverage
    field_status: CmbsExposureResponseFieldStatus


class FreshnessGetResponse(TypedDict):
    content_as_of: str
    last_enriched_at: str
    content_date_basis: str
    content_date_note: str
    content_median_date: str
    content_max_date: str
    content_oldest_date: str
    content_source_count: int
    content_active_source_count: int
    swapped_at: str
    updated_at: str
    snapshot_built_at: str
    parcel_count: int


class FreshnessDatasetsResponseDatasetsItemRefresh(TypedDict):
    source_watermark: Optional[str]
    source_age_hours: Optional[float]
    evaluated_at: Optional[str]
    published_at: Optional[str]
    status: Optional[str]
    warning_reason: Optional[str]


class FreshnessDatasetsResponseDatasetsItemRecordActivity(TypedDict):
    latest_at: Optional[str]
    evaluated_at: Optional[str]
    basis: Optional[str]
    age_hours: Optional[float]
    max_age_hours: Optional[float]
    status: Optional[str]


class FreshnessDatasetsResponseDatasetsItemCoverage(TypedDict):
    status: Optional[str]
    unit: Optional[str]
    covered: Optional[float]
    as_of: Optional[str]


class FreshnessDatasetsResponseDatasetsItem(TypedDict):
    dataset: Optional[str]
    availability: Optional[str]
    freshness: Optional[str]
    freshness_reason: Optional[str]
    refresh: FreshnessDatasetsResponseDatasetsItemRefresh
    record_activity: FreshnessDatasetsResponseDatasetsItemRecordActivity
    coverage: FreshnessDatasetsResponseDatasetsItemCoverage


class FreshnessDatasetsResponse(TypedDict):
    contract_version: float
    generated_at: str
    status: str
    datasets: List[FreshnessDatasetsResponseDatasetsItem]


class CoverageMapResponseMetaTotals(TypedDict):
    parcels: float
    with_owner: float
    with_address: float
    with_geometry: float
    with_value: float
    counties: int


class CoverageMapResponseMeta(TypedDict):
    epoch: str
    generated_at: str
    totals: CoverageMapResponseMetaTotals


class CoverageMapResponseCountiesItem(TypedDict):
    s: Optional[str]
    c: Optional[Union[float, str]]
    nm: Optional[str]
    n: Optional[int]
    o: Optional[float]
    a: Optional[float]
    g: Optional[float]
    v: Optional[float]
    lat: Optional[float]
    lon: Optional[float]


class CoverageMapResponse(TypedDict):
    meta: CoverageMapResponseMeta
    counties: List[CoverageMapResponseCountiesItem]


class CrimeLookupResponseCrime(TypedDict):
    crime_score: Optional[float]
    crime_tier: Optional[float]
    crime_trend: Optional[str]
    county_violent_crime_rate: Optional[float]
    county_property_crime_rate: Optional[float]


class CrimeLookupResponse(TypedDict):
    crime: CrimeLookupResponseCrime


class TrafficStationsResponseDataItem(TypedDict):
    lat: Optional[float]
    lng: Optional[float]
    aadt: Optional[float]
    route: Optional[str]


class TrafficStationsResponse(TypedDict):
    data: List[TrafficStationsResponseDataItem]


class CohortsListResponseCohortsItem(TypedDict):
    id: str
    name: Optional[str]
    color: Optional[str]
    created_at: Optional[str]
    parcel_count: Optional[int]
    total_value: Optional[int]


class CohortsListResponse(TypedDict):
    cohorts: List[CohortsListResponseCohortsItem]


Error = Problem
WebhookFilter = Union[WebhookFilterVariant1, WebhookFilterVariant2, WebhookFilterVariant3]
ParcelsGetResponse = Parcel
ParcelsPermitsResponse = Union[List[Permit], ParcelsPermitsResponseVariant2]
ParcelsDeedsResponse = Union[List[Deed], ParcelsDeedsResponseVariant2]
ParcelsRisksResponse = RiskAssessment
OwnersGetResponse = Owner
DealsEntitiesResponse = Union[DealsEntitiesResponseVariant1, DealsEntitiesResponseVariant2]
DealsMarketResponse = Union[DealsMarketResponseVariant1, DealsMarketResponseVariant2]
WebhooksCreateResponse = WebhookCreated
WebhooksGetResponse = Webhook
SearchAutocompleteResponse = AutocompleteResult
SearchExportResponse = str
SearchFullResponse = FullSearchResult
ParcelsGeojsonResponse = ParcelGeoJSON
ParcelsReportResponse = ParcelDossier
ParcelsTrafficHistoryResponse = TrafficStationHistory
MarketCountyResponse = CountyDetail
AccountUsageResponse = AccountUsage
LeadsFindResponse = Union[LeadFeedPreview, LeadFeed]
CreditsTopupResponse = Dict[str, Any]
CreditsBalanceResponse = Dict[str, Any]
WatchListResponse = Dict[str, Any]
WatchCreateResponse = Dict[str, Any]
WatchDeleteResponse = Dict[str, Any]
OwnersCardResponse = OwnerCard
CohortsExportResponse = Union[str, Dict[str, Any]]
WebhooksRetryDeliveryResponse = Any
