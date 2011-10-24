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
from rmtoo.lib.configuration.Cfg import Cfg

class TestParse:

    def test_positive_01(self):
        "TopicSet - constructor with only one element"
        try:
            tioconfig = TxtIOConfig()
            cfg = Cfg()
            cfg.set_value('ahah.directory',
                          'tests/unit-test/topic-tests/testdata/topicset01')
            cfg.set_value('ahah.name', 't01')
            cfg.set_value('topics.bkdkd.output', {})
            topicset = TopicSet(None, cfg, "bkdkd", "ahah")
            assert(False)
        except AssertionError, ae:
            pass

    def test_positive_02(self):
        "TopicSet - valid"
        cfg = Cfg()
        cfg.set_value('hahaha.directory',
                      'tests/unit-test/topic-tests/testdata/topicset01')
        cfg.set_value('hahaha.name', 't01')
        cfg.set_value('topics.test-name01.output', {})
        tioconfig = TxtIOConfig()
        topicset = TopicSet(
            None, cfg, "test-name01", "hahaha")
#            ["tests/unit-test/topic-tests/testdata/topicset01",
#             "t01"], tioconfig)

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
        cfg = Cfg()
        cfg.set_value('huhuhu.directory',
                      'tests/unit-test/topic-tests/testdata/topicset01')
        cfg.set_value('huhuhu.name', 't01')
        cfg.set_value('topics.test-name02.output', {})
        topicset = TopicSet(
            rs, cfg, "test-name02", "huhuhu")
#            ["tests/unit-test/topic-tests/testdata/topicset01",
#             "t01"], tioconfig)
