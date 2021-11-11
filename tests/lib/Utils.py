'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Test utilities.

 (c) 2011,2017 by flonatel

 For licensing details see COPYING
'''

import tempfile
import shutil
import re


def create_tmp_dir():
    '''Create a temporary directory.'''
    return tempfile.mkdtemp(prefix="rmtoo-tst-ris-")


def delete_tmp_dir(dirname):
    '''Deletes a temporary directory.'''
    shutil.rmtree(dirname)


_date_re = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}"
                      ":[0-9]{2},[0-9]{3}")


def hide_timestamp(istr):
    return _date_re.sub("===DATETIMESTAMP===", istr)


def hide_lineno(istr):
    res = ""
    slines = istr.split("\n")
    for line in slines:
        if line == "":
            break
        sline = line.split(";")

        if sline[0] != "===DATETIMESTAMP===":
            res += line + "\n"
            continue

        sline[5] = "===LINENO==="
        res += ";".join(sline) + "\n"
    return res


def hide_volatile(istr):
    return hide_lineno(hide_timestamp(istr))
