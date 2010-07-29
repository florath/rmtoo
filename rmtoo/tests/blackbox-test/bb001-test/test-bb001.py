#
# Blackbox rmtoo tests
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import clear_result_is, compare_results

mdir = "tests/blackbox-test/bb001-test"

class TestBB001:

    def test_pos_001(self):
        "BB Basic with one requirement"

        clear_result_is(mdir)
        main(["-f", mdir + "/input/Config.py", "-m", ".."])
        missing_files, additional_files, diffs = compare_results(mdir)
        assert(len(missing_files)==0)
        assert(len(additional_files)==0)
        # The count stats is always different because of the timestamp
        assert(len(diffs)==1)
        # ['---  \n',
        #  '+++  \n', 
        #  '@@ -1,1 +1,1 @@\n',
        #  '-2010-07-29_21:47:26 1\n',
        #  '+2010-07-29_21:26:21 1\n']
        assert(len(diffs["stats_reqs_cnt.csv"])==5)
