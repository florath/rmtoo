#
# Blackbox rmtoo tests
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import clear_result_is, compare_results

mdir = "tests/blackbox-test/bb002-test"

class TestBB001:

    def test_pos_001(self):
        "BB Basic with one requirement - reqs only from FILES"

        clear_result_is(mdir)
        main(["-f", mdir + "/input/Config2.py", "-m", ".."])
        missing_files, additional_files, diffs = compare_results(mdir)
        assert(len(missing_files)==0)
        assert(len(additional_files)==0)
        assert(len(diffs)==0)

