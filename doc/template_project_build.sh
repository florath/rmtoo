#!/bin/bash

TP_RESULT_SHOULD=rmtoo/tests/RMTTest-Blackbox/TemplateProject/result_should

WD=$(mktemp --directory -q --tmpdir rmtoo-template-projct-XXXXXXXX)
# trap "rm -fr $WD" EXIT

cp -r contrib/template_project ${WD}/MyProject

(
    cd ${WD}/MyProject
    . setenv.sh VENV
    make artifacts/reqsprios.tex
)

# Remove the not comparable elements
FILES_NOT_TO_BE_COMPARED="
stats_reqs_cnt.csv
.git_do_not_ignore_empty_dir
"

ARTIFACT_DIR=${WD}/MyProject/artifacts

for tbrf in ${FILES_NOT_TO_BE_COMPARED}; do
    rm -f ${TP_RESULT_SHOULD}/${tbrf}
    rm -f ${ARTIFACT_DIR}/${tbrf}
done

diff -r ${TP_RESULT_SHOULD} ${ARTIFACT_DIR}
