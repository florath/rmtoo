'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqInventedBy

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.inputs.ReqInventedBy import ReqInventedBy
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry

class RMTTest_ReqInventedBy:

    def rmttest_positive_01(self):
        "Requirement Tag Invented by - tag given"
        config, req = create_parameters()
        config.set_value('requirements.inventors',
                         ["meinereiner", "keinerseiner"])
        req["Invented by"] = RecordEntry("Invented by", "meinereiner")

        rt = ReqInventedBy(config)
        name, value = rt.rewrite("InventedBy-test", req)
        assert(name == "Invented by")
        assert(value == "meinereiner")

    def rmttest_negative_01(self):
        "Requirement Tag Invented by - no tag given"
        config, req = create_parameters()
        config.inventors = ["meinereiner", "keinerseiner"]

        rt = ReqInventedBy(config)
        try:
            name, value = rt.rewrite("InventedBy-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 5)

    def rmttest_negative_02(self):
        "Requirement Tag Invented by - invalid tag given"
        config, req = create_parameters()
        config.set_value('requirements.inventors',
                         ["meinereiner", "keinerseiner"])
        req["Invented by"] = RecordEntry("Invented by", "MeinNameIstHase")

        rt = ReqInventedBy(config)
        try:
            name, value = rt.rewrite("InventedBy-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 6)
