#
# Do not execute this - source it like
#
#  . setenv.sh param
#  source setenv.sh param
#

if test $# -ne 1;
then
    echo "+++ Usage: . setenv.sh [VENV|EDITABLE|path to rmtoo]"
    echo "    use VENV when using pip install rmtoo in virtualenv"
    echo "    use EDITABLE when using pip install -e . in development"
    echo "    specify the (absolute) path to the unpackaged rmtoo package"
else
    RMTOO_DIR=$1

    if test ${RMTOO_DIR} = 'VENV' -o ${RMTOO_DIR} = 'EDITABLE';
    then
	RMTOO_CALL="rmtoo"
	RMTOO_CONTRIB_DIR=$(rmtoo-contrib-dir)
    else
	RMTOO_CALL="${RMTOO_DIR}/bin/rmtoo -m${RMTOO_DIR}"
	PYTHONPATH=${RMTOO_DIR}
	export PYTHONPATH
	RMTOO_CONTRIB_DIR=${RMTOO_DIR}
    fi

    export RMTOO_CALL
    export RMTOO_CONTRIB_DIR
fi

