'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB007(BBHelper):

    out_test_dir = "tests/RMTTest-Blackbox/RMTTest-BB007"
    in_test_dir = "tests/blackbox-test/bb007-test"

    def rmttest_pos_001(self):
        "BB Basic with one requirement - check log output for typo in topic"
        self.run_test(success=False)
