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
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig

class TestParse:

    def test_positive_01(self):
        "TopicSet - constructor with only one element"
        try:
            tioconfig = TxtIOConfig()
            topicset = TopicSet(None, "bkdkd", ["ahah"], tioconfig);
#                                TestConfig().txtio["topics"])
            assert(False)
        except AssertionError, ae:
            pass

    def test_positive_02(self):
        "TopicSet - valid"
        tioconfig = TxtIOConfig()
        topicset = TopicSet(
            None, "test-name01",
            ["tests/unit-test/topic-tests/testdata/topicset01",
             "t01"], tioconfig)

    def test_positive_03(self):
        "TopicSet - valid with empty requirement set"

        class ReqSet(Digraph):

            def __init__(self):
                self.mods = None
                self.opts = None
                self.config = None
                self.reqs = {}

        rs = ReqSet()

        tioconfig = TxtIOConfig()
        topicset = TopicSet(
            rs, "test-name02",
            ["tests/unit-test/topic-tests/testdata/topicset01",
             "t01"], tioconfig)
