'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqTopic

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.inputs.ReqTopic import ReqTopic
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry


class RMTTest_ReqTopic:

    def rmttest_positive_01(self):
        "Requirement Tag Topic - tag given"
        config, req = create_parameters()
        req["Topic"] = RecordEntry("Topic", "This is something")

        rt = ReqTopic(config)
        name, value = rt.rewrite("Topic-test", req)
        assert(name == "Topic")
        assert(value == "This is something")

    def rmttest_negative_01(self):
        "Requirement Tag Topic - no Topic set"
        config, req = create_parameters()

        rt = ReqTopic(config)
        try:
            name, value = rt.rewrite("Topic-test", req)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 9)
