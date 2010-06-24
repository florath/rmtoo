#
# ReqsContinuum hold all the different requirement sets from the
# past. 
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import git
import os

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.PyGitCompat import PyGitCompat

#
# The Continuum holds all the RequirementSets from the history,
# i.e. all which are known to git.  It also holds the current
# available (possible not checked in) pointer to the appropriate files
# in the file system.
#

class ReqsContinuum:

    commit_bulk_size = 10

    def __init__(self, directory, mods, opts, config):
        self.mods = mods
        self.opts = opts
        self.config = config
        self.directory = directory

        # Check for command line parameters.
        self.handle_clp(opts.base_version)
        # At this point, 
        #  self.use_files is True, iff local files should be used

        # Check, if there is a git repo available
        self.create_repo(directory)
        # At this point, 
        #  self.repo_available is True, iff a repo is available
        # The repo itself can be found in self.repo.

        # Check if the combination of the (non)existance of a repo and
        # the command line paramters make any sense.
        if self.use_files==False and self.repo_available==False:
            raise RMTException(29, "No FILES specified but there "
                               "is no git repository available for "
                               "the requirements")            

        # ... and repository.
        # Even if FILES is specified, for handling the tree
        # (history and statistics) some git version is needed.
        if self.repo_available:
            # When the files should be used - HEAD will be used for
            # git repository (if available)
            vers = opts.base_version
            if self.use_files:
                vers = "HEAD"
            self.set_base_commit(vers)
        else:
            # If there is no repo, the FILES are used
            self.use_files = True

        # Depending on the set of input to work on, prepare the files...
        if self.use_files:
            self.create_base_reqset_from_files()
        else:
            self.create_base_reqset_from_git()

    # Depending on the command line parameter and if there is a git
    # available, the handling of commands look different.
    def handle_clp(self, bv):
        self.use_files = (bv=="FILES")

    # This method sets up the repository and splits out the repository
    # dir from the requirements dir.
    def create_repo(self, directory):
        # When the directory is not absolute, convert it to an
        # absolute path that it can be comparted to the outcome of the
        # git.Repo. 
        if not os.path.isabs(directory):
            directory = os.path.abspath(directory)

        try:
            self.repo = git.Repo(directory)
            self.repo_available = True
            rpath = PyGitCompat.Repo.git_dir(self.repo)

            if not directory.startswith(rpath):
                raise RMTException(28, "Cannot split up the given "
                                   "directory name")
        
            self.reqs_subdir = directory[len(rpath):]
            self.reqs_subdir_parts = self.reqs_subdir.split("/")
        except git.errors.InvalidGitRepositoryError, igre:
            # There is no git repo here - therefore nothing to do.
            self.repo = None
            self.repo_available = False

    # Depending on the vers set the base commit (i.e. the base which
    # to work with during the livetime of the continuum object.)
    def set_base_commit(self, vers):
        self.base_commit = self.repo.commit(vers)

    # Build up the requirements tree
    def get_reqs_tree(self, tree):
        for d in self.reqs_subdir_parts:
            tree = tree[d]
        return tree

    def create_base_reqset_from_git(self):
        self.base_requirement_set = \
            RequirementSet(self.mods, self.opts, self.config)
        try:
            reqs_tree = self.get_reqs_tree(self.base_commit.tree)
            self.base_requirement_set.read_from_git_tree(reqs_tree)
            self.base_git_requirement_set = self.base_requirement_set
        except KeyError, ke:
            # This is thrown if the requirements are not git based.
            self.base_git_requirement_set = None

    def create_base_reqset_from_files(self):
        self.base_requirement_set = \
            RequirementSet(self.mods, self.opts, self.config)
        self.base_requirement_set.read_from_filesystem(self.directory)

    # CMAD write REQS list
    def cmad_write_reqs_list(self, ofile):
        # Write out the list
        ofile.write("REQS=")
        for r in self.base_requirement_set.reqs:
            ofile.write("%s.req " % os.path.join(self.opts.directory, r))
        ofile.write("\n")

