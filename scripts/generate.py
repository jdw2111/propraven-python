#!/usr/bin/env python3
"""Generate the typed layer of the PropRaven Python SDK from ``openapi.json``.

Writes:
  * ``src/propraven/types/__init__.py``      TypedDicts / aliases for every schema and response
  * ``src/propraven/resources/<group>.py``   sync + async resource classes per ``x-sdk-group``
  * ``src/propraven/resources/__init__.py``  client mixins exposing ``client.<group>``
  * the method table between the markers in ``README.md``

Usage::

    python scripts/generate.py            # (re)write the generated files
    python scripts/generate.py --check    # exit 1 if the generated files are stale

Standard library only; output is deterministic for a given ``openapi.json``.
"""

from __future__ import annotations

import argparse
import json
import keyword
import re
import sys
import textwrap
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "openapi.json"
PKG = ROOT / "src" / "propraven"
README = ROOT / "README.md"
HEADER = "# Code generated from openapi.json by scripts/generate.py. DO NOT EDIT.\n"
README_BEGIN = "<!-- BEGIN GENERATED METHODS (scripts/generate.py) -->"
README_END = "<!-- END GENERATED METHODS -->"

HTTP_METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")

# kwargs every generated method owns; spec params that collide get a trailing underscore.
RESERVED_KWARGS = {
    "self",
    "extra_headers",
    "extra_query",
    "extra_body",
    "timeout",
    "max_retries",
    "page_size",
    "max_items",
}
# attributes of the client that a namespace must not shadow.
RESERVED_CLIENT_ATTRS = {
    "request",
    "close",
    "api_key",
    "base_url",
    "timeout",
    "max_retries",
    "last_rate_limit",
}
TYPING_NAMES = {"Any", "Dict", "List", "Literal", "Optional", "Union", "TypedDict", "Sequence", "Mapping"}
RESERVED_TYPE_NAMES = TYPING_NAMES | {"Iterator", "AsyncIterator", "TYPE_CHECKING", "NotGiven", "NOT_GIVEN", "httpx"}


# ---------------------------------------------------------------------------
# naming helpers


def pascal(value: str) -> str:
    parts = re.split(r"[^0-9A-Za-z]+", value)
    out = "".join(p[:1].upper() + p[1:] for p in parts if p)
    if not out:
        out = "Schema"
    if out[0].isdigit():
        out = "T" + out
    return out


def snake(value: str) -> str:
    s = re.sub(r"[^0-9A-Za-z]+", "_", value)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = s.strip("_").lower()
    s = re.sub(r"_+", "_", s)
    if not s:
        s = "value"
    if s[0].isdigit():
        s = "_" + s
    return s


def safe_ident(name: str, reserved: Optional[Set[str]] = None) -> str:
    if not name.isidentifier():
        name = snake(name)
    if keyword.iskeyword(name) or name in (reserved or set()):
        name = name + "_"
    return name


def py_group_name(group: str) -> str:
    return safe_ident(snake(group), RESERVED_CLIENT_ATTRS)


def py_method_name(method: str) -> str:
    return safe_ident(snake(method))


def header_param_name(wire: str) -> str:
    name = wire
    if name.lower().startswith("x-"):
        name = name[2:]
    return safe_ident(snake(name.lower().replace("-", "_")), RESERVED_KWARGS)


def docstring(text: str, indent: str) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    text = text.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    width = max(40, 100 - len(indent))
    lines: List[str] = []
    for raw in text.splitlines():
        raw = raw.rstrip()
        if len(raw) <= width:
            lines.append(raw)
            continue
        lead = len(raw) - len(raw.lstrip())
        sub = " " * (lead + 4 if lead else 0)
        lines.extend(
            textwrap.wrap(raw, width=width, subsequent_indent=sub, break_long_words=False, break_on_hyphens=False)
            or [raw]
        )
    if lines[-1].endswith('"'):
        lines[-1] += " "
    if len(lines) == 1:
        return f'{indent}"""{lines[0]}"""\n'
    body = "\n".join((indent + ln) if ln else "" for ln in lines[1:])
    return f'{indent}"""{lines[0]}\n{body}\n{indent}"""\n'


# ---------------------------------------------------------------------------
# type generation


