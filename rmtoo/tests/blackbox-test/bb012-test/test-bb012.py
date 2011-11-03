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
    unify_output_dir, check_file_results

mdir = "tests/blackbox-test/bb012-test"

class TestBB012:

    def test_pos(self):
        "BB resulting requirements are not dependend"

        mout, merr = prepare_result_is_dir()
        result = main_impl(["-f", mdir + "/input/Config1.py", "-m", ".."],
                           mout, merr)
        cleanup_std_log(mout, merr)
        check_file_results(mdir)
        delete_result_is_dir()
