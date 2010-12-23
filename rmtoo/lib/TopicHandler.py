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

    def __init__(self, config, reqs):
        self.config = config
        self.topics = {}
        self.setup_topics(reqs)

    def setup_topics(self, reqs):
        for k, v in self.config.topic_specs.iteritems():
            self.topics[k] = TopicSet(reqs, k, v, self.config)

    def get(self, k):
        return self.topics[k]

    # Write out all logs for all existing Topic Sets.
    def write_log(self, mstderr):
        for k, v in self.topics.iteritems():
            v.write_log(mstderr)
