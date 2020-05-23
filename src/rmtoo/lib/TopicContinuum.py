'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Collection of collection of topics.
  In each run of rmtoo it is possible to have many different
  TopicSets handled.
  This object handles the collection of TopicSets.
  A TopicContinuum has a name - which is configured directly under
  the 'topic' tag.
  The top level access of this are the different version numbers
  of the topic sets.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.logging import tracer
from rmtoo.lib.UsableFlag import UsableFlag
from rmtoo.lib.TopicSet import TopicSet
from rmtoo.lib.vcs.Factory import Factory
from rmtoo.lib.TopicSetWCI import TopicSetWCI
from rmtoo.lib.vcs.CommitInfo import CommitInfo
from rmtoo.lib.FuncCall import FuncCall


class TopicContinuum(UsableFlag):
    '''A TopicContinuum holds different (historic) versions
       of TopicSets.'''

    # pylint: disable=too-many-arguments
    def __init__(self, ts_name, config, ts_config, object_cache, input_mods):
        UsableFlag.__init__(self)
        self.__name = ts_name
        tracer.info("Called: name [%s]", self.__name)
        self._config = config
        self.__topic_sets = {}
        # This is the list of all version control system ids.
        # Those ids are sorted by time.
        # The first is the vcs id of the (sub-)element,
        # The second is the commit.
        # The oldest versions is the first one - sorted.
        # Note: this does not contain any other data, only the ids.
        # To access the data, use some construct like:
        #   self.__topic_sets[self.__vcs_commit_ids[n].get_commit()]
        #
        self.__vcs_commit_ids = []
        self.__object_cache = object_cache
        self.__input_mods = input_mods
        self.__read_topic_sets(ts_config)
        self.__ts_config = ts_config
        tracer.debug("Finished; topic set count [%d]", len(self.__topic_sets))

    def __read_commits(self, input_handler, commits):
        '''Creates a TopicSet for each commit with the help of
           the input_handler.'''
        tracer.debug("Called.")
        for commit in commits:
            tracer.debug("Handling commit [%s]", commit)
            topic_set_vcs_id = \
                input_handler.get_vcs_id_with_type(commit, "topics")
            tracer.debug("Read topics with oid [%s]", topic_set_vcs_id)
            topic_set = self.__object_cache.get("TopicSet", topic_set_vcs_id)

            if topic_set is None:
                tracer.debug("TopicSet with ID [%s] not in cache",
                             topic_set_vcs_id)
                topic_set = TopicSet(self._config, input_handler, commit,
                                     self.__object_cache, self.__input_mods)
                self.__object_cache.add(topic_set_vcs_id,
                                        "TopicSet", topic_set)
                self._adapt_usablility(topic_set)

            commit_info = CommitInfo(input_handler, commit, topic_set_vcs_id)
            tswci = TopicSetWCI(topic_set, commit_info)
            tracer.debug("Add topic set [%s]", topic_set_vcs_id)
            self.__continuum_add(commit_info, tswci)
            tracer.debug("Finished.")

    def __read_topic_sets(self, ts_config):
        '''Reads in all the topic sets from the specified sources.'''
        tracer.debug("Called.")
        for source in ts_config['sources']:
            input_handler = Factory.create(source[0], source[1])
            if input_handler is None:
                continue
            commits = input_handler.get_commits()
            self.__read_commits(input_handler, commits)
        tracer.debug("Finished.")

    def __continuum_add(self, commit_info, topic_set_wci):
        '''Add one to the end of the continuum container.'''
        self.__vcs_commit_ids.insert(0, commit_info)
        self.__topic_sets[commit_info.get_commit()] = topic_set_wci

    def execute(self, executor, func_prefix):
        '''Execute the parts which are needed for TopicsContinuum.'''
        tracer.debug("Calling pre [%s]", self.__name)
        FuncCall.pcall(executor, func_prefix + "topic_continuum_pre", self)
        tracer.debug("Calling sub [%s]", self.__name)
        for topic_set in executor.topic_continuum_sort(
                self.__vcs_commit_ids, self.__topic_sets):
            topic_set.execute(executor, func_prefix)
        tracer.debug("Calling post [%s]", self.__name)
        FuncCall.pcall(executor, func_prefix + "topic_continuum_post", self)
        tracer.debug("Finished [%s]", self.__name)

    def get_output_config(self):
        """Returns the configuration for the output."""
        return self.__ts_config["output"]

    def get_vcs_commit_ids(self):
        '''Returns the vcs_commit_ids.'''
        return self.__vcs_commit_ids

    def get_name(self):
        '''Return the name of the topic continuum.'''
        return self.__name

    def get_topic_set(self, oid):
        '''Returns the topic set with the given id.'''
        return self.__topic_sets[oid]

    def __str__(self):
        return "TopicContinuum [%s]" % self.__name
