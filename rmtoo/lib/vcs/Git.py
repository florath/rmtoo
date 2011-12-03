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
# (Calling this during the main does not help - because this might
# already been loaded.) 
# Note that this is a hack which will be removed when the API 
# to the git-python is stable.
for sp in sys.path:
    rc = os.path.join(sp, 'rmtoo/contrib')
    if os.path.exists(rc):
        sys.path.insert(0, rc)
        break
import git

from types import ListType, StringType, UnicodeType

from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.vcs.Interface import Interface
from rmtoo.lib.vcs.ObjectCache import ObjectCache
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.RMTException import RMTException

# TODO: use sub-directories for requirements and topics
#   (adapt the RID)

class Git(Interface):
    '''Handles a git repository.'''

    @staticmethod
    def __check_list_of_strings(name, tbc):
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
        if self.__repo_base_dir == None:
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

        # When the directory is not absolute, convert it to an
        # absolute path that it can be compared to the outcome of the
        # git.Repo. 
        self.__dirs = {}
        self.__repo_base_dir = None
        self.__repo = None
        self.__setup_directories(cfg)

    def get_commits(self):
        '''Return an iterator for all the commits.'''
        return self.__repo.iter_commits(
                    self.__start_vers + ".." + self.__end_vers)

    def __get_blob_direct(self, tree, name):
        '''Return the blob of the tree with the given name.
           If name is not available, an exception is thrown.'''
        tracer.debug("called: name [%s]" % name)
        for blob in tree.blobs:
            if blob.name == name:
                return blob
        raise RMTException(109, "blob entry [%s] not found in tree."
                           % name)

    def __get_tree_direct(self, base_tree, directory):
        '''Return the tree of the given directory.
           This does not walk down the directory structure.
           It just checks the current hierarchy.'''
        for tree in base_tree.trees:
            if tree.name == directory:
                return tree
        raise RMTException(108, "directory entry [%s] not found in tree "
                           "[%s]." % (directory, base_tree.name))

    def __get_tree(self, base_tree, dir_split):
        '''Returns the tree starting from the base_tree walking down
           the path of dir_split.'''
        tree = self.__get_tree_direct(base_tree, dir_split[0])
        if len(dir_split) > 1:
            return self.__get_tree(tree, dir_split[1:])
        return tree

    def __get_file_names_from_tree(self, tree, directory):
        '''Returns all the file names (i.e. the blob names) 
           recursive starting with the given directory.'''
        tracer.debug("called: directory [%s]" % directory)

        dir_split = directory.split("/")
        ltree = self.__get_tree(tree, dir_split)

        result = []
        for blob in ltree.blobs:
            result.append(os.path.join(directory, blob.name))
        return result

    def __get_blob_with_filename_split(self, commit, filename_split):
        '''Returns the blob for the given filename.'''
        ltree = self.__get_tree(commit.tree, filename_split[:-1])
        return self.__get_blob_direct(ltree, filename_split[-1])

    def get_vcs_id(self, commit, filename):
        '''Returns the vcs id of the given filename.'''
        tracer.debug("called: commit [%s] filename [%s]"
                     % (commit, filename))
        filename_split = filename.split("/")
        return self.__get_blob_with_filename_split(commit, filename_split).hexsha

    def get_vcs_id_with_type(self, commit, dir_type):
        '''Return the vcs id from the base directories of the given dir_type.'''
        tracer.debug("called: commit [%s] directory type [%s]"
                     % (commit, dir_type))
        result = []
        for directory in self.__dirs[dir_type]:
            dir_split = directory.split("/")
            ltree = self.__get_tree(commit.tree, dir_split)
            result.append(ltree.hexsha)
        return ObjectCache.create_hashable(result)

    def get_file_names(self, commit, dir_type):
        '''Return all filenames of the given commit and of the
           given directory type.'''
        tracer.debug("called: commit [%s] directory type [%s]"
                     % (commit, dir_type))
        result = []
        for directory in self.__dirs[dir_type]:
            # TODO: Do something like return a list of pairs
            #  1. element: pathname
            #  2. element: rid (pathname without the __dirs[dir_type] part
            assert False
            result.extend(self.__get_file_names_from_tree(
                                    commit.tree, directory))
        return result

    def get_fd(self, commit, filename):
        '''Return the file descriptor to read in filename from
           the given commit.'''
        tracer.debug("called: commit [%s] filename [%s]"
                     % (commit, filename))
        filename_split = filename.split("/")
        return self.__get_blob_with_filename_split(
                        commit, filename_split).data_stream

    def read(self):
        '''Read in the TopicSets from git.'''
        assert False
        # Do the whole history.
        for commit in self.repo.iter_commits(
                        self.start_vers + ".." + self.end_vers):
            self.internal_read_commit(commit)


        assert False
