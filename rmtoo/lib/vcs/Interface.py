'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Abstract Base Class (ABC) to handle different version control systems.
  This includes also reading in the latest version from the file system.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import abc

from rmtoo.lib.Encoding import Encoding
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.lib.logging import tracer


class Interface(object):
    '''Defines the interface for input fontends like
       VCS or filesystem.'''
    __metaclass__ = abc.ABCMeta

    def __init__(self, config):
        self._config = config
        self._txt_io_config = TxtIOConfig(config)
        self._topic_root_node = config.get_value("topic_root_node")

    def get_txt_io_config(self):
        """Return the appropriate TxtIOConfig"""
        return self._txt_io_config

    def get_topic_base_file_info(self, commit):
        '''Return the base filename for the topics.'''
        tracer.debug("called")
        return self.get_file_info_with_type(
            commit, "topics", self._topic_root_node + '.tic')

    @abc.abstractmethod
    def get_commits(self):
        '''Return an iterator for the given commit.'''
        assert False

    @abc.abstractmethod
    def get_vcs_id_with_type(self, commit, dir_type):
        '''Return the vcs id from the base dir of the given dir_type.'''
        assert commit
        assert dir_type
        assert False

    @abc.abstractmethod
    def get_timestamp(self, commit):
        '''Returns the timestamp of the set of requirements.
           This is, e.g. for files 'now()', for commits the date of the
           commit.'''
        assert commit
        assert False

    # pylint: disable=no-init
    class FileInfo:
        '''Holds information about a file in a repository.
        Information are filename, vcs_id and a method to
        access the file's content.
        '''
        __metaclass__ = abc.ABCMeta

        @abc.abstractmethod
        def get_filename(self):
            '''Returns the filename.'''
            assert False

        @abc.abstractmethod
        def get_vcs_id(self):
            '''Returns the vcs id of this file.'''
            assert False

        @abc.abstractmethod
        def get_filename_sub_part(self):
            '''Return the part of the filename which is beneath the
               base directory.'''
            assert False

        @abc.abstractmethod
        def get_content(self):
            '''Returns the file content.'''
            assert False

        @abc.abstractmethod
        def __str__(self):
            '''Returns the string representation.'''
            assert False

    @abc.abstractmethod
    def get_file_infos(self, commit, dir_type):
        '''Return all fileinfos of the given commit and of the
           given directory type.'''
        assert commit
        assert dir_type
        assert False

    @abc.abstractmethod
    def get_file_info_with_type(self, commit, file_type, filename):
        '''Returns the FileInfo object for the given filename.'''
        assert False

    # Common helper methods
    @staticmethod
    def _check_list_of_strings(name, tbc):
        '''Checks if the given variable is a list of strings or None.'''
        if tbc is None:
            tracer.debug("Ignoring non existent configuration for [%s]", tbc)
            return

        if not isinstance(tbc, list):
            assert False
            raise RMTException(103, "Configuration error: [%s] configuration "
                               "must be a list, is [%s]" % (name, type(tbc)))

        if not tbc:
            raise RMTException(105, "Configuration error: [%s] configuration "
                               "must be a non empty list" % name)

        for string in tbc:
            if not Encoding.is_unicode(string):
                raise RMTException(104, "Configuration error: [%s].[%s] "
                                   " configuration must be a string"
                                   % (name, string))
