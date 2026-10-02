"""The generated surface matches openapi.json: every operation has a sync + async method."""

from __future__ import annotations

import importlib.util
import inspect
import json
import re
import sys
import typing
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, List, Tuple

import pytest

import propraven
from propraven import AsyncPropRaven, PropRaven, types

ROOT = Path(__file__).resolve().parent.parent
SPEC = json.loads((ROOT / "openapi.json").read_text(encoding="utf-8"))
METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")


def load_generator() -> ModuleType:
    spec = importlib.util.spec_from_file_location("propraven_generate", ROOT / "scripts" / "generate.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["propraven_generate"] = module
    spec.loader.exec_module(module)
    return module


gen = load_generator()


def operations() -> List[Tuple[str, str, Dict[str, Any]]]:
    out = []
    for path, item in SPEC["paths"].items():
        for method in METHODS:
            if method in item:
                out.append((path, method, item[method]))
    return out


OPS = operations()


def test_operation_count() -> None:
    assert len(OPS) >= 69


@pytest.mark.parametrize("path,method,op", OPS, ids=[f"{m.upper()} {p}" for p, m, _ in OPS])
def test_every_operation_has_a_method(path: str, method: str, op: Dict[str, Any]) -> None:
    group = gen.py_group_name(op["x-sdk-group"])
    name = gen.py_method_name(op["x-sdk-method"])
    sync = PropRaven(api_key="pz_x")
    asyn = AsyncPropRaven(api_key="pz_x")
    sync_fn = getattr(getattr(sync, group), name)
    async_fn = getattr(getattr(asyn, group), name)
    assert callable(sync_fn)
    assert inspect.iscoroutinefunction(async_fn)

    sig = inspect.signature(sync_fn)
    params = sig.parameters
    path_names = re.findall(r"{([^}]+)}", path)
    positional = [p for p in params.values() if p.kind == p.POSITIONAL_OR_KEYWORD]
    assert len(positional) == len(path_names), f"path params of {name}: {positional}"
    keyword = {p.name for p in params.values() if p.kind == p.KEYWORD_ONLY}
    for prm in op.get("parameters", []):
        if prm["in"] == "query":
            assert gen.safe_ident(prm["name"], gen.RESERVED_KWARGS) in keyword
        elif prm["in"] == "header":
            assert gen.header_param_name(prm["name"]) in keyword
    for extra in ("extra_headers", "extra_query", "timeout", "max_retries"):
        assert extra in keyword

    if op.get("x-sdk-pagination"):
        assert callable(getattr(getattr(sync, f"{group}"), f"{name}_iter"))
        assert inspect.isasyncgenfunction(getattr(type(getattr(asyn, group)), f"{name}_iter"))

    # every method's annotations resolve (also on Python 3.9)
    typing.get_type_hints(getattr(type(getattr(sync, group)), name))
    sync.close()


def test_response_type_names_exist() -> None:
    for _, _, op in OPS:
        name = gen.pascal(op["x-sdk-group"]) + gen.pascal(op["x-sdk-method"]) + "Response"
        assert hasattr(types, name), name


def test_component_types_exist() -> None:
    for comp in SPEC["components"]["schemas"]:
        assert hasattr(types, gen.pascal(comp)), comp


def test_all_types_resolve() -> None:
    for name in types.__all__:
        obj = getattr(types, name)
        if isinstance(obj, type):
            typing.get_type_hints(obj)


def test_typed_dicts_are_plain_dicts() -> None:
    parcel: types.Parcel = {"parcel_id": "1", "assessed_value": 1.5}
    assert isinstance(parcel, dict)


def test_generated_files_are_up_to_date() -> None:
    files = gen.generate(SPEC)
    for path, text in files.items():
        assert path.read_text(encoding="utf-8") == text, f"{path} is stale: run python scripts/generate.py"


def test_generation_is_deterministic() -> None:
    a = gen.generate(json.loads(json.dumps(SPEC)))
    b = gen.generate(json.loads(json.dumps(SPEC)))
    assert a == b


def test_public_exports() -> None:
    for name in propraven.__all__:
        assert hasattr(propraven, name), name
