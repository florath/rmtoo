'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Collection of collection of collection of topics.
  The continuum holds all the different versions of TopicSetCollections
  from the whole time of being.
  The key to access this is the 'name' under 'topic' (in the configuration).

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from six import iteritems

from rmtoo.lib.TopicContinuum import TopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.vcs.ObjectCache import ObjectCache
from rmtoo.lib.UsableFlag import UsableFlag
from rmtoo.lib.FuncCall import FuncCall
from rmtoo.lib.GenIterator import GenIterator


class TopicContinuumSet(UsableFlag):
    '''Class holding all the available TopicSetCollections
       of the past and possible the current.'''

    def __init__(self, input_mods, config):
        '''Sets up a TopicContinuum for use.'''
        tracer.info("called")
        UsableFlag.__init__(self)
        self.__input_mods = input_mods
        self._config = config
        # This dictionary holds all the TopicSetCollections
        # available in the configured time period.
        self.__continuum = {}
        # Store objects with IDs also in the cache - so that they
        # can be reused.
        self.__object_cache = ObjectCache()
        self.__init_continuum_set()
        self.__object_cache.log_stats()
        tracer.debug("Finished.")

    def __init_continuum_set(self):
        '''Initialize the continuum:
           Check the configuration for the appropriate interval parameters
           and read in the TopicContinuum.'''
        tracer.debug("Called.")
        # Step through all the available topic sets.
        for ts_name, ts_config in iteritems(self._config.get_value("topics")):
            topic_cont = TopicContinuum(ts_name, self._config, ts_config,
                                        self.__object_cache, self.__input_mods)
            self.__continuum[ts_name] = topic_cont
            self._adapt_usablility(topic_cont)
        tracer.debug("Finished; count [%d]", len(self.__continuum))

    def execute(self, executor, func_prefix):
        '''Execute the parts which are needed for TopicsContinuumSet.'''
        tracer.debug("Calling pre.")
        FuncCall.pcall(executor, func_prefix + 'topic_continuum_set_pre', self)
        tracer.debug("Calling sub.")
        for continuum in executor.topic_continuum_set_sort(
                self.__continuum.values()):
            continuum.execute(executor, func_prefix)
        tracer.debug("Calling Post")
        FuncCall.pcall(executor, func_prefix + 'topic_continuum_set_post',
                       self)
        tracer.debug("Finished.")

    def get_continuum_dict(self):
        '''Returns the continuum.'''
        return self.__continuum


class TopicContinuumSetIterator(GenIterator):
    '''This class provides an iterator interface for all the sub-elements
       of a topic continuum set.'''

    def __init__(self, topic_continuum_set):
        '''Initialize the iterator.'''
        GenIterator.__init__(
            self, iteritems(topic_continuum_set.get_continuum_dict()))

    def has_child(self):
        '''If the current element has a child, true is returned.'''
        return len(self._current[1].get_vcs_commit_ids()) > 0
