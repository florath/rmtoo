#
# Blackbox helper
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import time
import shutil
import difflib
import zipfile
import xml.dom.minidom

from rmtoo.lib.xmlutils.xmlcmp import xmlcmp_files
from rmtoo.tests.lib.Utils import create_tmp_dir

def tmp_dir():
    return os.environ["rmtoo_test_dir"]

def find(mdir):
    r = set()
    for d, _, files in os.walk(mdir):
        for f in files:
            o = os.path.join(d, f)
            # Cut off the mdir at the beginning
            assert(o.startswith(mdir))
            r.add(o[len(mdir) + 1:])
    return r

def unified_diff(mdir, fname):
    fa = file(os.path.join(os.environ["rmtoo_test_dir"], fname), "r")
    a = fa.readlines()
    fa.close()

    fb = file(os.path.join(mdir, "result_should", fname), "r")
    b = fb.readlines()
    fb.close()

    r = []
    for l in difflib.unified_diff(a, b):
        r.append(l)

    if len(r) == 0:
        return None
    return r

# This implements the compare_xml with the help of the xmldiff
# package.
def compare_xml(mdir, fname):
    if fname == "reqspricing.ods-extracted/content.xml":
        # Skip this (output from oomodule)
        return True

    file1 = os.path.join(os.environ["rmtoo_test_dir"], fname)
    file2 = os.path.join(mdir, "result_should", fname)

    r, s = xmlcmp_files(file1, file2)

    if not r:
        print("XMLCmp difference: file [%s] diff [%s]" % (fname, s))

    return r

# This returns a trippel:
#  missing files in result_is
#  additional files in result_is
#  differences in files
# The differences is a map where the key is the filename and the
# content is a unified diff output.
def compare_results(mdir):
    files_is = find(os.path.join(os.environ["rmtoo_test_dir"]))
    files_should = find(os.path.join(mdir, "result_should"))

    missing_files = files_is - files_should
    additional_files = files_should - files_is

    files_to_compare = files_is.intersection(files_should)

    r = {}
    for df in files_to_compare:
        # XML files must be handled differently: they might be
        # different when compared with diff but might have the same
        # semantic.
        if df.endswith(".xml"):
            if not compare_xml(mdir, df):
                r[df] = "XML files differ"
        else:
            ud = unified_diff(mdir, df)
            if ud != None:
                r[df] = ud

    return missing_files, additional_files, r

# Open up the stdout and stderr files for testing proposes
def create_std_log(mdir):
    mout = file(os.path.join(mdir, "stdout"), "w")
    merr = file(os.path.join(mdir, "stderr"), "w")
    return mout, merr

def cleanup_std_log(mout, merr):
    mout.close()
    merr.close()

def delete_result_is_dir():
    assert(os.environ["rmtoo_test_dir"] != None)
    shutil.rmtree(os.environ["rmtoo_test_dir"])
    del(os.environ["rmtoo_test_dir"])

def prepare_result_is_dir():
    td = create_tmp_dir()
    os.environ["rmtoo_test_dir"] = td
    mout, merr = create_std_log(td)
    return mout, merr

def makedirs2(d):
    try:
        os.makedirs(d)
    except OSError, ose:
        # If it already exists - it is no error.
        pass

# For some testcases there is the need to compare tarred, zipped
# etc. containers.  Because the container store also some meta-data it
# ist mostly impossible to compare them directly.  This functions
# extracts all given containers and removes the original files, so
# that the above implemented unified diff can be used to compate also
# these files.
def extract_container_files(lof):

    def extract_one_container_file_zip(fn):
        zip_filename = os.path.join(os.environ["rmtoo_test_dir"], fn)
        zf = zipfile.ZipFile(zip_filename, "r")
        # The python 2.6 extractall is not available....
        #zf.extractall(os.path.join(os.environ["rmtoo_test_dir"],
        #     fn, "-extracted"))
        bdir = os.path.join(os.environ["rmtoo_test_dir"], fn + "-extracted")
        fl = zf.infolist()
        for f in fl:
            full_name = os.path.join(bdir, f.filename)
            directory = os.path.dirname(full_name)
            makedirs2(directory)
            ofile = file(full_name, "w")
            ofile.write(zf.read(f.filename))
            ofile.close()
        zf.close()
        # Remove the original
        os.unlink(zip_filename)

    def extract_one_container_file(fn):
        if fn.endswith(".ods"):
            extract_one_container_file_zip(fn)
        else:
            # Unknown extension
            assert(False)

    for f in lof:
        extract_one_container_file(f)

# Some output files do contain the temporary output dir (e.g. the
# makefile dependencies).  To compare them with old versions, this
# function rewrites the file unifying the output dir.
# (This function does a replace string on the output dir with a
# defined fixed string.)
def unify_output_dir(filename):
    fullpathname = os.path.join(os.environ["rmtoo_test_dir"], filename)
    # Read it in
    fd = file(fullpathname, "r")
    c = fd.read()
    fd.close()
    # Replace
      
    d = c.replace(os.environ["rmtoo_test_dir"],
                  "===SYMBOLIC-OUTPUT-DIR===")
    # Write out
    fd = file(fullpathname, "w")
    fd.write(d)
    fd.close()

def check_result(missing_files, additional_files, diffs):
    assert(len(missing_files) == 0)

    if len(additional_files) != 0:
        print("ADDITIONAL FILES [%s]" % additional_files)
    assert(len(additional_files) == 0)

    if len(diffs) != 0:
        print("DIFFS [%s]" % diffs)
    assert(len(diffs) == 0)

def check_file_results(mdir):
    missing_files, additional_files, diffs = compare_results(mdir)
    check_result(missing_files, additional_files, diffs)

