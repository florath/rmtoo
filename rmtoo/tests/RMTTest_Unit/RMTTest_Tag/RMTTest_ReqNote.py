'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for ReqNote
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.inputs.ReqNote import ReqNote
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters

class RMTTest_ReqNote:

    def rmttest_positive_01(self):
        "Requirement Tag Note - no tag given"
        config, req = create_parameters()

        rt = ReqNote(config)
        name, value = rt.rewrite("Note-test", req)
        assert(name == "Note")
        assert(value == None)

    def rmttest_positive_02(self):
        "Requirement Tag Note - Note set"
        config, req = create_parameters()
        req = {"Note": "something"}

        rt = ReqNote(config)
        name, value = rt.rewrite("Note-test", req)
        assert(name == "Note")
        assert(value == "something")

