"""Read the free catalog and availability; no purchase or payment calls."""

from ._runtime import main


def run(client):
    catalog = client.storefront.catalog(state="NC", fields="none")
    availability = client.storefront.availability(state="NC", county="37183")
    return {
        "catalog_version": catalog["catalog_version"],
        "availability_catalog_version": availability["catalog_version"],
        "availability_disclosures": availability["disclosures"],
    }


if __name__ == "__main__":
    main(run)
