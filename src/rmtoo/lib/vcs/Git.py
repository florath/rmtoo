'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Version Control System.
   Git implementation.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import copy
import os

import git

from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.vcs.Interface import Interface
from rmtoo.lib.vcs.FileInterface import FileInterface
from rmtoo.lib.vcs.ObjectCache import ObjectCache
from rmtoo.lib.logging import tracer
from rmtoo.lib.RMTException import RMTException


class Git(FileInterface):
    '''Handles a git repository.'''

    # This is overloaded and therefore must be a normal method.
    # pylint: disable=no-self-use
    def _adapt_dir_path(self, directory):
        '''Convert the given directory path into an absolute path.'''
        if not os.path.isabs(directory):
            return os.path.abspath(directory)
        return directory

    def _extended_directory_check(self, directory):
        '''Checks if all the directories are the in repository.
           The absolute path is computed if the path is relative and
           then compared to the repository base directory.'''
        tracer.debug("called: directory [%s]", directory)
        if self.__repo_base_dir is None:
            self.__setup_repo(directory)
        if not directory.startswith(self.__repo_base_dir):
            raise RMTException(28, "directory [%s] not in repository"
                               % directory)
        return

    def _adapt_ext_path(self, directory):
        '''Cuts off the repository directory from the directory.'''
        # +1: cut off the '/' also.
        len_repo_base_dir = len(self.__repo_base_dir) + 1
        return directory[len_repo_base_dir:]

    def __setup_repo(self, directory):
        '''Sets up the repository.'''
        tracer.debug("called")

        # Get one sample directory and create the repository from this.
        # Check all if they are in the same repository.
        # Note: because every directory list must contain at least one
        #  directory, use just one.
        repo_found = False
        while len(directory) > 1:
            try:
                tracer.debug("using [%s] as sample directory", directory)
                self.__repo = git.Repo(directory)
                repo_found = True
                break
            except (git.exc.InvalidGitRepositoryError,
                    git.exc.NoSuchPathError):
                tracer.debug("Sample directory [%s] does not exists",
                             directory)
                directory = os.path.dirname(directory)
        if not repo_found:
            assert False

        # :-4: cut off the '/.git'.
        self.__repo_base_dir = self.__repo.git_dir[:-5]
        tracer.debug("repository base directory [%s]", self.__repo_base_dir)

    def __init__(self, config):
        tracer.info("called")
        cfg = Cfg(config)
        FileInterface.__init__(self, cfg)
        self.__start_vers = cfg.get_rvalue("start_vers")
        self.__end_vers = cfg.get_rvalue("end_vers")
        self.__topic_root_node = cfg.get_rvalue("topic_root_node")
        tracer.debug("start version [%s] end version [%s] "
                     "topic root node [%s]",
                     self.__start_vers, self.__end_vers,
                     self.__topic_root_node)

        # When the directory is not absolute, convert it to an
        # absolute path that it can be compared to the outcome of the
        # git.Repo.
        self.__dirs = {}
        self.__repo_base_dir = None
        self.__repo = None
        self.__dirs = self._setup_directories(cfg)

    def get_commits(self):
        '''Return an iterator for all the commits.'''
        return self.__repo.iter_commits(
            self.__start_vers + ".." + self.__end_vers)

    def get_timestamp(self, commit):
        '''Return the commit time.'''
        return commit.authored_date

    class FileInfo(Interface.FileInfo):
        '''Holds information about a file in a repository.
           Typical information are filename, vcs_id.'''

        def __init__(self, base_dir, sub_dir, blob):
            Interface.FileInfo.__init__(self)
            self.__base_dir = base_dir
            self.__blob = blob
            self.__sub_dir = sub_dir

            self.__base_dirname = os.path.join(*self.__base_dir)
            self.__sub_dirname = ""
            if self.__sub_dir:
                self.__sub_dirname = os.path.join(*self.__sub_dir)
            tracer.debug(self)
            self.__filename = os.path.join(
                self.__base_dirname, self.__sub_dirname,
                self.__blob.name)

        def __str__(self):
            '''Returns the string representation.'''
            return "base [%s] sub [%s] name [%s]" % \
                (self.__base_dirname, self.__sub_dirname,
                 self.__blob.name)

        def get_filename(self):
            '''Returns the filename.'''
            return self.__filename

        def get_vcs_id(self):
            '''Returns the vcs id of this file.'''
            return self.__blob.hexsha

        def get_filename_sub_part(self):
            '''Return the part of the filename which is beneath the
               base directory.'''
            return os.path.join(self.__sub_dirname, self.__blob.name)

        def get_content(self):
            '''Returns the file content.'''
            return self.__blob.data_stream.read().decode("utf-8")

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

    def __get_file_infos_from_tree_rec(self, tree, base_dir, sub_dir):
        '''Returns recursively all file infos.'''
        tracer.info("called: base [%s] sub [%s]", base_dir, sub_dir)
        result = []
        for blob in tree.blobs:
            result.append(Git.FileInfo(base_dir, sub_dir, blob))
        for stree in tree.trees:
            sub_sub_dir = copy.deepcopy(sub_dir)
            sub_sub_dir.append(stree.name)
            result.extend(self.__get_file_infos_from_tree_rec(
                stree, base_dir, sub_sub_dir))
        return result

    def __get_file_infos_from_tree(self, tree, base_dir):
        '''Returns all the file infos recursive starting with
           the given directory.'''
        tracer.info("called: base [%s]", base_dir)
        base_dir_split = base_dir.split("/")
        ltree = self.__get_tree(tree, base_dir_split)
        return self.__get_file_infos_from_tree_rec(ltree, base_dir_split, [])

    def get_vcs_id_with_type(self, commit, dir_type):
        '''Return the vcs id from the base dir of the given dir_type.'''
        tracer.debug("called: commit [%s] directory type [%s]",
                     commit, dir_type)
        result = []
        for directory in self.__dirs[dir_type]:
            dir_split = directory.split("/")
            ltree = self.__get_tree(commit.tree, dir_split)
            result.append(ltree.hexsha)
        return ObjectCache.create_hashable(result)

    def get_file_infos(self, commit, dir_type):
        '''Return all fileinfos of the given commit and of the
           given directory type.'''
        tracer.debug("called: commit [%s] directory type [%s]",
                     commit, dir_type)
        if dir_type not in self.__dirs:
            tracer.debug("Skipping non existent directory for [%s]", dir_type)
            return []

        result = []
        for directory in self.__dirs[dir_type]:
            result.extend(self.__get_file_infos_from_tree(
                commit.tree, directory))
        return result

    def __get_blob_direct(self, base_tree, filename):
        '''Return the tree of the given file (blob).
           This does not walk down the directory structure.
           It just checks the current hierarchy.'''
        for blob in base_tree.blobs:
            if blob.name == filename:
                return blob
        return None

    def __get_blob(self, commit, base_dir, sub_path):
        '''Returns the blob from the give base directory and path.
           If the file (blob) is not available, a None is returned.
           If the directory is not available / accessable an exception
           is thrown.'''
        assert sub_path
        full_path = base_dir.split("/")
        sub_path_split = sub_path.split("/")
        if len(sub_path_split) > 1:
            full_path.extend(sub_path_split[:-1])
        ltree = self.__get_tree(commit.tree, full_path)
        return self.__get_blob_direct(ltree, sub_path_split[-1])

    def get_file_info_with_type(self, commit, file_type, filename):
        '''Returns the FileInfo object for the given filename.'''
        tracer.debug("called: commit [%s] file type [%s] filename [%s]",
                     commit, file_type, filename)
        for directory in self.__dirs[file_type]:
            tracer.debug("searching in directory [%s]", directory)
            blob = self.__get_blob(commit, directory, filename)
            if blob is not None:
                dir_split = directory.split("/")
                sub_split = os.path.dirname(filename).split("/")
                return Git.FileInfo(dir_split, sub_split, blob)
        raise RMTException(111, "file [%s] in [%s] base file not found"
                           % (filename, file_type))
