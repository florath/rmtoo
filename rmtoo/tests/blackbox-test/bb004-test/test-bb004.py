'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Blackbox test: Pulp Fiction in German.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, \
    compare_results, cleanup_std_log, delete_result_is_dir, check_file_results

mdir = "tests/blackbox-test/bb004-test"

class TestBB004:

    def test_PulpFictionInGermanOldConfig(self):
        "Pulp Fiction's Mr Wulf in German (old configuration)."

        def myexit(n):
            pass

        mout, merr = prepare_result_is_dir()
        main(["-f", mdir + "/input/Config2.py", "-m", ".."], mout, merr,
             exitfun=myexit)
        cleanup_std_log(mout, merr)
        check_file_results(mdir)
        delete_result_is_dir()
