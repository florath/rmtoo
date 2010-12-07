#
# Requirement Management Toolset
#
#  Unit test for calling main
#
# (c) 2010 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.analytics.TopicCohe import TopicCohe

class TestTopicCohe:

    def test_pos_01(self):
        "TopicCohe: Check different ways of topic coherence"

        class LNTopic:

            def __init__(self, name):
                self.name = name

            def is_self_of_ancient(self, t):
                return False

        tcnt = {}

        TopicCohe.add_releation(tcnt, LNTopic("first"), LNTopic("second"))
        
        assert(tcnt=={'second': [0, 1], 'first': [0, 1]})
