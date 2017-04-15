'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Blackbox test: Pulp Fiction in German.
   
 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import os

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, \
    compare_results, cleanup_std_log, delete_result_is_dir, check_file_results

mdir = "tests/RMTTest_Blackbox/RMTTest_BB004"

class RMTTest_BB004:

    def rmttest_PulpFictionInGermanOldConfig(self):
        "Pulp Fiction's Mr Wulf in German (old configuration)."

        def myexit(n):
            pass

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        main(["-j", "file://" + mdir + "/input/Config.json"], 
             mout, merr, exitfun=myexit)
        cleanup_std_log(mout, merr)
        check_file_results(mdir)
        delete_result_is_dir()
