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
BIDI_CONTROL_RE = re.compile(r"[\u202A-\u202E\u2066-\u2069]")
TEXT_SUFFIXES = {".yaml", ".yml", ".md", ".json", ".cff", ".toml", ".py", ".txt"}
TEXT_FILENAMES = {"CITATION.cff", ".gitattributes"}
VALIDATION_MODES = {"public_draft", "release_candidate"}

IGNORED_ACTUAL_PATHS = {
    ".gitignore",
    "FRAMEWORK_AUDIT_2026-04-27.md",
}
IGNORED_ACTUAL_PREFIXES = {
    ".git/",
    "__pycache__/",
    "_unmapped/",
}
DEFERRED_MARKER_EXEMPT_PATHS = {
    "records/validation/validation-summary-latest.json",
}

SCHEMA_INSTANCE_PAIRS = {
    "schemas/artifact-profile.schema.json": [
        "artifact-profile.yaml",
        "templates/artifact-profile-template.yaml",
    ],
    "schemas/package-inventory.schema.json": [
        "package-inventory.yaml",
        "templates/package-inventory-template.yaml",
        "examples/canonical-minimal-dsr-package/package-inventory.yaml",
    ],
    "schemas/conformance-declaration.schema.json": [
        "conformance-declaration.yaml",
        "templates/conformance-declaration-template.yaml",
    ],
    "schemas/dsr-evaluation-plan.schema.json": [
        "templates/evaluation-plan-template.yaml",
        "records/evaluations/record-evaluation-plan-0001.yaml",
        "examples/canonical-minimal-dsr-package/evaluation-plan.yaml",
    ],
    "schemas/dsr-evaluation-report.schema.json": [
        "templates/evaluation-report-template.yaml",
    ],
    "schemas/dsr-contribution-claim.schema.json": [
        "templates/contribution-claim-template.yaml",
        "examples/canonical-minimal-dsr-package/contribution-claim.yaml",
    ],
    "schemas/dsr-transparency-crosswalk.schema.json": [
        "templates/dsr-transparency-crosswalk-template.yaml",
        "records/dsr-transparency/record-dsr-transparency-crosswalk-0001.yaml",
        "examples/canonical-minimal-dsr-package/transparency-crosswalk.yaml",
    ],
}

V1_RELEASE_CANDIDATE_REQUIRED_PATHS = {
    "canonical worked example": "examples/canonical-minimal-dsr-package/README.md",
    "claim-level traceability crosswalk": "crosswalks/claim-to-source-traceability.yaml",
    "source anomaly disposition review": "records/reviews/record-review-source-anomaly-disposition-0001-v1-0-0.yaml",
    "template and checklist stabilization review": "records/reviews/record-review-template-checklist-stabilization-0001-v1-0-0.yaml",
    "schema hardening review": "records/reviews/record-review-schema-hardening-0001-v1-0-0.yaml",
    "completeness review": "records/reviews/record-review-0002-completeness-v1-0-0.yaml",
    "kick-the-tires review": "records/reviews/record-review-0003-kick-the-tires-v1-0-0.yaml",
    "full review": "records/reviews/record-review-0004-full-review-v1-0-0.yaml",
    "author response": "records/reviews/record-author-response-0001-v1-0-0.yaml",
    "metadata freeze": "records/releases/record-metadata-freeze-0001-v1-0-0.yaml",
    "v1 release record": "records/releases/record-release-0002-v1-0-0.yaml",
    "release approval": "records/releases/record-release-approval-0001-v1-0-0.yaml",
}

L5_CLAIM_PATTERNS = {
    "l5_claimed: true": "L5 claimed flag",
    "archival_publication_ready: true": "archival publication readiness true flag",
    "package_conformance: l5_archival_publication_ready": "L5 package conformance claim",
    "conformance_claim_supported: l5_archival_publication_ready": "L5 supported conformance claim",
}


