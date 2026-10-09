#!/usr/bin/env python3
"""Validate skill metadata, Python/JSON syntax and the recorded upstream snapshot.

Run: python scripts/validate-skills.py
Optional PyYAML enables full YAML parsing; core checks use the standard library.
"""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import re
import sys


def content_hash(data: bytes) -> str:
    """Ignore Git checkout newline conversion for UTF-8 text only."""
    if b"\0" not in data:
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            pass
        else:
            data = data.replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    errors: list[str] = []
    try:
        import yaml
    except ImportError:
        yaml = None
    skills = sorted(p for p in (root / "skills").iterdir() if (p / "SKILL.md").is_file())
    agents = [p for p in (root / "agents").glob("*.md") if p.read_text(encoding="utf-8-sig").startswith("---")]
    for skill in skills:
        text = (skill / "SKILL.md").read_text(encoding="utf-8-sig")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        if not match:
            errors.append(f"{skill.name}: missing YAML frontmatter")
            continue
        try:
            if yaml:
                metadata = yaml.safe_load(match.group(1))
                if not isinstance(metadata, dict) or metadata.get("name") != skill.name or not metadata.get("description"):
                    errors.append(f"{skill.name}: invalid name or description")
            else:
                name = re.search(r"^name:\s*([^\r\n]+)", match.group(1), re.M)
                if not name or name.group(1).strip().strip("\"'") != skill.name or not re.search(r"^description:\s*\S", match.group(1), re.M):
                    errors.append(f"{skill.name}: invalid name or description")
        except Exception as exc:
            errors.append(f"{skill.name}: {exc}")

    lock = json.loads((root / "docs/upstream-skills-lock.json").read_text(encoding="utf-8"))
    if lock.get("hash_format") != "sha256-utf8-lf":
        errors.append("unknown lock hash format")
    expected: dict[str, str] = {}
    for entry in lock["entries"]:
        for name, digest in entry["installed_sha256"].items():
            if name in expected and expected[name] != digest:
                errors.append(f"conflicting snapshot records: {name}")
            expected[name] = digest
    python_count = json_count = 0
    for name, digest in expected.items():
        path = root / name
        if not path.resolve().is_relative_to(root):
            errors.append(f"snapshot path outside repository: {name}")
            continue
        if not path.is_file():
            errors.append(f"missing snapshot file: {name}")
            continue
        data = path.read_bytes()
        if content_hash(data) != digest:
            errors.append(f"snapshot hash mismatch: {name}")
        try:
            if path.suffix == ".py":
                python_count += 1
                ast.parse(data.decode("utf-8-sig"), filename=name)
            elif path.suffix == ".json":
                json_count += 1
                json.loads(data.decode("utf-8-sig"))
        except Exception as exc:
            errors.append(f"syntax: {name}: {exc}")

    plugin = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    if plugin.get("name") != "sean-s-skills":
        errors.append("invalid plugin name")
    print(f"Skills: {len(skills)}; agents: {len(agents)}; snapshot files: {len(expected)}; Python: {python_count}; JSON: {json_count}")
    print("Metadata: " + ("full YAML parser" if yaml else "name/description only; install PyYAML for full YAML validation"))
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Errors: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
