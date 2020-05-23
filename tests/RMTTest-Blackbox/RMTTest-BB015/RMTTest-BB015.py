'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for Topic

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os
import shutil


from rmtoo.lib.main.NormalizeDependencies import main_impl, main_func
from BBHelper import prepare_result_is_dir, \
    cleanup_std_log, delete_result_is_dir, tmp_dir, check_file_results

mdir = "tests/RMTTest-Blackbox/RMTTest-BB015"


class RMTTestBB015(object):

    def rmttest_pos_01(self):
        "Normalization test"

        def myexit(n):
            self.rval = n

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        td = tmp_dir()

        # Copy requirements to tmp dir
        destdir = os.path.join(td, "reqs")
        shutil.copytree("%s/input/reqs" % mdir, destdir,
                        ignore=shutil.ignore_patterns('*~',))

        # Call the converter
        main_impl(["-j", "file://" + mdir + "/input/Config.json"],
                  mout, merr, main_func, myexit)
        assert 0 == self.rval
        cleanup_std_log(mout, merr)
        check_file_results(mdir)
        delete_result_is_dir()
