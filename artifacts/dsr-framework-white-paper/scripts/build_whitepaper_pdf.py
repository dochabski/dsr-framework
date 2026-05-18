#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Build the white paper PDF with repeatable PDF layout hardening."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
PDF = BUILD / "dsr-framework-whitepaper.pdf"
LOG = BUILD / "whitepaper_build_pdf.log"


def run_capture(cmd: list[str], cwd: Path) -> tuple[int, str]:
    result = subprocess.run(
        cmd,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return result.returncode, result.stdout


def harden_longtable_layout(latex: str) -> tuple[str, int, int, int]:
    """Style generated longtable headers and insert body row rules."""

    table_count = 0
    header_count = 0
    rule_count = 0

    def patch_table(match: re.Match[str]) -> str:
        nonlocal table_count, header_count, rule_count
        table = match.group(0)
        if "whitepaper-table-layout-patched" in table:
            return table
        header, head_marker, after_head = table.partition("\\endhead")
        if not head_marker:
            return table
        head, lastfoot_marker, tail = after_head.partition("\\endlastfoot")
        if not lastfoot_marker:
            return table
        body, end_marker, rest = tail.partition("\\end{longtable}")
        if not end_marker:
            return table

        styled_header = header
        styled_header = styled_header.replace(
            "\\toprule\\noalign{}\n",
            "\\toprule\\noalign{}\n\\rowcolor{whitepaperheader}\n",
            1,
        )
        styled_header = re.sub(
            r"(\\begin\{minipage\}\[b\]\{\\linewidth\}\\raggedright)\n",
            r"\1\\bfseries\n",
            styled_header,
        )
        styled_header = styled_header.replace(
            "\\midrule\\noalign{}\n",
            "\\specialrule{0.7pt}{0pt}{0pt}\n",
            1,
        )

        patched_lines: list[str] = ["% whitepaper-table-layout-patched"]
        inserted = 0
        for line in body.splitlines():
            patched_lines.append(line)
            if re.search(r"\\\\\s*$", line):
                patched_lines.append(r"\midrule\noalign{}")
                inserted += 1

        table_count += 1
        header_count += 1
        rule_count += inserted
        return styled_header + head_marker + head + lastfoot_marker + "\n".join(patched_lines) + "\n" + end_marker + rest

    patched = re.sub(
        r"\\begin\{longtable\}.*?\\end\{longtable\}",
        patch_table,
        latex,
        flags=re.DOTALL,
    )
    return patched, table_count, header_count, rule_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-engine", default="tectonic")
    args = parser.parse_args()

    BUILD.mkdir(parents=True, exist_ok=True)
    engine = args.pdf_engine.strip('"')
    if not Path(engine).exists():
        found = shutil.which(engine)
        if found:
            engine = found

    lines = [
        "python scripts/assemble_whitepaper.py",
        "pandoc whitepaper/whitepaper_unified.md --standalone --metadata-file build/pandoc-metadata.yaml --citeproc --include-in-header=build/latex-preamble.tex -t latex",
    ]

    with tempfile.TemporaryDirectory(prefix="dsr-whitepaper-pdf-") as tmp_name:
        tmp = Path(tmp_name)
        tex_path = tmp / "dsr-framework-whitepaper.tex"
        pandoc_cmd = [
            "pandoc",
            "whitepaper/whitepaper_unified.md",
            "--standalone",
            "--metadata-file",
            "build/pandoc-metadata.yaml",
            "--citeproc",
            "--include-in-header=build/latex-preamble.tex",
            "-t",
            "latex",
            "-o",
            str(tex_path),
        ]
        code, output = run_capture(pandoc_cmd, ROOT)
        lines.append(output)
        if code:
            LOG.write_text("\n".join(lines), encoding="utf-8")
            return code

        latex = tex_path.read_text(encoding="utf-8")
        patched, table_count, header_count, rule_count = harden_longtable_layout(latex)
        tex_path.write_text(patched, encoding="utf-8", newline="\n")
        lines.append(
            f"[OK] styled {header_count} table headers and inserted {rule_count} table row rules across {table_count} longtable blocks."
        )

        if PDF.exists():
            PDF.unlink()
        tex_cmd = [engine, "--outdir", str(BUILD), str(tex_path)]
        lines.append(" ".join(tex_cmd))
        code, output = run_capture(tex_cmd, ROOT)
        lines.append(output)

    if not PDF.exists():
        LOG.write_text("\n".join(lines), encoding="utf-8")
        return code or 1

    if code:
        lines.append(f"[WARN] PDF engine returned {code}, but PDF output was produced; inspect warnings above.")

    lines.append(
        f"[OK] built build/dsr-framework-whitepaper.pdf with table header styling and row-rule patching on {dt.date.today().isoformat()}"
    )
    LOG.write_text("\n".join(lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
