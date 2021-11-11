'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB012(BBHelper):

    test_dir = "tests/RMTTest-Blackbox/RMTTest-BB012"

    def rmttest_pos(self):
        "BB resulting requirements are not dependend"
        self.run_test(success=False)
