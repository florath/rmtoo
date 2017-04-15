'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Blackbox test for rmtoo.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, compare_results, \
    cleanup_std_log, delete_result_is_dir

mdir = "tests/RMTTest_Blackbox/RMTTest_BB005"


class RMTTest_BB001:

    def rmttest_pos_002(self):
        "BB Basic with one requirement - reqs only from FILES"

        def myexit(n):
            pass

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        main(["-j", "file://" + mdir + "/input/Config.json"], mout, merr,
             exitfun=myexit)
        cleanup_std_log(mout, merr)
        #        extract_container_files(["reqspricing.ods", ])
        missing_files, additional_files, diffs = compare_results(mdir)
        assert(len(missing_files) == 0)
        if len(additional_files) != 0:
            print("ADDITIONAL FILES [%s]" % additional_files)
        assert(len(additional_files) == 0)
        # The count stats is always different because of the timestamp

        if len(diffs) != 1:
            print("DIFFS '%s'" % diffs)

        assert(len(diffs) == 1)
        # Diffs are the from the stats count file:
        # ['---  \n',
        #  '+++  \n',
        #  '@@ -1,1 +1,5 @@\n',
        #  '-2010-07-31_06:11:27 1\n', -- or similar
        #  '+2010-07-30_21:04:35 1\n',
        #  '+2010-07-30_21:03:22 1\n',
        #  '+2010-07-30_20:57:36 1\n',
        #  '+2010-07-29_21:17:15 1\n',
        #  '+2010-07-29_21:09:03 1\n']
        assert(len(diffs["stats_reqs_cnt.csv"]) == 9)
        delete_result_is_dir()
