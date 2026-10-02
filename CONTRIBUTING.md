# Contributing

## Setup

```sh
uv venv && uv pip install -e . pytest pytest-asyncio ruff
# or: python -m venv .venv && .venv/bin/pip install -e . pytest pytest-asyncio ruff
```

## Layout

- `src/propraven/_client.py`, `_transport.py`, `_errors.py`, `_pagination.py`, `webhooks.py`:
  the hand-written core (edit freely).
- `src/propraven/types/__init__.py`, `src/propraven/resources/*.py`, and the method table in
  `README.md`: **generated** from `openapi.json` by `scripts/generate.py`. Do not edit them by hand.

## Regenerating

```sh
cp /path/to/new/openapi.json openapi.json   # or: curl -fsSL https://propraven.com/openapi.json -o openapi.json
python scripts/generate.py
python -m pytest -q
```

CI runs `python scripts/generate.py --check`, which fails when generated files are stale.

## Checks

```sh
python -m pytest -q
ruff check src tests scripts && ruff format --check src tests scripts
uv build && uvx twine check dist/*
```

`scripts/live_smoke.py` exercises the real API (at most 12 requests, read-only). It needs
`PROPRAVEN_API_KEY` and is never run in CI.

## Releasing

Bump `version` in `pyproject.toml` and `__version__` in `src/propraven/_version.py`, add a
`CHANGELOG.md` entry, merge, then publish a GitHub release. `.github/workflows/publish-pypi.yml`
publishes to PyPI through trusted publishing (`bin/publish-pypi`), and refuses to publish a version
that is already on PyPI.
