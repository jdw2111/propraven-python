"""Run all four examples: python -m examples.run --mock."""

from . import coverage, parcel, search, storefront
from ._runtime import main


def run(client):
    return {module.__name__.split(".")[-1]: module.run(client) for module in (search, parcel, coverage, storefront)}


if __name__ == "__main__":
    main(run)
