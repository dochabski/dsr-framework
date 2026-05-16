<!--
SPDX-License-Identifier: CC0-1.0
item_id: rubrics_process_readme
item_type: documentation
status: post_v1_3_0_repository_hardening
version: 1.3.0
-->

# Rubric Generation Process

This directory preserves process and provenance files used to generate the individual DSR assessment rubrics.

These files are not the canonical rubric artifacts. The canonical editable rubrics live directly under `rubrics/`. The unified YAML collection and JSON sidecar are generated convenience and integrity artifacts for review, search, AI ingestion, and distribution.

| File | Role |
|---|---|
| `dsr_rubric_generation_spec_v0_1_0.yaml` | Generation specification and required rubric structure. |
| `dsr_rubric_generation_index_v0_1_0.md` | Rubric sequence, dependency map, IDs, output paths, and prompt IDs. |
| `dsr_rubric_generation_prompts_v0_1_0.txt` | Prompt bank used to generate the individual rubric YAML files. |
| `prompt_stub_2026-05-15.txt` | Short local handoff stub; original source filename was `Prompt.txt`. |

Update these files only when the rubric-generation method changes. When process files change, regenerate or recheck the individual rubric YAML files, `rubrics/dsr_assessment_rubrics_unified.yaml`, and `rubrics/dsr_assessment_rubrics_unified_sidecar.json`.

This provenance package does not claim L5 archival/publication-ready status and does not replace human review of rubric quality or source-to-claim fit.
