#!/bin/bash
#
# This needs to be called on a plain Ubuntu 16.04 to be
# able to build the rmtoo virtual machines
#
# Before:
#  git clone https://github.com/florath/rmtoo.git
#

sudo apt update
sudo apt upgrade
sudo apt install qemu-utils debootstrap virtualenv kpartx

mkdir devel
cd devel
virtualenv venv
source venv/bin/activate
cd venv
pip install diskimage-builder
pip install awscli
aws configure
