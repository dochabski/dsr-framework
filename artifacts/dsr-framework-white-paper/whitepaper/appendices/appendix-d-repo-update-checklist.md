# Appendix D: Repository update checklist {.unnumbered}

- Create branch: `whitepaper/citation-build-fix`.
- Preserve the package under `artifacts/dsr-framework-white-paper/`.
- Update chapter source files, not only `whitepaper/whitepaper_unified.md`, because the assembly script regenerates the unified manuscript.
- Replace the manual numbered reference list with `whitepaper/references.bib` plus Pandoc citeproc.
- Preserve the full parsed source bibliography as a source registry or supplement, not as the main reference list.
- Use simple scalar author metadata so the PDF title page prints `David Ochabski`, not `true`.
- Remove the duplicate body H1 that repeats the document title.
- Remove manual leading numbers from Markdown headings when `numbersections: true` is enabled.
- Add unnumbered attributes to front matter, executive summary, appendices, and references.
- Run YAML/JSON/CFF validation already used by the repository.
- Render unified Markdown, HTML, and PDF if tooling exists.
- Confirm no L5 claims are introduced unless L5 release evidence is completed.
- Commit with a clear message: `Fix white paper citations and PDF heading build`.
- Tag only after final human edit and metadata freeze.
