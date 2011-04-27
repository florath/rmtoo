#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Unit test for ReqStatus
#
# (c) 2010-2011 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqStatus import ReqStatus
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned, RequirementStatusFinished

class TestReqStatus:

    def test_positive_01(self):
        "Requirement Tag Status - tag given 'not done'"
        opts, config, req = create_parameters()
        req["Status"] = RecordEntry("Status", "not done")

        rt = ReqStatus(opts, config)
        name, value = rt.rewrite("Status-test", req)
        assert(name=="Status")
        assert(isinstance(value, RequirementStatusNotDone))

    def test_positive_02(self):
        "Requirement Tag Status - tag given 'finished'"
        opts, config, req = create_parameters()
        req["Status"] = RecordEntry("Status", "finished")

        rt = ReqStatus(opts, config)
        name, value = rt.rewrite("Status-test", req)
        assert(name=="Status")
        assert(isinstance(value, RequirementStatusFinished))
        assert(value.get_person()==None)
        assert(value.get_duration()==None)

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
        req["Status"] = RecordEntry("Status", "dasjibtedjarnich")

        rt = ReqStatus(opts, config)
        try:
            name, value = rt.rewrite("Status-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==91)

