rmToo
+++++

Open Source Requirements Management Tool

.. image:: https://img.shields.io/github/release/florath/rmtoo.svg
    :target: https://github.com/florath/rmtoo/releases
.. image:: https://travis-ci.org/florath/rmtoo.svg?branch=master
    :target: https://travis-ci.org/florath/rmtoo
.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
    :target: http://www.gnu.org/licenses/gpl-3.0
.. image:: https://img.shields.io/codecov/c/github/codecov/example-python.svg
    :target: https://codecov.io/gh/florath/rmtoo
.. image:: https://img.shields.io/github/downloads/florath/rmtoo/total.svg
    :target: http://rmtoo.florath.net
.. image:: https://img.shields.io/pypi/dm/rmtoo.svg
    :target: https://pypi.python.org/pypi/rmtoo
.. image:: https://img.shields.io/pypi/v/rmtoo.svg
    :target: https://pypi.python.org/pypi/rmtoo


Introduction
============

This Readme gives a short overview over the available online
documentation for rmtoo.

Content
=======

This file contains the following chapters:

.. contents:: Table of Contents


Conventions
===========

``YY``
  names the version of rmtoo.  You have to replace this with the real
  version number.

``$ cmd``
  This is a command you have to type in.  The ``$`` is a replacement for
  the shell prompt - do not enter it as a part of the command.


Operating System Support
========================

rmtoo is fully supported under Linux.  Nevertheless, because it is
written in computer independent programming languages (such as
python), is also works on other operating systems.

Mac OS X users might want to read ``Readme-OS-X.txt``.

Windows users might want to read the ``Readme-Windows.txt``.


Installation
============

The following sections assume, that you are using Linux.  Please
refer to the appropriate Readme file for your operating system for
more information if you do not use Linux.

Dependencies
------------

To use rmtoo, other software packages must be installed.

rmtoo is written in python.  At least version 2.7 of python is needed.
(Starting with version 24 python 3 will be supported.)

When you want to create LaTeX or PDF documentation, LaTeX is needed.

For the requirements dependency graph, graphviz is used.

For statistics plot gnuplot is used.  For the estimation module the
python-scipy package is needed.

Typically the packages from your distribution will work.

First Project
-------------

The recommended way of starting is to copy the provided template
project.

Using the provided template projects depends whether you use the deb
package or the tar package.  Please consult the appropriate sections
how to use the template project.

Nevertheless the basic steps are:

1) Copy over the template project to some other directory.
2) Set up the environment
3) Run ``make``
4) Check, if everything worked
5) Start changing / adapting things to your needs

Note that during this document the project will be called
'MyNewProject'.  Please adapt the name for your needs.


Using virtualenv
================

This is the preferred installation method - it takes care that
at least the python dependencies are correctly installed.

Installation
------------

To install ``rmtoo`` in a virtualenv, execute the following steps:

.. code:: bash

   $ mkdir RMTOO
   $ cd RMTOO
   $ virtualenv venv
   $ source venv/bin/activate
   $ pip install --upgrade pip setuptools wheel
   $ pip install --only-binary=numpy,scipy numpy scipy
   $ pip install rmtoo
   $ export RMTOO_CONTRIB=${PWD}/venv/rmtoo/contrib

Please see the section 'First Project' how to use the template
project.


Using tar package
=================

Installation
------------

Just untar the downloaded package.  You need not to be root to do
this.
Change to the directory where you want to install rmtoo to.
To refer to the current directory, it is called RMTOO_BASE_PATH.

.. code:: bash

   $ export RMTOO_BASE_PATH=$PWD
   $ export RMTOO_PATH=${RMTOO_BASE_PATH}/rmtoo-YY
   $ export RMTOO_CONTRIB=${RMTOO_PATH}/contrib
   $ tar -xf rmtoo-YY.tar.gz

To use rmtoo, you have to include
``${RMTOO_PATH}/bin`` to your path,  include
``${RMTOO_PATH}`` to your ``PYTHONPATH``.
When you use the template project (see section 'First Project' some
lines below), the shell script ``setenv.sh`` is doing this for you.

First Project
=============

Change to a directory where you want to create the new project.  In
the following code, please replace ``${RMTOO_PATH}`` with ``VENV`` if
you are using virtualenv.

.. code:: bash

   $ cp -r ${RMTOO_CONTRIB}/template_project MyNewProject
   $ cd MyNewProject
   $ source ./setenv.sh ${RMTOO_PATH}
   $ make
   $ ls artifacts

In the artifacts directory there are all the generated files.

Man Pages
=========

The man pages are located in the sub-directory doc/man.  Please use
the command

.. code:: bash

   $ man -l ${RMTOO_PATH}/doc/man/rmtoo.7

When using the virtualenv, the use

.. code:: bash

   $ man -l venv/rmtoo/doc/man/rmtoo.7

to get an overview over all available man pages.
Those other man pages you can read also with man. Replace the
file name with the appropriate manual page, like:

.. code:: bash

   $ man -l ${RMTOO_BASE_PATH}/rmtoo-YY/doc/man/rmtoo-analytics.7

Additional Documentation
------------------------

Additional documentation can be found in the directories
``${RMTOO_PATH}/rmtoo-YY`` (especially the Readme files)
``${RMTOO_PATH}/rmtoo-YY/doc/other``.  When using ``VENV`` the
documentation is stored in ``venv/rmtoo/doc``.

Other Documentation
===================

FAQ
---
Frequently asked questions
A collection of questions which were ask in the past - including
the answers.

Presentations
-------------
There are also two presentations about the design and features of
rmtoo. Theese presentations can be found in the download section of
the sourceforge project page.  Please visit the projects home page
http://www.flonatel.de/projekte/rmtoo for appropriate links.

Readme-Overview.txt
-------------------
Description of the features of rmtoo.

Readme-Hacking.txt
------------------
Small (and yet unfinished) document how to develop functionality
and modules for rmtoo.

Readme-OS-X.txt
---------------
Hints for Mac Users.

Readme-Windows.txt
------------------
Hints for Windows users.

Readme-RmtooOnRmtoo.txt
-----------------------
Run rmtoo to get the documentation for rmtoo itself.

Readme-GitPython.txt
--------------------
Some note about the (internal) use of GitPython.

Emacs Mode for Editing Requirements
===================================

When using the tar package, emacs mode can be loaded in emacs by:
``M-x load-file``
point to ``${RMTOO_BASE_PATH}/rmtoo-YY/contrib/req-mode.el``
All files with suffix .req will now use the requirements editing
mode.

Footer
======

If you have some problems, remarks or feature request, you're welcome
to visit the project home page

http://rmtoo.florath.net

| flonatel GmbH & Co. KG
| Andreas Florath
| rmtoo@florath.net
| 2017-04-14
