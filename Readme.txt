
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                   THIS SOFTWARE IS BETA!

       IT MAY HARM YOUR COMPUTER, SOFTWARE AND DATA!

                   USE AT YOUR OWN RISK!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

rmtoo checks the given set of requirments and optionally outputs LaTeX
source and a requirments dependency graph.

To run rmtoo, first set the PYTHONPATH to the directoy where everything
was unpacked. (Sourcing the 'setenv.sh' from the current directory
exactly does this.) (Note: currently rmtoo comes as a tar ball where
everything is unpacked in a local directory. This will change in
future.) 

You can get a short help by calling:
$ ./bin/rmtoo -h


--- Introduction ---

The simplest way of getting in, is handling the requirments which
comes with rmtoo (which document the requirments of the rmtoo
itself). 

There is currently no documentation about the format and supported
fields, so please have a look at the files at doc/requirements to get
an impression, what is possible.


--- Check them all ---

To simply check the requirments, do
$ ./bin/rmtoo -m . -f doc/requirements/Config.py \
      -d doc/requirements -c check 

If there are some errors, they will be printed.
If everything is fine, nothing will be printed.


--- LaTeX Output ---

For LaTeX output, run:
$ ./bin/rmtoo -m . -f doc/requirements/Config.py \
       -d doc/requirements -c latex -l doc/latex
(Note: the file requirement.tex is parsed and checked, if all
available requirments are included.)

This converts all requirments into 'tex' files under doc/latex/reqs
and generates a dot file 'doc/latex/reqs/dependsgraph.dot'.

To generate a PDF from the LaTeX sources, do:
$ cd doc/latex
$ pdflatex requirements.tex

The pdflatex might be run twice to get the references resolved.

If you include the priority list, please have a look there how to
create. 


--- Dependency Graph ---

To output the requirements dependency graph (as a .dot file), use
$ ./bin/rmtoo -m . -f doc/requirements/Config.py \
       -d doc/requirements -c dot -o reqtree.dot

To convert the dot file into some graphics, install the graphviz
package and run:
$ dot -Tpng -o reqtree.png reqtree.dot


--- Priority List ---

To get a prioritized list of open requirments (which can be used as
the current backlog) call:

$ ./bin/rmtoo -m . -f doc/requirements/Config.py \
       -d doc/requirements -c prios -p doc/latex/reqsprios.tex


--- Emacs Mode ---

Emacs mode can be loaded in emacs by:
M-x load-file
point to contrib/req-mode.el
All files with suffix .req will now use the REQ editing mode.


--- Tailer ---

If you have some problems, remarks or feature request, you're welcome
to visit the sourceforge project page at:
   http://sourceforge.net/projects/rmtoo
or write a mail.

Andreas Florath
sf@flonatel.org
2010-02-13
