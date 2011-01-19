#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Unit test for ReqType
#
# (c) 2010-2011 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqType import ReqType
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry

class TestReqType:

    def test_positive_01(self):
        "Requirement Tag Type - tag given 'master requirement'"
        opts, config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "master requirement")

        rt = ReqType(opts, config)
        name, value = rt.rewrite("Type-test", req)
        assert(name=="Type")
        assert(value==Requirement.rt_master_requirement)

    def test_positive_02(self):
        "Requirement Tag Type - tag given 'initial requirement'"
        opts, config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "initial requirement")

        rt = ReqType(opts, config)
        name, value = rt.rewrite("Type-test", req)
        assert(name=="Type")
        assert(value==Requirement.rt_initial_requirement)

    def test_positive_03(self):
        "Requirement Tag Type - tag given 'design decision'"
        opts, config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "design decision")

        rt = ReqType(opts, config)
        name, value = rt.rewrite("Type-test", req)
        assert(name=="Type")
        assert(value==Requirement.rt_design_decision)

    def test_positive_04(self):
        "Requirement Tag Type - tag given 'requirement'"
        opts, config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "requirement")

        rt = ReqType(opts, config)
        name, value = rt.rewrite("Type-test", req)
        assert(name=="Type")
        assert(value==Requirement.rt_requirement)

    def test_negative_01(self):
        "Requirement Tag Type - no tag given"
        opts, config, req = create_parameters()

        rt = ReqType(opts, config)
        try:
            name, value = rt.rewrite("Type-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==18)

    def test_negative_02(self):
        "Requirement Tag Type - invalid tag given"
        opts, config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "dasjibtedjarnich")

        rt = ReqType(opts, config)
        try:
            name, value = rt.rewrite("Type-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==19)

