#
# Requirement Management Toolset
#
#  Unit test for Topic
#
# (c) 2010 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Topic import Topic
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.TestConfig import TestConfig

class TestTopic:

    def test_neg_01(self):
        "Topic: (internal) check if Name tag exists"
        dg = Digraph()

        topic = Topic(None, None, dg, TestConfig())
        try:
            topic.extract_name()
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==62)

