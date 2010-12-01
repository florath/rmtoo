
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                   THIS SOFTWARE IS BETA!

       IT MAY HARM YOUR COMPUTER, SOFTWARE AND DATA!

                   USE AT YOUR OWN RISK!

     PLEASE NOTE THAT rmToo IS UNDER HEAVY DEVELOPMENT!
    EVERYTHING (ESPECIALLY INPUT FILES AND COMMMAND LINE
          PARAMERERS AND CONFIG) WILL CHANGE!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

rmtoo reads in and checks the given set of requirments and optionally
outputs a wide range of different artifacts.

To run rmtoo, first set the PYTHONPATH to the directoy where
everything was unpacked. (See the 'setenv.sh' shell script which
exactly does this.) (Note: rmtoo may come as a tar ball where
everything is unpacked in a local directory)


--- Preconditions ---

rmtoo is written in python.  At least version 2.5 of python is
needed. 

When you want to create LaTeX or PDF documentation, LaTeX is needed. 

For the requirements dependency graph, graphviz is used.

For statistics plot gnuplot is used.

Typically the packages from your distribution will work.

Starting with rmtoo version 11, git-python is shipped with rmtoo.  The
API of git-python is changing rapidly - there are currently three
different APIs out there.  As soon as the change rate settles, the
git-python will be removed from the package and the OS / distribution
version should be used. git-python home page is at
http://gitorious.org/git-python.


--- Introduction ---

The recommended way of starting is to copy the provided template
project.

The unpacked rmtoo package can directly by used. Nevertheless it is
possible to create the documents for rmtoo itself.  Please consult the
file Install.txt.


--- First project ---

This is a short introduction how to start a new project with rmtoo.

First copy over the template project to some location where you want
to use it.  When using the tar, it is located under
contrib/template_project.  When using the Debian package it is located
under /usr/share/doc/rmtoo/template_project. (In the following example
it is assumed, that the tar was unpacked in your home directory and
that the new project is called MyNewProject and will also go into the
home directory. You have to adapt the path names to adapt this to your
local setup. YY is the version of the rmtoo.)

      $ cp -r ~/rmtoo-YY/contrib/template_project ~/MyNewProject

The template project comes with complete makefile support setup, with
two requirements and two topics.

      $ cd ~/MyNewProject
      $ ./setup.sh ~/rmtoo-YY
      $ make


--- Documentation ---

There is a large number of man pages. They are placed in the
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
2010-11-12

