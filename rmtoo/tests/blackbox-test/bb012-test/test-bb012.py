#
# Blackbox rmtoo tests
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os

from rmtoo.lib.RmtooMain import main_impl
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, compare_results, \
    cleanup_std_log, delete_result_is_dir, extract_container_files, \
    unify_output_dir

mdir = "tests/blackbox-test/bb012-test"

class TestBB012:

    def test_pos(self):
        "BB resulting requirements are not dependend"

        mout, merr = prepare_result_is_dir()
        result = main_impl(["-f", mdir + "/input/Config1.py", "-m", ".."],
                           mout, merr)
        cleanup_std_log(mout, merr)
        missing_files, additional_files, diffs = compare_results(mdir)
        assert(result==False)

        # WHY : stop on errors is set to True!
        assert(len(missing_files)==0)
        assert(len(additional_files)==0)

        if len(diffs)!=0:
            print("DIFFS: %s" % diffs)

        assert(len(diffs)==0)
        delete_result_is_dir()
