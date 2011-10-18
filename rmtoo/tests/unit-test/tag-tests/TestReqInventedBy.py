#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Unit test for ReqInventedBy
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqInventedBy import ReqInventedBy
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry

class TestReqInventedBy:

    def test_positive_01(self):
        "Requirement Tag Invented by - tag given"
        config, req = create_parameters()
        config.set_value('requirements.inventors',
                         ["meinereiner", "keinerseiner"])
        req["Invented by"] = RecordEntry("Invented by", "meinereiner")

        rt = ReqInventedBy(config)
        name, value = rt.rewrite("InventedBy-test", req)
        assert(name == "Invented by")
        assert(value == "meinereiner")

    def test_negative_01(self):
        "Requirement Tag Invented by - no tag given"
        config, req = create_parameters()
        config.inventors = ["meinereiner", "keinerseiner"]

        rt = ReqInventedBy(config)
        try:
            name, value = rt.rewrite("InventedBy-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 5)

    def test_negative_02(self):
        "Requirement Tag Invented by - invalid tag given"
        config, req = create_parameters()
        config.inventors = ["meinereiner", "keinerseiner"]
        req["Invented by"] = RecordEntry("Invented by", "MeinNameIstHase")

        rt = ReqInventedBy(config)
        try:
            name, value = rt.rewrite("InventedBy-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 6)

