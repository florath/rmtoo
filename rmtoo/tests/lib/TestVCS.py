'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Implementation of  test VCS interface.
   
 (c) 2011-2012 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import os
import stat
import time

from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.vcs.Interface import Interface
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.vcs.ObjectCache import ObjectCache
from rmtoo.lib.RMTException import RMTException

class TestVCS(Interface):

    def __init__(self, config):
        Interface.__init__(self, config)

    def get_tfile1(self):
        return self.FileInfo()

    def get_commits(self):
        '''Return an iterator for the given commit.'''
        assert False

    def get_vcs_id_with_type(self, commit, dir_type):
        '''Return the vcs id from the base directories of the given dir_type.'''
        assert commit
        assert dir_type
        assert False

    def get_timestamp(self, commit):
        '''Returns the timestamp of the set of requirements.
           This is, e.g. for files 'now()', for commits the date of the
           commit.'''
        assert commit
        assert False

    class FileInfo(Interface.FileInfo):

        def get_filename(self):
            '''Returns the filename.'''
            assert False

        def get_vcs_id(self):
            '''Returns the vcs id of this file.'''
            assert False

        def get_filename_sub_part(self):
            '''Return the part of the filename which is beneath the 
               base directory.'''
            return "/does/not/exist/topic.tic"

        def get_content(self):
            '''Returns the file content.'''
            return "Nothing: Else"

        def __str__(self):
            '''Returns the string representation.'''
            assert False

    def get_file_infos(self, commit, dir_type):
        '''Return all fileinfos of the given commit and of the
           given directory type.'''
        assert commit
        assert dir_type
        assert False

    def get_file_info_with_type(self, commit, file_type, filename):
        '''Returns the FileInfo object for the given filename.'''
        assert False
