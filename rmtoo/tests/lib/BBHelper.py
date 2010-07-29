#
# Blackbox helper
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import shutil
import difflib

def clear_result_is(mdir):
    p = os.path.join(mdir, "result_is")
    shutil.rmtree(p)
    os.makedirs(p)

def find(mdir):
    r = set()
    for d, _, files in os.walk(mdir):
        for f in files:
            o = os.path.join(d, f)
            # Cut off the mdir at the beginning
            assert(o.startswith(mdir))
            r.add(o[len(mdir)+1:])
    return r

def unified_diff(mdir, fname):
    fa = file(os.path.join(mdir, "result_is", fname), "r")
    a = fa.readlines()
    fa.close()

    fb = file(os.path.join(mdir, "result_should", fname), "r")
    b = fb.readlines()
    fb.close()

    r = []
    for l in difflib.unified_diff(a, b):
        r.append(l)

    if len(r)==0:
        return None
    return r

# This returns a trippel:
#  missing files in result_is
#  additional files in result_is
#  differences in files
# The differences is a map where the key is the filename and the
# content is a unified diff output.
def compare_results(mdir):
    files_is = find(os.path.join(mdir, "result_is"))
    files_should = find(os.path.join(mdir, "result_should"))

    missing_files = files_is - files_should
    additional_files = files_should - files_is

    files_to_compare = files_is.intersection(files_should)

    r = {}
    for df in files_to_compare:
        ud = unified_diff(mdir, df)
        if ud!=None:
            r[df] = ud

    return missing_files, additional_files, r
