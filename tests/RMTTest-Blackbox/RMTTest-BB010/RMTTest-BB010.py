'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB010(BBHelper):

    test_dir = "tests/RMTTest-Blackbox/RMTTest-BB010"

    def rmttest_pos_001(self):
        "BB Basic with some requirements - used for the slides"
        self.run_test(container_files=["reqspricing.ods", ], relaxed=True)

    def rmttest_pos_002(self):
        "BB Basic with some requirements - used for the slides (yaml)"
        self.run_test(container_files=["reqspricing.ods", ],
                      relaxed=True, yaml=True)
