'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB003(BBHelper):

    test_dir = "tests/RMTTest-Blackbox/RMTTest-BB003"

    def rmttest_pos_001(self):
        "Pulp Fiction's Mr Wulf in English"
        self.run_test()