class ValidationRun:
    def __init__(self, mode: str = "public_draft") -> None:
        if mode not in VALIDATION_MODES:
            raise ValueError(f"Unsupported validation mode: {mode}")
        self.mode = mode
        self.release_candidate = mode == "release_candidate"
        self.validation_scope = "v1_l4_release_candidate" if self.release_candidate else "public_draft"
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.counts: dict[str, int] = {}
        self.notes: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def note(self, message: str) -> None:
        self.notes.append(message)


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


def walk_values(value: Any) -> list[str]:
    if isinstance(value, dict):
        values: list[str] = []
        for item in value.values():
            values.extend(walk_values(item))
        return values
    if isinstance(value, list):
        values = []
        for item in value:
            values.extend(walk_values(item))
        return values
    if value is None:
        return []
    return [str(value)]


def iter_text_files() -> list[Path]:
    return [path for path in iter_files() if path.suffix.lower() in TEXT_SUFFIXES or path.name in TEXT_FILENAMES]


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
    docs_pages = 0
    docs_pages_with_yaml_links = 0
    for path in sorted(ROOT.rglob("*.md")):
        rpath = rel(path)
        if is_ignored(rpath):
            continue
        text = path.read_text(encoding="utf-8")
        page_yaml_links = 0
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
            if target.endswith((".yaml", ".yml", ".json", ".schema.json")):
                page_yaml_links += 1
            if not target_path.exists():
                run.warn(f"{rpath}: relative link target not found: {target}")
        if rpath.startswith("docs/protocol/"):
            docs_pages += 1
            if page_yaml_links:
                docs_pages_with_yaml_links += 1
            else:
                run.warn(f"{rpath}: docs/protocol page has no Markdown link to a controlled YAML/JSON source file.")
    run.counts["markdown_relative_links_checked"] = checked
    run.counts["docs_protocol_pages_checked"] = docs_pages
    run.counts["docs_protocol_pages_with_controlled_source_links"] = docs_pages_with_yaml_links


def validate_unicode_controls(run: ValidationRun) -> None:
    findings = 0
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if BIDI_CONTROL_RE.search(line):
                findings += 1
                run.error(f"{rel(path)}:{line_number}: hidden or bidirectional Unicode control character detected.")
    run.counts["unicode_control_findings"] = findings