class TypeGen:
    def __init__(self, spec: Dict[str, Any]) -> None:
        self.spec = spec
        self.used: Set[str] = set(RESERVED_TYPE_NAMES)
        self.preassigned: Set[str] = set()
        self.classes: Dict[str, str] = {}  # name -> code
        self.class_order: List[str] = []
        self.aliases: Dict[str, str] = {}  # name -> expression
        self.alias_order: List[str] = []
        self.public: List[str] = []
        # id(schema) -> (schema, expr); the schema is kept alive so its id is never reused.
        self.memo: Dict[int, Tuple[Any, str]] = {}
        self.component_names: Dict[str, str] = {}
        for comp in spec.get("components", {}).get("schemas", {}):
            self.component_names[comp] = self.preassign(pascal(comp))

    def preassign(self, base: str) -> str:
        """Reserve a unique name for a specific later definition (component / response)."""
        name = self.reserve(base)
        self.preassigned.add(name)
        return name

    def claim(self, name: str) -> str:
        """Name to use for a new definition requested as ``name``."""
        if name in self.preassigned:
            self.preassigned.discard(name)
            return name
        return self.reserve(name)

    def reserve(self, base: str) -> str:
        name = base
        i = 2
        while name in self.used or keyword.iskeyword(name):
            name = f"{base}{i}"
            i += 1
        self.used.add(name)
        return name

    def resolve_ref(self, ref: str) -> Any:
        if not ref.startswith("#/"):
            return {}
        node: Any = self.spec
        for part in ref[2:].split("/"):
            part = part.replace("~1", "/").replace("~0", "~")
            if not isinstance(node, dict) or part not in node:
                return {}
            node = node[part]
        return node

    def deref(self, schema: Any, depth: int = 0) -> Any:
        while isinstance(schema, dict) and "$ref" in schema and depth < 32:
            schema = self.resolve_ref(schema["$ref"])
            depth += 1
        return schema

    def ref_name(self, ref: str) -> Optional[str]:
        prefix = "#/components/schemas/"
        if ref.startswith(prefix):
            return self.component_names.get(ref[len(prefix) :].replace("~1", "/").replace("~0", "~"))
        return None

    # -- annotations ------------------------------------------------------

    def ann(self, schema: Any, name: str) -> str:
        """Return a Python type expression for ``schema``; registers TypedDicts named ``name``."""
        if not isinstance(schema, dict) or not schema:
            return "Any"
        key = id(schema)
        if key in self.memo:
            return self.memo[key][1]
        expr = self._ann(schema, name)
        self.memo[key] = (schema, expr)
        return expr

    def _ann(self, schema: Dict[str, Any], name: str) -> str:
        if "$ref" in schema:
            target = self.ref_name(schema["$ref"])
            if target:
                return target
            return self.ann(self.resolve_ref(schema["$ref"]), name)

        nullable = bool(schema.get("nullable"))
        typ = schema.get("type")
        types: List[str] = []
        if isinstance(typ, list):
            types = [t for t in typ if isinstance(t, str)]
            if "null" in types:
                nullable = True
                types = [t for t in types if t != "null"]
        elif isinstance(typ, str):
            if typ == "null":
                return "None"
            types = [typ]

        if "const" in schema:
            return self._optional(f"Literal[{self._lit(schema['const'])}]", nullable)

        if isinstance(schema.get("enum"), list) and schema["enum"]:
            values = schema["enum"]
            has_null = any(v is None for v in values)
            lits = [self._lit(v) for v in values if v is not None and isinstance(v, (str, int, float, bool))]
            if not lits:
                return "None" if has_null else "Any"
            return self._optional(f"Literal[{', '.join(lits)}]", nullable or has_null)

        for comb in ("oneOf", "anyOf"):
            if isinstance(schema.get(comb), list) and schema[comb]:
                return self._union(schema[comb], name, nullable)

        if isinstance(schema.get("allOf"), list) and schema["allOf"]:
            return self._optional(self._all_of(schema, name), nullable)

        if len(types) > 1:
            members = [self.ann(dict(schema, type=t), f"{name}{pascal(t)}") for t in types]
            return self._optional(self._join_union(members), nullable)

        t = types[0] if types else None
        if t is None:
            if isinstance(schema.get("properties"), dict) or "additionalProperties" in schema:
                t = "object"
            elif "items" in schema:
                t = "array"
        if t == "object":
            return self._optional(self._object(schema, name), nullable)
        if t == "array":
            item = self.ann(schema.get("items"), f"{name}Item")
            return self._optional(f"List[{item}]", nullable)
        scalar = {"string": "str", "integer": "int", "number": "float", "boolean": "bool"}.get(t or "")
        if scalar:
            return self._optional(scalar, nullable)
        return "Any"

    @staticmethod
    def _lit(value: Any) -> str:
        if isinstance(value, str):
            return json.dumps(value, ensure_ascii=False)
        if isinstance(value, bool):
            return "True" if value else "False"
        if value is None:
            return "None"
        return repr(value)

    @staticmethod
    def _optional(expr: str, nullable: bool) -> str:
        if not nullable or expr in ("Any", "None") or expr.startswith("Optional["):
            return expr
        return f"Optional[{expr}]"

    @staticmethod
    def _join_union(members: List[str]) -> str:
        seen: List[str] = []
        for m in members:
            if m not in seen:
                seen.append(m)
        if "Any" in seen:
            return "Any"
        if len(seen) == 1:
            return seen[0]
        return f"Union[{', '.join(seen)}]"

    def _union(self, variants: List[Any], name: str, nullable: bool) -> str:
        members: List[str] = []
        for i, variant in enumerate(variants, start=1):
            expr = self.ann(variant, f"{name}Variant{i}")
            if expr == "None":
                nullable = True
                continue
            members.append(expr)
        if not members:
            return "None"
        joined = self._join_union(members)
        return self._optional(joined, nullable)

    def _collect_object(self, schema: Any, props: Dict[str, Any], required: Set[str], depth: int = 0) -> bool:
        schema = self.deref(schema)
        if not isinstance(schema, dict) or depth > 16:
            return False
        ok = True
        if isinstance(schema.get("allOf"), list):
            for member in schema["allOf"]:
                ok = self._collect_object(member, props, required, depth + 1) and ok
        if isinstance(schema.get("properties"), dict):
            for k, v in schema["properties"].items():
                props.setdefault(k, v)
        if isinstance(schema.get("required"), list):
            required.update(r for r in schema["required"] if isinstance(r, str))
        typ = schema.get("type")
        if any(k in schema for k in ("oneOf", "anyOf")) or (typ not in (None, "object") and typ != ["object"]):
            ok = False
        return ok

    def _all_of(self, schema: Dict[str, Any], name: str) -> str:
        members = schema["allOf"]
        own = {k: v for k, v in schema.items() if k not in ("allOf", "description", "example", "title", "nullable")}
        if len(members) == 1 and not own.get("properties"):
            return self.ann(members[0], name)
        props: Dict[str, Any] = {}
        required: Set[str] = set()
        if not self._collect_object(schema, props, required):
            return "Dict[str, Any]"
        if not props:
            return "Dict[str, Any]"
        return self._typed_dict(name, props, required, schema.get("description"))

    def _object(self, schema: Dict[str, Any], name: str) -> str:
        props = schema.get("properties")
        if isinstance(props, dict) and props:
            required = {r for r in schema.get("required", []) if isinstance(r, str)}
            return self._typed_dict(name, props, required, schema.get("description"))
        extra = schema.get("additionalProperties")
        if isinstance(extra, dict) and extra:
            return f"Dict[str, {self.ann(extra, f'{name}Value')}]"
        return "Dict[str, Any]"

    def _typed_dict(self, name: str, props: Dict[str, Any], required: Set[str], description: Any) -> str:
        name = self.claim(name)
        fields: List[Tuple[str, str, bool, str]] = []
        for prop, sub in props.items():
            expr = self.ann(sub, f"{name}{pascal(prop)}")
            desc = ""
            if isinstance(sub, dict):
                desc = str(sub.get("description") or "")
                if not desc and "$ref" in sub:
                    desc = ""
            fields.append((prop, expr, prop in required, desc))

        doc = docstring(str(description or ""), "    ")
        valid = all(f[0].isidentifier() and not keyword.iskeyword(f[0]) for f in fields)
        req = [f for f in fields if f[2]]
        opt = [f for f in fields if not f[2]]
        lines: List[str] = []

        def body(items: List[Tuple[str, str, bool, str]]) -> List[str]:
            out: List[str] = []
            for prop, expr, _, desc in items:
                out.append(f"    {prop}: {expr}\n")
                d = docstring(desc, "    ")
                if d:
                    out.append(d)
            return out

        if not valid:
            mapping = ", ".join(f"{json.dumps(f[0])}: {json.dumps(f[1])}" for f in fields)
            lines.append(f'{name} = TypedDict("{name}", {{{mapping}}}, total=False)\n')
            if doc:
                lines.insert(0, "# " + str(description).strip().splitlines()[0] + "\n")
        elif req and opt:
            base = f"_{name}Required"
            self.used.add(base)
            lines.append(f"class {base}(TypedDict):\n")
            lines.extend(body(req))
            lines.append("\n\n")
            lines.append(f"class {name}({base}, total=False):\n")
            if doc:
                lines.append(doc)
            lines.extend(body(opt))
        elif req:
            lines.append(f"class {name}(TypedDict):\n")
            if doc:
                lines.append(doc)
            lines.extend(body(req))
        else:
            lines.append(f"class {name}(TypedDict, total=False):\n")
            if doc:
                lines.append(doc)
            lines.extend(body(opt))
        self.classes[name] = "".join(lines)
        self.class_order.append(name)
        self.public.append(name)
        return name

    def named(self, schema: Any, name: str) -> str:
        """Ensure ``name`` exists as a type for ``schema`` (class or alias). Returns ``name``."""
        if isinstance(schema, dict) and id(schema) in self.memo:
            expr = self.memo[id(schema)][1]
        else:
            expr = self.ann(schema, name)
        if expr != name:
            self.alias(name, expr)
        return name

    def alias(self, name: str, expr: str) -> None:
        if name in self.aliases or name in self.classes:
            return
        name = self.claim(name)
        self.aliases[name] = expr
        self.alias_order.append(name)
        self.public.append(name)

    # -- emit -------------------------------------------------------------

    def render(self) -> str:
        out = [HEADER, '"""Response and request types generated from openapi.json.\n\n']
        out.append("Every type is a ``TypedDict`` (a plain ``dict`` at runtime; no validation).\n")
        out.append('"""\n\n')
        out.append("from __future__ import annotations\n\n")
        out.append("from typing import Any, Dict, List, Literal, Optional, TypedDict, Union\n\n")
        names = sorted(set(self.public))
        out.append("__all__ = [\n")
        for n in names:
            out.append(f'    "{n}",\n')
        out.append("]\n\n\n")
        for n in self.class_order:
            out.append(self.classes[n])
            out.append("\n\n")
        for n in self._sorted_aliases():
            out.append(f"{n} = {self.aliases[n]}\n")
        text = "".join(out).rstrip() + "\n"
        return text

    def _sorted_aliases(self) -> List[str]:
        order: List[str] = []
        state: Dict[str, int] = {}
        token = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")

        def visit(n: str) -> None:
            if state.get(n) == 2:
                return
            if state.get(n) == 1:  # cycle: break it
                self.aliases[n] = "Any"
                return
            state[n] = 1
            for dep in token.findall(self.aliases[n]):
                if dep in self.aliases and dep != n:
                    visit(dep)
            state[n] = 2
            order.append(n)

        for n in self.alias_order:
            visit(n)
        return order


