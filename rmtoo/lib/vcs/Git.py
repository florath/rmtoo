'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Version Control System.
   Git implementation.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import os
import sys

# To find the correct version of git-python (and friends) [the rmtoo
# local version must be used], the sys.path is scanned and when a
# sp/rmtoo/contrib is found, this is included (prepended) to sys.path.
# This can be removed once the git-pyhton is removed.
# (Calling this durint the main does not help - because this might
# already been loaded.) 
# Note that this is a hack which will be removed when the API 
# to the git-python is stable.
for sp in sys.path:
    rc = os.path.join(sp, 'rmtoo/contrib')
    if os.path.exists(rc):
        sys.path.insert(0, rc)
        break
import git

import re
from types import ListType, StringType, UnicodeType

from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.vcs.Interface import Interface
from rmtoo.lib.vcs.VCSException import VCSException
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.RMTException import RMTException

class Git(Interface):
    '''Handles a git repository.'''

    # TODO: Needed?
    class Commit:
        '''Encapsulates a git commit.'''
        pass

    @staticmethod
    def __check_list_of_strings(name, tbc):
        '''Checks if the given variable is a list of strings.'''
        if type(tbc)!=ListType:
            raise RMTException(103, "Configuration error: [%s] configuration "
                               "must be a list" % name)
            
        if len(tbc)==0:
            raise RMTException(105, "Configuration error: [%s] configuration "
                               "must be a non empty list" % name)
        
        for string in tbc:
            if type(string) not in [StringType, UnicodeType]:
                raise RMTException(104, "Configuration error: [%s].[%s] "
                                   " configuration must be a string" 
                                   % (name, string))
            
    @staticmethod
    def __abs_path(directory):
        '''Convert the given directory path into an absolute path.'''
        if not os.path.isabs(directory):
            return os.path.abspath(directory)
        return directory

    def __check_if_dir_is_in_repo(self, directory):
        '''Checks if all the directories are the in repository.
           The absolute path is computed if the path is relative and
           then compared to the repository base directory.'''
        tracer.debug("called: directory [%s]" % directory)
        if self.__repo_base_dir==None:
            self.__setup_repo(directory)
        if not directory.startswith(self.__repo_base_dir):
            raise RMTException(28, "directory [%s] not in repository")
        
    def __cut_off_repo_dir(self, directory):
        '''Cuts off the repository directory from the directory.'''
        # +1: cut off the '/' also.
        len_repo_base_dir = len(self.__repo_base_dir) + 1
        return directory[len_repo_base_dir:]
        
    def __setup_directories(self, cfg):
        '''Cleans up and unifies the directories.'''
        tracer.debug("called")
        for dir_type in ["requirements", "topics", "constraints"]:
            dirs = map(self.__abs_path, cfg.get_value(dir_type + "_dirs"))
            self.__check_list_of_strings(dir_type, dirs)
            
            new_directories = []
            for directory in dirs:
                self.__check_if_dir_is_in_repo(directory)
                new_directories.append(self.__cut_off_repo_dir(directory))
            self.__dirs[dir_type] = new_directories
            
        for dir_type, directory in self.__dirs.iteritems():
            tracer.debug("[%s] directories [%s]" % (dir_type, directory))

    def __setup_repo(self, directory):
        '''Sets up the repository.'''
        tracer.debug("called")

        # Get one sample directory and create the repository from this.
        # Check all if they are in the same repository.
        # Note: because every directory list must contain at least one
        #  directory, use just one.
        tracer.debug("using [%s] as sample directory" % directory)
        self.__repo = git.Repo(directory)
        # :-4: cut off the '/.git'.
        self.__repo_base_dir = self.__repo.git_dir[:-5]
        tracer.debug("repository base directory [%s]" % self.__repo_base_dir)

    def __init__(self, config):
        tracer.info("called")
        cfg = Cfg(config)
        self.__start_vers = cfg.get_value("start_vers")
        self.__end_vers = cfg.get_value("end_vers")
        self.__topic_root_node = cfg.get_value("topic_root_node")
        tracer.debug("start version [%s] end version [%s] "
                     "topic root node [%s]"
                     % (self.__start_vers, self.__end_vers,
                        self.__topic_root_node))

        self.__current_commit = None

        # When the directory is not absolute, convert it to an
        # absolute path that it can be compared to the outcome of the
        # git.Repo. 
        self.__dirs = {}
        self.__repo_base_dir = None
        self.__setup_directories(cfg)

    def get_commits(self):
        '''Return an iterator for all the commits.'''
        return self.__repo.iter_commits(
                    self.__start_vers + ".." + self.__end_vers)

    def set_commit(self, commit):
        '''For all upcomig read accesses the given commit
           will be used.'''
        self.current_commit = commit

    def UNUSED_internal_read_file(self, path, blob, creator):
        '''Read file from given blob'''
        tracer.debug("called: path [%s] name [%s]" % (path, blob.name))
        if not creator.check_filename(blob.name):
            tracer.debug("ignoring file [%s]" % blob.name)
            return
        creator.create(blob)

        assert False

    def UNUSED_internal_read_tree(self, path, tree, creator):
        '''Read the tree.  The tree has the name 'path'.'''
        tracer.debug("path [%s]" % path)
        for entry in tree.blobs:
            self.internal_read_file(path, entry, creator)
        for entry in tree.trees:
            lpath = path
            lpath.append(entry.name)
            self.internal_read_tree(lpath, entry, creator)

    def UNUSED_internal_read_commit(self, commit):
        '''Reads in one commit - which the given index - from the git.'''
        tracer.debug("read commit [%s]" % commit)

        class TopicCreator:

            @staticmethod
            def check_filename(filename):
                tracer.debug("filename [%s]" % filename)
                return re.match("^.*\.tic$", filename) != None

            @staticmethod
            def create(blob):
                tracer.debug("create [%s]" % blob.name)
                assert False

        self.internal_read_tree([], commit.tree[self.topics_subdir],
                                TopicCreator)

#        try:
#            tree = commit.tree[self.topics_subdir]
#            print("TREE: [%s]" % tree)
#            print("TREE: [%s]" % dir(tree))
#            print("TREE: [%s]" % tree.list_traverse())
#        except KeyError, ke:
#            # This means, that at this point of time the directory was
#            # not available.
#            assert False
#            

    def read(self):
        '''Read in the TopicSets from git.'''
        assert False
        # Do the whole history.
        for commit in self.repo.iter_commits(
                        self.start_vers + ".." + self.end_vers):
            self.internal_read_commit(commit)


        assert False
