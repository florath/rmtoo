#!/bin/bash
set -e

# The first and one and only argument must be the version number. 
if test $# -ne 1;
then
    echo "+++ Usage: build_tar.sh <version>"
    exit 1
fi

PACKAGE_NAME=rmtoo-$1

# Create requirments dependency graph and PDF.
make clean
make all

# Temporary store documents in an own directory: a make clean will
# remove them - but we need it.
rm -fr ttt
mkdir ttt
mv artifacts/requirements.pdf ttt
mv artifacts/req-graph1.png artifacts/req-graph2.png ttt

# Clean up everything before copying into the tar ball directory.
make clean

mkdir -p package/${PACKAGE_NAME}
for d in bin COPYING doc gpl-3.0.txt rmtoo setenv.sh Readme-GitPython.txt Readme-Hacking.txt Readme-OS-X.txt Readme-Overview.txt Readme-RmtooOnRmtoo.txt Readme.rst Readme-Windows.txt Makefile contrib
do
    cp -r $d package/${PACKAGE_NAME}
done

# The picture and the pdf are delivered seperatly
# mv ttt/* package/${PACKAGE_NAME}/doc

# Do not deliver emacs backup files
find package/${PACKAGE_NAME} -name "*~" | xargs rm -f
# Do not deliver compiled python files
find package/${PACKAGE_NAME} -name "*.pyc" | xargs rm -f
# Also remove the presentation (will be delivered seperatly)
rm -fr package/${PACKAGE_NAME}/doc/presentations
# Create the artifacts directory (used when rmtoo itself if build)
mkdir -p package/${PACKAGE_NAME}/artifacts

# Create tag ball
(cd package
tar -cf ${PACKAGE_NAME}.tar ${PACKAGE_NAME}
gzip -9 ${PACKAGE_NAME}.tar
)
mv package/${PACKAGE_NAME}.tar.gz .

# Clean up
rm -fr package ttt
