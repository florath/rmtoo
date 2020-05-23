'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Blackbox test: Pulp Fiction in German.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB004(BBHelper):

    test_dir = "tests/RMTTest-Blackbox/RMTTest-BB004"

    def rmttest_PulpFictionInGermanOldConfig(self):
        "Pulp Fiction's Mr Wulf in German (new configuration)."
        self.run_test()
