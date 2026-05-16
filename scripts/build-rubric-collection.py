#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Build the unified DSR assessment rubric collection."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - dependency guard
    raise SystemExit("Missing dependency: PyYAML. Install with `pip install pyyaml`.") from exc


ROOT = Path(__file__).resolve().parents[1]
RUBRICS_DIR = ROOT / "rubrics"
OUTPUT_PATH = RUBRICS_DIR / "dsr_assessment_rubrics_unified.yaml"

PREFERRED_ORDER = [
    "problem_research_worthiness_rubric",
    "problem_solvability_rubric",
    "problem_framing_quality_rubric",
    "context_stakeholder_adequacy_rubric",
    "requirements_traceability_rubric",
    "input_knowledge_solution_grounding_rubric",
    "design_rationale_build_trace_rubric",
    "demonstration_use_readiness_rubric",
    "evaluation_alignment_quality_rubric",
    "contribution_quality_rubric",
    "projectability_boundary_conditions_rubric",
    "reliability_replication_readiness_rubric",
    "responsible_design_constraints_rubric",
    "repository_documentation_conformance_rubric",
    "transparency_trace_quality_rubric",
]

SNAKE_CASE_RE = re.compile(r"^[a-z][a-z0-9_]*$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_rubric(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    if not isinstance(loaded, dict) or "rubric" not in loaded:
        raise ValueError(f"{path.name}: expected top-level `rubric` key")
    rubric = loaded["rubric"]
    if not isinstance(rubric, dict):
        raise ValueError(f"{path.name}: `rubric` must be a mapping")
    metadata = rubric.get("rubric_metadata")
    if not isinstance(metadata, dict):
        raise ValueError(f"{path.name}: expected `rubric.rubric_metadata` mapping")
    rubric_id = metadata.get("id")
    if not rubric_id:
        raise ValueError(f"{path.name}: expected `rubric.rubric_metadata.id`")
    if not SNAKE_CASE_RE.match(str(rubric_id)):
        raise ValueError(f"{path.name}: rubric id must use lower snake case: {rubric_id}")
    return loaded


def normalize_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def metadata_value(metadata: dict[str, Any], key: str) -> Any:
    value = metadata.get(key)
    if value is None:
        return None
    return value


def sort_key(item: dict[str, Any]) -> tuple[int, str]:
    rubric_id = item["rubric_id"]
    try:
        return (PREFERRED_ORDER.index(rubric_id), item["source_file"])
    except ValueError:
        return (len(PREFERRED_ORDER), item["source_file"])


def build_collection(generated_on: str) -> dict[str, Any]:
    if not RUBRICS_DIR.exists():
        raise SystemExit(f"Rubrics directory not found: {RUBRICS_DIR}")

    source_paths = sorted(
        path
        for path in RUBRICS_DIR.glob("*_rubric.yaml")
        if path.name != OUTPUT_PATH.name
    )
    if not source_paths:
        raise SystemExit("No individual rubric YAML files found.")

    items: list[dict[str, Any]] = []
    seen_ids: dict[str, str] = {}
    duplicate_ids: list[str] = []

    for path in source_paths:
        loaded = load_rubric(path)
        rubric = loaded["rubric"]
        metadata = rubric["rubric_metadata"]
        rubric_id = str(metadata["id"])
        if rubric_id in seen_ids:
            duplicate_ids.append(rubric_id)
        seen_ids[rubric_id] = path.name
        local_file_name = metadata.get("local_file_name")
        intended_file_path = metadata.get("intended_file_path")
        expected_path = f"rubrics/{path.name}"
        warnings: list[str] = []
        if local_file_name and str(local_file_name) != path.name:
            warnings.append(f"local_file_name differs from source file name: {local_file_name}")
        if intended_file_path and str(intended_file_path) != expected_path:
            warnings.append(f"intended_file_path differs from repository path: {intended_file_path}")
        items.append(
            {
                "source_file": path.name,
                "source_sha256": sha256(path),
                "rubric_id": rubric_id,
                "label": metadata_value(metadata, "label"),
                "version": metadata_value(metadata, "version"),
                "status": metadata_value(metadata, "status"),
                "priority": metadata_value(metadata, "priority"),
                "lifecycle_phase": metadata_value(metadata, "lifecycle_phase"),
                "assessment_target": metadata_value(metadata, "assessment_target"),
                "prompt_id": metadata_value(metadata, "prompt_id"),
                "depends_on": normalize_list(metadata.get("depends_on")),
                "intended_file_path": expected_path,
                "rubric": rubric,
                "warnings": warnings,
            }
        )

    if duplicate_ids:
        raise SystemExit(f"Duplicate rubric IDs found: {sorted(set(duplicate_ids))}")

    items = sorted(items, key=sort_key)
    known_ids = {item["rubric_id"] for item in items}
    missing_dependency_map: dict[str, list[str]] = {}
    for item in items:
        for dependency in item["depends_on"]:
            if dependency and dependency not in known_ids:
                missing_dependency_map.setdefault(dependency, []).append(item["rubric_id"])

    source_warnings = [
        {"rubric_id": item["rubric_id"], "warnings": item["warnings"]}
        for item in items
        if item["warnings"]
    ]
    missing_dependency_references = [
        {
            "missing_rubric_id": missing_id,
            "referenced_by": sorted(refs),
        }
        for missing_id, refs in sorted(missing_dependency_map.items())
    ]
    warnings: list[str] = []
    if missing_dependency_references:
        warnings.append(
            "Some rubrics reference dependency rubric IDs not present in this collection; these are reported, not fabricated."
        )
    if source_warnings:
        warnings.append("Some rubric metadata differs from repository import paths; inspect source_file_warnings.")

    rubric_index = []
    rubric_records = []
    for sequence, item in enumerate(items, start=1):
        index_entry = {
            "sequence": sequence,
            "rubric_id": item["rubric_id"],
            "label": item["label"],
            "source_file": item["source_file"],
            "source_sha256": item["source_sha256"],
            "version": item["version"],
            "status": item["status"],
            "priority": item["priority"],
            "lifecycle_phase": item["lifecycle_phase"],
            "assessment_target": item["assessment_target"],
            "prompt_id": item["prompt_id"],
            "intended_file_path": item["intended_file_path"],
            "depends_on": item["depends_on"],
        }
        if item["warnings"]:
            index_entry["warnings"] = item["warnings"]
        rubric_index.append(index_entry)
        rubric_records.append(
            {
                "sequence": sequence,
                "source_file": item["source_file"],
                "source_sha256": item["source_sha256"],
                "rubric_id": item["rubric_id"],
                "rubric": item["rubric"],
            }
        )

    return {
        "rubric_collection": {
            "collection_metadata": {
                "id": "dsr_assessment_rubrics_unified",
                "label": "DSR Assessment Rubrics Unified Collection",
                "version": "0.1.0-draft",
                "status": "draft",
                "generated_on": generated_on,
                "generated_by": "codex",
                "collection_role": "generated_convenience_artifact",
                "canonical_source_policy": "individual_files_in_rubrics_directory_are_canonical",
                "unified_file_policy": "unified_file_is_for_review_search_ingestion_and_distribution",
                "source_directory_policy": "source_files_imported_from_local_staging_folder_without_publishing_absolute_local_paths",
                "identifier_policy": "stable_ascii_lowercase_snake_case",
                "record_preservation_policy": "each_rubric_is_preserved_as_a_distinct_collection_item",
                "sort_policy": "generation_index_order_then_filename_fallback",
                "validation_policy": {
                    "yaml_parse_policy": "single_yaml_document_parseable_by_yaml.safe_load",
                    "duplicate_rubric_id_policy": "error",
                    "missing_required_metadata_policy": "error",
                    "missing_dependency_policy": "warning_unless_dependency_should_be_in_collection",
                },
                "integrity_summary": {
                    "rubric_count": len(items),
                    "source_file_count": len(source_paths),
                    "duplicate_rubric_ids": [],
                    "missing_dependency_references": missing_dependency_references,
                    "source_file_warnings": source_warnings,
                    "warnings": warnings,
                },
            },
            "rubric_index": rubric_index,
            "rubrics": rubric_records,
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Generation date to write into collection metadata.",
    )
    args = parser.parse_args()

    collection = build_collection(args.date)
    text = yaml.safe_dump(collection, sort_keys=False, allow_unicode=False, width=120)
    OUTPUT_PATH.write_text("# SPDX-License-Identifier: CC0-1.0\n" + text, encoding="utf-8", newline="\n")
    loaded = yaml.safe_load(OUTPUT_PATH.read_text(encoding="utf-8"))
    if not isinstance(loaded, dict) or "rubric_collection" not in loaded:
        raise SystemExit("Generated collection did not parse with expected top-level key.")
    metadata = loaded["rubric_collection"]["collection_metadata"]
    print(
        "Built "
        f"{OUTPUT_PATH.relative_to(ROOT).as_posix()} with "
        f"{metadata['integrity_summary']['rubric_count']} rubrics."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
