'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for ReqHistory
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.inputs.ReqHistory import ReqHistory
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters

class RMTTest_ReqHistory:

    def rmttest_positive_01(self):
        "Requirement Tag History - no tag given"
        config, req = create_parameters()

        rt = ReqHistory(config)
        name, value = rt.rewrite("History-test", req)
        assert(name == "History")
        assert(value == None)

    def rmttest_positive_02(self):
        "Requirement Tag History - History set"
        config, req = create_parameters()
        req = {"History": "something"}

        rt = ReqHistory(config)
        name, value = rt.rewrite("History-test", req)
        assert(name == "History")
        assert(value == "something")

