'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB014(BBHelper):

    test_dir = "tests/RMTTest-Blackbox/RMTTest-BB014"

    def rmttest_pos_001(self):
        "Pulp Fiction's Mr Wulf in English with Solved by"
        self.run_test(relaxed=True)
