'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqInventedOn

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import datetime
from rmtoo.inputs.ReqInventedOn import ReqInventedOn
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry


class RMTTest_ReqInventedOn:

    def rmttest_positive_01(self):
        "Requirement Tag Invented on - tag given"
        config, req = create_parameters()
        req["Invented on"] = RecordEntry("Invented on", "2010-03-08")

        rt = ReqInventedOn(config)
        name, value = rt.rewrite("InventedOn-test", req)
        assert(name == "Invented on")
        assert(value == datetime.date(2010, 3, 8))

    def rmttest_negative_01(self):
        "Requirement Tag Invented on - no tag given"
        config, req = create_parameters()

        rt = ReqInventedOn(config)
        try:
            name, value = rt.rewrite("InventedOn-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 7)

    def rmttest_negative_02(self):
        "Requirement Tag Invented on - invalid tag given"
        config, req = create_parameters()
        req["Invented on"] = RecordEntry("Invented on", "2010a-09-01")

        rt = ReqInventedOn(config)
        try:
            name, value = rt.rewrite("InventedOn-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 8)
