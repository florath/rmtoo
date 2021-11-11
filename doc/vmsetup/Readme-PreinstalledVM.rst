Preinstalled VMs
++++++++++++++++

This document describes how to work with one of the preinstalled
VMs.

In this document the example Project is called ``MyProject``.  Of
course you can and should adapt this name to your needs.


Prerequisites
=============

Please note that some knowledge is needed to be able to use rmtoo.
These are:

#. Basic Linux knowledge:
   Logging in a system, using a console / shell, executing a command,
   using ``make``.
#. Using a text editor:
   Any text editor is usable - preferred: emacs.
#. Basic YAML or JSON knowledge:
   The configuration is using either format.

For the requirement management tool ``rmtoo`` itself:

#. Concept of requirement and design decision.
#. Concept of rmtoo.
#. Concept of a directed graph (digraph).

If not already done, **now** is the time to step through
the rmtoo presentations which can be found on
http://rmtoo.florath.net.

This document **is not** an introduction to Linux; this document **is
not** an introduction to rmtoo.


Starting Preinstalled VMs
=========================

For different usage scenarios there are different VM flavors.  There
is a dedicated document_ where the flavors are described.

.. _document: Readme-Flavors.rst

To use the preinstalled VMs you need access to AWS EC2.  Please
consult the Readme_ for hints and tips.

.. _Readme: Readme-AWSStartVM.rst


No automated Backup
===================

There is no backup done of any data.  If you start your own project
you need to create backups by yourself.


Copy the Template Project
=========================

Copy the template project to the home directory and change the working
directory to the new project.

.. code:: bash

   cp -r /usr/local/pkg/rmtoo/rmtoo/contrib/template_project MyProject
   cd MyProject

This is a minimalist project with only two requirements - but the
whole environment and infrastructure is set up so that is easy to
extend this.

Create All Artifacts
====================

To create all artifacts for the project, type:

.. code:: bash

   make

Check Artifacts
===============

All artifacts are created in the sub-directory ``artifacts``.

.. code:: bash

   ls -l artifacts

A possible result looks like:

.. code:: bash

   drwxr-xr-x 2 rmtoo rmtoo   4096 May  9 08:33 html
   -rw-r--r-- 1 rmtoo rmtoo    268 May  9 08:33 req-graph1.dot
   -rw-r--r-- 1 rmtoo rmtoo  13027 May  9 08:33 req-graph1.png
   -rw-r--r-- 1 rmtoo rmtoo    333 May  9 08:33 req-graph2.dot
   -rw-r--r-- 1 rmtoo rmtoo  16375 May  9 08:33 req-graph2.png
   -rw-r--r-- 1 rmtoo rmtoo   1369 May  9 08:33 reqsprios.tex
   -rw-r--r-- 1 rmtoo rmtoo     30 May  9 08:33 reqs-version.txt
   -rw-r--r-- 1 rmtoo rmtoo   1224 May  9 08:33 reqtopics.tex
   -rw-r--r-- 1 rmtoo rmtoo   3390 May  9 08:33 requirements.aux
   -rw-r--r-- 1 rmtoo rmtoo  17073 May  9 08:33 requirements.log
   -rw-r--r-- 1 rmtoo rmtoo    885 May  9 08:33 requirements.out
   -rw-r--r-- 1 rmtoo rmtoo 106423 May  9 08:33 requirements.pdf
   -rw-r--r-- 1 rmtoo rmtoo   1098 May  9 08:33 requirements.toc
   -rw-r--r-- 1 rmtoo rmtoo  41819 May  9 08:33 stats_burndown.csv
   -rw-r--r-- 1 rmtoo rmtoo      0 May  9 08:33 stats_burndown.csv.est
   -rw-r--r-- 1 rmtoo rmtoo  72883 May  9 08:33 stats_burndown.eps
   -rw-r--r-- 1 rmtoo rmtoo   7677 May  9 08:33 stats_burndown.pdf
   -rw-r--r-- 1 rmtoo rmtoo     22 May  9 08:33 stats_reqs_cnt.csv
   -rw-r--r-- 1 rmtoo rmtoo  18187 May  9 08:33 stats_reqs_cnt.eps
   -rw-r--r-- 1 rmtoo rmtoo   6963 May  9 08:33 stats_reqs_cnt.pdf
   -rw-r--r-- 1 rmtoo rmtoo  41819 May  9 08:33 stats_sprint_burndown.csv
   -rw-r--r-- 1 rmtoo rmtoo      0 May  9 08:33 stats_sprint_burndown.csv.est
   -rw-r--r-- 1 rmtoo rmtoo  72904 May  9 08:33 stats_sprint_burndown.eps
   -rw-r--r-- 1 rmtoo rmtoo   7909 May  9 08:33 stats_sprint_burndown.pdf

For a complete description of all artifacts consult the rmtoo
presentations or man pages (as described later in this document).

View Artifacts
==============

There are two ways to view the generated artifacts: using local
installed tools or transfer the files to your local computer and view
them there.

