'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for Topic

 (c) 2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.lib.Topic import Topic
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
from TestConfig import TestConfig
from TestVCS import TestVCS
import pytest


class RMTTestTopic(object):

    def rmttest_neg_01(self):
        "Topic: (internal) check if Name tag exists"
        dg = Digraph()

        tconfig = TestConfig()
        tconfig.set_value("topic_root_node", "/nothing/compare")
        tvcs = TestVCS(tconfig)
        tfileinfo = TestVCS.FileInfo(1)

        with pytest.raises(RMTException) as rmte:
            Topic(dg, tconfig, tvcs, None, tfileinfo, None)
            assert 62 == rmte.get_id()
