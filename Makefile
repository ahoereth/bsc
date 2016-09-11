all: thesis_skeleton.latex 000_abstract.latex
	pandoc config.yaml [1-9][0-9][0-9]_*.md ./frontback/appendix.tex \
		--include-before=./frontback/title.tex \
		--include-before=$(word 2,$^) \
		--include-after=./frontback/declaration.tex \
		--template=$< \
		--atx-headers \
		--latex-engine=pdflatex \
		--bibliography=library.bib \
		--csl=apa.csl \
		--filter=./scripts/.cabal-sandbox/bin/pandoc-crossref \
		--filter=./scripts/.cabal-sandbox/bin/pandoc-citeproc \
		--filter=./scripts/dot.py \
		--filter=./scripts/marginnotes.py \
		--filter=./scripts/shadowedimages.py \
		--listings \
		-f markdown+definition_lists \
		-o thesis.pdf
	rm $^

thesis_skeleton.latex: ClassicThesis.tex
	python scripts/template_gen.py

%.latex:
	pandoc $*.md -o $@