def validate_release_status_consistency(run: ValidationRun) -> None:
    metadata = load_yaml_file(ROOT / "metadata.yaml")
    release_readiness = metadata["versioning_and_release"]["release_readiness"]
    current_state = str(release_readiness.get("current_state", ""))
    if current_state == "0.1.0_public_draft" and release_readiness.get("release_candidate") is not False:
        run.error("metadata.yaml: release_readiness.release_candidate must be false for v0.1.0 public draft.")
    if release_readiness.get("archival_publication_ready") is not False:
        run.error(
            "metadata.yaml: release_readiness.archival_publication_ready must remain false unless L5 gates are complete."
        )

    release_record = load_yaml_file(ROOT / "records/releases/record-release-0001-v0-1-0.yaml")["release_record"]
    if release_record.get("conformance_target") == "l5_archival_publication_ready":
        run.error("v0.1.0 release record must not target l5_archival_publication_ready.")

    confirmed = release_record.get("confirmed_public_draft_facts", {})
    required_confirmed_facts = {
        "release_tag": "v0.1.0",
        "release_url": "https://github.com/dochabski/dsr-framework/releases/tag/v0.1.0",
        "zenodo_doi": "10.5281/zenodo.19835424",
        "zenodo_record_url": "https://zenodo.org/records/19835424",
    }
    for key, expected in required_confirmed_facts.items():
        if confirmed.get(key) != expected:
            run.error(f"release record: confirmed_public_draft_facts.{key} must be {expected!r}.")

    stale_release_phrases = [
        "No DOI, Zenodo, GitHub release",
        "Has the v0.1.0 repository tag been created",
        "Will v0.1.0 be deposited in Zenodo",
        "Verify archive or DOI metadata",
        "Unverified repository, archive, DOI",
        "evidence_status: " + "TO" + "DO",
    ]
    release_text = "\n".join(walk_values(release_record))
    for phrase in stale_release_phrases:
        if phrase in release_text:
            run.error(f"release record: stale public-draft contradiction remains: {phrase}")

    restricted_patterns = {
        **L5_CLAIM_PATTERNS,
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


def expected_package_conformance(inventory: dict[str, Any]) -> str:
    status = str(inventory.get("status", ""))
    package_conformance = str(inventory.get("package_conformance", ""))
    if status.startswith("1.0.0") or package_conformance == "l4_reusable_stable":
        return "l4_reusable_stable"
    return "l2_reviewable_qualified_public_draft"


def validate_conformance_scope(run: ValidationRun, inventory: dict[str, Any]) -> None:
    expected_conformance = expected_package_conformance(inventory)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "file_conformance: l1_documented" not in readme:
        run.error("README.md: missing explicit conformance scope field: file_conformance: l1_documented")
    if f"package_conformance: {expected_conformance}" not in readme:
        run.error(f"README.md: missing explicit current package conformance field: package_conformance: {expected_conformance}")
    if expected_conformance == "l2_reviewable_qualified_public_draft" and "v1_target_package_conformance: l4_reusable_stable" not in readme:
        run.error("README.md: missing v1 target field while package remains a public draft.")
    if "conformance_target:" in readme.split("-->", 1)[0]:
        run.error("README.md: front-matter comment must not use ambiguous conformance_target.")

    manifest = load_yaml_file(ROOT / "manifest.yaml")["manifest"]
    conformance = manifest.get("conformance", {})
    for old_key in [
        "generated_file_conformance_target",
        "package_default_conformance_target",
        "v1_stable_conformance_target",
    ]:
        if old_key in conformance:
            run.error(f"manifest.yaml: use explicit file/package conformance scope instead of {old_key}.")
    if conformance.get("file_conformance") != "l1_documented":
        run.error("manifest.yaml: conformance.file_conformance must be l1_documented.")
    if conformance.get("package_conformance") != expected_conformance:
        run.error(f"manifest.yaml: conformance.package_conformance must be {expected_conformance}.")
    if expected_conformance == "l2_reviewable_qualified_public_draft" and conformance.get("v1_target_package_conformance") != "l4_reusable_stable":
        run.error("manifest.yaml: conformance.v1_target_package_conformance must be l4_reusable_stable.")

    if "conformance_target" in inventory:
        run.error("package-inventory.yaml: use package_conformance instead of ambiguous conformance_target.")
    if inventory.get("package_conformance") != expected_conformance:
        run.error(f"package-inventory.yaml: package_conformance must be {expected_conformance}.")

    artifact = load_yaml_file(ROOT / "artifact-profile.yaml")["artifact_profile"]
    selection = artifact.get("selection_metadata", {})
    if "conformance_target" in selection:
        run.error("artifact-profile.yaml: selection_metadata must not use ambiguous conformance_target.")
    quality = artifact.get("quality_and_conformance_profile", {})
    if "current_conformance_level" in quality:
        run.error("artifact-profile.yaml: use current_package_conformance_level and file_conformance.")
    if quality.get("file_conformance", {}).get("id") != "l1_documented":
        run.error("artifact-profile.yaml: quality_and_conformance_profile.file_conformance.id must be l1_documented.")
    if quality.get("current_package_conformance_level", {}).get("id") != expected_conformance:
        run.error(f"artifact-profile.yaml: current_package_conformance_level.id must be {expected_conformance}.")

    for entry in inventory.get("file_inventory", []):
        if str(entry.get("default_conformance", "")).lower() == "l5":
            scope = str(entry.get("default_conformance_scope", ""))
            if "not_package_claim" not in scope and "source_selection" not in scope:
                run.error(
                    "package-inventory.yaml: default_conformance l5 must be explicitly scoped as historical or not a package claim "
                    f"for {entry.get('path')}."
                )

    release_record_text = (ROOT / "records/releases/record-release-0001-v0-1-0.yaml").read_text(encoding="utf-8")
    if re.search(r"(?m)^\s+default_conformance:\s*", release_record_text):
        run.error("release record: default_conformance must be renamed or scoped so it cannot read as a current target.")

    conformance_declaration = load_yaml_file(ROOT / "conformance-declaration.yaml")["conformance_declaration"]
    declaration = conformance_declaration.get("declaration", {})
    if declaration.get("current_package_conformance", {}).get("id") != expected_conformance:
        run.error(f"conformance-declaration.yaml: declaration.current_package_conformance.id must be {expected_conformance}.")
    if declaration.get("file_conformance", {}).get("id") != "l1_documented":
        run.error("conformance-declaration.yaml: declaration.file_conformance.id must be l1_documented.")
    if expected_conformance == "l2_reviewable_qualified_public_draft" and declaration.get("v1_target_package_conformance", {}).get("id") != "l4_reusable_stable":
        run.error("conformance-declaration.yaml: declaration.v1_target_package_conformance.id must be l4_reusable_stable.")

    catalog_ids = {
        item.get("level_id")
        for item in conformance_declaration.get("conformance_level_catalog", [])
        if isinstance(item, dict)
    }
    if expected_conformance == "l2_reviewable_qualified_public_draft" and "l2_reviewable_qualified_public_draft" not in catalog_ids:
        run.error("conformance-declaration.yaml: conformance catalog must include l2_reviewable_qualified_public_draft or an explicit mapping.")

    conformance_text = (ROOT / "conformance-declaration.yaml").read_text(encoding="utf-8")
    stale_conformance_phrases = [
        "must not claim L2 or higher",
        "prevents_l2_or_higher_package_claim",
        "L1 is declared and higher-level claims are explicitly reserved",
        "claims L2 or higher conformance without",
    ]
    if declaration.get("current_package_conformance", {}).get("id") == "l2_reviewable_qualified_public_draft":
        for phrase in stale_conformance_phrases:
            if phrase in conformance_text:
                run.error(f"conformance-declaration.yaml: stale L1-era conformance phrase remains: {phrase}")


def validate_public_draft_metadata_status(run: ValidationRun) -> None:
    inventory_text = (ROOT / "package-inventory.yaml").read_text(encoding="utf-8")
    manifest_text = (ROOT / "manifest.yaml").read_text(encoding="utf-8")
    stale_inventory_phrases = [
        "needs_creator_repository_and_release_metadata",
        "do_not_publish_until_metadata_confirmed",
        "needs_public_metadata_confirmation",
        "retain " + "TO" + "DO" + " values until public repository, creator, release, and archival details are confirmed",
    ]
    for phrase in stale_inventory_phrases:
        if phrase in inventory_text:
            run.error(f"package-inventory.yaml: stale unconfirmed public-draft metadata status remains: {phrase}")

    stale_manifest_statuses = [
        "present_release_metadata_updated_with_reserved_doi",
        "present_release_metadata_updated_pending_publish_confirmation",
        "present_draft_needs_public_metadata_confirmation",
    ]
    for phrase in stale_manifest_statuses:
        if phrase in manifest_text:
            run.error(f"manifest.yaml: stale unconfirmed public-draft metadata status remains: {phrase}")

    inventory = load_yaml_file(ROOT / "package-inventory.yaml")["package_inventory"]
    expected_conformance = expected_package_conformance(inventory)
    root_status_by_path = {
        entry.get("path"): entry.get("current_status")
        for entry in inventory.get("root_file_inventory", [])
        if isinstance(entry, dict)
    }
    if expected_conformance == "l4_reusable_stable":
        expected_statuses = {
            "CITATION.cff": "present_v1_citation_metadata_frozen_1_0_0",
            ".zenodo.json": "present_v1_zenodo_metadata_prepared_l5_not_claimed",
            "metadata.yaml": "present_v1_metadata_frozen_1_0_0",
        }
    else:
        expected_statuses = {
            "CITATION.cff": "present_public_draft_metadata_confirmed_v0_1_0_v1_freeze_pending",
            ".zenodo.json": "present_public_draft_zenodo_metadata_confirmed_v0_1_0_l5_preservation_pending",
            "metadata.yaml": "present_public_draft_metadata_confirmed_v0_1_0_v1_freeze_pending",
        }
    for path, expected in expected_statuses.items():
        if root_status_by_path.get(path) != expected:
            run.error(f"package-inventory.yaml: root_file_inventory status for {path} must be {expected}.")

    manifest = load_yaml_file(ROOT / "manifest.yaml")["manifest"]
    manifest_root_status_by_path = {
        entry.get("path"): entry.get("validation_status")
        for entry in manifest.get("repository_architecture", {}).get("required_root_files", [])
        if isinstance(entry, dict)
    }
    if expected_conformance == "l4_reusable_stable":
        expected_manifest_statuses = {
            "CITATION.cff": "present_v1_citation_metadata_frozen_1_0_0",
            ".zenodo.json": "present_v1_zenodo_metadata_prepared_l5_not_claimed",
            "metadata.yaml": "present_v1_metadata_frozen_1_0_0",
        }
    else:
        expected_manifest_statuses = {
            "CITATION.cff": "present_public_draft_citation_metadata_confirmed_v0_1_0_v1_freeze_pending",
            ".zenodo.json": "present_public_draft_zenodo_metadata_confirmed_v0_1_0_l5_preservation_pending",
            "metadata.yaml": "present_public_draft_metadata_confirmed_v0_1_0_v1_freeze_pending",
        }
    for path, expected in expected_manifest_statuses.items():
        if manifest_root_status_by_path.get(path) != expected:
            run.error(f"manifest.yaml: required_root_files status for {path} must be {expected}.")


DEFERRED_MARKER_RE = re.compile(
    r"\b("
    + "|".join(
        [
            "TO" + "DO",
            "T" + "BD",
            "FIX" + "ME",
            "not_yet" + "_mapped",
            "not_yet" + "_generated",
            "not_yet" + "_available",
        ]
    )
    + r")\b",
    re.IGNORECASE,
)


def validate_deferred_markers(run: ValidationRun) -> None:
    marker_count = 0
    for path in iter_text_files():
        if rel(path) in DEFERRED_MARKER_EXEMPT_PATHS:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        matches = DEFERRED_MARKER_RE.findall(text)
        if matches:
            marker_count += len(matches)
            if run.release_candidate:
                run.error(f"{rel(path)}: contains deferred markers in release-candidate mode.")
    run.counts["deferred_or_todo_markers"] = marker_count
    if marker_count:
        run.warn(f"Found {marker_count} deferred markers; acceptable for public draft, not for release-candidate mode.")


def validate_release_candidate_gates(run: ValidationRun) -> None:
    if not run.release_candidate:
        return
    run.note(
        "Release-candidate mode validates v1.0.0/L4 reusable-stable readiness; explicit L5 non-claims and post-v1 L5 work do not block this mode."
    )
    if run.counts.get("inventory_file_entries") != run.counts.get("actual_controlled_files_seen"):
        run.error("package-inventory.yaml: inventory count must equal actual controlled file count in release-candidate mode.")

    for label, path in V1_RELEASE_CANDIDATE_REQUIRED_PATHS.items():
        if not (ROOT / path).exists():
            run.error(f"{path}: missing required v1 L4 release-candidate evidence ({label}).")

    v1_release_record_path = ROOT / "records/releases/record-release-0002-v1-0-0.yaml"
    if not v1_release_record_path.exists():
        return

    try:
        v1_release_record = load_yaml_file(v1_release_record_path)["release_record"]
    except Exception as exc:
        run.error(f"records/releases/record-release-0002-v1-0-0.yaml: could not load release_record: {exc}")
        return

    blockers = v1_release_record.get("v1_release_blockers", [])
    if blockers:
        run.error("records/releases/record-release-0002-v1-0-0.yaml: unresolved v1_release_blockers remain.")

    if v1_release_record.get("package_conformance") != "l4_reusable_stable":
        run.error("records/releases/record-release-0002-v1-0-0.yaml: package_conformance must be l4_reusable_stable.")

    if v1_release_record.get("l5_claimed") is True:
        run.error(
            "records/releases/record-release-0002-v1-0-0.yaml: v1.0.0 release-candidate mode must not claim L5."
        )

    for path in [
        ROOT / "records/releases/record-metadata-freeze-0001-v1-0-0.yaml",
        ROOT / "records/releases/record-release-approval-0001-v1-0-0.yaml",
    ]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern, label in L5_CLAIM_PATTERNS.items():
            if pattern in text:
                run.error(f"{rel(path)}: contains restricted {label}: {pattern}")


def write_summary(run: ValidationRun, inventory: dict[str, Any]) -> None:
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    mode = run.mode
    existing: dict[str, Any] = {}
    if SUMMARY_PATH.exists():
        try:
            existing = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {}
    validation_summary = existing.get("validation_summary", {})
    validation_runs = validation_summary.get("validation_runs", {})
    run_summary = {
        "generated_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "mode": mode,
        "validation_scope": run.validation_scope,
        "result": "pass" if not run.errors else "fail",
        "expected_failure": bool(run.release_candidate and run.errors),
        "error_count": len(run.errors),
        "warning_count": len(run.warnings),
        "counts": run.counts,
        "errors": run.errors,
        "warnings": run.warnings,
        "notes": run.notes,
    }
    validation_runs[mode] = run_summary
    summary = {
        "validation_summary": {
            "generated_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
            "repository": "dochabski/dsr-framework",
            "latest_mode": mode,
            "public_draft_result": validation_runs.get("public_draft", {}).get("result"),
            "release_candidate_result": validation_runs.get("release_candidate", {}).get("result"),
            "release_candidate_expected_failure": validation_runs.get("release_candidate", {}).get("expected_failure"),
            "release_candidate_scope": "v1.0.0_l4_reusable_stable_not_l5",
            "validation_runs": validation_runs,
            "inventory_status": {
                "package_status": inventory.get("status"),
                "package_conformance": inventory.get("package_conformance"),
                "v1_target_package_conformance": inventory.get("v1_target_package_conformance")
                or inventory.get("package_conformance"),
                "l5_claimed": inventory.get("l5_claimed"),
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
        "--mode",
        choices=sorted(VALIDATION_MODES),
        help="Validation mode. Defaults to public_draft unless --release-candidate is set.",
    )
    parser.add_argument(
        "--release-candidate",
        action="store_true",
        help="Alias for --mode release_candidate; validates v1.0.0/L4 release-candidate gates.",
    )
    parser.add_argument(
        "--write-summary",
        action="store_true",
        help=f"Write validation summary to {SUMMARY_PATH.relative_to(ROOT).as_posix()}.",
    )
    args = parser.parse_args()

    mode = args.mode or ("release_candidate" if args.release_candidate else "public_draft")
    if args.release_candidate and args.mode and args.mode != "release_candidate":
        parser.error("--release-candidate cannot be combined with --mode public_draft.")

    run = ValidationRun(mode=mode)

    validate_parseability(run)
    validate_json_schemas(run)
    inventory = validate_inventory(run)
    validate_markdown_links(run)
    validate_unicode_controls(run)
    validate_release_status_consistency(run)
    validate_conformance_scope(run, inventory)
    validate_public_draft_metadata_status(run)
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