# ---------------------------------------------------------------------------
# operations


class Param:
    def __init__(self, py: str, wire: str, where: str, ann: str, required: bool, desc: str, explode: bool) -> None:
        self.py = py
        self.wire = wire
        self.where = where  # path | query | header | body | bodyall
        self.ann = ann
        self.required = required
        self.desc = desc
        self.explode = explode


class Operation:
    def __init__(self, path: str, method: str, op: Dict[str, Any]) -> None:
        self.path = path
        self.http = method.upper()
        self.op = op
        self.group = op["x-sdk-group"]
        self.wire_method = op["x-sdk-method"]
        self.py_group = py_group_name(self.group)
        self.py_method = py_method_name(self.wire_method)
        self.type_base = pascal(self.group) + pascal(self.wire_method)
        self.pagination = op.get("x-sdk-pagination")
        self.params: List[Param] = []
        self.response_type = "None"
        self.kind = "json"
        self.accept: Optional[str] = None
        self.item_type = "Any"
        self.summary = str(op.get("summary") or "").strip()
        self.description = str(op.get("description") or "").strip()


def build_operations(spec: Dict[str, Any], tg: TypeGen) -> List[Operation]:
    ops: List[Operation] = []
    for path, item in spec.get("paths", {}).items():
        if not isinstance(item, dict):
            continue
        shared = item.get("parameters", [])
        for method in HTTP_METHODS:
            op = item.get(method)
            if not isinstance(op, dict):
                continue
            if "x-sdk-group" not in op or "x-sdk-method" not in op:
                raise SystemExit(f"{method.upper()} {path}: missing x-sdk-group / x-sdk-method")
            o = Operation(path, method, op)
            # reserve the response name first so nested types do not take it
            o.response_type = tg.preassign(o.type_base + "Response")
            ops.append(o)
            _params(o, shared, tg)
            _response(o, tg)
    # duplicate method check
    seen: Dict[Tuple[str, str], str] = {}
    for o in ops:
        k = (o.py_group, o.py_method)
        if k in seen:
            raise SystemExit(f"duplicate SDK method {k}: {seen[k]} and {o.http} {o.path}")
        seen[k] = f"{o.http} {o.path}"
    return ops


