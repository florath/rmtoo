Starting rmtoo VM on AWS EC2
============================

Please note that the procedure as described here is not suitable
any longer.

As soon as the VMs are placed on the AWS marketplace, this description
will be updated.


Introduction
------------

This document describes how to start a preinstalled VM on AWS EC2.
Doing so is a complex process and some steps have to be followed.  The
initial process i.e. registering at AWS EC2, reading the documents and
getting knowledge about how to use the GUI is lengthy.  If this step
is taken, starting a rmtoo predefined VM is done in a couple of
minutes.


Using AWS EC2
--------------

To start a VM on AWS EC2 you need an account on AWS_.

.. _AWS: http://aws.amazon.com/ec2‎

Create an account and make sure that you are able to launch VM
instances.


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
