'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for Topic

 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os
import shutil

from rmtoo.lib.main.NormalizeDependencies import main, main_impl
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, compare_results, \
    cleanup_std_log, delete_result_is_dir, extract_container_files, tmp_dir, \
    check_file_results

mdir = "tests/blackbox-test/bb015-test"

class TestBB015:

    def test_pos_01(self):
        "Normalization test"

        def myexit(n):
            self.rval = n

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        td = tmp_dir()

        #print("TD %s" % td)

        # Copy requirements to tmp dir
        destdir = os.path.join(td, "reqs")
        shutil.copytree("%s/input/reqs" % mdir, destdir,
                        ignore=shutil.ignore_patterns('*~',))

        # Call the converter
        main(["-j", "file://" + mdir + "/input/Config.json"],
             mout, merr, main_impl, myexit)
        assert(self.rval == 0)
        cleanup_std_log(mout, merr)
        check_file_results(mdir)
        delete_result_is_dir()