def _params(o: Operation, shared: List[Any], tg: TypeGen) -> None:
    raw: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for p in list(shared) + list(o.op.get("parameters", [])):
        p = tg.deref(p)
        if isinstance(p, dict) and "name" in p and "in" in p:
            raw[(p["in"], p["name"])] = p
    used: Set[str] = set(RESERVED_KWARGS)

    def unique(name: str, where: str) -> str:
        if name in used:
            name = f"{name}_{where}"
        while name in used:
            name += "_"
        used.add(name)
        return name

    # path params in path order
    order = re.findall(r"{([^}]+)}", o.path)
    for wire in order:
        p = raw.get(("path", wire), {"name": wire, "in": "path", "required": True, "schema": {"type": "string"}})
        py = unique(safe_ident(snake(wire), RESERVED_KWARGS), "path")
        ann = tg.ann(p.get("schema"), f"{o.type_base}Params{pascal(wire)}")
        if ann in ("Any", "str"):
            ann = "str"
        o.params.append(Param(py, wire, "path", ann, True, str(p.get("description") or ""), False))

    for (where, wire), p in raw.items():
        if where not in ("query", "header"):
            continue
        if where == "header":
            py = unique(header_param_name(wire), "header")
        else:
            py = unique(safe_ident(wire, RESERVED_KWARGS), "query")
        ann = tg.ann(p.get("schema"), f"{o.type_base}Params{pascal(wire)}")
        if ann.startswith("List["):
            ann = "Sequence[" + ann[5:]
        o.params.append(
            Param(
                py, wire, where, ann, bool(p.get("required")), str(p.get("description") or ""), p.get("explode") is True
            )
        )

    rb = tg.deref(o.op.get("requestBody"))
    if isinstance(rb, dict):
        content = rb.get("content", {})
        schema = None
        for ct, media in content.items():
            if "json" in ct:
                schema = media.get("schema")
                break
        if schema is not None:
            props: Dict[str, Any] = {}
            required: Set[str] = set()
            flat_ok = tg._collect_object(schema, props, required)
            if flat_ok and props:
                body_required = bool(rb.get("required"))
                for wire, sub in props.items():
                    py = unique(safe_ident(wire, RESERVED_KWARGS), "body")
                    ann = tg.ann(sub, f"{o.type_base}Params{pascal(wire)}")
                    if ann.startswith("List["):
                        ann = "Sequence[" + ann[5:]
                    desc = str(sub.get("description") or "") if isinstance(sub, dict) else ""
                    o.params.append(Param(py, wire, "body", ann, body_required and wire in required, desc, False))
            else:
                ann = tg.ann(schema, f"{o.type_base}Body")
                if ann.startswith("List["):
                    ann = "Sequence[" + ann[5:]
                py = unique("body", "body")
                o.params.append(Param(py, "body", "bodyall", ann, bool(rb.get("required")), "Request body.", False))


