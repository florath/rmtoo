'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os
import unittest

from rmtoo.lib.RmtooMain import main_func
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, \
    cleanup_std_log, delete_result_is_dir, check_file_results

mdir = "tests/RMTTest-Blackbox/RMTTest-BB009"


class RMTTestBB009(unittest.TestCase):

    def rmttest_pos(self):
        "BB Basic with one requirement - bad analytics"

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        result = main_func(["-j", "file://" + mdir + "/input/Config.json"],
                           mout, merr)
        cleanup_std_log(mout, merr)
        self.assertFalse(result)
        check_file_results(mdir)
        delete_result_is_dir()
