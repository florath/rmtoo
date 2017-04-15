'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for ReqRationale
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.inputs.ReqRationale import ReqRationale
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry

class TestReqRationale:

    def test_positive_01(self):
        "Requirement Tag Rationale - no tag given"
        config, req = create_parameters()

        rt = ReqRationale(config)
        name, value = rt.rewrite("Rationale-test", req)
        assert(name == "Rationale")
        assert(value == None)

    def test_positive_02(self):
        "Requirement Tag Rationale - Rationale set"
        config, req = create_parameters()
        req = {"Rationale": RecordEntry("Rationale", "something")}

        rt = ReqRationale(config)
        name, value = rt.rewrite("Rationale-test", req)
        assert(name == "Rationale")
        assert(value.get_content() == "something")

