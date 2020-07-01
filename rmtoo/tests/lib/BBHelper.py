'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox helper

 (c) 2010,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import print_function

import io
import os
import shutil
import difflib
import zipfile

import time

from rmtoo.lib.xmlutils.xmlcmp import xmlcmp_files
from rmtoo.tests.lib.Utils import create_tmp_dir, hide_volatile
from rmtoo.lib.logging import tear_down_log_handler, tear_down_trace_handler
from rmtoo.lib.RmtooMain import main_func


def tmp_dir():
    return os.environ["rmtoo_test_dir"]


def find(mdir):
    r = set()
    for d, _, files in os.walk(mdir):
        for f in files:
            o = os.path.join(d, f)
            # Cut off the mdir at the beginning
            assert o.startswith(mdir)
            r.add(o[len(mdir) + 1:])
    return r


def unified_diff(mdir, fname, sorted_diff=False, artifacts_dir=None):
    if artifacts_dir is None:
        artifacts_path = os.environ["rmtoo_test_dir"]
    else:
        artifacts_path = os.path.join(os.environ["rmtoo_test_dir"],
                                      artifacts_dir)

    with io.open(os.path.join(artifacts_path, fname), "r",
                 encoding="utf-8") as fa:
        a = fa.readlines()

    with io.open(os.path.join(mdir, "result_should", fname), "r",
                 encoding="utf-8") as fb:
        b = fb.readlines()

    if sorted_diff:
        a = sorted(a)
        b = sorted(b)

    r = []
    for line in difflib.unified_diff(a, b):
        r.append(line)

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
def compare_results(mdir, relaxed=False, artifacts_dir=None):
    if artifacts_dir is None:
        artifacts_path = os.environ["rmtoo_test_dir"]
    else:
        artifacts_path = os.path.join(os.environ["rmtoo_test_dir"],
                                      artifacts_dir)

    files_is = find(artifacts_path)
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
            sorted_diff = relaxed and \
                df in ['stderr', 'makefile_deps', 'req-graph1.dot',
                                 'reqsprios.tex']
            ud = unified_diff(mdir, df, sorted_diff, artifacts_dir)
            if ud is not None:
                r[df] = ud

    return missing_files, additional_files, r


# Open up the stdout and stderr files for testing proposes
def create_std_log(mdir):
    mout = io.open(os.path.join(mdir, "stdout"), "w", encoding="utf-8")
    merr = io.open(os.path.join(mdir, "stderr"), "w", encoding="utf-8")
    return mout, merr


def cleanup_std_log(mout, merr):
    mout.flush()
    merr.flush()
    tear_down_log_handler()
    tear_down_trace_handler()
    mout.close()
    merr.close()


def delete_result_is_dir():
    assert os.environ["rmtoo_test_dir"] is not None
    shutil.rmtree(os.environ["rmtoo_test_dir"])
    del os.environ["rmtoo_test_dir"]


def prepare_result_is_dir():
    td = create_tmp_dir()
    os.environ["rmtoo_test_dir"] = td
    mout, merr = create_std_log(td)
    return mout, merr


def makedirs2(d):
    try:
        os.makedirs(d)
    except OSError:
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
        # zf.extractall(os.path.join(os.environ["rmtoo_test_dir"],
        #     fn, "-extracted"))
        bdir = os.path.join(os.environ["rmtoo_test_dir"], fn + "-extracted")
        fl = zf.infolist()
        for f in fl:
            full_name = os.path.join(bdir, f.filename)
            directory = os.path.dirname(full_name)
            makedirs2(directory)
            with io.open(full_name, "w", encoding="utf-8") as ofile:
                data = zf.read(f.filename).decode("utf-8")
                ofile.write(data)
        zf.close()
        # Remove the original
        os.unlink(zip_filename)

    def extract_one_container_file(fn):
        if fn.endswith(".ods"):
            extract_one_container_file_zip(fn)
        else:
            # Unknown extension
            assert False

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
    with io.open(fullpathname, "r", encoding="utf-8") as fd:
        c = fd.read()
    # Replace

    d = c.replace(os.environ["rmtoo_test_dir"],
                  "===SYMBOLIC-OUTPUT-DIR===")
    # Write out
    with io.open(fullpathname, "w", encoding="utf-8") as fd:
        fd.write(d)


