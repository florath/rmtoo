'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for ReqName
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.inputs.ReqName import ReqName
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters

class RMTTest_ReqName:

    def rmttest_positive_01(self):
        "Requirement Tag Name - tag given"
        config, req = create_parameters()
        req["Name"] = "This is something"

        rt = ReqName(config)
        name, value = rt.rewrite("Name-test", req)
        assert(name == "Name")
        assert(value == "This is something")

    def rmttest_negative_01(self):
        "Requirement Tag Name - no Name set"
        config, req = create_parameters()

        rt = ReqName(config)
        try:
            name, value = rt.rewrite("Name-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 37)

