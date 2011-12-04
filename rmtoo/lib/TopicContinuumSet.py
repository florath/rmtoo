'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Collection of collection of collection of topics.
  The continuum holds all the different versions of TopicSetCollections
  from the whole time of being.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import os
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.VersionControlSystem import VersionControlSystem
from rmtoo.lib.TopicContinuum import TopicContinuum
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.vcs.ObjectCache import ObjectCache

class TopicContinuumSet(MemLogStore):
    '''Class holding all the available TopicSetCollections
       of the past and possible the current.'''

    def __init__(self, input_mods, config):
        '''Sets up a TopicContinuum for use.'''
        tracer.info("called")
        MemLogStore.__init__(self)
        self.__input_mods = input_mods
        self.__config = config

        # This dictionary holds all the TopicSetCollections
        # available in the configured time period.
        self.__continuum = {}
        # The VCS repository.
        # If this is None - there is no repository available.
        self.__deprecated_repo = None
        # Because the construction / evaluation should continue even in
        # error cases, a flag is available to check if the (possible only
        # partially) constructed element is usable.
        self.__is_usable = True
        # Store objects with IDs also in the cache - so that they can be reused.
        self.__object_cache = ObjectCache()
        self.__init_continuum_set()
        self.__object_cache.log_stats()

    def __init_continuum_set(self):
        '''Initialize the continuum:
           Check the configuration for the appropriate interval parameters
           and read in the TopicSetCollections.'''
        tracer.debug("called")
        # Step through all the available topic sets.
        for ts_name, ts_config in \
            self.__config.get_value("topics").get_dict().iteritems():
            topic_cont = TopicContinuum(ts_name, self.__config, ts_config,
                               self.__object_cache, self.__input_mods)
            self.__continuum[ts_name] = topic_cont
            if not topic_cont.is_usable():
                self.__is_usable = False

    def is_usable(self):
        '''Returns True iff the object is really usable, i.e.
           if there was no problem during construction.'''
        return self.__is_usable
