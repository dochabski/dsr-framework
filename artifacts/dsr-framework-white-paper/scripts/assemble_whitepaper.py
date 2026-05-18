from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORDER = [
    'chapters/00-front-matter.md',
    'chapters/01-executive-summary.md',
    'chapters/02-introduction.md',
    'chapters/03-what-dsr-is.md',
    'chapters/04-operational-model.md',
    'chapters/05-repository-native-operationalization.md',
    'chapters/06-how-we-are-operationalizing.md',
    'chapters/07-publication-and-dissemination.md',
    'chapters/08-limitations-and-roadmap.md',
    'chapters/09-conclusion.md',
    'appendices/appendix-a-source-basis.md',
    'appendices/appendix-b-platform-matrix.md',
    'appendices/appendix-c-codex-build-plan.md',
    'appendices/appendix-d-repo-update-checklist.md',
    'appendices/appendix-e-glossary.md',
    'appendices/references.md',
]
parts = []
for rel in ORDER:
    path = ROOT / 'whitepaper' / rel
    if not path.exists():
        raise FileNotFoundError(path)
    parts.append(path.read_text(encoding='utf-8').strip())
(ROOT / 'whitepaper' / 'whitepaper_unified.md').write_text('\n\n---\n\n'.join(parts) + '\n', encoding='utf-8')
print('[OK] assembled whitepaper/whitepaper_unified.md')
