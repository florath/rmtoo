#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, \
    compare_results, cleanup_std_log, delete_result_is_dir, check_file_results

mdir = "tests/blackbox-test/bb003-test"

class TestBB003:

    def test_pos_001(self):
        "Pulp Fiction's Mr Wulf in English"

        def myexit(n):
            pass

        mout, merr = prepare_result_is_dir()
        main(["-f", mdir + "/input/Config2.py", "-m", ".."], mout, merr,
             exitfun=myexit)
        cleanup_std_log(mout, merr)
        check_file_results(mdir)
        delete_result_is_dir()
