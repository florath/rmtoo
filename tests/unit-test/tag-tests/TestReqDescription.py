#
# Requirement Management Toolset
#
# Unit test for ReqDescription
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqDescription import ReqDescription
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException

class TestReqClass:

    def test_positive_01(self):
        "Requirement Tag Description - one word Description"
        opts = {}
        config = {}
        req = {"Description": "short"}

        rt = ReqDescription(opts, config)
        name, value = rt.rewrite("Description-test", req)
        assert(name=="Description")
        assert(value=="short")

    def test_positive_02(self):
        "Requirement Tag Description - some words Description"
        opts = {}
        config = {}
        d = "This are some words description."
        req = {"Description": d}

        rt = ReqDescription(opts, config)
        name, value = rt.rewrite("Description-test", req)
        assert(name=="Description")
        assert(value==d)

    def test_positive_03(self):
        "Requirement Tag Description - 500 chars description"
        opts = {}
        config = {}
        long_text = ""
        for c in xrange(0, 500):
            long_text += "A"
        req = {"Description": long_text}

        rt = ReqDescription(opts, config)
        name, value = rt.rewrite("Description-test", req)
        assert(name=="Description")
        assert(value==long_text)

    def test_negative_01(self):
        "Requirement Tag Description - empty reqs"
        opts = {}
        config = {}
        req = {}

        rt = ReqDescription(opts, config)
        try:
            name, value = rt.rewrite("Description-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.eid==2)

    def test_negative_02(self):
        "Requirement Tag Description - description much too long"
        opts = {}
        config = {}
        long_text = ""
        for c in xrange(0, 1500):
            long_text += "A"
        req = {"Description": long_text}

        rt = ReqDescription(opts, config)
        try:
            name, value = rt.rewrite("Description-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.eid==3)

