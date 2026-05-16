#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validate a minimal L1/L2 DSR documentation package.

This validator intentionally checks only the lightweight pathway. It does not
replace the repository's full package validator.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None


L1_KEY = "minimal_l1_documentation_record"
L2_KEY = "minimal_l2_reviewable_documentation_record"


class ValidationError(Exception):
    pass


def load_yaml(path: pathlib.Path) -> dict[str, Any]:
    if yaml is None:
        raise ValidationError("PyYAML is required: pip install pyyaml")
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"Could not parse YAML {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValidationError(f"YAML root must be a mapping: {path}")
    return data


def is_blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def require_path(record: dict[str, Any], dotted_path: str, errors: list[str]) -> None:
    current: Any = record
    for part in dotted_path.split("."):
        if not isinstance(current, dict) or part not in current:
            errors.append(f"missing required field: {dotted_path}")
            return
        current = current[part]
    if is_blank(current):
        errors.append(f"blank required field: {dotted_path}")


def require_false(record: dict[str, Any], dotted_path: str, errors: list[str]) -> None:
    current: Any = record
    for part in dotted_path.split("."):
        if not isinstance(current, dict) or part not in current:
            errors.append(f"missing required field: {dotted_path}")
            return
        current = current[part]
    if current is not False:
        errors.append(f"field must be false for minimal pathway: {dotted_path}")


def find_record(package_path: pathlib.Path) -> tuple[pathlib.Path, str, dict[str, Any]]:
    candidates = [package_path]
    if package_path.is_dir():
        candidates = sorted(package_path.glob("*.yaml")) + sorted(package_path.glob("*.yml"))
    for candidate in candidates:
        if not candidate.is_file():
            continue
        data = load_yaml(candidate)
        if L2_KEY in data and isinstance(data[L2_KEY], dict):
            return candidate, L2_KEY, data[L2_KEY]
        if L1_KEY in data and isinstance(data[L1_KEY], dict):
            return candidate, L1_KEY, data[L1_KEY]
    raise ValidationError(f"No {L1_KEY} or {L2_KEY} record found in {package_path}")


def validate_l1(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for path in [
        "record_metadata.record_id",
        "record_metadata.responsible_party",
        "record_metadata.review_status",
        "record_metadata.conformance_target",
        "record_metadata.tailoring_rationale",
        "identity.artifact_id",
        "identity.title",
        "identity.version",
        "identity.authors_or_creators",
        "identity.license.spdx_id",
        "identity.license.license_rationale",
        "identity.maintenance_status",
        "scope.purpose",
        "scope.intended_audience",
        "scope.artifact_type",
        "scope.artifact_boundary",
    ]:
        require_path(record, path, errors)
    require_false(record, "record_metadata.full_l4_package_adopted", errors)
    return errors


def validate_l2(record: dict[str, Any]) -> list[str]:
    errors = validate_l1(record)
    for path in [
        "problem_space.problem_instance",
        "problem_space.problem_class",
        "problem_space.relevance_justification",
        "problem_space.stakeholders",
        "problem_space.context",
        "problem_space.boundary_conditions",
        "solution_and_design_space.objectives",
        "solution_and_design_space.requirements",
        "solution_and_design_space.artifact_or_design_entity.artifact_name",
        "solution_and_design_space.artifact_or_design_entity.artifact_boundary",
        "solution_and_design_space.design_decisions",
        "demonstration_and_evaluation.demonstration.status",
        "demonstration_and_evaluation.evaluation.status",
        "demonstration_and_evaluation.evaluation.criteria",
        "contribution_and_reuse.contribution_claim.statement",
        "contribution_and_reuse.contribution_claim.evidence_basis",
        "contribution_and_reuse.not_claimed",
        "traceability.trace_edges",
        "review.review_result",
        "review.acceptance_criteria",
    ]:
        require_path(record, path, errors)

    trace_edges = record.get("traceability", {}).get("trace_edges", [])
    if not isinstance(trace_edges, list) or len(trace_edges) < 5:
        errors.append("L2 record must include at least five traceability edges")
    else:
        edge_types = {edge.get("edge_type") for edge in trace_edges if isinstance(edge, dict)}
        for required_edge_type in {
            "problem_to_requirement",
            "requirement_to_design_decision",
            "design_decision_to_evaluation",
            "evaluation_to_contribution",
            "contribution_to_boundary_condition",
        }:
            if required_edge_type not in edge_types:
                errors.append(f"missing L2 traceability edge type: {required_edge_type}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Package directory or YAML record to validate")
    parser.add_argument("--level", choices=["l1", "l2"], default="l1")
    parser.add_argument("--json", action="store_true", help="Emit JSON summary")
    args = parser.parse_args()

    package_path = pathlib.Path(args.path)
    try:
        record_path, key, record = find_record(package_path)
        errors = validate_l1(record) if args.level == "l1" else validate_l2(record)
        if args.level == "l2" and key != L2_KEY:
            errors.append(f"--level l2 requires {L2_KEY}, found {key}")
    except ValidationError as exc:
        errors = [str(exc)]
        record_path = package_path
        key = "none"

    summary = {
        "path": str(record_path),
        "record_key": key,
        "level": args.level,
        "ok": not errors,
        "errors": errors,
    }
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    elif errors:
        print("Minimal L1/L2 validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
    else:
        print(f"Minimal L1/L2 validation passed for {record_path} at {args.level}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
