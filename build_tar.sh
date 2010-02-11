#!/bin/bash

PACKAGE_NAME=rmtoo-1

./bin/rmtoo -c latex -d doc/requirements -f doc/requirements/Config.py -l doc/latex -m .
(cd doc/latex && pdflatex requirements.tex ; pdflatex requirements.tex )
mv doc/latex/requirements.pdf doc
dot -Tpng -o doc/reqsdepgraph.png doc/latex/reqs/dependsgraph.dot

mkdir -p package/${PACKAGE_NAME}
for d in bin COPYING doc gpl-3.0.txt rmtoo setenv.sh Readme.txt
do
    cp -r $d package/${PACKAGE_NAME}
done

find package/${PACKAGE_NAME} -name "*~" | xargs rm

(cd package
tar -cf ${PACKAGE_NAME}.tar ${PACKAGE_NAME}
gzip -9 ${PACKAGE_NAME}.tar
)
mv package/${PACKAGE_NAME}.tar.gz .
rm -fr package
