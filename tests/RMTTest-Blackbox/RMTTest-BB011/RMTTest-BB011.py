'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB011(BBHelper):

    test_dir = "tests/RMTTest-Blackbox/RMTTest-BB011"

    def rmttest_pos(self):
        "BB Basic where one requirement is not used because not in topic"
        self.run_test(success=False)
