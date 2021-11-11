'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqDescription

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.inputs.ReqDescription import ReqDescription
from rmtoo.lib.RMTException import RMTException
from ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
import pytest


class RMTTestReqClass(object):

    def rmttest_positive_01(self):
        "Requirement Tag Description - one word Description"
        config, req = create_parameters()
        req = {"Description": RecordEntry("Description", "short")}

        rt = ReqDescription(config)
        name, value = rt.rewrite("Description-test", req)
        assert "Description" == name
        assert "short" == value.get_content()

    def rmttest_positive_02(self):
        "Requirement Tag Description - some words Description"
        config, req = create_parameters()
        d = "This are some words description."
        req = {"Description": RecordEntry("Description", d)}

        rt = ReqDescription(config)
        name, value = rt.rewrite("Description-test", req)
        assert "Description" == name
        assert d == value.get_content()

    def rmttest_positive_03(self):
        "Requirement Tag Description - 500 chars description"
        config, req = create_parameters()
        long_text = ""
        for c in range(0, 500):
            long_text += "A"
        req = {"Description": RecordEntry("Description", long_text)}

        rt = ReqDescription(config)
        name, value = rt.rewrite("Description-test", req)
        assert "Description" == name
        assert long_text == value.get_content()

    def rmttest_negative_01(self):
        "Requirement Tag Description - empty reqs"
        config, req = create_parameters()

        rt = ReqDescription(config)
        with pytest.raises(RMTException) as rmte:
            rt.rewrite("Description-test", req)
            assert 2 == rmte.id()

    def rmttest_negative_02(self):
        "Requirement Tag Description - description much too long"
        config, req = create_parameters()
        long_text = ""
        for c in range(0, 1500):
            long_text += "A"
        req = {"Description": RecordEntry("Description", long_text)}

        rt = ReqDescription(config)
        with pytest.raises(RMTException) as rmte:
            rt.rewrite("Description-test", req)
            assert 3 == rmte.id()
