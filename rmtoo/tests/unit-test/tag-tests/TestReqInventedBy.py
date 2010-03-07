#
# Requirement Management Toolset
#
# Unit test for ReqInventedBy
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqInventedBy import ReqInventedBy
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters

class TestReqInventedBy:

    def test_positive_01(self):
        "Requirement Tag Invented by - tag given"
        opts, config, req = create_parameters()
        config.inventors = ["meinereiner", "keinerseiner"]
        req["Invented by"] = "meinereiner"

        rt = ReqInventedBy(opts, config)
        name, value = rt.rewrite("InventedBy-test", req)
        assert(name=="Invented by")
        assert(value=="meinereiner")

    def test_negative_01(self):
        "Requirement Tag Invented by - no tag given"
        opts, config, req = create_parameters()
        config.inventors = ["meinereiner", "keinerseiner"]

        rt = ReqInventedBy(opts, config)
        try:
            name, value = rt.rewrite("InventedBy-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.eid==5)

    def test_negative_02(self):
        "Requirement Tag Invented by - invalid tag given"
        opts, config, req = create_parameters()
        config.inventors = ["meinereiner", "keinerseiner"]
        req["Invented by"] = "MeinNameIstHase"

        rt = ReqInventedBy(opts, config)
        try:
            name, value = rt.rewrite("InventedBy-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.eid==6)

