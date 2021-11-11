'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqName

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


from rmtoo.inputs.ReqName import ReqName
from rmtoo.lib.RMTException import RMTException
from ReqTag import create_parameters
import pytest


class RMTTestReqName(object):

    def rmttest_positive_01(self):
        "Requirement Tag Name - tag given"
        config, req = create_parameters()
        req["Name"] = "This is something"

        rt = ReqName(config)
        name, value = rt.rewrite("Name-test", req)
        assert "Name" == name
        assert "This is something" == value

    def rmttest_negative_01(self):
        "Requirement Tag Name - no Name set"
        config, req = create_parameters()

        rt = ReqName(config)

        with pytest.raises(RMTException) as rmte:
            rt.rewrite("Name-test", req)
            assert 37 == rmte.id()
