Usage of Preinstalled GUI VMs
=============================

Introduction
------------

Preinstalled VMs are available with a Linux text based console or a
graphical user interface.
With the help of the GUI mostly all operations of *rmtoo* can be
executed, like adding or changing requirements, topics, creating the
artifacts and viewing them.

To be able to use the GUI there is the need to take care about a few
things.

Please note that depending on your internet connection to the chosen
data center the usage of the GUI might be slow and include lags.  If
you need a VM in your own data center / public cloud, please contact
our service: rmtoo@florath.net

Start the VMS.....


User Init
---------

Call

.. code:: bash

   rmtoo-user-init


rdesktop
--------

A rdesktop client program is used to connect to the VM.  This section
lists some examples.  You can use your favorite rdesktop client.

Linux
.....

rdesktop -u debian -p <password> <VMIpAddress>

Template Project
----------------

The first step is to copy the template project.  This can be used as a
base for your project.

On the desktop there is a directory called ``rmtoo-system``. Double
click this icon.  A window opens.  Choose ``rmtoo`` and then
``contrib``.  Click the ``template_project`` once; right mouse button
and choose ``Copy``.  Move the window to the right that the ``Home``
directory can be seen.

Double click the ``Home``. A window opens.  Move the mouse into the
window and press the right mouse button.  Choose ``Paste``.  Click the
new ``template_project`` once, press the right mouse button and chose
``Rename``.  Enter a sensible name for your project.  (In this example
the project is called ``MyProject``.)

Double click ``MyProject``.  This is the complete project.  The
requirements are located under ``requirements`` and the topics in the
directory ``topics``.

To check the contents of a directory: double click.  To see the
contents of the file or change it: double click.

To create all artifacts, double click ``make.sh`` in the ``MyProject``
folder.  You can consult (double-click) the logs of the ``rmtoo`` run
in ``make.log``.

All the generated artifacts (pictures, documents, html pages) are
located in the ``artifacts`` folder.  You can view them by
double-clicking them.

Manual Pages
------------

Using GUI (yelp)
................

Double click ``rmtoo-system`` icon on the desktop.  Choose ``share``,
``man`` and ``man7``.  Click ``rmtoo.7`` once, then press the right
mouse button and chose ``Open with other application``.  Chose ``Use a
custom command`` and enter ``yelp``.  Click ``Open``.

The blue links in the section ``See Also`` lead to other parts of the
manual pages.


Using Terminal
..............

Open a terminal (either from the applications menu or from the panel
at the bottom of the screen).

Type

.. code:: bash

   man rmtoo

To read other man pages change the parameter to one of the listed
under ``See Also``, like

.. code:: bash

   man rmtoo-art-latex2

to get information about the latex2 artifact output module.
   
