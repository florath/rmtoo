'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for topic coherence

 (c) 2010,2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import unittest

from rmtoo.lib.analytics.TopicCohe import TopicCohe
from rmtoo.tests.lib.TestConfig import TestConfig


class RMTTestTopicCohe(unittest.TestCase):

    def rmttest_pos_01(self):
        "TopicCohe: Check different ways of topic coherence"

        class LNTopic:

            def __init__(self, name):
                self.name = name

            def is_self_of_ancient(self, t):
                return False

        cfg = TestConfig()
        topic_cohe = TopicCohe(cfg)
        topic_cohe._add_topic_relation(LNTopic("first"), LNTopic("second"))

        self.assertEqual(
            {'second': [0, 1], 'first': [0, 1]}, topic_cohe._get_tcnt())
