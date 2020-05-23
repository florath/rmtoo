'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqType

 (c) 2010-2012,2016 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.inputs.ReqType import ReqType
from rmtoo.lib.Requirement import RequirementType
from rmtoo.lib.RMTException import RMTException
from ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
import pytest


class RMTTestReqType(object):

    def rmttest_positive_01(self):
        "Requirement Tag Type - tag given 'master requirement'"
        config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "master requirement")

        rt = ReqType(config)
        name, value = rt.rewrite("Type-test", req)
        assert "Type" == name
        assert RequirementType.master_requirement == value

    def rmttest_positive_02(self):
        "Requirement Tag Type - tag given 'initial requirement'"
        config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "initial requirement")

        rt = ReqType(config)
        name, value = rt.rewrite("Type-test", req)
        assert "Type" == name
        assert RequirementType.initial_requirement == value

    def rmttest_positive_03(self):
        "Requirement Tag Type - tag given 'design decision'"
        config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "design decision")

        rt = ReqType(config)
        name, value = rt.rewrite("Type-test", req)
        assert "Type" == name
        assert RequirementType.design_decision == value

    def rmttest_positive_04(self):
        "Requirement Tag Type - tag given 'requirement'"
        config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "requirement")

        rt = ReqType(config)
        name, value = rt.rewrite("Type-test", req)
        assert "Type" == name
        assert RequirementType.requirement == value

    def rmttest_negative_01(self):
        "Requirement Tag Type - no tag given"
        config, req = create_parameters()

        rt = ReqType(config)
        with pytest.raises(RMTException) as rmte:
            rt.rewrite("Type-test", req)
            assert 18 == rmte.id()

    def rmttest_negative_02(self):
        "Requirement Tag Type - invalid tag given"
        config, req = create_parameters()
        req["Type"] = RecordEntry("Type", "dasjibtedjarnich")

        rt = ReqType(config)
        with pytest.raises(RMTException) as rmte:
            rt.rewrite("Type-test", req)
            assert 19 == rmte.id()
