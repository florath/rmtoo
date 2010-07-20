#
# TopicHandler
#
#  This class coordinates the output handling for (possible many)
#  different topics.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.TopicSet import TopicSet

class TopicHandler:

    def __init__(self, config):
        self.config = config
        self.topics = {}
        self.setup_topics()

    def setup_topics(self):
        for k, v in self.config.topic_specs:
            self.topics[k] = TopicSet(k, v)

    def get(self, k):
        return self.topics[k]

