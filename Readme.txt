
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                       THIS IS SOFTWARE!

       IT MAY HARM YOU, YOUR COMPUTER, SOFTWARE AND DATA!

                     USE AT YOUR OWN RISK!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

--- Overview ---

rmtoo is a free and open source requirements management tool.

rmtoo uses a different approach than most other requirements
management tools: it comes as a command line tool which is optimized
for handling requirements. The power of rmtoo lies in the fact that
the development environment can handle the input and output files -
there is no need for a special tool set environment.

Example: if you need to handle baselines (and there often is), rmtoo
can be configured using a revision control system (e.g. git). The
revision control system can handle different revisions, baselining,
tagging, branching and many other things extremely well - there is no
reason to reinvent the wheel and making it less efficient.

Let one thing do one thing.


--- Unique Feature Set ---

rmtoo fits perfectly in a development environment using text editors
and command line tools such as emacs, vi, eclipse, make, maven. 

o Use simple text files as input - use your favorite editor
o Many different output formats and artifacts are supported:
  * PDF - with links to dependent requirements
  * HTML - also with links to dependent requirements
  * Requirements dependency graph
  * Requirement count history graph
  * Lists of unfinished requirements including priority and effort
    estimation - e.g. for use in agile project development 
o Fully integrated revision control system: git. Usages: history,
  statistics and baseline handling. 
o A topic based output handling provides a common set of files for
  different types of output (PDF, HTML, ...) 
o Analytics modules: Heuristics help to evaluate the quality of
  requirements 
o Modules to support commercial biddings based on a given set of
  requirements 
o Emacs mode files for editing requirements and topics included
o Experimental output in XML
o Fully integrated with Makefile handling of all artifacts
o Fully modular design: additional output requires minimal effort
o During parsing most common problems are detected: all syntax errors
  and also many semantic errors. 
o Fully automated test environment - tests about 95% of the code and
  is shipped with rmtoo packages to check for possible problems in
  different environments. 

rmtoo is not a fully integrated, tries-to-do-everything tool with a
colorful GUI or different database backends. 


--- Packaging ---

For Debian Sqeeze exists a deb package which can be installed with
dpkg. 

All other (including Ubuntu) should use the provided tar ball.


--- Preconditions ---

rmtoo is written in python.  At least version 2.5 of python is
needed. 

When you want to create LaTeX or PDF documentation, LaTeX is needed. 

For the requirements dependency graph, graphviz is used.

For statistics plot gnuplot is used.

Typically the packages from your distribution will work.

(Starting with rmtoo version 11, git-python is shipped with rmtoo.  The
API of git-python is changing rapidly - there are currently three
different APIs out there.  As soon as the change rate settles, the
git-python will be removed from the package and the OS / distribution
version should be used. git-python home page is at
http://gitorious.org/git-python.)


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
local setup. YY is the version of rmtoo.)

      $ cp -r ~/rmtoo-YY/contrib/template_project ~/MyNewProject

The template project comes with complete makefile support, with
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
includes the references to other man pages.

There is also a FAQ. It is placed under 'doc/other/FAQ.txt' or when
using the package it's placed in '/usr/share/doc/rmtoo'.

There are also two presentations about the design and features of
rmtoo. Theese presentations can be found in the download section of 
the sourceforge project page.  Please visit the projects home page
http://www.flonatel.de/projekte/rmtoo for appropriate links.


--- Emacs Mode ---

Emacs mode can be loaded in emacs by:
M-x load-file
point to contrib/req-mode.el
All files with suffix .req will now use the REQ editing mode.


--- Tailer ---

If you have some problems, remarks or feature request, you're welcome
to visit the project home page
   http://www.flonatel.de/projekte/rmtoo
or the sourceforge project page
   http://sourceforge.net/projects/rmtoo
or write a mail.

Andreas Florath
sf@flonatel.org
2011-01-05