def _response(o: Operation, tg: TypeGen) -> None:
    responses = o.op.get("responses", {})
    code = next((c for c in ("200", "201", "202", "203", "206") if c in responses), None)
    if code is None:
        code = next((c for c in sorted(responses) if str(c).startswith("2")), None)
    name = o.response_type
    if code is None:
        tg.alias(name, "None")
        return
    resp = tg.deref(responses[code])
    content = resp.get("content") if isinstance(resp, dict) else None
    if not content:
        tg.alias(name, "None")
        return
    json_schema = None
    json_found = False
    text_types: List[str] = []
    for ct, media in content.items():
        if "json" in ct.lower():
            if not json_found:
                json_found = True
                json_schema = media.get("schema") if isinstance(media, dict) else None
        else:
            text_types.append(ct)
    if json_found and not text_types:
        tg.named(json_schema if json_schema is not None else {}, name)
        o.kind = "json"
    elif json_found:
        jexpr = tg.ann(json_schema, f"{name}Json") if json_schema is not None else "Any"
        tg.alias(name, tg._join_union(["str", jexpr]))
        o.kind = "json"
        o.accept = ", ".join(content.keys())
    else:
        tg.alias(name, "str")
        o.kind = "text"
        o.accept = ", ".join(content.keys())

    if o.pagination and json_schema is not None:
        o.item_type = _item_type(tg, json_schema, str(o.pagination.get("items") or "data"), name + "Item")


def _item_type(tg: TypeGen, schema: Any, key: str, fallback: str, depth: int = 0) -> str:
    if depth > 8:
        return "Any"
    s = tg.deref(schema)
    if not isinstance(s, dict):
        return "Any"
    for comb in ("oneOf", "anyOf"):
        if isinstance(s.get(comb), list):
            return tg._join_union([_item_type(tg, v, key, fallback, depth + 1) for v in s[comb]])
    if s.get("type") == "array":
        return tg.ann(s.get("items"), fallback)
    props: Dict[str, Any] = {}
    tg._collect_object(s, props, set())
    sub = tg.deref(props.get(key))
    if isinstance(sub, dict) and (sub.get("type") == "array" or "items" in sub):
        return tg.ann(sub.get("items"), fallback)
    return "Any"


# ---------------------------------------------------------------------------
# resource rendering


_TYPE_NAMES: Set[str] = set()
_STRING = re.compile(r'("(?:[^"\\]|\\.)*")')
_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def q(expr: str) -> str:
    """Qualify generated type names in ``expr`` as ``_t.<Name>`` (string literals untouched)."""
    parts = _STRING.split(expr)
    for i in range(0, len(parts), 2):
        parts[i] = _TOKEN.sub(lambda m: f"_t.{m.group(0)}" if m.group(0) in _TYPE_NAMES else m.group(0), parts[i])
    return "".join(parts)


def _sig_lines(params: List[Param], extra_body: bool) -> List[str]:
    lines = ["        self,\n"]
    for p in params:
        if p.where == "path":
            lines.append(f"        {p.py}: {q(p.ann)},\n")
    kw = [p for p in params if p.where != "path"]
    lines.append("        *,\n")
    for p in kw:
        if p.required:
            lines.append(f"        {p.py}: {q(p.ann)},\n")
    for p in kw:
        if not p.required:
            ann = p.ann if p.ann.startswith("Optional[") or p.ann in ("Any", "None") else f"Optional[{p.ann}]"
            lines.append(f"        {p.py}: {q(ann)} = None,\n")
    return lines


def _common_kwargs(extra_body: bool) -> List[str]:
    lines = [
        "        extra_headers: Optional[Mapping[str, str]] = None,\n",
        "        extra_query: Optional[Mapping[str, Any]] = None,\n",
    ]
    if extra_body:
        lines.append("        extra_body: Optional[Mapping[str, Any]] = None,\n")
    lines += [
        "        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,\n",
        "        max_retries: Union[int, NotGiven] = NOT_GIVEN,\n",
    ]
    return lines


