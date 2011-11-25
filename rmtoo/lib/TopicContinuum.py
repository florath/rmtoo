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
from rmtoo.lib.vcs.Factory import Factory

class TopicContinuum:
    '''A TopicContinuum holds different (historic) versions
       of TopicSets.'''

    def __init__(self, ts_name, config, ts_config):
        tracer.info("called: name [%s]" % ts_name)
        self.config = config
        self.topic_sets = {}
        # This is the list of all version control system ids.
        # Those ids are sorted by time.
        # The oldest versions is the first one - sorted.
        # Note: this does not contain any other data, only the ids.
        # To access the data, use some construct like:
        #   self.topic_sets[self.vcs_ids[n]]
        self.vcs_ids = []
        self.internal_read_topic_sets(ts_config)

    def __read_commits(self, input_handler, commits):
        '''Creates a TopicSet for each commit with the help of
           the input_handler.'''
        tracer.debug("called")
        for commit in commits:
            input_handler.set_commit(commit)
            print("HOW TO HANDLE CACHEING?????? in the input_handler obj?")
            print(dir(commit))
            self.internal_continuum_add(
                    commit.hexsha,
                    TopicSet(self.config, input_handler))

    def internal_read_topic_sets(self, ts_config):
        '''Reads in all the topic sets from the specified sources.'''
        tracer.debug("called")
        for source in ts_config['sources']:
            input_handler = Factory.create(source[0], source[1])
            commits = input_handler.get_commits()
            self.__read_commits(input_handler, commits)
        assert False

    def internal_continuum_add(self, cid, topic_set_collection):
        '''Add one to the end of the continuum container.'''
        self.vcs_ids.append(cid)
        self.topic_sets[cid] = topic_set_collection

    ### EVERYTHING BENEATH IN DEPRECATED

    def deprecared_setup_topic_sets(self, reqs):
        for k in self.config.get_value('topics').get_dict().keys():
            self.topic_sets[k] = \
                TopicSet(reqs, self.config, k, 'topics.' + k)

    def deprecared_get(self, k):
        return self.topic_sets[k]

    def deprecared_get_topic_sets(self):
        return self.topic_sets

    # Write out all logs for all existing Topic Sets.
    def deprecared_write_log(self, mstderr):
        for k, v in self.topic_sets.iteritems():
            v.write_log(mstderr)

    def deprecared_output(self, rc):
        for k, v in self.topic_sets.iteritems():
            v.output(rc)

    def deprecared_create_makefile_dependencies(self, ofile, rc):
        for k, v in self.topic_sets.iteritems():
            v.cmad(rc, ofile)

    def deprecared_read_from_filesystem(self, req_input_dir):
        '''Read all the needed (and configured) TopicSets into memory.'''
        tracer.debug("called: req_input_dir [%s]" % req_input_dir)
        for k in self.config.get_value('topics').get_dict().keys():
            tracer.debug("create TopicSet [" + k + "]")
            self.topic_sets[k] = \
                TopicSet(self.config, k, 'topics.' + k, req_input_dir)
