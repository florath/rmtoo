'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqPriority

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.inputs.ReqPriority import ReqPriority
from rmtoo.lib.RMTException import RMTException
from ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry


class RMTTestReqPriority(object):

    def rmttest_positive_01(self):
        "Requirement Tag Priority - no tag given"
        config, req = create_parameters()

        rt = ReqPriority(config)
        name, value = rt.rewrite("Priority-test", req)
        assert "Factor" == name
        assert 0.0 == value

    def rmttest_positive_02(self):
        "Requirement Tag Priority - tag given one stakeholder"
        config, req = create_parameters()
        config.set_value('requirements.stakeholders',
                         ["marketing", "security"])
        req["Priority"] = RecordEntry("Priority", "marketing:7")

        rt = ReqPriority(config)
        name, value = rt.rewrite("Priority-test", req)
        assert "Factor" == name
        assert 0.7 == value

    def rmttest_positive_03(self):
        "Requirement Tag Priority - tag given two stakeholders"
        config, req = create_parameters()
        config.set_value('requirements.stakeholders',
                         ["marketing", "security"])
        req["Priority"] = RecordEntry("Priority", "marketing:7 security:3")

        rt = ReqPriority(config)
        name, value = rt.rewrite("Priority-test", req)
        assert "Factor" == name
        assert 0.5 == value

    def rmttest_negative_01(self):
        "Requirement Tag Priority - faulty priority declaration ':'"
        config, req = create_parameters()
        config.set_value('requirements.stakeholders',
                         ["marketing", "security"])
        req["Priority"] = RecordEntry("Priority", "marketing:")

        rt = ReqPriority(config)
        try:
            name, value = rt.rewrite("Priority-test", req)
            assert False
        except RMTException as rmte:
            assert 12 == rmte.get_id()

    def rmttest_negative_02(self):
        "Requirement Tag Priority - invalid stakeholder"
        config, req = create_parameters()
        config.set_value('requirements.stakeholders',
                         ["marketing", "security"])
        req["Priority"] = RecordEntry("Priority", "nixda:3")

        rt = ReqPriority(config)
        try:
            name, value = rt.rewrite("Priority-test", req)
            assert False
        except RMTException as rmte:
            assert 13 == rmte.get_id()

    def rmttest_negative_03(self):
        "Requirement Tag Priority - stakeholder voted more than once"
        config, req = create_parameters()
        config.set_value('requirements.stakeholders',
                         ["marketing", "security"])
        req["Priority"] = RecordEntry("Priority",
                                      "security:3 marketing:7 security:4")

        rt = ReqPriority(config)
        try:
            name, value = rt.rewrite("Priority-test", req)
            assert False
        except RMTException as rmte:
            assert 14 == rmte.get_id()

    def rmttest_negative_04(self):
        "Requirement Tag Priority - invalid priority (too big)"
        config, req = create_parameters()
        config.set_value('requirements.stakeholders',
                         ["marketing", "security"])
        req["Priority"] = RecordEntry("Priority", "security:30")

        rt = ReqPriority(config)
        try:
            name, value = rt.rewrite("Priority-test", req)
            assert False
        except RMTException as rmte:
            assert 15 == rmte.get_id()

    def rmttest_negative_05(self):
        "Requirement Tag Priority - invalid priority (too small)"
        config, req = create_parameters()
        config.set_value('requirements.stakeholders',
                         ["marketing", "security"])
        req["Priority"] = RecordEntry("Priority", "security:-10")

        rt = ReqPriority(config)
        try:
            name, value = rt.rewrite("Priority-test", req)
            assert False
        except RMTException as rmte:
            assert 15 == rmte.get_id()