def _method_doc(o: Operation, params: List[Param], extra: str = "") -> str:
    parts: List[str] = []
    if o.summary:
        parts.append(o.summary)
        parts.append("")
    parts.append(f"``{o.http} {o.path}``")
    if o.description and o.description != o.summary:
        parts.append("")
        parts.append(o.description)
    if extra:
        parts.append("")
        parts.append(extra)
    documented = [p for p in params if p.desc]
    if documented:
        parts.append("")
        parts.append("Args:")
        for p in documented:
            desc = " ".join(p.desc.split())
            wire = f" (``{p.wire}`` header)" if p.where == "header" else ""
            parts.append(f"    {p.py}{wire}: {desc}")
    return docstring("\n".join(parts), "        ")


def _call_body(o: Operation, aw: str, overrides: Dict[str, str]) -> List[str]:
    """Lines of the ``self._client._request(...)`` call."""

    def val(p: Param) -> str:
        return overrides.get(p.py, p.py)

    lines = [
        f'        return cast("{q(o.response_type)}", {aw}self._client._request(\n',
        f'            "{o.http}",\n',
        f'            "{o.path}",\n',
    ]
    path = [p for p in o.params if p.where == "path"]
    query = [p for p in o.params if p.where == "query"]
    header = [p for p in o.params if p.where == "header"]
    body = [p for p in o.params if p.where == "body"]
    bodyall = [p for p in o.params if p.where == "bodyall"]
    if path:
        lines.append("            path_params={" + ", ".join(f'"{p.wire}": {val(p)}' for p in path) + "},\n")
    if query:
        lines.append("            query={\n")
        for p in query:
            lines.append(f'                "{p.wire}": {val(p)},\n')
        lines.append("            },\n")
    if header:
        lines.append("            headers={" + ", ".join(f'"{p.wire}": {val(p)}' for p in header) + "},\n")
    if body:
        lines.append("            body={\n")
        for p in body:
            lines.append(f'                "{p.wire}": {val(p)},\n')
        lines.append("            },\n")
    if bodyall:
        lines.append(f"            body={val(bodyall[0])},\n")
    explode = [p.wire for p in query if p.explode]
    if explode:
        lines.append("            explode=(" + ", ".join(f'"{w}"' for w in explode) + ",),\n")
    if o.accept:
        lines.append(f"            accept={json.dumps(o.accept)},\n")
    if o.kind != "json":
        lines.append(f'            kind="{o.kind}",\n')
    lines.append("            extra_headers=extra_headers,\n")
    lines.append("            extra_query=extra_query,\n")
    if body or bodyall:
        lines.append("            extra_body=extra_body,\n")
    lines.append("            timeout=timeout,\n")
    lines.append("            max_retries=max_retries,\n")
    lines.append("        ))\n")
    return lines


def render_method(o: Operation, is_async: bool) -> str:
    has_body = any(p.where in ("body", "bodyall") for p in o.params)
    lines: List[str] = []
    prefix = "async def" if is_async else "def"
    lines.append(f"    {prefix} {o.py_method}(\n")
    lines += _sig_lines(o.params, has_body)
    lines += _common_kwargs(has_body)
    lines.append(f"    ) -> {q(o.response_type)}:\n")
    lines.append(_method_doc(o, o.params))
    lines += _call_body(o, "await " if is_async else "", {})
    return "".join(lines)


def _pagination_params(o: Operation) -> Optional[Tuple[str, Optional[Param], Param]]:
    """(style, limit_param, position_param) or None if the op cannot be iterated."""
    pg = o.pagination or {}
    style = pg.get("style")
    by_wire = {p.wire: p for p in o.params if p.where in ("query", "body")}
    limit = by_wire.get("limit")
    if style == "offset":
        pos = by_wire.get("offset")
    elif style == "cursor":
        pos = by_wire.get(str(pg.get("cursor_param") or "after"))
    else:
        return None
    if pos is None:
        return None
    return str(style), limit, pos


