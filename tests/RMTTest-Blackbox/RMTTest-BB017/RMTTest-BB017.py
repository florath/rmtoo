'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox test for simple constraint handling

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB17(BBHelper):

    test_dir = "tests/RMTTest-Blackbox/RMTTest-BB017"

    def rmttest_pos_001(self):
        "Blackbox test for simple constraint handling"
        self.run_test()
