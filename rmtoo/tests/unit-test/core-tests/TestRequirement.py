'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit Test cases for Requirement

 (c) 2010,2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.tests.lib.TestConfig import TestConfig

class TestRequirement:

    def test_positive_01(self):
        "Requirement: parser returns error"

        try:
            req = Requirement("DTag: content1\n"
                              "DTag: content2\n", 1, None,
                              MemLogStore(), None, TestConfig())
            assert(False)
        except RMTException, rmte:
            assert(rmte.get_id() == 81)
