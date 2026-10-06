from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import httpx
import pytest
from jsonschema import Draft202012Validator

from examples import run
from examples._runtime import FIXTURE, Replay, client_context

ROOT = Path(__file__).resolve().parents[1]
SPEC = json.loads((ROOT / "openapi.json").read_text())
RECORDS = json.loads(FIXTURE.read_text())["records"]


def pointer(root, path):
    for part in path.removeprefix("/").split("/"):
        root = root[part.replace("~1", "/").replace("~0", "~")]
    return root


def resolved(value):
    if isinstance(value, list):
        return [resolved(v) for v in value]
    if not isinstance(value, dict):
        return value
    if "$ref" in value:
        return resolved(pointer(SPEC, value["$ref"][1:]))
    return {k: resolved(v) for k, v in value.items()}


@pytest.mark.parametrize("row", RECORDS, ids=[r["name"] for r in RECORDS])
def test_recordings_follow_pinned_schema_and_reject_missing_required_field(row):
    schema = resolved(pointer(SPEC, row["schema_pointer"]))
    digest = hashlib.sha256(json.dumps(schema, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    assert digest == row["schema_sha256"], "Review recordings when the upstream response contract changes"
    validator = Draft202012Validator(schema)
    validator.validate(row["response"])
    broken = copy.deepcopy(row["response"])
    del broken[schema["required"][0]]
    assert not validator.is_valid(broken)


def test_all_examples_use_keyless_transport_even_with_ambient_credentials(monkeypatch):
    monkeypatch.setenv("PROPRAVEN_API_KEY", "DO_NOT_USE_THIS_TEST_SENTINEL")
    monkeypatch.setenv("PROPRAVEN_BASE_URL", "https://must-not-contact.invalid")
    with client_context() as client:
        result = run.run(client)
    assert set(result) == {"search", "parcel", "coverage", "storefront"}
    assert result["parcel"]["address"] == SPEC["components"]["schemas"]["Parcel"]["properties"]["address"]["example"]
    assert result["search"]["bounds_total"] == 1
    assert result["coverage"][0]["state_fips"] == "37"


def test_replay_refuses_unknown_endpoints_and_wrong_request_parameters():
    replay = Replay()
    for url in ["/api/v1/owners/anything", "/api/v1/storefront/buy_dossier", "/api/v1/coverage?state=06"]:
        with pytest.raises(AssertionError, match="Unrecorded"):
            replay(httpx.Request("GET", "https://example.invalid" + url))
    ok = replay(httpx.Request("GET", "https://example.invalid/api/v1/coverage?state=37"))
    assert ok.status_code == 200 and replay.seen == ["coverage"]


def test_no_person_values_in_recordings():
    def visit(value):
        if isinstance(value, list):
            for item in value:
                visit(item)
        if isinstance(value, dict):
            for key, item in value.items():
                if (key.startswith("owner_") and key != "owner_pct") or key in {"email", "phone", "contact_name"}:
                    assert item is None
                visit(item)
    for row in RECORDS:
        visit(row["response"])


def snapshot(path):
    return {str(p.relative_to(path)): p.read_bytes() for p in path.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts}


def assert_preserved(before, path):
    assert snapshot(path) == before, "Regeneration changed examples"


def test_real_regeneration_preserves_examples_and_guard_detects_changes(tmp_path):
    for name in ["scripts", "src", "examples"]:
        shutil.copytree(ROOT / name, tmp_path / name, ignore=shutil.ignore_patterns("__pycache__"))
    for name in ["openapi.json", "README.md"]:
        shutil.copy2(ROOT / name, tmp_path / name)
    # A changed description ensures this is a writing regeneration, not --check.
    spec = json.loads((tmp_path / "openapi.json").read_text())
    spec["paths"]["/api/v1/coverage"]["get"]["summary"] = "Synthetic regeneration preservation probe"
    (tmp_path / "openapi.json").write_text(json.dumps(spec))
    before = snapshot(tmp_path / "examples")
    old_resources = snapshot(tmp_path / "src")
    subprocess.run([sys.executable, "scripts/generate.py"], cwd=tmp_path, check=True, capture_output=True)
    assert snapshot(tmp_path / "src") != old_resources
    assert_preserved(before, tmp_path / "examples")
    (tmp_path / "examples" / "search.py").write_text("changed")
    with pytest.raises(AssertionError, match="Regeneration changed"):
        assert_preserved(before, tmp_path / "examples")
