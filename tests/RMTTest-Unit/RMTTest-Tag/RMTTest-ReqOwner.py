'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqOwner

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.inputs.ReqOwner import ReqOwner
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from ReqTag import create_parameters
import pytest


class RMTTestReqOwner(object):

    def rmttest_positive_01(self):
        "Requirement Tag Owner - tag given"
        config, req = create_parameters()
        config.set_value('requirements.stakeholders',
                         ["marketing", "security"])
        req["Owner"] = RecordEntry("Owner", "marketing")

        rt = ReqOwner(config)
        name, value = rt.rewrite("Owner-test", req)
        assert "Owner" == name
        assert "marketing" == value

    def rmttest_negative_01(self):
        "Requirement Tag Owner - no tag given"
        config, req = create_parameters()
        config.stakeholders = ["marketing", "security"]

        rt = ReqOwner(config)
        with pytest.raises(RMTException) as rmte:
            rt.rewrite("Owner-test", req)
            assert 10 == rmte.id()

    def rmttest_negative_02(self):
        "Requirement Tag Owner - invalid tag given"
        config, req = create_parameters()
        config.set_value('requirements.stakeholders',
                         ["marketing", "security"])
        req["Owner"] = RecordEntry("Owner", "SomethingDifferent")

        rt = ReqOwner(config)
        with pytest.raises(RMTException) as rmte:
            rt.rewrite("Owner-test", req)
            assert 11 == rmte.id()
