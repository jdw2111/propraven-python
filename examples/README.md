# Python examples

From a checkout:

```sh
python -m pip install -e .
python -m examples.run --mock
```

Run one example with `python -m examples.search --mock`, `python -m examples.parcel --mock`, `python -m examples.coverage --mock`, or `python -m examples.storefront --mock`. Python 3.9+ is supported. For local checks, install `pytest pytest-asyncio jsonschema ruff` and run `python -m pytest -q` plus `ruff check src tests scripts examples`.

These are illustrative, schema-derived recordings, not captured production data or current coverage claims. Each response records its JSON Pointer and the digest of the resolved response schema. Values come from `public/openapi.json` in `jdw2111/propzilla` at `93a4c8048888f8049cdd65894f610e2247575021`; the six response schemas also match this SDK's checked-in spec. Required fields without examples use explicitly synthetic constants, nulls, zero/false, or empty arrays. Owner/contact values are null. The schema's sample location fields are not a verified, internally consistent parcel geography.

All four examples use the SDK's public methods: address search (`field=address`), bounding-box search, one parcel, state coverage, and free storefront catalog/availability. They print selected non-person fields and make no purchase, credit, payment, owner, or contact calls. Mock mode is the default, ignores ambient credentials/base URLs, serves six exact method/path/query/body recordings in memory, and refuses unknown requests without any network fallback.

`--live` explicitly opts into normal SDK configuration and real requests. It is never used in tests or CI. A live example may require an API key for the chosen endpoint; use the documented environment variable, not a key in source.

CI validates each recording against the upstream response schema, checks the request parameters and keyless transport, runs all examples in mock mode, and executes the real generator on a temporary copy with an intentionally changed spec. That last test verifies that regeneration changes generated output while preserving every file in `examples/`. Schema drift fails the recording digest check until the examples are reviewed. No generated source, version, release, tag, or publish workflow changes are included.
