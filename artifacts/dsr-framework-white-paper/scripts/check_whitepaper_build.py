from pathlib import Path
import re
import sys
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
md_path = ROOT / 'whitepaper' / 'whitepaper_unified.md'
meta_path = ROOT / 'build' / 'pandoc-metadata.yaml'
bib_path = ROOT / 'whitepaper' / 'references.bib'
make_path = ROOT / 'Makefile'

errors = []
text = md_path.read_text(encoding='utf-8') if md_path.exists() else ''
meta = meta_path.read_text(encoding='utf-8') if meta_path.exists() else ''
make = make_path.read_text(encoding='utf-8') if make_path.exists() else ''

if 'author: "David Ochabski"' not in meta and 'author: David Ochabski' not in meta:
    errors.append('build/pandoc-metadata.yaml should use scalar author: "David Ochabski"')

front_matter = text.split('---', 2)[1] if text.startswith('---') and text.count('---') >= 2 else ''
if 'author: "David Ochabski"' not in front_matter and 'author: David Ochabski' not in front_matter:
    errors.append('whitepaper front matter should use scalar author: "David Ochabski"')

manual_numbered = []
for n, line in enumerate(text.splitlines(), 1):
    if re.match(r'^#{1,6}\s+(\d+\.|Appendix\s+[A-Z]\.)\s+', line):
        manual_numbered.append((n, line))
if manual_numbered:
    details = '; '.join(f'L{n}: {line}' for n, line in manual_numbered[:8])
    errors.append('Manual numbered headings found while numbersections is enabled: ' + details)

if '# From Design Science Research Theory to Repository-Native Operationalization' in text:
    errors.append('Duplicate body H1 title found; the title should live only in YAML metadata/title block.')

if '--citeproc' not in make:
    errors.append('Makefile should use Pandoc --citeproc.')

if not bib_path.exists():
    errors.append('whitepaper/references.bib is missing.')
else:
    bib = bib_path.read_text(encoding='utf-8')
    for key in ['hevner_2004_design', 'peffers_2007_dsr_methodology', 'hevner_2024_transparency', 'ochabski_2026_dsr_framework']:
        if '{' + key + ',' not in bib:
            errors.append(f'references.bib missing @{key}')

if 'References and parsed source bibliography' in text:
    errors.append('Manual parsed bibliography is still in the main manuscript; move it to a supplement/source registry.')

pdf_path = ROOT / 'build' / 'dsr-framework-whitepaper.pdf'
pdf_text_path = ROOT / 'build' / 'dsr-framework-whitepaper.txt'
if pdf_path.exists() and shutil.which('pdftotext') and not pdf_text_path.exists():
    subprocess.run(['pdftotext', str(pdf_path), str(pdf_text_path)], check=False)
pdf_text = ''
if pdf_text_path.exists():
    pdf_text = pdf_text_path.read_text(encoding='utf-8', errors='replace')
elif pdf_path.exists():
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(pdf_path))
        pdf_text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    except Exception:
        pdf_text = ''

if pdf_text:
    if re.search(r'\ntrue\n', pdf_text[:1000]):
        errors.append('PDF title page appears to contain standalone "true" where the author should be.')
    if re.search(r'\n\d+\s+\d+\.\s+Introduction\n', pdf_text):
        errors.append('PDF text still shows double-numbered Introduction heading.')
    if '1 From Design Science Research Theory to Repository-Native Operationalization' in pdf_text:
        errors.append('PDF text still shows the title as a numbered section.')
    if re.search(r'\n\d+\.\d+\s+(Source-use rule|Copyright and publication caution|Files Codex should read first|Build commands)\n', pdf_text):
        errors.append('PDF text still shows numbered appendix subheadings.')

if errors:
    print('[FAIL] white paper build checks failed:')
    for e in errors:
        print('- ' + e)
    sys.exit(1)

print('[OK] white paper build checks passed')
