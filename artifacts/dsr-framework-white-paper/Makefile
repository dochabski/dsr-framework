PANDOC_COMMON = --standalone --metadata-file build/pandoc-metadata.yaml --citeproc
PDF_ENGINE ?= tectonic

.PHONY: md html pdf check clean

md:
	python scripts/assemble_whitepaper.py

html: md
	mkdir -p build
	pandoc whitepaper/whitepaper_unified.md $(PANDOC_COMMON) -o build/dsr-framework-whitepaper.html

pdf: md
	mkdir -p build
	pandoc whitepaper/whitepaper_unified.md $(PANDOC_COMMON) --pdf-engine="$(PDF_ENGINE)" --include-in-header=build/latex-preamble.tex -o build/dsr-framework-whitepaper.pdf

check: md
	python scripts/check_whitepaper_build.py

clean:
	rm -f build/dsr-framework-whitepaper.html build/dsr-framework-whitepaper.pdf
