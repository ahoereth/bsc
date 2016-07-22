all: thesis_skeleton.latex
	pandoc config.yaml [0-9][0-9]_*.md \
		--atx-headers \
		--latex-engine=pdflatex \
		--template=thesis_skeleton.latex \
		--bibliography=library.bib \
		--csl=apa.csl \
		--metadata=link-citations:true \
		--listings \
		-f markdown \
		-o thesis.pdf
	rm thesis_skeleton.latex

thesis_skeleton.latex: ClassicThesis.tex
	python scripts/template_gen.py
