'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqDescription

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.inputs.ReqDescription import ReqDescription
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry


class RMTTest_ReqClass:

    def rmttest_positive_01(self):
        "Requirement Tag Description - one word Description"
        config, req = create_parameters()
        req = {"Description": RecordEntry("Description", "short")}

        rt = ReqDescription(config)
        name, value = rt.rewrite("Description-test", req)
        assert(name == "Description")
        assert(value.get_content() == "short")

    def rmttest_positive_02(self):
        "Requirement Tag Description - some words Description"
        config, req = create_parameters()
        d = "This are some words description."
        req = {"Description": RecordEntry("Description", d)}

        rt = ReqDescription(config)
        name, value = rt.rewrite("Description-test", req)
        assert(name == "Description")
        assert(value.get_content() == d)

    def rmttest_positive_03(self):
        "Requirement Tag Description - 500 chars description"
        config, req = create_parameters()
        long_text = ""
        for c in range(0, 500):
            long_text += "A"
        req = {"Description": RecordEntry("Description", long_text)}

        rt = ReqDescription(config)
        name, value = rt.rewrite("Description-test", req)
        assert(name == "Description")
        assert(value.get_content() == long_text)

    def rmttest_negative_01(self):
        "Requirement Tag Description - empty reqs"
        config, req = create_parameters()

        rt = ReqDescription(config)
        try:
            name, value = rt.rewrite("Description-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 2)

    def rmttest_negative_02(self):
        "Requirement Tag Description - description much too long"
        config, req = create_parameters()
        long_text = ""
        for c in range(0, 1500):
            long_text += "A"
        req = {"Description": RecordEntry("Description", long_text)}

        rt = ReqDescription(config)
        try:
            name, value = rt.rewrite("Description-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 3)
