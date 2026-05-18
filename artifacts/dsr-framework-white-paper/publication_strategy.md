# 6. Publication and Dissemination Strategy

The publication strategy should maximize visibility without creating multiple competing sources of truth. The recommended architecture is:

- Canonical living source: GitHub.
- Archival citation snapshot: Zenodo DOI release.
- Project/discovery hub: OSF project, optional OSF Preprint.
- Research-process publication: Octopus, optional after stable modularization.
- Data-only secondary deposits: Mendeley Data or Dryad only if releasing a genuine data package.
- Profile/dissemination mirrors: ResearchGate, Academia.edu, LinkedIn, Substack, ORCID, and personal website.
- Teaching/OER derivative: OER Commons or VIVA Open only after adapting the paper into learning materials.

## Recommended platform roles

| Platform | Recommended role | Use now? | Rationale |
|---|---|---:|---|
| GitHub | Canonical living source and source-of-truth repository. | Yes | Best fit for Markdown, metadata, version control, issue review, release records, schemas, validation scripts, and repo-native DSR logic. |
| Zenodo | DOI-bearing archival snapshot of GitHub release. | Yes | Best fit for citable release snapshot and long-term scholarly reference. |
| OSF | Project/discovery hub; optional preprint and linked materials. | Yes, after GitHub release and Zenodo DOI are available | Useful for open-science visibility, supplemental files, and discovery. Keep GitHub/Zenodo canonical. |
| Octopus | Modular research-process record. | Optional | Useful if you want to publish problem, method, results/synthesis, interpretation, and application as linked units. Do after the paper is stable. |
| SSRN | Discipline-facing preprint for IS/management/social-science audiences. | Optional | Consider if you want social-science and management discovery; do not make it canonical. |
| Mendeley Data | Data package only. | Optional later | Use only for source extraction corpus, concept inventory, or artifact data that can be openly licensed and safely shared. |
| Dryad | Curated data package only. | Usually no for this paper | Not the right primary home for a white paper; use only if releasing reusable research data under compatible terms. |
| ResearchGate | Profile dissemination link or licensed full-text mirror. | Optional | Good for visibility, not canonicality. Link to GitHub/Zenodo. |
| Academia.edu | Profile dissemination link or licensed full-text mirror. | Optional | Good for visibility, not canonicality. Link to GitHub/Zenodo. |
| OER Commons / VIVA Open | Teaching derivative or workbook. | Not yet | Use after making an instructional version, not for the primary white paper. |
| arXiv | Preprint only if a suitable category and format fit. | Probably no | DSR framework and methodology may fit better on OSF Preprints or SSRN unless there is a clear computing or information science framing. |
| bioRxiv and medRxiv | Not relevant. | No | The paper is not a life science or medical preprint. |
| HAL | Optional institutional/open archive mirror. | Optional | Consider only if you want a European open-archive mirror and can maintain metadata consistency. |

The main rule is simple: do not scatter the white paper as unrelated uploads. Create one canonical GitHub release, archive it through Zenodo, then point all other platforms to that release or deposit a clearly labeled derivative.


# Appendix B. Platform Matrix

| Platform | Canonical? | Best object to post | Recommended timing | Notes |
|---|---:|---|---|---|
| GitHub | Yes | Markdown source, build files, metadata, release records | First | Use as living source of truth. |
| Zenodo | Yes for archival snapshot | GitHub release archive, PDF, unified Markdown, metadata | After GitHub release | Use DOI-bearing snapshot. |
| OSF | No | Project page, optional preprint, links to GitHub/Zenodo, supplemental files | After GitHub release and DOI | Use for discovery and open-science hub. |
| Octopus | No | Modular research-process records | After stable paper | Publish problem, method, results, interpretation, and application records if useful. |
| SSRN | No | Preprint PDF | Optional | Use if you want social science, management, and IS preprint discovery. |
| Mendeley Data | No | Data package, not paper | Optional later | Use only for data/materials that are safe and legal to share. |
| Dryad | No | Curated data package, not paper | Usually not needed | Consider only for reusable data requiring data repository curation. |
| ResearchGate | No | Link or licensed full-text mirror | After DOI | Use for visibility. |
| Academia.edu | No | Link or licensed full-text mirror | After DOI | Use for visibility. |
| OER Commons and VIVA Open | No | Teaching derivative, workbook, module | Later | Create after adapting for instruction. |
| arXiv | No | Preprint if category fit is clear | Optional, probably not first | Use only if scope fits. |
| bioRxiv and medRxiv | No | None | Never for this paper | Not relevant. |
| HAL | No | Archive mirror or preprint | Optional | Consider only with metadata consistency plan. |

Decision: keep GitHub + Zenodo as the canonical pair. Everything else should point back to that pair or be clearly labeled as a derivative.

## Rights and reuse policy

Use CC0-1.0 for original project-authored white paper text, metadata, and package materials so the paper is maximally reusable by people, repositories, indexes, and AI systems. Citation is recommended for scholarly traceability but is not a license condition. Executable tooling follows the repository code-license policy. Third-party sources, cited works, trademarks, source PDFs, and source-derived quotations are not relicensed by the white paper package.
