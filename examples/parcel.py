"""Get one parcel using the OpenAPI's composite-identifier example."""

from ._runtime import main


def run(client):
    row = client.parcels.get("37:119:12104406")
    return {key: row.get(key) for key in ("parcel_id", "address", "zoning", "year_built")}


if __name__ == "__main__":
    main(run)
