"""Search a street address, then a geographic bounding box."""

from ._runtime import main


def run(client):
    text = client.search.full(q="123 Main St", field="address", state="NC", limit=5)
    bounded = client.search.parcels(
        bounds={"north": 35.215, "south": 35.205, "east": -80.855, "west": -80.865},
        filters={"valueRange": {"min": 100000}},
        limit=50,
    )
    return {
        "address_results": [{"parcel_id": r["parcel_id"], "address": r["site_address"]} for r in text["results"]],
        "bounds_results": [{"parcel_id": r["parcel_id"], "address": r["address"]} for r in bounded["data"]],
        "bounds_total": bounded["total"],
        "bounds_has_more": bounded["has_more"],
    }


if __name__ == "__main__":
    main(run)