def render_iter(o: Operation, is_async: bool) -> str:
    info = _pagination_params(o)
    if info is None:
        return ""
    style, limit, pos = info
    skip = {pos.py} | ({limit.py} if limit else set())
    params = [p for p in o.params if p.py not in skip]
    has_body = any(p.where in ("body", "bodyall") for p in o.params)
    pg = o.pagination or {}
    items = str(pg.get("items") or "data")
    lines: List[str] = []
    name = f"{o.py_method}_iter"
    ret = f"AsyncIterator[{q(o.item_type)}]" if is_async else f"Iterator[{q(o.item_type)}]"
    lines.append(f"    {'async def' if is_async else 'def'} {name}(\n")
    lines += _sig_lines(params, has_body)
    lines.append("        page_size: Optional[int] = None,\n")
    lines.append("        max_items: Optional[int] = None,\n")
    lines += _common_kwargs(has_body)
    lines.append(f"    ) -> {ret}:\n")
    if style == "offset":
        extra = (
            f"Auto-paginating iterator over every item (``{items}``) of :meth:`{o.py_method}`. "
            f"Pages are fetched on demand, ``page_size`` items at a time (sent as ``limit``), "
            f"advancing ``offset`` until a short page, ``offset >= total`` or ``has_more`` false. "
            f"``max_items`` caps the number of items yielded."
        )
    else:
        cursor_param = pg.get("cursor_param") or "after"
        nxt = pg.get("next") or "nextCursor"
        extra = (
            f"Auto-paginating iterator over every item (``{items}``) of :meth:`{o.py_method}`. "
            f"Passes ``{cursor_param}=<{nxt}>`` until ``{nxt}`` is null/absent or ``hasMore`` is false. "
            f"``page_size`` is sent as ``limit``; ``max_items`` caps the number of items yielded."
        )
    lines.append(_method_doc(o, params, extra))
    args = []
    for p in o.params:
        if p.where == "path":
            continue
        if p is pos:
            args.append(f"{p.py}=_pos")
        elif limit is not None and p is limit:
            args.append(f"{p.py}=_limit")
        else:
            args.append(f"{p.py}={p.py}")
    path_args = [p.py for p in o.params if p.where == "path"]
    common = ["extra_headers=extra_headers", "extra_query=extra_query"]
    if has_body:
        common.append("extra_body=extra_body")
    common += ["timeout=timeout", "max_retries=max_retries"]
    call_args = ", ".join(path_args + args + common)
    fetch = f"lambda _limit, _pos: self.{o.py_method}({call_args})"
    if style == "offset":
        helper = "aiterate_offset" if is_async else "iterate_offset"
        tail = f'items="{items}", page_size=page_size, max_items=max_items'
    else:
        helper = "aiterate_cursor" if is_async else "iterate_cursor"
        tail = f'items="{items}", next_key="{pg.get("next") or "nextCursor"}", page_size=page_size, max_items=max_items'
    if is_async:
        lines.append(f"        async for item in {helper}(\n")
        lines.append(f"            {fetch},\n")
        lines.append(f"            {tail},\n")
        lines.append("        ):\n")
        lines.append("            yield item\n")
    else:
        lines.append(f"        return {helper}(\n")
        lines.append(f"            {fetch},\n")
        lines.append(f"            {tail},\n")
        lines.append("        )\n")
    return "".join(lines)


