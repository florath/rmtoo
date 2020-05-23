'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Topic tests

 (c) 2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.lib.TopicSet import TopicSet
from TestVCS import TestVCS
from TestInputModules import TestInputModules
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.vcs.ObjectCache import ObjectCache


class RMTTestParse(object):

    def rmttest_positive_01(self):
        "TopicSet - constructor with only one element"
        try:
            cfg = Cfg()
            cfg.set_value('ahah.directory',
                          'tests/unit-test/topic-tests/testdata/topicset01')
            cfg.set_value('ahah.name', 't01')
            cfg.set_value('topics.bkdkd.output', {})

            cfg.set_value('topic_root_node', 'RootNode')
            tvcs = TestVCS(cfg)
            tobjcache = ObjectCache()
            tinmod = TestInputModules()
            TopicSet(cfg, tvcs, "bkdkd", tobjcache, tinmod)
            assert False
        except AssertionError:
            pass

    def rmttest_positive_02(self):
        "TopicSet - valid"
        cfg = Cfg()
        cfg.set_value('hahaha.directory',
                      'tests/unit-test/topic-tests/testdata/topicset01')
        cfg.set_value('hahaha.name', 't01')
        cfg.set_value('topics.test-name01.output', {})
        cfg.set_value('topic_root_node', 'RootNode')
        tvcs = TestVCS(cfg)
        tobjcache = ObjectCache()
        tinmod = TestInputModules()
        TopicSet(
            cfg, tvcs, "test-name01", tobjcache, tinmod)

    def rmttest_positive_03(self):
        "TopicSet - valid with empty requirement set"

        cfg = Cfg()
        cfg.set_value('huhuhu.directory',
                      'tests/unit-test/topic-tests/testdata/topicset01')
        cfg.set_value('huhuhu.name', 't01')
        cfg.set_value('topics.test-name02.output', {})
        cfg.set_value('topic_root_node', 'RootNode')
        tvcs = TestVCS(cfg)
        tobjcache = ObjectCache()
        tinmod = TestInputModules()
        TopicSet(cfg, tvcs, "test-name02", tobjcache, tinmod)
