'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os

from rmtoo.lib.RmtooMain import main_impl
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, \
    cleanup_std_log, delete_result_is_dir, \
    unify_output_dir, check_file_results

mdir_orig = "tests/blackbox-test/bb006-test"
mdir = "tests/RMTTest-Blackbox/RMTTest-BB006"


class RMTTestBB006:

    def rmttest_pos_001(self):
        "BB Basic with one requirement - check makefile dependencies"

        def myexit(n):
            pass

        os.environ["basedir"] = mdir_orig
        os.environ["rbasedir"] = mdir
        mout, merr = prepare_result_is_dir()
        main_impl(["-j", "file://" + mdir + "/input/Config.json",
                   "-j", '''json:{"actions": {"create_makefile_dependencies":
                 "${ENV:rmtoo_test_dir}/makefile_deps"}}'''],
                  mout, merr, exitfun=myexit)
        cleanup_std_log(mout, merr)
        unify_output_dir("makefile_deps")
        check_file_results(mdir, "BB006", True)
        delete_result_is_dir()
