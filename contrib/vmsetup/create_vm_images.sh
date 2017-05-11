#!/bin/bash
#
# Creates the different flavor VM images for rmToo.
#

set -e

# Use Debian Jessie

DIST=debian-minimal
export DIB_RELEASE=jessie
ADD_ELEMENTS=""

case ${DIST} in
    debian*)
	mirror=debian
	;;
    ubuntu*)
	mirror=ubuntu
	;;
esac

# For local testing build
if test "${RMTOO_VM_TEST_BUILD}" == "yes"; then
    export DIB_DISTRIBUTION_MIRROR=http://10.4.0.4:3142/${mirror}
    export DIB_APT_SOURCES_CONF="default:deb http://10.4.0.4:3142/${mirror} ${DIB_RELEASE} main contrib non-free"
    export DIB_DEV_USER_PWDLESS_SUDO=yes
    export DIB_DEV_USER_USERNAME="rmtoo"
    export DIB_DEV_USER_PASSWORD="rmtoo"
    export DIB_DEV_USER_SHELL="/bin/bash"
    ADD_ELEMENTS+=" devuser"
fi

ADD_ELEMENTS+=" rmtoo-small"

export DIB_DEBOOTSTRAP_EXTRA_ARGS="--include=apt-transport-https"
export DIB_INIT_SYSTEM=systemd
export ELEMENTS_PATH=${PWD}/dib-elements

VM_NAME=rmtoo-vm-${DIST}-${DIB_RELEASE}
disk-image-create --image-size=2G -o ${VM_NAME} ${DIST} ${ADD_ELEMENTS} 2>&1 | tee ${VM_NAME}-build.log
