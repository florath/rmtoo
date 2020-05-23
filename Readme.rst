slToo
+++++

Open Source Software development Life cycle Tool

.. image:: https://img.shields.io/github/release/kown7/sltoo.svg
    :target: https://github.com/kown7/sltoo/releases
.. image:: https://travis-ci.org/kown7/rmtoo.svg?branch=master
    :target: https://travis-ci.org/kown7/rmtoo
.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
    :target: http://www.gnu.org/licenses/gpl-3.0
.. image:: https://img.shields.io/codecov/c/github/codecov/example-python.svg
    :target: https://codecov.io/gh/kown7/rmtoo
.. image:: https://img.shields.io/pypi/v/sltoo.svg
    :target: https://pypi.python.org/pypi/sltoo

.. COMMENT pypi stats are not working
.. COMMENT .. image:: https://img.shields.io/pypi/dm/sltoo.svg
.. COMMENT    :target: https://pypi.python.org/pypi/sltoo
	     
Introduction
============

This is a fork of ``rmtoo``. This fork is supposed to offer 
software life-cycle management options as well, e.g., traceability.

At the moment the only difference is the Excel import and export.


Content
=======

See rmtoo_

.. _rmtoo: https://github.com/florath/rmtoo


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

It supports Python 3.6 and 3.8. Older version of Python should 
work without problems, but are officially deprecated.


Installation
============

Run ``pip install sltoo``. See `Installation using virtualenv / pip`_.


Dependencies
------------

To use rmtoo, other software packages must be installed.

rmtoo is written in python.  At least version 2.7 of python is needed.
Starting with version 24 python >3.4 is also supported.

When you want to create LaTeX or PDF documentation, LaTeX is needed.

For the requirements dependency graph, graphviz is used.

For statistics plot gnuplot is used.  For the estimation module the
python-scipy package is needed.

Typically the packages from your distribution will work. For Ubuntu the
following packages are needed:

.. code:: 

    sudo apt-get install texlive-font-utils texlive-latex-base \
    texlive-font-utils graphviz
    pip3 install unflatten

For Fedora these packets:

.. code:: 

    sudo dnf install gnuplot texlive-latex texlive-tocloft \
    texlive-fancyhdr texlive-epstodpf texlive-metafont texlive-mfware


First Project
-------------

The recommended way of starting is to copy the provided template
project.

The basic steps are:

1) Copy over the template project to some other directory.
2) Set up the environment
3) Run ``make``
4) Check, if everything worked
5) Start changing / adapting things to your needs

Note that during this document the project will be called
'MyNewProject'.  Please adapt the name for your needs.


Installation using virtualenv / pip
===================================

This is the preferred installation method - it takes care that
at least the python dependencies are correctly installed.

Installation
------------

To install ``sltoo`` in a virtualenv, execute the following steps:

.. code::

   $ virtualenv venv
   $ source venv/bin/activate
   $ pip install sltoo

This has only to be done once.

First Project
=============

Installation
------------

Change to a directory where you want to create the new project. This
is needed only once.

.. code:: 

   # cd to virtualenv directory - if not already there
   $ cd RMTOO
   $ cp -r venv/rmtoo/contrib/template_project MyNewProject

Usage
-----

To create all the artifacts for the template project, execute

.. code::

   $ cd MyNewProject
   $ source ./setenv.sh VENV
   $ make
   $ ls artifacts

In the artifacts directory there are all the generated files.
A typical workflow is, to change or add requirements, topics or the
configuration in the ``MyNewProject`` directory, run ``make`` again
and check the artifacts.

