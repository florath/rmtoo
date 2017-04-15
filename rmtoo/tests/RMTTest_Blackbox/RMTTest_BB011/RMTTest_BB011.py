'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Blackbox rmtoo test
   
 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os

from rmtoo.lib.RmtooMain import main_impl
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, compare_results, \
    cleanup_std_log, delete_result_is_dir, extract_container_files, \
    unify_output_dir, check_file_results

mdir = "tests/RMTTest_Blackbox/RMTTest_BB011"

class RMTTest_BB011:

    def rmttest_pos(self):
        "BB Basic where one requirement is not used because not in topic"

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        result = main_impl(["-j", "file://" + mdir + "/input/Config.json"],
                           mout, merr)
        cleanup_std_log(mout, merr)
        assert(result == False)
        check_file_results(mdir)
        delete_result_is_dir()