View Artifacts using Tools installed on the VM
----------------------------------------------

As a precondition you need a local X-Server and you need to connect to
the VM using ``ssh -X``.  In this case you can open the files with the
pre-installed tools on the VM.  Example: to open a PDF file use:

.. code:: bash

   evince artifacts/requirements.pdf

For viewing the generated images:

.. code:: bash

   eog artifacts/req-graph1.png

If you want to have a look at the generated html files, start

.. code:: bash

   firefox

and browse to:

.. code:: bash

   file:///home/<username>/MyProject/artifacts/html/ReqsDocument.html

The username is the default username of the VM.  Depending on the
flavor, distribution and boot configurations that might differ.

View Artifacts using local Tools
--------------------------------

Another possibility is to transfer the data to your local computer
using the ssh or sftp protocol.  For every (local) operating system
there exist many different tools.  Please consult the internet.

Optional: Configuring Emacs
===========================

When using emacs it is very convinient to enable syntax highlighting.
To enable this, run

.. code:: bash

   emacs ~/.emacs

and add the line

.. code:: bash

   (load-file "/usr/local/pkg/rmtoo/rmtoo/contrib/req-mode.el")

If your internet connection is not that fast, you can use the emacs
directly in the console.  To enable this, always use the ``-nw``
option to emacs, also e.g.:

.. code:: bash

   emacs -nw ~/.emacs

Use Cases
=========

Add a Requirement
-----------------

Adding a requirement consists of two steps:

1. Create new requirement.
2. Create dependency from existing to new requirement.

The easiest way to create a new requirement is to create a copy of an
existing:

.. code:: bash

   cp requirements/req1.req requirements/req2.req

Then change the new requirement with the text editor:

.. code:: bash

   emacs requirements/req2.req

You must change the name (this must be unique).  A good practice is to
use the same name for the requirement as for the file.  You might also
want to change other values as well.

As a second step you have to create the link between the existing
requirements and the new requirement.  In this example we assume that
the new ``req2`` is a detail or breakdown of ``req1``.

To add this relation, edit the existing ``req1``

.. code:: bash

   emacs requirements/req1.req

and add the line

.. code:: bash

   Solved by: req2

To recreate the complete set of artifacts with the new requirement
included, call

.. code:: bash

   make

You can have a look at the changes as described in the previous
section ``View Artifacts``.

Add a Topic
===========

A topic is a way of clustering requirements; depending on the output
they appear as different chapters, sections or pages.

Topic can have sub-topics; sub-topic can have sub-sub-topics and so
on.

To create a new topic, the easiest way is to copy an existing one:

.. code:: bash

   cp topics/WhatsAbout.tic topics/NewTopic.tic

As for the requirement, change the content of the new topic:

.. code:: bash

   emacs topics/NewTopic.tic

Especially change the name.  Also here it is best practice to use the
same (or a similar) name as for the filename.

The next step is to include the new topic into the topic hierarchy.
For example we will add here the ``NewTopic`` as a subtopic of the
``WhatsAbout``.  Therefore edit the existing topic

.. code:: bash

   emacs topics/WhatsAbout.tic

And add a line like:

.. code:: bash

   SubTopic: NewTopic

The last step is to move the requirement to the topic. Edit the
requirement:

.. code:: bash

   emacs requirements/req2.req

And change the ``Topic:`` to:

.. code:: bash

   Topic: NewTopic

To update all the artifacts based on the new data set, call

.. code:: bash

   make

In rare cases - depending on how you change the files and how the VM
is time synchronized - when adding new elements, the call to make will
do nothing (Message: make: Nothing to be done for 'all'.).  To get
around this, remove the Makefile dependencies and run ``make`` again.

.. code:: bash

   rm -f .rmtoo_dependencies
   make


Using man Pages
===============

The complete documentation of rmtoo can be read as man pages.  There
are about 30 man pages - each describing a different aspect of rmtoo.

To get an overview over the available man pages, use

.. code:: bash

   man rmtoo

This page lists all the available man pages.  To read one of them,
e.g. the page that describes the analytics, use

.. code:: bash

   man rmtoo-analytics

Next Steps
==========

There are two additional example projects availble:

EMail client
------------
A small project with eight requirements.  This can be found in

.. code:: bash

   https://github.com/florath/rmtoo/tree/master/doc/examples/EMailClient

rmtoo
-----
Of course the requirements for rmtoo itself are written in rmtoo.
Currently it contains about 200 requirements - including mostly
all different types of outputs.

.. code:: bash

   https://github.com/florath/rmtoo/tree/master/doc

In this directory, you can find the ``requirements``, ``topics`` and
so on.

FAQ
===
Some frequently asked questions with answers:

.. code:: bash

   /usr/local/pkg/rmtoo/rmtoo/doc/other/FAQ.txt

Issues and Problems
===================

If you run into issues or problems, you can report them on

.. code:: bash

   https://github.com/florath/rmtoo/issues

Commercial Support
==================

If you need extensions or consulting setting up or using rmtoo, please
contact: rmtoo@florath.net
