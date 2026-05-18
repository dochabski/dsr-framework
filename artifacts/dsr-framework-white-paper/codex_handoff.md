# Codex Handoff Prompt

You are working in the `dochabski/dsr-framework` repository. Your task is to integrate and build a white paper package prepared from the DSR theory synthesis materials.

## High-priority constraints

- Preserve the distinction between DSR theory and this repository's operationalization of DSR.
- Do not claim L5 archival/publication-ready status unless the repository already contains explicit L5 release evidence.
- Treat GitHub as the living source of truth and Zenodo as the archival DOI release.
- Do not publish to external platforms. Prepare files and checklists only.
- Minimize token usage: read the package README, this handoff, the unified white paper, and the repository update checklist before reading any large source files.

## Integration target

Preferred path:

```text
artifacts/dsr-framework-white-paper/
```

Fallback path if the maintainer prefers public docs:

```text
docs/white-papers/dsr-framework-operationalization/
```

## Steps

1. Create branch `whitepaper/dsr-framework-operationalization`.
2. Copy this package into the integration target.
3. Run `python scripts/assemble_whitepaper.py` from the package root.
4. If Pandoc is available, run `make html` and `make pdf`; otherwise skip PDF and record that in a build note.
5. Update root README with one short entry pointing to the white paper package.
6. Update package inventory and artifacts index only if those files currently track bounded artifacts.
7. Add the decision record and release checklist from this package to the appropriate repository records path, or keep them in the subpackage if that is the repository convention.
8. Check for overclaiming: replace any accidental L5/validated/peer-reviewed claims with draft/reviewable language.
9. Prepare a concise commit.

## Do not do unless explicitly requested

- Do not read the 5 MB extraction chunks unless revising the source registry appendix.
- Do not attempt to log in to Zenodo, OSF, Octopus, Mendeley Data, Dryad, ResearchGate, Academia.edu, or OER platforms.
- Do not make new scholarly claims beyond the source files.
- Do not copy source PDFs or local absolute paths into public files.
