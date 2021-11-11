'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Implementation of test VCS interface.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import time

from rmtoo.lib.vcs.Interface import Interface


class TestVCS(Interface):

    def __init__(self, config):
        Interface.__init__(self, config)

    def get_tfile1(self):
        return self.FileInfo()

    def get_commits(self):
        '''Return an iterator for the given commit.'''
        assert False

    def get_vcs_id_with_type(self, commit, dir_type):
        '''Return the vcs id from the base directories of the given dir_type'''
        return "TheStaticVcsId"

    def get_timestamp(self, commit):
        '''Returns the current time.'''
        return time.time()

    class FileInfo(Interface.FileInfo):

        def __init__(self, tc=0):
            if tc == 0:
                self.__content = u"Name: ItsMe\nNothing: Else\n"
            if tc == 1:
                self.__content = u"Nothing: Else\n"

        def get_filename(self):
            '''Returns the filename.'''
            assert False

        def get_vcs_id(self):
            '''Returns the vcs id of this file.'''
            assert False

        def get_filename_sub_part(self):
            '''Return the part of the filename which is beneath the
               base directory.'''
            return u"/does/not/exist/topic.tic"

        def get_content(self):
            '''Returns the file content.'''
            return self.__content

        def __str__(self):
            '''Returns the string representation.'''
            return u"NothingElse"

    def get_file_infos(self, commit, dir_type):
        '''Return all fileinfos of the given commit and of the
           given directory type.'''
        return []

    def get_file_info_with_type(self, commit, file_type, filename):
        '''Returns the FileInfo object for the given filename.'''
        return TestVCS.FileInfo()
