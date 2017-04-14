'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Test utilities.
 
 (c) 2011-2012 by flonatel

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
    '''Hides the line number from the stderr/stdout output.'''
    res = []
    for line in istr.split("\n"):
        isplit = line.split(";")
        if len(isplit) >= 5:
            isplit[5] = "===SOURCELINENO==="
            res.append(";".join(isplit))
        else:
            res.append(line)
    return "\n".join(res)
