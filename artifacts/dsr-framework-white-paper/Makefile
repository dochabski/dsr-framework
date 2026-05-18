.PHONY: md html pdf clean

md:
	python scripts/assemble_whitepaper.py

html: md
	mkdir -p build
	pandoc whitepaper/whitepaper_unified.md --standalone --metadata-file build/pandoc-metadata.yaml -o build/dsr-framework-whitepaper.html

pdf: md
	mkdir -p build
	pandoc whitepaper/whitepaper_unified.md --standalone --metadata-file build/pandoc-metadata.yaml --pdf-engine=xelatex --include-in-header=build/latex-preamble.tex -o build/dsr-framework-whitepaper.pdf

clean:
	rm -f build/dsr-framework-whitepaper.html build/dsr-framework-whitepaper.pdf
