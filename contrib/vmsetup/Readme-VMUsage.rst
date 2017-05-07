How to use a preinstalled VM?
+++++++++++++++++++++++++++++

This document is a small tutorial for all who want to work with
rmToo - the free and open source requirements management tool.

In this tutorial the example Project is called ``MyProject``.  Of
course you can and should adapt this name to your needs.

Please note that this is not an introduction to the concepts and
structures used by rmtoo.  Before you start, please read the
presentations at http://rmtoo.florath.net.

Copy the Template Project
-------------------------

Copy the template project to the home directory:

.. code:: bash

   cp -r /usr/local/pkg/rmtoo/rmtoo/contrib/template_project MyProject

This is a minimalist project with only two requirements - but the
whole environment and infrastructure is set up so that is easy to
extend this.

Create All Artifacts
--------------------

To create all artifacts for the project, type:

.. code:: bash

   make

Check Artifacts
---------------

All artifacts are created in the sub-directory ``artifacts``.

.. code:: bash

   ls -l artifacts

View Artifacts
--------------


