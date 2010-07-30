
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                   THIS SOFTWARE IS BETA!

       IT MAY HARM YOUR COMPUTER, SOFTWARE AND DATA!

                   USE AT YOUR OWN RISK!

     PLEASE NOTE THAT rmToo IS UNDER HEAVY DEVELOPMENT!
    EVERYTHING (ESPECIALLY INPUT FILES AND COMMMAND LINE
          PARAMERERS AND CONFIG) WILL CHANGE!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

rmtoo checks the given set of requirments and optionally outputs LaTeX
source and a requirments dependency graph.

To run rmtoo, first set the PYTHONPATH to the directoy where
everything was unpacked. (Sourcing the 'setenv.sh' from the current
directory exactly does this.) (Note: rmtoo may come as a tar ball
where everything is unpacked in a local directory)


--- Preconditions ---

rmtoo is written in python.  At least version 2.5 of python is
needed. 

Starting with version 11, git-python is shipped with rmtoo.
The API is changing rapidly - there are currently three different APIs
out there.  As soon as the change rate settles, the git-python will be
removed from the package and the OS / distribution version should be
used. git-python home page is at http://gitorious.org/git-python.

When you want to create the document, LaTeX is needed.

For the requirements dependency graph, graphviz is used.

For statistics plot gnuplot can be used.

Typically the packages from your distribution will work.


--- Introduction ---

The simplest way of getting in, is have a closer look at the
requirments and topics which comes with rmtoo (which document the
requirments of the rmtoo itself).  In the FAQ document does exist a
'Getting Started' section (see doc/other/FAQ.txt).


--- Check and create them all ---

Try a 
$ make 
$ make tests
The configuration file where the output artifacts are configured are
doc/requirements/ConfigX.py.


--- Documentation ---

There is a growing number of man pages. They are placed in the
'doc/man' folder.  If you use the tar file or the sources, try using
$ man -l doc/man/rmtoo.7
When you use the package, just try
$ man rmtoo
This gives a short introduction what rmtoo is.  This man page also
includes all the references to other man pages.

There is also a FAQ. It is placed under 'doc/other/FAQ.txt' or when
using the package it's placed in '/usr/share/doc/rmtoo'.

There is also a presentation about the design and features of
rmtoo. The current version can be found in the download section of the
sourceforge project page.  Please visit the projects home page
'http://rmtoo.gnu4u.org for appropriate links.


--- Emacs Mode ---

Emacs mode can be loaded in emacs by:
M-x load-file
point to contrib/req-mode.el
All files with suffix .req will now use the REQ editing mode.


--- Known Issues ---

* Sometimes the 'make tests' output gives a very low coverage.  It is
  unknown why.  After removing all (old) .pyc files
        find . -name "*.pyc" | xargs rm
  is correctly computed.


--- Tailer ---

If you have some problems, remarks or feature request, you're welcome
to visit the project home page
   http://rmtoo.gnu4u.org
or the sourceforge project page
   http://sourceforge.net/projects/rmtoo
or write a mail.

Andreas Florath
sf@flonatel.org
2010-07-30

