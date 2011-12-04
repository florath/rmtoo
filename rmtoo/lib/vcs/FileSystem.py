'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Implementation of the VCS interface for the local file system.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.vcs.Interface import Interface
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.vcs.ObjectCache import ObjectCache

class FileSystem(Interface):
    '''Implementation of the input interface for files in the file system.
       Some aspects of the used and needed things for common VCS are not
       needed here.
       The commit object is replaced by None.
       The vcs id is the full (absolute) path name of a file
       or directory.'''

    def __setup_directories(self, cfg):
        '''Cleans up and unifies the directories.'''
        tracer.debug("called")
        for dir_type in ["requirements", "topics", "constraints"]:
            dirs = cfg.get_value(dir_type + "_dirs")
            self._check_list_of_strings(dir_type, dirs)

            new_directories = []
            for directory in dirs:
                new_directories.append(directory)
            self.__dirs[dir_type] = new_directories

        for dir_type, directory in self.__dirs.iteritems():
            tracer.debug("[%s] directories [%s]" % (dir_type, directory))

    def __init__(self, config):
        tracer.info("called")
        cfg = Cfg(config)
        self.__topic_root_node = cfg.get_value("topic_root_node")
        self.__dirs = {}
        self.__setup_directories(cfg)

    def get_commits(self):
        '''There is no need for an iterator here.'''
        return [None]

    def get_vcs_id_with_type(self, commit, dir_type):
        '''Return the filename of the given dir_type.'''
        assert commit == None
        tracer.debug("called: directory type [%s]" % dir_type)
        return ObjectCache.create_hashable(self.__dirs[dir_type])

    class FileInfo(Interface.FileInfo):
        '''Holds information about a file in a repository.
           Information are filename, vcs_id and a method to
           access the file's content.'''

        def get_filename(self):
            '''Returns the filename.'''
            assert False

        def get_vcs_id(self):
            '''Returns the vcs id of this file.'''
            assert False

        def get_filename_sub_part(self):
            '''Return the part of the filename which is beneath the 
               base directory.'''
            assert False

        def get_content(self):
            '''Returns the file content.'''
            assert False

    def __get_file_infos_from_dir(self, directory):
        '''Return all the fileinfos from the given directory.'''
        assert False
        os.listdir(path)
        os.stat(path + sub)
        if stat.is_file() - - - -
        if stat.is_dir()...

    def get_file_infos(self, commit, dir_type):
        '''Return all fileinfos of the given commit and of the
           given directory type.'''
        assert commit == None
        tracer.debug("called: directory type [%s]" % dir_type)
        result = []
        for directory in self.__dirs[dir_type]:
            result.extend(self.__get_file_infos_from_dir(directory))
        return result
