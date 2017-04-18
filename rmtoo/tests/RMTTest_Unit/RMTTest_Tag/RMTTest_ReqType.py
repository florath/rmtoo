'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqType

 (c) 2010-2012,2016 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.inputs.ReqType import ReqType
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry


class RMTTest_ReqType:

    def rmttest_positive_01(self):
        "Requirement Tag Type - tag given 'master requirement'"
        config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "master requirement")

        rt = ReqType(config)
        name, value = rt.rewrite("Type-test", req)
        assert(name == "Type")
        assert(value == Requirement.rt_master_requirement)

    def rmttest_positive_02(self):
        "Requirement Tag Type - tag given 'initial requirement'"
        config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "initial requirement")

        rt = ReqType(config)
        name, value = rt.rewrite("Type-test", req)
        assert(name == "Type")
        assert(value == Requirement.rt_initial_requirement)

    def rmttest_positive_03(self):
        "Requirement Tag Type - tag given 'design decision'"
        config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "design decision")

        rt = ReqType(config)
        name, value = rt.rewrite("Type-test", req)
        assert(name == "Type")
        assert(value == Requirement.rt_design_decision)

    def rmttest_positive_04(self):
        "Requirement Tag Type - tag given 'requirement'"
        config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "requirement")

        rt = ReqType(config)
        name, value = rt.rewrite("Type-test", req)
        assert(name == "Type")
        assert(value == Requirement.rt_requirement)

    def rmttest_negative_01(self):
        "Requirement Tag Type - no tag given"
        config, req = create_parameters()

        rt = ReqType(config)
        try:
            name, value = rt.rewrite("Type-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 18)

    def rmttest_negative_02(self):
        "Requirement Tag Type - invalid tag given"
        config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "dasjibtedjarnich")

        rt = ReqType(config)
        try:
            name, value = rt.rewrite("Type-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 19)
