#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

import os

from rmtoo.lib.main.NormalizeDependencies import main
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, compare_results, \
    cleanup_std_log, delete_result_is_dir, extract_container_files, tmp_dir

mdir = "tests/blackbox-test/bb015-test"

class TestBB015:

    def test_pos_01(self):
        "Normalization test"

        def myexit(n):
            pass

        mout, merr = prepare_result_is_dir()
        td = tmp_dir()

        print("TD %s" % td)

        # Copy requirements to tmp dir
        destdir = os.path.join(td, "reqs") 
        os.mkdir(destdir)
        os.system("cp %s/input/reqs/* %s" % (mdir, destdir))


#        main(["-f", mdir + "/input/Config1.py", "-m", ".."], mout, merr,
#             exitfun=myexit)
#        cleanup_std_log(mout, merr)
#        extract_container_files(["reqspricing.ods",])
#        missing_files, additional_files, diffs = compare_results(mdir)
#        assert(len(missing_files)==0)
#        assert(len(additional_files)==0)
#        assert(len(diffs)==0)

#        delete_result_is_dir()
