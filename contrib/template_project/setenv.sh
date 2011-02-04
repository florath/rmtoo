#
# Do not execute this - source it like
#
#  . setenv.sh param
#  source setenv.sh param
#

if test $# -ne 1;
then
    echo "+++ Usage: . setenv.sh [DEB|path to rmtoo]"
    echo "    use DEB when using the installed DEB package"
    echo "    specify the (absolut) path to the unpackaged rmtoo package"
else
    RMTOO_DIR=$1

    if test ${RMTOO_DIR} = 'DEB';
    then
        # The path to the Debian package should not be given
	RMTOO_CALL="rmtoo"
	RMTOO_CONTRIB_DIR=/usr/share/doc/rmtoo
    else
	RMTOO_CALL="${RMTOO_DIR}/bin/rmtoo -m${RMTOO_DIR}"
	PYTHONPATH=${RMTOO_DIR}
	export PYTHONPATH
	RMTOO_CONTRIB_DIR=${RMTOO_DIR}
    fi

    export RMTOO_CALL
    export RMTOO_CONTRIB_DIR
fi

