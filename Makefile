all: thesis_skeleton.latex 000_abstract.latex
	pandoc config.yaml [1-9][0-9][0-9]_*.md \
		--include-before=$(word 2,$^) \
		--atx-headers \
		--latex-engine=pdflatex \
		--template=$< \
		--bibliography=library.bib \
		--csl=apa.csl \
		--metadata=link-citations:true \
		--listings \
		--include-in-header=scripts/pandoc-dot2tex-filter/tikz-preamble.latex \
		--filter=scripts/pandoc-dot2tex-filter/dot2tex-filter.py \
		-f markdown+definition_lists \
		-o thesis.pdf
	rm $^

thesis_skeleton.latex: ClassicThesis.tex
	python scripts/template_gen.py

%.latex:
	pandoc $*.md -o $@
