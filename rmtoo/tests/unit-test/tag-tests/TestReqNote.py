#
# Requirement Management Toolset
#
# Unit test for ReqNote
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqNote import ReqNote
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters

class TestReqNote:

    def test_positive_01(self):
        "Requirement Tag Note - no tag given"
        opts, config, req = create_parameters()

        rt = ReqNote(opts, config)
        name, value = rt.rewrite("Note-test", req)
        assert(name=="Note")
        assert(value==None)

    def test_positive_02(self):
        "Requirement Tag Note - Note set"
        opts, config, req = create_parameters()
        req = {"Note": "something"}

        rt = ReqNote(opts, config)
        name, value = rt.rewrite("Note-test", req)
        assert(name=="Note")
        assert(value=="something")

