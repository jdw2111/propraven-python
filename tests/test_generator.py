"""The generator copes with schema shapes the provisional spec does not (yet) use."""

from __future__ import annotations

import sys
import types as pytypes
import typing
from typing import Any, Dict

from .test_surface import gen

EDGE_SPEC: Dict[str, Any] = {
    "openapi": "3.1.0",
    "info": {"title": "edge", "version": "1"},
    "paths": {
        "/api/v1/things/{class}/items/{itemId}": {
            "parameters": [{"name": "class", "in": "path", "required": True, "schema": {"type": "string"}}],
            "get": {
                "x-sdk-group": "things",
                "x-sdk-method": "import",
                "summary": 'Has """quotes""" and \\ backslashes',
                "parameters": [
                    {"name": "itemId", "in": "path", "required": True, "schema": {"type": "integer"}},
                    {"name": "from", "in": "query", "required": True, "schema": {"type": "string", "format": "date"}},
                    {
                        "name": "ids",
                        "in": "query",
                        "schema": {"type": "array", "items": {"type": "string"}},
                        "explode": True,
                    },
                    {"name": "timeout", "in": "query", "schema": {"type": "number"}},
                    {"name": "X-Api-Trace", "in": "header", "schema": {"type": "string"}},
                    {"name": "limit", "in": "query", "schema": {"type": "integer"}},
                    {"name": "offset", "in": "query", "schema": {"type": "integer"}},
                ],
                "x-sdk-pagination": {"style": "offset", "items": "rows"},
                "responses": {
                    "200": {
                        "description": "ok",
                        "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Page"}}},
                    }
                },
            },
            "post": {
                "x-sdk-group": "things",
                "x-sdk-method": "bulkUpload",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"type": "array", "items": {"$ref": "#/components/schemas/Thing"}}
                        }
                    },
                },
                "responses": {"204": {"description": "no content"}},
            },
        },
        "/api/v1/things": {
            "post": {
                "x-sdk-group": "things",
                "x-sdk-method": "create",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "allOf": [
                                    {"$ref": "#/components/schemas/Thing"},
                                    {
                                        "type": "object",
                                        "required": ["name"],
                                        "properties": {"name": {"type": "string"}},
                                    },
                                ]
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "created",
                        "content": {
                            "application/json": {
                                "schema": {"anyOf": [{"$ref": "#/components/schemas/Thing"}, {"type": "null"}]}
                            }
                        },
                    }
                },
            },
            "get": {
                "x-sdk-group": "other-things",
                "x-sdk-method": "list",
                "responses": {"200": {"description": "csv", "content": {"text/csv": {"schema": {"type": "string"}}}}},
            },
        },
    },
    "components": {
        "schemas": {
            "Thing": {
                "type": "object",
                "required": ["id"],
                "properties": {
                    "id": {"type": "string"},
                    "class": {"type": ["string", "null"]},
                    "kind": {"enum": ["a", "b", None]},
                    "version": {"const": 2},
                    "score": {"type": ["number", "integer"]},
                    "tags": {"type": "object", "additionalProperties": {"type": "integer"}},
                    "meta": {},
                    "child": {"$ref": "#/components/schemas/Thing"},
                    "nested": {
                        "type": "object",
                        "properties": {
                            "deep": {
                                "type": "array",
                                "items": {"type": "object", "properties": {"x": {"type": "boolean"}}},
                            }
                        },
                    },
                },
            },
            "Page": {
                "type": "object",
                "properties": {
                    "rows": {"type": "array", "items": {"$ref": "#/components/schemas/Thing"}},
                    "total": {"type": "integer"},
                },
            },
            "Odd-Name": {
                "type": "object",
                "properties": {"not-an-identifier": {"type": "string"}, "ok": {"type": "integer"}},
            },
            "Mixed": {
                "oneOf": [{"type": "string"}, {"$ref": "#/components/schemas/Thing"}, {"type": "array", "items": {}}]
            },
            "Untyped": {},
            "Self": {"type": "object", "properties": {"next": {"$ref": "#/components/schemas/Self"}}},
            "AliasA": {"$ref": "#/components/schemas/AliasB"},
            "AliasB": {"type": "array", "items": {"$ref": "#/components/schemas/Thing"}},
            "Req": {
                "type": "object",
                "required": ["a"],
                "properties": {"a": {"type": "string"}, "b": {"type": "integer"}},
            },
        }
    },
}


def _exec(name: str, source: str, package: Dict[str, Any]) -> pytypes.ModuleType:
    module = pytypes.ModuleType(name)
    module.__dict__.update(package)
    exec(compile(source, name, "exec"), module.__dict__)
    return module


def test_edge_spec_generates_valid_code() -> None:
    files = gen.generate(EDGE_SPEC)
    by_name = {p.name if p.parent.name != "types" else "types": t for p, t in files.items()}
    types_src = by_name["types"]
    types_mod = _exec("edge_types", types_src, {})
    sys.modules["edge_types"] = types_mod

    # every exported type resolves
    for name in types_mod.__all__:
        obj = getattr(types_mod, name)
        if isinstance(obj, type):
            typing.get_type_hints(obj, globalns=types_mod.__dict__)

    thing = types_mod.Thing
    # keys that are not identifiers ("class") force the functional form, where every key is optional
    assert {"id", "class"} <= thing.__optional_keys__
    assert types_mod.Req.__required_keys__ == frozenset({"a"})
    assert types_mod.Req.__optional_keys__ == frozenset({"b"})
    hints = typing.get_type_hints(thing, globalns=types_mod.__dict__)
    assert hints["class"] == typing.Optional[str]
    assert hints["version"] == typing.Literal[2]
    assert hints["tags"] == typing.Dict[str, int]
    assert hints["meta"] is typing.Any
    assert "OddName" in types_mod.__all__
    assert set(typing.get_type_hints(types_mod.OddName)) == {"not-an-identifier", "ok"}
    assert types_mod.AliasA == typing.List[thing]
    assert types_mod.ThingsCreateResponse == typing.Optional[thing]
    assert types_mod.OtherThingsListResponse is str
    assert types_mod.ThingsBulkUploadResponse is None

    things = by_name["things.py"]
    compile(things, "things.py", "exec")
    assert "def import_(" in things
    assert "def import__iter(" in things
    assert "class_: str," in things
    assert "item_id: int," in things
    assert "from_: str," in things
    assert "timeout_: Optional[float] = None," in things
    assert "api_trace: Optional[str] = None," in things
    assert '"from": from_,' in things
    assert 'explode=("ids",),' in things
    assert '\\"\\"\\"quotes' in things
    assert "def bulk_upload(" in things and "body: Sequence[_t.Thing]," in things
    create_sig = things.split("def create(")[1].split(") ->")[0]
    # the request body is optional (no `required: true`), so even allOf-required members are optional kwargs
    assert "name: Optional[str] = None," in create_sig and "class_: Optional[str] = None," in create_sig
    assert "-> Iterator[_t.Thing]:" in things
    other = by_name["other_things.py"]
    assert 'kind="text"' in other and 'accept="text/csv"' in other
    init = by_name["__init__.py"]
    assert "def other_things(self) -> OtherThingsResource:" in init


def test_edge_spec_is_deterministic() -> None:
    import json

    a = gen.generate(json.loads(json.dumps(EDGE_SPEC)))
    b = gen.generate(json.loads(json.dumps(EDGE_SPEC)))
    assert a == b
