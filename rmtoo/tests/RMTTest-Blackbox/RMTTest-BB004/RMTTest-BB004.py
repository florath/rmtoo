'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Blackbox test: Pulp Fiction in German.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import os

from rmtoo.lib.RmtooMain import main_impl
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, \
    cleanup_std_log, delete_result_is_dir, check_file_results

mdir = "tests/RMTTest-Blackbox/RMTTest-BB004"


class RMTTestBB004:

    def rmttest_PulpFictionInGermanOldConfig(self):
        "Pulp Fiction's Mr Wulf in German (new configuration)."

        def myexit(n):
            pass

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        main_impl(["-j", "file://" + mdir + "/input/Config.json"],
                  mout, merr, exitfun=myexit)
        cleanup_std_log(mout, merr)
        check_file_results(mdir, "BB004")
        delete_result_is_dir()
