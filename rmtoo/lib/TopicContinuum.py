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
from rmtoo.lib.vcs.ObjectCache import ObjectCache

class TopicContinuum:
    '''A TopicContinuum holds different (historic) versions
       of TopicSets.'''

    def __init__(self, ts_name, config, ts_config, object_cache, input_mods):
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
        self.__object_cache = object_cache
        self.__input_mods = input_mods
        self.__read_topic_sets(ts_config)

    def __read_commits(self, input_handler, commits):
        '''Creates a TopicSet for each commit with the help of
           the input_handler.'''
        tracer.debug("called")
        for commit in commits:
            topic_set_vcs_id = \
                input_handler.get_vcs_id_with_type(commit, "topics")
            tracer.debug("read topics with oid [%s]" % topic_set_vcs_id)
            topic_set = self.__object_cache.get("TopicSet", topic_set_vcs_id)

            if topic_set == None:
                tracer.debug("TopicSet with ID [%s] not in cache"
                             % topic_set_vcs_id)
                topic_set = TopicSet(self.config, input_handler, commit,
                                     self.__object_cache, self.__input_mods)
                self.__object_cache.add(topic_set_vcs_id,
                                        "TopicSet", topic_set)
            self.__continuum_add(topic_set_vcs_id, topic_set)
        # TODO: Long term: maybe remove this.
        self.__object_cache.log_stats()

    def __read_topic_sets(self, ts_config):
        '''Reads in all the topic sets from the specified sources.'''
        tracer.debug("called")
        for source in ts_config['sources']:
            input_handler = Factory.create(source[0], source[1])
            commits = input_handler.get_commits()
            self.__read_commits(input_handler, commits)
        assert False

    def __continuum_add(self, cid, topic_set_collection):
        '''Add one to the end of the continuum container.'''
        self.vcs_ids.append(cid)
        self.topic_sets[cid] = topic_set_collection

    ### EVERYTHING BENEATH IN DEPRECATED

    def continuum_latest(self):
        '''Return the latest version of the continuum.'''
        # The latest version is entry 0
        assert len(self.__vcs_ids) > 0
        return self.__continuum[self.__vcs_ids[0]]

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
