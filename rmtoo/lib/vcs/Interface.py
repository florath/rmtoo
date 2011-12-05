'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Abstract Base Class (ABC) to handle different version control systems.
  This includes also reading in the latest version from the file system.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import abc
from types import ListType, StringType, UnicodeType
from rmtoo.lib.RMTException import RMTException

class Interface:
    '''Defines the interface for input fontends like
       VCS or filesystem.'''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_commits(self):
        '''Return an iterator for all available commits.'''
        assert False

    @abc.abstractmethod
    def get_vcs_id_with_type(self, commit, dir_type):
        '''Return the vcs id from the base directories of the given dir_type.'''
        assert commit
        assert dir_type
        assert False

    class FileInfo:
        '''Holds information about a file in a repository.
           Information are filename, vcs_id and a method to
           access the file's content.'''
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

    # Common helper methods
    @staticmethod
    def _check_list_of_strings(name, tbc):
        '''Checks if the given variable is a list of strings.'''
        if type(tbc) != ListType:
            raise RMTException(103, "Configuration error: [%s] configuration "
                               "must be a list" % name)

        if len(tbc) == 0:
            raise RMTException(105, "Configuration error: [%s] configuration "
                               "must be a non empty list" % name)

        for string in tbc:
            if type(string) not in [StringType, UnicodeType]:
                raise RMTException(104, "Configuration error: [%s].[%s] "
                                   " configuration must be a string"
                                   % (name, string))


