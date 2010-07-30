#
# Requirement Management Toolset
#
# Unit test for ReqPriority
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqPriority import ReqPriority
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters

class TestReqPriority:

    def test_positive_01(self):
        "Requirement Tag Priority - no tag given"
        opts, config, req = create_parameters()

        rt = ReqPriority(opts, config)
        name, value = rt.rewrite("Priority-test", req)
        assert(name=="Factor")
        assert(value==0.0)

    def test_positive_02(self):
        "Requirement Tag Priority - tag given one stakeholder"
        opts, config, req = create_parameters()
        config.stakeholders = ["marketing", "security"]
        req["Priority"] = "marketing:7"

        rt = ReqPriority(opts, config)
        name, value = rt.rewrite("Priority-test", req)
        assert(name=="Factor")
        assert(value==0.7)

    def test_positive_03(self):
        "Requirement Tag Priority - tag given two stakeholders"
        opts, config, req = create_parameters()
        config.stakeholders = ["marketing", "security"]
        req["Priority"] = "marketing:7 security:3"

        rt = ReqPriority(opts, config)
        name, value = rt.rewrite("Priority-test", req)
        assert(name=="Factor")
        assert(value==0.5)

    def test_negative_01(self):
        "Requirement Tag Priority - faulty priority declaration ':'"
        opts, config, req = create_parameters()
        config.stakeholders = ["marketing", "security"]
        req["Priority"] = "marketing:"

        rt = ReqPriority(opts, config)
        try:
            name, value = rt.rewrite("Priority-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==12)

    def test_negative_02(self):
        "Requirement Tag Priority - invalid stakeholder"
        opts, config, req = create_parameters()
        config.stakeholders = ["marketing", "security"]
        req["Priority"] = "nixda:3"

        rt = ReqPriority(opts, config)
        try:
            name, value = rt.rewrite("Priority-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==13)

    def test_negative_03(self):
        "Requirement Tag Priority - stakeholder voted more than once"
        opts, config, req = create_parameters()
        config.stakeholders = ["marketing", "security"]
        req["Priority"] = "security:3 marketing:7 security:4"

        rt = ReqPriority(opts, config)
        try:
            name, value = rt.rewrite("Priority-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==14)

    def test_negative_04(self):
        "Requirement Tag Priority - invalid priority (too big)"
        opts, config, req = create_parameters()
        config.stakeholders = ["marketing", "security"]
        req["Priority"] = "security:30"

        rt = ReqPriority(opts, config)
        try:
            name, value = rt.rewrite("Priority-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==15)

    def test_negative_05(self):
        "Requirement Tag Priority - invalid priority (too small)"
        opts, config, req = create_parameters()
        config.stakeholders = ["marketing", "security"]
        req["Priority"] = "security:-10"

        rt = ReqPriority(opts, config)
        try:
            name, value = rt.rewrite("Priority-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==15)
