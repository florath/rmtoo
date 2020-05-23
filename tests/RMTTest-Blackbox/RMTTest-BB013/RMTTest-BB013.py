'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB013(BBHelper):

    test_dir = "tests/RMTTest-Blackbox/RMTTest-BB013"

    def rmttest_pos_001(self):
        "BB Basic with one requirement - graph output with defined tags"
        self.run_test()
