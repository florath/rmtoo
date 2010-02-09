#!/bin/bash

PACKAGE_NAME=rmtoo-0.9

mkdir -p package/${PACKAGE_NAME}
for d in bin COPYING doc gpl-3.0.txt rmtoo setenv.sh
do
    cp -r $d package/${PACKAGE_NAME}
done

(cd package
tar -cf ${PACKAGE_NAME}.tar ${PACKAGE_NAME}
gzip -9 ${PACKAGE_NAME}.tar
)
mv package/${PACKAGE_NAME}.tar.gz .
rm -fr package
