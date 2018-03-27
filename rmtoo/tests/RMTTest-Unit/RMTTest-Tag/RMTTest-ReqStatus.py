'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqStatus

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.inputs.ReqStatus import ReqStatus
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusFinished

import pytest


class RMTTestReqStatus(object):

    def rmttest_positive_01(self):
        "Requirement Tag Status - tag given 'not done'"
        config, req = create_parameters()
        req["Status"] = RecordEntry("Status", "not done")

        rt = ReqStatus(config)
        name, value = rt.rewrite("Status-test", req)
        assert "Status" == name
        assert isinstance(value, RequirementStatusNotDone)

    def rmttest_positive_02(self):
        "Requirement Tag Status - tag given 'finished'"
        config, req = create_parameters()
        req["Status"] = RecordEntry("Status", "finished")

        rt = ReqStatus(config)
        name, value = rt.rewrite("Status-test", req)
        assert "Status" == name
        assert isinstance(value, RequirementStatusFinished)
        assert value.get_person() is None
        assert value.get_duration() is None

    def rmttest_negative_01(self):
        "Requirement Tag Status - no tag given"
        config, req = create_parameters()

        rt = ReqStatus(config)
        with pytest.raises(RMTException) as rmte:
            rt.rewrite("Status-test", req)
            assert 16 == rmte.get_id()

    def rmttest_negative_02(self):
        "Requirement Tag Status - invalid tag given"
        config, req = create_parameters()
        req["Status"] = RecordEntry("Status", "dasjibtedjarnich")

        rt = ReqStatus(config)
        with pytest.raises(RMTException) as rmte:
            rt.rewrite("Status-test", req)
            assert 91 == rmte.get_id()
