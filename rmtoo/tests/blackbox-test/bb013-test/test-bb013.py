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
    unify_output_dir, check_result

mdir = "tests/blackbox-test/bb013-test"

class TestBB007:

    def test_pos_001(self):
        "BB Basic with one requirement - graph output with defined tags"

        mout, merr = prepare_result_is_dir()
        result = main_impl(["-f", mdir + "/input/Config1.py", "-m", ".."],
                           mout, merr)
        cleanup_std_log(mout, merr)
        missing_files, additional_files, diffs = compare_results(mdir)
        check_result(result, missing_files, additional_files, diffs)
        delete_result_is_dir()
