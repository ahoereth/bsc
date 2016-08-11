all: thesis_skeleton.latex 000_abstract.latex
	pandoc config.yaml [1-9][0-9][0-9]_*.md \
		--include-before=$(word 2,$^) \
		--template=$< \
		--atx-headers \
		--latex-engine=pdflatex \
		--bibliography=library.bib \
		--csl=apa.csl \
		--include-in-header=scripts/pandoc-dot2tex-filter/tikz-preamble.latex \
		--filter=./scripts/.cabal-sandbox/bin/pandoc-crossref \
		--filter=./scripts/.cabal-sandbox/bin/pandoc-citeproc \
		--filter=./scripts/dot2tex.py \
		--filter=./scripts/dotpng.py \
		--filter=./scripts/dotpdf.py \
		--listings \
		-f markdown+definition_lists \
		-o thesis.pdf
	rm $^

thesis_skeleton.latex: ClassicThesis.tex
	python scripts/template_gen.py

%.latex:
	pandoc $*.md -o $@
