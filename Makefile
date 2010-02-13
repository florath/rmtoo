
.PHONY: all

all: reqtree.png

.PHONY: reqtree.dot

reqtree.dot:
	./bin/rmtoo -m . -f doc/requirements/Config.py \
		-d doc/requirements -c dot -o reqtree.dot -l doc/latex

reqtree.png: reqtree.dot
	dot -Tpng -o reqtree.png reqtree.dot

.PHONY: latex
latex:
	./bin/rmtoo -m . -f doc/requirements/Config.py \
		-d doc/requirements -c latex -l doc/latex
	(cd doc/latex && pdflatex requirements.tex; pdflatex requirements.tex)

.PHONY: clean
clean:
	rm -f reqtree.dot reqtree.png doc/latex/reqs/*.tex \
		doc/latex/requirements.aux doc/latex/requirements.dvi \
		doc/latex/requirements.log doc/latex/requirements.out \
		doc/latex/requirements.pdf doc/latex/requirements.toc
