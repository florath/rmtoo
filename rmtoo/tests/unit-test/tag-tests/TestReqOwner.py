#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Unit test for ReqOwner
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqOwner import ReqOwner
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry

class TestReqOwner:

    def test_positive_01(self):
        "Requirement Tag Owner - tag given"
        config, req = create_parameters()
        config.set_value('requirements.stakeholders',
                         ["marketing", "security"])
        req["Owner"] = RecordEntry("Owner", "marketing")

        rt = ReqOwner(config)
        name, value = rt.rewrite("Owner-test", req)
        assert(name == "Owner")
        assert(value == "marketing")

    def test_negative_01(self):
        "Requirement Tag Owner - no tag given"
        config, req = create_parameters()
        config.stakeholders = ["marketing", "security"]

        rt = ReqOwner(config)
        try:
            name, value = rt.rewrite("Owner-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 10)

    def test_negative_02(self):
        "Requirement Tag Owner - invalid tag given"
        config, req = create_parameters()
        config.stakeholders = ["marketing", "security"]
        req["Owner"] = RecordEntry("Owner", "SomethingDifferent")

        rt = ReqOwner(config)
        try:
            name, value = rt.rewrite("Owner-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 11)

