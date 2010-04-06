.PHONY: all
all: reqtree.png doc/latex/requirements.pdf

#
# This is the way the rmtoo must be called.
#
CALL_RMTOO=./bin/rmtoo -m . -f doc/requirements/Config.py -d doc/requirements

#
# Dependency handling
#  The file .rmtoo_dependencies is created by rmtoo itself.
#
include .rmtoo_dependencies

# And how to make the dependencies
.rmtoo_dependencies:
	./bin/rmtoo -m . -f doc/requirements/Config.py \
		-d doc/requirements \
		--create-makefile-dependencies=.rmtoo_dependencies

reqtree.png: reqtree.dot
	dot -Tpng -o reqtree.png reqtree.dot

# Two calls are needed: one for the requirments converting and one for
# backlog creation.
doc/latex/requirements.pdf: ${REQS_TEX} doc/latex/requirements.tex
	(cd doc/latex && \
	   gnuplot ../../contrib/gnuplot_stats_reqs_cnt.inc && \
	   epstopdf stats_reqs_cnt.eps)
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
	nosetests -w rmtoo -v --with-coverage -s --cover-package=rmtoo

.PHONY: deb
deb:
	debuild -I -Imake_latex.log
