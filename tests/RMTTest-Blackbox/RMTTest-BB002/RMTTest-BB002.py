'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB002(BBHelper):

    out_test_dir = "tests/RMTTest-Blackbox/RMTTest-BB002"
    in_test_dir = "tests/blackbox-test/bb002-test"

    def rmttest_pos_001(self):
        """BB Hotspot in the middle of the graph 2"""
        self.run_test(relaxed=True)

    def rmttest_pos_002(self):
        """BB Hotspot in the middle of the graph 2 (yaml)"""
        self.run_test(relaxed=True, yaml=True)
