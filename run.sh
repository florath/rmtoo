#!/bin/bash
# Create a new document from template within venv environment
FILE=$(readlink -f $0)
BASEDIR=$(dirname ${FILE})
cd $BASEDIR/..

# sudo apt install texlive-latex-extra graphivz

if [ -d venv ]; then 
  . venv/bin/activate
else
  python3 -m virtualenv venv
  . venv/bin/activate
  cd rmtoo
  python3 setup.py install
  cd -
fi

rm -rf venv/test42
cp -r rmtoo/contrib/template_project venv/test42

ln -fs ../rmtoo venv/rmtoo

cd venv/
. test42/setenv.sh VENV

cd test42
make clean && rm .rmtoo_dependencies
make

