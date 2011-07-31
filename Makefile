.PHONY: all
.PHONY: all_html
all: artifacts/requirements.pdf artifacts/req-graph1.png \
	artifacts/req-graph2.png all_html

# Adding new files (especially requirements) can not automatically
# handled.  The 'force' target tries to handle this.
.PHONY: force
force: 
	rm artifacts/.rmtoo_dependencies
	${MAKE} all

#
# This is the way the rmtoo must be called.
#
CALL_RMTOO=./bin/rmtoo -m . -f doc/requirements/Config3.py

#
# Dependency handling
#  The file .rmtoo_dependencies is created by rmtoo itself.
#
include artifacts/.rmtoo_dependencies

all_html: ${OUTPUT_HTML}

# And how to make the dependencies
artifacts/.rmtoo_dependencies:
	./bin/rmtoo -m . -f doc/requirements/Config3.py \
		--create-makefile-dependencies=artifacts/.rmtoo_dependencies

artifacts/req-graph1.png: artifacts/req-graph1.dot
	unflatten -l 23 artifacts/req-graph1.dot | \
		dot -Tpng -o artifacts/req-graph1.png

artifacts/req-graph2.png: artifacts/req-graph2.dot
	dot -Tpng -o artifacts/req-graph2.png artifacts/req-graph2.dot

# Two calls are needed: one for the requirments converting and one for
# backlog creation.
artifacts/requirements.pdf: ${REQS_LATEX2} doc/latex2/requirements.tex
	(cd artifacts && \
	   gnuplot ../contrib/gnuplot_stats_reqs_cnt.inc && \
	   epstopdf stats_reqs_cnt.eps)
	(cd artifacts && \
	   gnuplot ../contrib/gnuplot_stats_burndown.inc && \
	   epstopdf stats_burndown.eps)
	(cd artifacts && pdflatex ../doc/latex2/requirements.tex; \
		pdflatex ../doc/latex2/requirements.tex; \
		pdflatex ../doc/latex2/requirements.tex)

.PHONY: clean
clean:
	rm -f artifacts/req-graph1.png artifacts/req-graph2.png \
		artifacts/reqtopics.tex artifacts/reqspricing.ods \
		artifacts/req-graph1.dot artifacts/req-graph2.dot \
		artifacts/requirements.aux artifacts/requirements.dvi \
		artifacts/requirements.log artifacts/requirements.out \
		artifacts/requirements.pdf artifacts/requirements.toc \
		add_data.py*
	rm -fr debian/rmtoo build

PYSETUP = python setup.py

.PHONY: install
install:
	$(PYSETUP) install --prefix=${DESTDIR}/usr \
		--install-scripts=${DESTDIR}/usr/bin

.PHONY: tests
tests:
	nosetests -w rmtoo -v --with-coverage -s \
		--cover-package=rmtoo.lib,rmtoo.output,rmtoo.modules

.PHONY: deb
deb:
	debuild -I -Imake_latex.log

.PHONY: last_test
last_test:
	nosetests -w rmtoo -v -s \
		tests/blackbox-test/bb010-test/test-bb010.py
