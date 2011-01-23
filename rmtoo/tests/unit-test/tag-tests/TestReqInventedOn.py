#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Unit test for ReqInventedOn
#
# (c) 2010-2011 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqInventedOn import ReqInventedOn
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry

class TestReqInventedOn:

    def test_positive_01(self):
        "Requirement Tag Invented on - tag given"
        opts, config, req = create_parameters()
        req["Invented on"] = RecordEntry("Invented on", "2010-03-08")

        rt = ReqInventedOn(opts, config)
        name, value = rt.rewrite("InventedOn-test", req)
        assert(name=="Invented on")
        assert(value==(2010, 3, 8, 0, 0, 0, 0, 67, -1))

    def test_negative_01(self):
        "Requirement Tag Invented on - no tag given"
        opts, config, req = create_parameters()

        rt = ReqInventedOn(opts, config)
        try:
            name, value = rt.rewrite("InventedOn-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==7)

    def test_negative_02(self):
        "Requirement Tag Invented on - invalid tag given"
        opts, config, req = create_parameters()
        req["Invented on"] = RecordEntry("Invented on", "2010a-09-01")

        rt = ReqInventedOn(opts, config)
        try:
            name, value = rt.rewrite("InventedOn-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==8)

