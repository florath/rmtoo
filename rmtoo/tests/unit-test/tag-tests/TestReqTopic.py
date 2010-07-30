#
# Requirement Management Toolset
#
#  Unit test for ReqTopic
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqTopic import ReqTopic
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters

class TestReqTopic:

    def test_positive_01(self):
        "Requirement Tag Topic - tag given"
        opts, config, req = create_parameters()
        req["Topic"] = "This is something"

        rt = ReqTopic(opts, config)
        name, value = rt.rewrite("Topic-test", req)
        assert(name=="Topic")
        assert(value=="This is something")

    def test_negative_01(self):
        "Requirement Tag Topic - no Topic set"
        opts, config, req = create_parameters()

        rt = ReqTopic(opts, config)
        try:
            name, value = rt.rewrite("Topic-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==9)
