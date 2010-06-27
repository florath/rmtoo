#
# Requirement Management Toolset
#
#  Topic tests
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.TopicSet import TopicSet
from rmtoo.lib.digraph.Digraph import Digraph

class TestParse:

    def test_positive_01(self):
        "TopicSet - constructor with only one element"
        try:
            topicset = TopicSet("bkdkd")
            assert(False)
        except AssertionError, ae:
            pass

    def test_positive_02(self):
        "TopicSet - valid"
        topicset = TopicSet(
            ["tests/unit-test/topic-tests/testdata/topicset01",
             "t01"])

    def test_positive_03(self):
        "TopicSet - valid with empty requirement set"
        topicset = TopicSet(
            ["tests/unit-test/topic-tests/testdata/topicset01",
             "t01"])

        class ReqSet(Digraph):
            pass

        rs = ReqSet()
        topicset.depict(rs)

