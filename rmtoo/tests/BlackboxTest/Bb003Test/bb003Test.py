'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Blackbox rmtoo test
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os
from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, \
    cleanup_std_log, delete_result_is_dir, check_file_results

mdir = "tests/BlackboxTest/Bb003Test"

class TestBB003:

    def test_pos_001(self):
        "Pulp Fiction's Mr Wulf in English"

        def myexit(n):
            pass

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        main(["-j", "file://" + mdir + "/input/Config.json"], mout, merr,
             exitfun=myexit)
        cleanup_std_log(mout, merr)
        check_file_results(mdir)
        delete_result_is_dir()
