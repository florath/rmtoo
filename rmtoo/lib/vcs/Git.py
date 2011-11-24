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

from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.vcs.Interface import Interface
from rmtoo.lib.vcs.VCSException import VCSException
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.RMTException import RMTException

class Git(Interface):
    
    def __init__(self, config):
        tracer.info("called")
        cfg = Cfg(config)
        self.start_vers = cfg.get_value("start_vers")
        self.end_vers = cfg.get_value("end_vers")
        # When the directory is not absolute, convert it to an
        # absolute path that it can be compared to the outcome of the
        # git.Repo. 
        self.requirements_dir = \
            self.internal_abs_path(cfg.get_value("requirements_dir"))
        self.topics_dir = \
            self.internal_abs_path(cfg.get_value("topics_dir"))
        self.topic_root_node = cfg.get_value("topic_root_node")

        tracer.debug("start version [%s] end version [%s] "
                     "requirements dir [%s] topics dir [%s] "
                     "topic root node [%s]" 
                     % (self.start_vers, self.end_vers,
                        self.requirements_dir, self.topics_dir,
                        self.topic_root_node))
        
        self.internal_setup_repo()
        
    @staticmethod
    def internal_abs_path(directory):
        '''Convert the given directory path into an absolute path.'''
        if not os.path.isabs(directory):
            return os.path.abspath(directory)
        return directory
    
    def internal_setup_repo(self):
        '''Sets up the repository.
           This also checks, if the requirements and topics are in the
           same directory.'''
        
        self.repo = git.Repo(self.requirements_dir)
        self.repo_base_dir = self.repo.git_dir[:-4]
        len_repo_base_dir = len(self.repo_base_dir)

        # Check that the topic directory has the same base.
        topic_repo = git.Repo(self.topics_dir)
        if self.repo_base_dir != topic_repo.git_dir[:-4]:
            raise RMTException(101, 
                "requirements dir [%s] and topic dir [%s] not " \
                "in the same repository." \
                % (self.requirements_dir, self.topics_dir))
        
        if not self.requirements_dir.startswith(self.repo_base_dir):
            raise RMTException(28, "Cannot split up the given "
                                   "requirements directory name")
        self.requirements_subdir = self.requirements_dir[len_repo_base_dir:]
                
        if not self.topics_dir.startswith(self.repo_base_dir):
            raise RMTException(102, "Cannot split up the given "
                                    "topics directory name")
        self.topics_subdir = self.topics_dir[len_repo_base_dir:]
        
        tracer.debug("requirements subdir [%s] topic subdir [%s]" %
                     (self.requirements_subdir, self.topics_subdir))

    def internal_read_file(self, path, blob, creator):
        '''Read file from given blob'''
        tracer.debug("called: path [%s] name [%s]" % (path, blob.name))
        if not creator.check_filename(blob.name):
            tracer.debug("ignoring file [%s]" % blob.name)
            return
        creator.create(blob)
        
        assert False

    def internal_read_tree(self, path, tree, creator):
        '''Read the tree.  The tree has the name 'path'.'''
        tracer.debug("path [%s]" % path)
        for entry in tree.blobs:
            self.internal_read_file(path, entry, creator)
        for entry in tree.trees:
            lpath = path
            lpath.append(entry.name)
            self.internal_read_tree(lpath, entry, creator)

    def internal_read_commit(self, commit):
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
        # Do the whole history.
        for commit in self.repo.iter_commits(
                        self.start_vers + ".." + self.end_vers):
            self.internal_read_commit(commit)


        assert False