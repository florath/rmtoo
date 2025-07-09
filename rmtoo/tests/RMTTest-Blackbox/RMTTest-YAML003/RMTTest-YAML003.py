'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test - YAML format support

 Based on RMTTest-BB003 but using YAML files instead of .req/.tic files
 to demonstrate YAML input support.

 (c) 2025 by flonatel GmbH & Co. KG / Andreas Florath

 SPDX-License-Identifier: GPL-3.0-or-later

 For licensing details see COPYING
'''
from rmtoo.tests.lib.BBHelper import BBHelper


class RMTTestYAML003(BBHelper):

    test_dir = "tests/RMTTest-Blackbox/RMTTest-YAML003"

    def rmttest_pos_001(self):
        "BB YAML: Basic test with YAML requirement and topic files"
        self.run_test(relaxed=True)
