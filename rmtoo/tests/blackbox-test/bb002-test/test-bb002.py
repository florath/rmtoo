#
# Blackbox rmtoo tests
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import clear_result_is, compare_results, create_std_log, cleanup_std_log

mdir = "tests/blackbox-test/bb002-test"

class TestBB001:

    def test_pos_001(self):
        "BB Hotspot in the middle of the graph 2"

        clear_result_is(mdir)
        mout, merr = create_std_log(mdir)
        main(["-f", mdir + "/input/Config2.py", "-m", ".."], mout, merr)
        cleanup_std_log(mout, merr)
        missing_files, additional_files, diffs = compare_results(mdir)
        assert(len(missing_files)==0)
        assert(len(additional_files)==0)
        assert(len(diffs)==0)
