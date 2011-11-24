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
from rmtoo.lib.VersionControlSystem import VCSException, VersionControlSystem
from rmtoo.lib.TopicContinuum import TopicContinuum
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.lib.logging.EventLogging import tracer

class TopicContinuumSet(MemLogStore):
    '''Class holding all the available TopicSetCollections
       of the past and possible the current.'''

    def __init__(self, mods, config):
        '''Sets up a TopicContinuum for use.'''
        tracer.info("called")
        MemLogStore.__init__(self)
        self.mods = mods
        self.config = config

        # This dictionary holds all the TopicSetCollections
        # available in the configured time period.
        self.continuum = {}
        # The VCS repository.
        # If this is None - there is no repository available.
        self.deprecated_repo = None
        # Because the construction / evaluation should continue even in
        # error cases, a flag is available to check if the (possible only
        # partially) constructed element is usable.
        self.m_is_usable = True

        self.internal_init_continuum_set()

    def deprecated_internal_get_interval(self):
        '''Returns the configured interval [start, end].'''
        return [self.config.get_value('requirements.input.commit_interval.begin'),
                self.config.get_value('requirements.input.commit_interval.end')]

    def deprecated_internal_create_repo(self):
        '''This method sets up the repository and splits out the repository
           directory from the requirements directory.
           Sets up the repository variable with the repository object when
           a repository is available. In this case 'true' is returned.
           If there is no repository available, 'false' is returned.'''
        directory = self.config.get_value("requirements.input.directory")
        # When the directory is not absolute, convert it to an
        # absolute path that it can be compared to the outcome of the
        # git.Repo. 
        if not os.path.isabs(directory):
            directory = os.path.abspath(directory)

        try:
            self.repo = VersionControlSystem.create(directory)
            return True
        except VCSException:
            # There is no VCS repository here - therefore nothing to do.
            pass
        return False

    def deprecated_internal_repo_access_needed(self, versint):
        '''Checks if depending on the given versions interval 
           a repository is needed.'''
        # Only if FILES:FILES is specified, there is no need to access
        # the repository.
        return versint[0] != 'FILES' or versint[1] != 'FILES'

    def deprecated_internal_check_repo(self, versint):
        '''Checks if a repository is needed.
           If so, it checks whether a repository exists.  If (in this case)
           no repository exists, an exception is thrown.'''
        # Should the repository be accessed?
        if self.internal_repo_access_needed(versint):
            # Have a look, if there is a repository in the given directory.
            if not self.internal_create_repo():
                raise RMTException(40, "Based on the configuration a "
                                   "repository is needed - but there is "
                                   "none")

    def deprecated_internal_create_continuum_from_file(self):
        '''Reads in a TopicSetCollection from the file system.'''
        topic_set_collection = TopicSetCollection(self.config)
        req_input_dir = self.config.get_value('requirements.input.directory')
        topic_set_collection.read_from_filesystem(req_input_dir)
        self.internal_continuum_add("FILES", topic_set_collection)

    def deprecated_internal_create_continuum_from_vcs(self, start_vers, end_repo):
        '''Read in the continuum from the VCS.'''
        tsc_list = self.repo.read_history(start_vers, end_repo)
        # Copy over the result into the local (current)
        for tsc in tsc_list:
            self.internal_continuum_add(tsc[0], tsc[1])

    def deprecated_internal_read_continuum(self, versint):
        '''Read in the continuum from the VCS and / or file system.'''
        start_vers, end_vers = versint
        # Maybe add also the FILES:
        if end_vers == "FILES":
            self.internal_create_continuum_from_file()
        # Maybe add also some old versions
        if start_vers != "FILES":
            # When there is FILES given as last parameter - get
            # everything from start_vers upto HEAD
            end_repo = end_vers
            if end_vers == "FILES":
                end_repo = "HEAD"
            self.internal_create_continuum_from_vcs(start_vers, end_repo)

    def internal_init_continuum_set(self):
        '''Initialize the continuum:
           Check the configuration for the appropriate interval parameters
           and read in the TopicSetCollections.'''
        tracer.debug("called")
        # Step through all the available topic sets.
        for ts_name, ts_config in \
            self.config.get_value("topics").get_dict().iteritems():
            self.continuum[ts_name] = \
                TopicContinuum(ts_name, self.config, ts_config)

        assert False

        sources = self.config()


        versint = self.internal_get_interval()
        self.internal_check_repo(versint)
        self.internal_read_continuum(versint)

    def continuum_latest(self):
        '''Return the latest version of the continuum.'''
        # The latest version is entry 0
        assert len(self.vcs_ids) > 0
        return self.continuum[self.vcs_ids[0]]

    def is_usable(self):
        '''Returns True iff the object is really usable, i.e.
           if there was no problem during construction.'''
        return self.m_is_usable
