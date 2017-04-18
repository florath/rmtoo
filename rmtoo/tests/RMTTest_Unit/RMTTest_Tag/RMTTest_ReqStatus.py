'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqStatus

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.inputs.ReqStatus import ReqStatus
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned, RequirementStatusFinished


class RMTTest_ReqStatus:

    def rmttest_positive_01(self):
        "Requirement Tag Status - tag given 'not done'"
        config, req = create_parameters()
        req["Status"] = RecordEntry("Status", "not done")

        rt = ReqStatus(config)
        name, value = rt.rewrite("Status-test", req)
        assert(name == "Status")
        assert(isinstance(value, RequirementStatusNotDone))

    def rmttest_positive_02(self):
        "Requirement Tag Status - tag given 'finished'"
        config, req = create_parameters()
        req["Status"] = RecordEntry("Status", "finished")

        rt = ReqStatus(config)
        name, value = rt.rewrite("Status-test", req)
        assert(name == "Status")
        assert(isinstance(value, RequirementStatusFinished))
        assert(value.get_person() == None)
        assert(value.get_duration() == None)

    def rmttest_negative_01(self):
        "Requirement Tag Status - no tag given"
        config, req = create_parameters()

        rt = ReqStatus(config)
        try:
            name, value = rt.rewrite("Status-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 16)

    def rmttest_negative_02(self):
        "Requirement Tag Status - invalid tag given"
        config, req = create_parameters()
        req["Status"] = RecordEntry("Status", "dasjibtedjarnich")

        rt = ReqStatus(config)
        try:
            name, value = rt.rewrite("Status-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 91)
