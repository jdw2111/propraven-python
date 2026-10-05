"""Read county coverage within a state (37 = North Carolina)."""

from ._runtime import main


def run(client):
    result = client.coverage.get(state="37")
    return [{key: row.get(key) for key in ("state_fips", "county_fips", "parcel_count", "last_updated")}
            for row in result["data"]]


if __name__ == "__main__":
    main(run)
