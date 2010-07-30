#
# Requirement Management Toolset
#
# Unit test for ReqStatus
#
# (c) 2010 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqStatus import ReqStatus
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters

class TestReqStatus:

    def test_positive_01(self):
        "Requirement Tag Status - tag given 'not done'"
        opts, config, req = create_parameters()
        req["Status"] = "not done"

        rt = ReqStatus(opts, config)
        name, value = rt.rewrite("Status-test", req)
        assert(name=="Status")
        assert(value==Requirement.st_not_done)

    def test_positive_02(self):
        "Requirement Tag Status - tag given 'finished'"
        opts, config, req = create_parameters()
        req["Status"] = "finished"

        rt = ReqStatus(opts, config)
        name, value = rt.rewrite("Status-test", req)
        assert(name=="Status")
        assert(value==Requirement.st_finished)

    def test_negative_01(self):
        "Requirement Tag Status - no tag given"
        opts, config, req = create_parameters()

        rt = ReqStatus(opts, config)
        try:
            name, value = rt.rewrite("Status-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==16)

    def test_negative_02(self):
        "Requirement Tag Status - invalid tag given"
        opts, config, req = create_parameters()
        req["Status"] = "dasjibtedjarnich"

        rt = ReqStatus(opts, config)
        try:
            name, value = rt.rewrite("Status-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==17)

