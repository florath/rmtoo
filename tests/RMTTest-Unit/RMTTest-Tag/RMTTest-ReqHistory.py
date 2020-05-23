'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqHistory

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


from rmtoo.inputs.ReqHistory import ReqHistory
from ReqTag import create_parameters


class RMTTestReqHistory(object):

    def rmttest_positive_01(self):
        "Requirement Tag History - no tag given"
        config, req = create_parameters()

        rt = ReqHistory(config)
        name, value = rt.rewrite("History-test", req)
        assert "History" == name
        assert value is None

    def rmttest_positive_02(self):
        "Requirement Tag History - History set"
        config, req = create_parameters()
        req = {"History": "something"}

        rt = ReqHistory(config)
        name, value = rt.rewrite("History-test", req)
        assert "History" == name
        assert "something" == value
