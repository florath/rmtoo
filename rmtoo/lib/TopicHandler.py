'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Collection of collection of topics.
  In each run of rmtoo it is possible to have many different
  TopicSets handled.
  This object handles the collection of TopicSets. 
   
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.TopicSet import TopicSet

class TopicSetCollection:

    def __init__(self, config, reqs):
        self.config = config
        self.topic_sets = {}
        self.setup_topic_sets(reqs)

    def setup_topic_sets(self, reqs):
        for k in self.config.get_value('topics').get_dict().keys():
            self.topic_sets[k] = \
                TopicSet(reqs, self.config, k, 'topics.' + k)

    def get(self, k):
        return self.topic_sets[k]

    # Write out all logs for all existing Topic Sets.
    def write_log(self, mstderr):
        for k, v in self.topic_sets.iteritems():
            v.write_log(mstderr)

    def output(self, rc):
        for k, v in self.topic_sets.iteritems():
            v.output(rc)

    def create_makefile_dependencies(self, ofile, rc):
        for k, v in self.topic_sets.iteritems():
            v.cmad(rc, ofile)