def _names_in(expr: str) -> Set[str]:
    return set(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", expr))


def resource_class(group: str, is_async: bool = False) -> str:
    return ("Async" if is_async else "") + pascal(group) + "Resource"


def render_group(group: str, ops: List[Operation]) -> str:
    typing_used: Set[str] = {"Any", "Mapping", "Optional", "Union", "cast"}
    uses_types = False
    for o in ops:
        exprs = [o.response_type] + [p.ann for p in o.params]
        if o.pagination:
            exprs.append(o.item_type)
        for e in exprs:
            for n in _names_in(_STRING.sub("", e)):
                if n in _TYPE_NAMES:
                    uses_types = True
                elif n in TYPING_NAMES:
                    typing_used.add(n)
    paginated = [o for o in ops if o.pagination and _pagination_params(o)]
    styles = {(o.pagination or {}).get("style") for o in paginated}
    if paginated:
        typing_used |= {"Iterator", "AsyncIterator"}
    typing_used.discard("TypedDict")

    out = [HEADER, f'"""The ``{group}`` namespace: ``client.{py_group_name(group)}``."""\n\n']
    out.append("from __future__ import annotations\n\n")
    out.append("from typing import " + ", ".join(sorted(typing_used)) + "\n\n")
    out.append("import httpx\n\n")
    if uses_types:
        out.append("from .. import types as _t\n")
    helpers = []
    if "offset" in styles:
        helpers += ["aiterate_offset", "iterate_offset"]
    if "cursor" in styles:
        helpers += ["aiterate_cursor", "iterate_cursor"]
    if helpers:
        out.append("from .._pagination import " + ", ".join(sorted(helpers)) + "\n")
    out.append("from .._resource import AsyncAPIResource, SyncAPIResource\n")
    out.append("from .._transport import NOT_GIVEN, NotGiven\n")
    out.append(f'\n__all__ = ["{resource_class(group)}", "{resource_class(group, True)}"]\n\n\n')

    for is_async in (False, True):
        name = resource_class(group, is_async)
        base = "AsyncAPIResource" if is_async else "SyncAPIResource"
        out.append(f"class {name}({base}):\n")
        out.append(f'    """``client.{py_group_name(group)}`` operations ({"async" if is_async else "sync"})."""\n')
        for o in ops:
            out.append("\n")
            out.append(render_method(o, is_async))
            it = render_iter(o, is_async) if o.pagination else ""
            if it:
                out.append("\n")
                out.append(it)
        out.append("\n\n")
    return "".join(out).rstrip() + "\n"


def render_resources_init(groups: List[Tuple[str, List[Operation]]]) -> str:
    out = [HEADER, '"""Generated resource namespaces and the client mixins that expose them."""\n\n']
    out.append("from __future__ import annotations\n\n")
    out.append("from functools import cached_property\n\n")
    for group, _ in groups:
        out.append(f"from .{snake(group)} import {resource_class(group, True)}, {resource_class(group)}\n")
    out.append("\n__all__ = [\n")
    names = []
    for group, _ in groups:
        names += [resource_class(group), resource_class(group, True)]
    for n in sorted(names + ["SyncResourcesMixin", "AsyncResourcesMixin"]):
        out.append(f'    "{n}",\n')
    out.append("]\n\n\n")
    for is_async in (False, True):
        mixin = "AsyncResourcesMixin" if is_async else "SyncResourcesMixin"
        out.append(f"class {mixin}:\n")
        out.append('    """Adds one attribute per API namespace to the client."""\n')
        for group, ops in groups:
            cls = resource_class(group, is_async)
            out.append("\n    @cached_property\n")
            out.append(f"    def {py_group_name(group)}(self) -> {cls}:\n")
            out.append(f'        """``{group}`` namespace ({len(ops)} operation{"s" if len(ops) != 1 else ""})."""\n')
            out.append(f"        return {cls}(self)\n")
        out.append("\n\n")
    return "".join(out).rstrip() + "\n"


def render_readme_table(groups: List[Tuple[str, List[Operation]]]) -> str:
    total = sum(len(ops) for _, ops in groups)
    lines = [
        README_BEGIN,
        "",
        f"{total} operations. Every method exists on both `PropRaven` and `AsyncPropRaven`; "
        "methods marked *iter* also have an auto-paginating `<method>_iter(...)` sibling.",
        "",
        "| Method | HTTP | Summary |",
        "| --- | --- | --- |",
    ]
    for _group, ops in groups:
        for o in ops:
            pos = ", ".join(p.py for p in o.params if p.where == "path")
            call = f"client.{o.py_group}.{o.py_method}({pos})"
            it = " (*iter*)" if o.pagination and _pagination_params(o) else ""
            summary = " ".join((o.summary or "").split()).replace("|", "\\|")
            lines.append(f"| `{call}`{it} | `{o.http} {o.path}` | {summary} |")
    lines += ["", README_END]
    return "\n".join(lines)


# ---------------------------------------------------------------------------


def generate(spec: Dict[str, Any]) -> Dict[Path, str]:
    tg = TypeGen(spec)
    # components first, in spec order, so their names are canonical
    for comp, schema in spec.get("components", {}).get("schemas", {}).items():
        tg.named(schema, tg.component_names[comp])
    ops = build_operations(spec, tg)

    groups: Dict[str, List[Operation]] = {}
    for o in ops:
        groups.setdefault(o.group, []).append(o)
    group_list = list(groups.items())
    # module and attribute collisions between groups
    mods: Dict[str, str] = {}
    for g, _ in group_list:
        m = snake(g)
        if m in mods:
            raise SystemExit(f"x-sdk-group {g!r} collides with {mods[m]!r}")
        mods[m] = g

    files: Dict[Path, str] = {}
    files[PKG / "types" / "__init__.py"] = tg.render()
    _TYPE_NAMES.clear()
    _TYPE_NAMES.update(tg.public)
    for g, gops in group_list:
        files[PKG / "resources" / f"{snake(g)}.py"] = render_group(g, gops)
    files[PKG / "resources" / "__init__.py"] = render_resources_init(group_list)

    if README.exists():
        readme = README.read_text(encoding="utf-8")
        table = render_readme_table(group_list)
        if README_BEGIN in readme and README_END in readme:
            start = readme.index(README_BEGIN)
            end = readme.index(README_END) + len(README_END)
            readme = readme[:start] + table + readme[end:]
        files[README] = readme
    return files


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--spec", default=str(SPEC_PATH), help="path to openapi.json (default: repo root)")
    parser.add_argument("--check", action="store_true", help="fail if generated files are out of date")
    args = parser.parse_args(argv)

    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    files = generate(spec)

    resources_dir = PKG / "resources"
    expected = {p for p in files if p.parent == resources_dir}
    stale = [
        p
        for p in sorted(resources_dir.glob("*.py"))
        if p not in expected and p.read_text(encoding="utf-8").startswith(HEADER)
    ]

    if args.check:
        bad = [
            str(p.relative_to(ROOT))
            for p, text in files.items()
            if not p.exists() or p.read_text(encoding="utf-8") != text
        ]
        bad += [str(p.relative_to(ROOT)) for p in stale]
        if bad:
            print("generated files are out of date:\n  " + "\n  ".join(bad), file=sys.stderr)
            return 1
        print("generated files are up to date")
        return 0

    for p in stale:
        p.unlink()
    for p, text in files.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        if not p.exists() or p.read_text(encoding="utf-8") != text:
            p.write_text(text, encoding="utf-8")
    n_ops = sum(
        1 for item in spec.get("paths", {}).values() for m in HTTP_METHODS if isinstance(item, dict) and m in item
    )
    print(f"generated {len(files)} files for {n_ops} operations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
