#
# Requirement Management Toolset
#
# Unit test for ReqName
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqName import ReqName
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters

class TestReqName:

    def test_positive_01(self):
        "Requirement Tag Name - tag given"
        opts, config, req = create_parameters()
        req["Name"] = "This is something"

        rt = ReqName(opts, config)
        name, value = rt.rewrite("Name-test", req)
        assert(name=="Name")
        assert(value=="This is something")

    def test_negative_01(self):
        "Requirement Tag Name - no Name set"
        opts, config, req = create_parameters()

        rt = ReqName(opts, config)
        try:
            name, value = rt.rewrite("Name-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.eid==9)

