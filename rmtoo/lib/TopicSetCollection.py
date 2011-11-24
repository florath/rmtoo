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

from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.TopicSet import TopicSet

class TopicSetCollection:
    '''A TopicSetCollection holds different (historic) versions
       of TopicSets.'''

    def __init__(self, ts_name, config, ts_config):
        tracer.info("called: name [%s]" % ts_name)
        self.config = config
        self.topic_sets = {}
        # This is the list of all version control system ids.
        # Those ids are sorted by time.
        # The newest versions is the first one - sorted backwards.
        # Note: this does not contain any other data, only the ids.
        # To access the data, use some construct like:
        #   self.continuum[self.vcs_ids[0]]
        self.vcs_ids = []
        ### TODO: Check it out
        assert False
        ### self.setup_topic_sets(reqs)

    def internal_continuum_add(self, cid, topic_set_collection):
        '''Add one to the end of the continuum container.'''
        self.vcs_ids.append(cid)
        self.continuum[cid] = topic_set_collection


    def setup_topic_sets(self, reqs):
        for k in self.config.get_value('topics').get_dict().keys():
            self.topic_sets[k] = \
                TopicSet(reqs, self.config, k, 'topics.' + k)

    def get(self, k):
        return self.topic_sets[k]

    def get_topic_sets(self):
        return self.topic_sets

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

    def read_from_filesystem(self, req_input_dir):
        '''Read all the needed (and configured) TopicSets into memory.'''
        tracer.debug("called: req_input_dir [%s]" % req_input_dir)
        for k in self.config.get_value('topics').get_dict().keys():
            tracer.debug("create TopicSet [" + k + "]")
            self.topic_sets[k] = \
                TopicSet(self.config, k, 'topics.' + k, req_input_dir)
