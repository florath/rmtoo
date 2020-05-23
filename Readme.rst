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
software development life-cycle management SDLC_ options as well, e.g.,
traceability.

At the moment the only difference is the Excel import and export.

.. _SDLC: https://en.wikipedia.org/wiki/Software_development_process

Content
=======

This file contains the following chapters:

.. contents:: Table of Contents

Installation
============

Dependencies
------------

To use ``sltoo``, other software packages must be installed.

``sltoo`` is written in python.  At least version 3.6 and 3.8 are supported,
but other versions should work just fine.

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


virtualenv / pip
----------------

This is the preferred installation method — it takes care of installing the
python dependencies correctly.

To install ``sltoo`` in a virtualenv, execute the following steps:

.. code::

   python3 -m virtualenv
   source venv/bin/activate
   pip install sltoo

This has to be done once.


First Project
=============

Setup
-----

Change to a directory where you want to create the new project. We assume the
``virtualenv`` is available is the same directory (this is not necessary).

.. code::

   git clone git@github.com:kown7/rmtoo.git
   cp -r rmtoo/contrib/template_project MyNewProject


Usage
-----

To create all the artifacts for the template project, execute

.. code::

   cd MyNewProject
   export RMTOO_CONTRIB_DIR=`pwd`/../rmtoo/
   make
   ls artifacts

All the generated files are in the artifacts directory.

A typical workflow is to change or add requirements, topics or the
configuration in the ``MyNewProject`` directory, run ``make`` again
and check the artifacts.


Release History
===================

* 24.3.x

    * Fix tests for `py38`
    * Testing automatic deployment
    * Fixes the issues related to rmtoo, see https://github.com/florath/rmtoo/issues/36
