'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Implementation of the VCS interface for the local file system.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import io
import os
import stat
import time

from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.vcs.Interface import Interface
from rmtoo.lib.vcs.FileInterface import FileInterface
from rmtoo.lib.logging import tracer
from rmtoo.lib.vcs.ObjectCache import ObjectCache
from rmtoo.lib.RMTException import RMTException


class FileSystem(FileInterface):
    '''Implementation of the input interface for files in the file system.
       Some aspects of the used and needed things for common VCS are not
       needed here.
       The commit object is replaced by None.
       The vcs id is the full (absolute) path name of a file
       or directory.'''

    def __init__(self, config):
        cfg = Cfg(config)
        FileInterface.__init__(self, cfg)
        tracer.info("called")
        self.__topic_root_node = cfg.get_rvalue("topic_root_node")
        self.__dirs = self._setup_directories(cfg)

    def get_commits(self):
        '''There is no need for an iterator here.'''
        return [None]

    def get_vcs_id_with_type(self, commit, dir_type):
        '''Return the filename of the given dir_type.'''
        assert commit is None
        tracer.debug("called: directory type [%s]", dir_type)
        return ObjectCache.create_hashable(self.__dirs[dir_type])

    def get_timestamp(self, commit):
        '''Return the file time: this is the current time.'''
        return time.time()

    class FileInfo(Interface.FileInfo):
        '''Holds information about a file in a repository.
           Information are filename, vcs_id and a method to
           access the file's content.'''

        def __init__(self, base_dir, sub_dir):
            '''Creates a file system file info object.'''
            Interface.FileInfo.__init__(self)
            self.__base_dir = base_dir
            self.__sub_dir = sub_dir
            self.__filename = os.path.join(self.__base_dir, self.__sub_dir)

        def get_filename(self):
            '''Returns the filename.'''
            return self.__filename

        def get_vcs_id(self):
            '''Returns the vcs id of this file.
               For this filesystem implementation this is the same as the
               filename.'''
            return self.__filename

        def get_filename_sub_part(self):
            '''Return the part of the filename which is beneath the
               base directory.'''
            return self.__sub_dir

        def get_content(self):
            '''Returns the file content.'''
            with io.open(self.__filename, "r", encoding="utf-8") as content_fd:
                content = content_fd.read()
            return content

        def __str__(self):
            '''Returns the string representation.'''
            return "base [%s] sub [%s]" % (self.__base_dir, self.__sub_dir)

    def __get_file_infos_from_dir_rec(self, base_dir, sub_dir):
        '''Recursively collect all file infos from given base directory.'''
        tracer.debug("called: base [%s] sub [%s]", base_dir, sub_dir)
        directory = os.path.join(base_dir, sub_dir)
        result = []
        for dentry in os.listdir(directory):
            pathname = os.path.join(directory, dentry)
            mode = os.stat(pathname).st_mode
            if stat.S_ISDIR(mode):
                # It's a directory, recurse into it
                result.extend(self.__get_file_infos_from_dir_rec(
                    base_dir, os.path.join(sub_dir, dentry)))
            elif stat.S_ISREG(mode):
                # It's a file, call the callback function
                sub_filename = os.path.join(sub_dir, dentry)
                result.append(FileSystem.FileInfo(base_dir, sub_filename))
            else:
                raise RMTException(110, "Invalid directory entry type for [%s]"
                                   % os.path.join(pathname, dentry))
        return result

    def __get_file_infos_from_dir(self, directory):
        '''Return all the fileinfos from the given directory.'''
        tracer.debug("called: directory [%s]", directory)
        return self.__get_file_infos_from_dir_rec(directory, "")

    def get_file_infos(self, commit, dir_type):
        '''Return all fileinfos of the given commit and of the
           given directory type.'''
        assert commit is None
        tracer.debug("called: directory type [%s]", dir_type)
        result = []
        if dir_type not in self.__dirs:
            # Key not available: no files
            return result

        for directory in self.__dirs[dir_type]:
            result.extend(self.__get_file_infos_from_dir(directory))
        return result

    def get_file_info_with_type(self, commit, file_type, filename):
        '''Returns the FileInfo object for the given filename.'''
        assert commit is None
        tracer.debug("called: file type [%s] filename [%s]",
                     file_type, filename)
        for directory in self.__dirs[file_type]:
            tracer.debug("searching in directory [%s]", directory)
            full_path = os.path.join(directory, filename)
            if os.path.exists(full_path):
                return FileSystem.FileInfo(directory, filename)
        raise RMTException(112, "file [%s] in [%s] base file not found"
                           % (filename, file_type))
