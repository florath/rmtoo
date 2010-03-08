.PHONY: all
all: reqtree.png latex

.PHONY: reqtree.dot

reqtree.dot:
	./bin/rmtoo -m . -f doc/requirements/Config.py \
		-d doc/requirements -c dot -o reqtree.dot -l doc/latex

reqtree.png: reqtree.dot
	dot -Tpng -o reqtree.png reqtree.dot

# Two calls are needed: one for the requirments converting and one for
# backlog creation.
.PHONY: latex
latex:
	./bin/rmtoo -m . -f doc/requirements/Config.py \
		-d doc/requirements -c prios -p doc/latex/reqsprios.tex
	./bin/rmtoo -m . -f doc/requirements/Config.py \
		-d doc/requirements -c latex -l doc/latex
	(cd doc/latex && pdflatex requirements.tex; \
		pdflatex requirements.tex; \
		pdflatex requirements.tex)

.PHONY: clean
clean:
	rm -f reqtree.dot reqtree.png doc/latex/reqs/*.tex \
		doc/latex/requirements.aux doc/latex/requirements.dvi \
		doc/latex/requirements.log doc/latex/requirements.out \
		doc/latex/requirements.pdf doc/latex/requirements.toc 
	rm -fr debian/rmtoo build



PYSETUP = python setup.py

.PHONY: install
install:
	$(PYSETUP) install --prefix=${DESTDIR}/usr \
		--install-scripts=${DESTDIR}/usr/bin

.PHONY: tests
tests:
	nosetests -v --with-coverage -s --cover-package=rmtoo

.PHONY: deb
deb:
	debuild -I -Imake_latex.log
