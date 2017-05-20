Usage of Preinstalled GUI VMs
=============================

Introduction
------------

Preinstalled VMs are available with a Linux graphical user interface.
With the help of the GUI mostly all operations of *rmtoo* can be
executed, like adding or changing requirements, topics, creating the
artifacts and viewing them.

To be able to use the GUI there is the need to take care about a few
things.

Please note that depending on your internet connection to the chosen
data center the usage of the GUI might be slow and include lags.  If
you need a VM in your own data center / public cloud, please contact
our service: rmtoo@florath.net

Start VM
--------

When starting a VM (either as 'Instance' or 'Spot Request') configure:

* AMI: choose 'Search'; choose 'Community AMIs' and search for rmtoo.
  A list of all available VMs with rmtoo is presented. Choose the
  version and flavor you like - please double check that the name
  includes 'GUI' (there are also console only VMs, which are described
  in a different document).
* Depending on the number of users and requirements choose an
  'Instance type'.  For evaluation proposes and small projects 1 CPU
  is enough.  If you plan to work with some people on a mid or large
  size project, you should use 2 CPUs.  There is no need to have more
  than 3-4 GByte RAM - especially for large sets of requirements.
* EBS volumes: one should be enough. For the operating system about
  2GByte should be reserved.  Each additional GByte can hold about
  1000 requirements.
* Security groups: Choose 'Create new security group'; again choose
  'Create Security Group'. As name enter 'rmtoo-gui'; enter a
  description like 'rmtoo GUI access' and choose a VPC.  Add two
  rules: *SSH - TCP - 22 - Anywhere (0.0.0.0/0)* and
  *RDP - TCP - 3389 - Anywhere (0.0.0.0/0)*.
  If you have a fixed IP you can use 'Custom' and your IP address
  instead of 'Anywhere.  Go back to the VM creation page, press reload
  near the security groups field and choose 'rmtoo-gui'.

Start the VM.

Initial Setup
-------------

Before it is possible to connect via rdesktop a password must be set.
Use the chosen ssh key to connect to your VM, e.g.

.. code:: bash

   ssh -i my_key debian@<VMIpAddress>

Use your favorite ssh client to connect.

Reset the User Password
-----------------------

Please note that it is mandatory to set the password for the user -
nevertheless this is seen as not that safe as using an ssh key.
When setting your password chose a strong one, e.g. which contains
lower and upper case letters, digits and special characters.

.. code:: bash

   sudo passwd debian

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
   
