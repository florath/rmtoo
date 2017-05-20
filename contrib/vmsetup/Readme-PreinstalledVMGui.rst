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

rdesktop
--------

All
...

Before it is possible to connect via rdesktop a password must be set.
Use the chosen ssh key to connect to your VM, e.g.

.. code:: bash

   ssh -i my_key debian@<VMIpAddress>



Linux
.....

rdesktop -u debian -p <password> 192.168.122.245
