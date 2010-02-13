#!/bin/bash

set -e

if test $# -ne 1;
then
    echo "+++ Usage: build_tar.sh <version>"
    exit 1
fi

PACKAGE_NAME=rmtoo-$1

make clean
make all
make latex

rm -fr ttt
mkdir ttt
mv doc/latex/requirements.pdf ttt
mv reqtree.png ttt

make clean

mkdir -p package/${PACKAGE_NAME}
for d in bin COPYING doc gpl-3.0.txt rmtoo setenv.sh Readme.txt
do
    cp -r $d package/${PACKAGE_NAME}
done

mv ttt/* package/${PACKAGE_NAME}/doc

find package/${PACKAGE_NAME} -name "*~" | xargs rm

(cd package
tar -cf ${PACKAGE_NAME}.tar ${PACKAGE_NAME}
gzip -9 ${PACKAGE_NAME}.tar
)
mv package/${PACKAGE_NAME}.tar.gz .
rm -fr package ttt
