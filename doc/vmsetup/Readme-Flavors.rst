Flavors
+++++++

There is the possiblity to use predefined VMs for the evaluation of
rmtoo as well as for daily work.  This document describes different
flavors of the preinstalled VMs for different rmtoo use cases.


Naming Conventions
------------------

The preinstalled VM images have a common naming schema:

.. code:: bash

   rmtoo-VV.WW.XX_size_variant_os_customer_release

where

* *VV.WW.XX* is the version of rmtoo that is installed on the VM.
* *size* is marker for a logical size. 
* *variant* is a list of additional properties (like GUI).
* *os names* the used operating system
* *customer* is the name of the customer / company.
* *release* gives information about the release number

For details please consult the next chapter in this document.

Please note that not all flavors are available on all virtualization
environments / market places.  If you want / need a special flavor
(e.g. operating system) that is not available on the platform you are
using, please contact us and we try to help: rmtoo@florath.net.

With the start of one of the VMs you accept the appropriate statements.


Product Introduction
--------------------

While in product introduction phase on the appropriate cloud
service, there might only a limited set of different VM flavors
available.


Size
----

=======================  =========  =========   =========
Description              Small      Medium      Large
=======================  =========  =========   =========
Evaulation of rmtoo        X           X          X
Number of requirements    <100       <=500      >500
Number of users           1          <=5        >5
=======================  =========  =========   =========

Small
.....

Use cases:

* Evaluation of rmtoo
* Small projects (<100 requirements)
* Single user

Features:

* Complete installation of rmtoo in a python virtual environment.
  This included binaries, man-pages and tools.
* Complete installation of all dependencies to create documents and
  graphs.
* Template project installed and usable.
  It is possible to use the template project and immediately start
  working.
* Support based on best effort.
  Reporting can be done on the project web page.

Not included:
  
* No additional support (like EMail, phone or IRC)
* No guaranteed reaction times.
* No guaranteed bug fix times.
* No backup of data.
* No security hardening of OS.
* No git / no baselines    
* No remote GUI access / only text console.
  Either ssh can be used (might be slow) or the created documents must
  be transferred to a local computer to be viewed.


Medium
......

Use cases:

* Mid-size projects (between 100 and 500 requirements)
* Up to five users
* Evaluation of rmtoo for larger projects

Features:

Same features as the Small size except the first bullet point
that is replaced by:

* Complete installation of rmtoo in a global python virtual
  environment. This included binaries, man-pages and tools.

Not included:

Same as for the Small size.


Large
-----

Use cases:

* large projects (more than 500 requirements)
* more than five users
* Evaluation of rmtoo for large projects

Features:

Same features as the Medium size except the first bullet point
that is replaced by:

* Complete installation of rmtoo in a global python virtual
  environment. This included binaries, man-pages and tools.

Not included:

Same as for the Medium size.


Variant
-------

console
.......

The VM comes with a console (terminal ssh) access only.  Commands must
be typed in as described in the documentation.  Nevertheless using a
file manager that is capable of (remote) ssh connections
(e.g. nautilus under Linux), file transfer to and from the VM might be
easier for those

gui
...

The VM comes with an installed and ready to use Linux X Windows
system.  It is possible to use a graphical remote client (like
rdesktop) to connect to the VM.  Using the remote desktop it is
possible to start an editor, call rmtoo or view generated artifacts.

Please note that there is no dedicated GUI for the rmtoo application
itself.  Nevertheless with the help of the desktop GUI it might be
easier to edit requirements, run rmtoo or view artifacts for users who
are not used to use the text console.


OS Names
--------

Currently only Debian Jessie is supported.


Customer
--------

The name of the customer - if this is a special setup VM for a
customer.  It is set to 'community' for general available VMs.


Release
-------

An indication of the release number / version.  From time to time
a new release will be build, even if the rmtoo version does not
change, because of e.g. operating system updates.
