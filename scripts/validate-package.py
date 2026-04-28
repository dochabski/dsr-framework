#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validate the DSR Framework package structure and controlled files."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import tomllib
import urllib.parse
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - dependency guard
    raise SystemExit("Missing dependency: PyYAML. Install with `pip install pyyaml`.") from exc

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - dependency guard
    raise SystemExit("Missing dependency: jsonschema. Install with `pip install jsonschema`.") from exc


ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = ROOT / "records" / "validation" / "validation-summary-latest.json"

IGNORED_ACTUAL_PATHS = {
    ".gitignore",
    "FRAMEWORK_AUDIT_2026-04-27.md",
}
IGNORED_ACTUAL_PREFIXES = {
    ".git/",
    "__pycache__/",
    "_unmapped/",
}

SCHEMA_INSTANCE_PAIRS = {
    "schemas/artifact-profile.schema.json": [
        "artifact-profile.yaml",
        "templates/artifact-profile-template.yaml",
    ],
    "schemas/package-inventory.schema.json": [
        "package-inventory.yaml",
        "templates/package-inventory-template.yaml",
    ],
    "schemas/conformance-declaration.schema.json": [
        "conformance-declaration.yaml",
        "templates/conformance-declaration-template.yaml",
    ],
    "schemas/dsr-evaluation-plan.schema.json": [
        "templates/evaluation-plan-template.yaml",
        "records/evaluations/record-evaluation-plan-0001.yaml",
    ],
    "schemas/dsr-evaluation-report.schema.json": [
        "templates/evaluation-report-template.yaml",
    ],
    "schemas/dsr-contribution-claim.schema.json": [
        "templates/contribution-claim-template.yaml",
    ],
    "schemas/dsr-transparency-crosswalk.schema.json": [
        "templates/dsr-transparency-crosswalk-template.yaml",
        "records/dsr-transparency/record-dsr-transparency-crosswalk-0001.yaml",
    ],
}


class ValidationRun:
    def __init__(self, release_candidate: bool) -> None:
        self.release_candidate = release_candidate
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.counts: dict[str, int] = {}

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_ignored(path: str) -> bool:
    return path in IGNORED_ACTUAL_PATHS or any(path.startswith(prefix) for prefix in IGNORED_ACTUAL_PREFIXES)


def iter_files() -> list[Path]:
    return sorted(
        p
        for p in ROOT.rglob("*")
        if p.is_file() and not is_ignored(rel(p))
    )


def load_yaml_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate_parseability(run: ValidationRun) -> None:
    yaml_count = json_count = toml_count = 0
    for path in iter_files():
        rpath = rel(path)
        try:
            if path.suffix in {".yaml", ".yml"} or path.name == "CITATION.cff":
                load_yaml_file(path)
                yaml_count += 1
            elif path.suffix == ".json":
                json.loads(path.read_text(encoding="utf-8"))
                json_count += 1
            elif path.suffix == ".toml":
                tomllib.loads(path.read_text(encoding="utf-8"))
                toml_count += 1
        except Exception as exc:
            run.error(f"{rpath}: parse failed: {exc}")
    run.counts["yaml_or_cff_files_parsed"] = yaml_count
    run.counts["json_files_parsed"] = json_count
    run.counts["toml_files_parsed"] = toml_count


def validate_json_schemas(run: ValidationRun) -> None:
    schema_count = pair_count = 0
    for schema_path in sorted((ROOT / "schemas").glob("*.schema.json")):
        r_schema = rel(schema_path)
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            validator_cls = jsonschema.validators.validator_for(schema)
            validator_cls.check_schema(schema)
            schema_count += 1
        except Exception as exc:
            run.error(f"{r_schema}: JSON Schema meta-validation failed: {exc}")
            continue

        for instance_name in SCHEMA_INSTANCE_PAIRS.get(r_schema, []):
            instance_path = ROOT / instance_name
            if not instance_path.exists():
                run.error(f"{r_schema}: expected instance missing: {instance_name}")
                continue
            try:
                instance = load_yaml_file(instance_path)
                validator_cls(schema).validate(instance)
                pair_count += 1
            except Exception as exc:
                run.error(f"{instance_name}: schema validation failed against {r_schema}: {exc}")

    run.counts["json_schemas_meta_validated"] = schema_count
    run.counts["schema_instance_pairs_validated"] = pair_count


def validate_inventory(run: ValidationRun) -> dict[str, Any]:
    inventory_path = ROOT / "package-inventory.yaml"
    inventory = load_yaml_file(inventory_path)["package_inventory"]
    entries = inventory.get("file_inventory", [])
    inventory_paths = {entry["path"] for entry in entries}

    for entry in entries:
        path = ROOT / entry["path"]
        status = str(entry.get("inventory_status", ""))
        if path.exists():
            continue
        if status.startswith("planned_not_present") or status.startswith("not_applicable"):
            continue
        run.error(f"package-inventory.yaml: listed file missing: {entry['path']}")

    for path in iter_files():
        rpath = rel(path)
        if rpath not in inventory_paths:
            run.error(f"package-inventory.yaml: actual controlled file is not inventoried: {rpath}")

    for directory in inventory.get("directory_inventory", []):
        status = str(directory.get("directory_status", ""))
        listed = directory.get("listed_files", []) or []
        if status.startswith("planned_not_present"):
            continue
        if not (ROOT / directory["path"]).exists():
            run.error(f"package-inventory.yaml: listed directory missing: {directory['path']}")
        for listed_file in listed:
            if not (ROOT / listed_file).exists():
                run.error(f"package-inventory.yaml: directory lists missing file: {listed_file}")

    run.counts["inventory_file_entries"] = len(entries)
    run.counts["actual_controlled_files_seen"] = len(iter_files())
    return inventory


MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def validate_markdown_links(run: ValidationRun) -> None:
    checked = 0
    for path in sorted(ROOT.rglob("*.md")):
        rpath = rel(path)
        if is_ignored(rpath):
            continue
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip()
            if (
                not target
                or target.startswith("#")
                or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target)
            ):
                continue
            target = target.split("#", 1)[0]
            target = urllib.parse.unquote(target)
            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                run.warn(f"{rpath}: relative link points outside repository: {target}")
                continue
            checked += 1
            if not target_path.exists():
                run.warn(f"{rpath}: relative link target not found: {target}")
    run.counts["markdown_relative_links_checked"] = checked


def validate_release_status_consistency(run: ValidationRun) -> None:
    metadata = load_yaml_file(ROOT / "metadata.yaml")
    release_readiness = metadata["versioning_and_release"]["release_readiness"]
    if release_readiness.get("release_candidate") is not False:
        run.error("metadata.yaml: release_readiness.release_candidate must be false for v0.1.0 public draft.")
    if release_readiness.get("archival_publication_ready") is not False:
        run.error(
            "metadata.yaml: release_readiness.archival_publication_ready must be false unless L5 gates are complete."
        )

    release_record = load_yaml_file(ROOT / "records/releases/record-release-0001-v0-1-0.yaml")["release_record"]
    if release_record.get("conformance_target") == "l5_archival_publication_ready":
        run.error("v0.1.0 release record must not target l5_archival_publication_ready.")

    restricted_patterns = {
        "archival_publication_ready: true": "archival publication readiness true flag",
        "conformance_target: l5_archival_publication_ready": "L5 conformance target",
    }
    for path in [
        ROOT / "metadata.yaml",
        ROOT / "manifest.yaml",
        ROOT / "package-inventory.yaml",
        ROOT / "conformance-declaration.yaml",
        ROOT / "artifact-profile.yaml",
        ROOT / "records/releases/record-release-0001-v0-1-0.yaml",
    ]:
        text = path.read_text(encoding="utf-8")
        for pattern, label in restricted_patterns.items():
            if pattern in text:
                run.error(f"{rel(path)}: contains restricted {label}: {pattern}")


TODO_RE = re.compile(r"\b(TODO|TBD|FIXME|not_yet_mapped|not_yet_generated|not_yet_available)\b", re.IGNORECASE)


def validate_deferred_markers(run: ValidationRun) -> None:
    marker_count = 0
    for path in iter_files():
        if path.suffix.lower() not in {".yaml", ".yml", ".md", ".json", ".cff", ".toml"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        matches = TODO_RE.findall(text)
        if matches:
            marker_count += len(matches)
            if run.release_candidate:
                run.error(f"{rel(path)}: contains deferred/TODO markers in release-candidate mode.")
    run.counts["deferred_or_todo_markers"] = marker_count
    if marker_count:
        run.warn(f"Found {marker_count} deferred/TODO markers; acceptable for public draft, not for release-candidate mode.")


def validate_release_candidate_gates(run: ValidationRun) -> None:
    if not run.release_candidate:
        return
    required_record_dirs = [
        ("records/reviews", ("*.yaml",)),
        ("records/releases", ("*.yaml",)),
        ("records/preservation", ("*.yaml",)),
        ("records/validation", ("*.yaml", "*.json")),
    ]
    for directory, patterns in required_record_dirs:
        files = [file for pattern in patterns for file in (ROOT / directory).glob(pattern)]
        if not files:
            run.error(f"{directory}: release-candidate mode requires at least one retained validation or record file.")


def write_summary(run: ValidationRun, inventory: dict[str, Any]) -> None:
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    summary = {
        "validation_summary": {
            "generated_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
            "repository": "dochabski/dsr-framework",
            "mode": "release_candidate" if run.release_candidate else "public_draft",
            "result": "pass" if not run.errors else "fail",
            "error_count": len(run.errors),
            "warning_count": len(run.warnings),
            "counts": run.counts,
            "errors": run.errors,
            "warnings": run.warnings,
            "inventory_status": {
                "package_status": inventory.get("status"),
                "conformance_target": inventory.get("conformance_target"),
                "controlled_file_inventory_entries": inventory.get("normalization_status", {}).get(
                    "controlled_file_inventory_entries"
                ),
            },
        }
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--release-candidate",
        action="store_true",
        help="Treat deferred markers and missing release records as errors.",
    )
    parser.add_argument(
        "--write-summary",
        action="store_true",
        help=f"Write validation summary to {SUMMARY_PATH.relative_to(ROOT).as_posix()}.",
    )
    args = parser.parse_args()

    run = ValidationRun(release_candidate=args.release_candidate)

    validate_parseability(run)
    validate_json_schemas(run)
    inventory = validate_inventory(run)
    validate_markdown_links(run)
    validate_release_status_consistency(run)
    validate_deferred_markers(run)
    validate_release_candidate_gates(run)

    if args.write_summary:
        write_summary(run, inventory)

    result = {
        "result": "pass" if not run.errors else "fail",
        "error_count": len(run.errors),
        "warning_count": len(run.warnings),
        "counts": run.counts,
    }
    print(json.dumps(result, indent=2))
    if run.errors:
        print("\nErrors:", file=sys.stderr)
        for error in run.errors:
            print(f"- {error}", file=sys.stderr)
    if run.warnings:
        print("\nWarnings:", file=sys.stderr)
        for warning in run.warnings:
            print(f"- {warning}", file=sys.stderr)
    return 1 if run.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
