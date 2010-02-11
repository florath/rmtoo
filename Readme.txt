
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                   THIS SOFTWARE IS ALPHA!

		  IT MAY HARM YOUR COMPUTER!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

rmtoo checks the given requirments and optionally outputs LaTeX source
and a requirments dependency graph.

To run this, first set the PYTHONPATH to the directoy where everything
was unpacked. (Sourcing the 'setenv.sh' from the current directory
exactly does this.)

You can get a short help by calling:
$ ./bin/rmtoo -h

The simplest way of getting in, is handling the requirments which
comes with rmtoo (which document the requirments of the rmtoo
itself). 

To simply check the requirments, do
$ ./bin/rmtoo -m . -f doc/requirements/Config.py \
      -d doc/requirements -c check 

If there are some errors, they will be printed.
If everything is fine, nothing will be printed.

For LaTeX and graphics output, run:
$ ./bin/rmtoo -m . -f doc/requirements/Config.py \
       -d doc/requirements -c latex -l doc/latex

This converts all requirments into 'tex' files under doc/latex/reqs
and generates a dot file 'doc/latex/reqs/dependsgraph.dot'.

To generate a PDF from the LaTeX sources, do:
$ cd doc/latex
$ pdflatex requirements.tex

The pdflatex might be run twice to get the references resolved.

To convert the dot file into some graphics, install the graphviz
package and run:
$ dot -Tpng -o doc/reqsdepgraph.png doc/latex/reqs/dependsgraph.dot

If you have some problems, remarks or feature request, you're welcome
to visit the sourceforge project page at:
   http://sourceforge.net/projects/rmtoo
or write a mail.

Andreas Florath
sf@flonatel.org
2010-02-11