# Deprecated: please use the BBHelper class
def check_result(missing_files, additional_files, diffs, tcname):
    if len(missing_files) != 0:
        print("[%s] MISSING FILES [%s]" % (tcname, missing_files))
    assert len(missing_files) == 0

    if len(additional_files) != 0:
        print("[%s] ADDITIONAL FILES [%s]" % (tcname, additional_files))
    assert len(additional_files) == 0

    if len(diffs) != 0:
        print("[%s] DIFFS [%s]" % (tcname, diffs))
    assert len(diffs) == 0


# Deprecated: please use the BBHelper class
def prepare_stderr():
    '''Some lines of the stderr contain a date / timestamp.
       This must be unified in order to be able to compare them.'''
    with open(os.path.join(os.environ["rmtoo_test_dir"], "stderr")) as ms:
        lines = ms.readlines()

    with open(os.path.join(
            os.environ["rmtoo_test_dir"], "stderr"), "w") as new_stderr:
        for line in lines:
            new_stderr.write("%s" % hide_volatile(line))


# Deprecated: please use the BBHelper class
def check_file_results(mdir, tcname="<UNKNOWN>", relaxed=False,
                       artifacts_dir=None):
    prepare_stderr()
    missing_files, additional_files, diffs \
        = compare_results(mdir, relaxed, artifacts_dir)
    check_result(missing_files, additional_files, diffs, tcname)


class BBHelper(object):

    @staticmethod
    def myexit(n):
        pass

    def setup_class(self):
        # Stored for logging proposes
        self.__name = type(self).__name__

        if hasattr(self, "test_dir"):
            self.__in_test_dir = self.test_dir
            self.__out_test_dir = self.test_dir
        else:
            if hasattr(self, "in_test_dir"):
                self.__in_test_dir = self.in_test_dir
            if hasattr(self, "out_test_dir"):
                self.__out_test_dir = self.out_test_dir

        os.environ["basedir"] = self.__in_test_dir
        os.environ["rbasedir"] = self.__out_test_dir

        os.environ['TZ'] = 'Europe/Berlin'
        time.tzset()

        self.config_file_subdir = "input"
        self.artifacts_dir = None

    def __check_result(self, missing_files, additional_files, diffs):
        if len(missing_files) != 0:
            print("[%s] MISSING FILES [%s]"
                  % (self.__name, missing_files))
        assert 0 == len(missing_files)

        if len(additional_files) != 0:
            print("[%s] ADDITIONAL FILES [%s]"
                  % (self.__name, additional_files))
        assert 0 == len(additional_files)

        if len(diffs) != 0:
            print("[%s] DIFFS [%s]" % (self.__name, diffs))
        assert 0 == len(diffs)

    def __check_file_results(self, relaxed):
        prepare_stderr()
        missing_files, additional_files, diffs \
            = compare_results(self.__out_test_dir, relaxed,
                              self.artifacts_dir)
        self.__check_result(missing_files, additional_files, diffs)

    def run_test(self, relaxed=False, container_files=[],
                 unify_output_dirs=[], cmd_line_params=[],
                 success=True, yaml=False):
        if not cmd_line_params:
            if not yaml:
                cmd_line_params = [
                    "-j",
                    "file://" + os.path.join(
                        self.__out_test_dir, self.config_file_subdir,
                        "Config.json")]
            else:
                cmd_line_params = [
                    "-y",
                    "file://" + os.path.join(
                        self.__out_test_dir, self.config_file_subdir,
                        "Config.yaml")]

        self.__mout, self.__merr = prepare_result_is_dir()
        if self.artifacts_dir is not None:
            makedirs2(os.path.join(os.environ["rmtoo_test_dir"],
                                   self.artifacts_dir))
        result = main_func(cmd_line_params,
                           self.__mout, self.__merr)
        cleanup_std_log(self.__mout, self.__merr)
        assert success == result
        if container_files:
            extract_container_files(container_files)
        if unify_output_dirs:
            for uod in unify_output_dirs:
                unify_output_dir(uod)
        self.__check_file_results(relaxed)
        delete_result_is_dir()
