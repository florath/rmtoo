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

    def __init__(self, mods, opts, config):
        self.mods = mods
        self.opts = opts
        self.config = config

        # This is the list of all requirements sets - ordered by time.
        self.continuum_order = []
        # The continnum itself - accessable by the version.
        self.continuum = {}

        self.init_continuum()

    def continuum_add(self, cid, req_set):
        self.continuum_order.append(cid)
        self.continuum[cid] = req_set

    def continnum_latest(self):
        return self.continuum[self.continuum_order[-1]]

    def repo_access_needed(self):
        # Only if FILES:FILES is specified, there is no need to access
        # the repo.
        return self.config.reqs_spec[1]!=["FILES", "FILES"]

    def init_continuum(self):
        start_vers = self.config.reqs_spec[1][0]
        end_vers = self.config.reqs_spec[1][1]

        # Should the repo be accessed?
        if self.repo_access_needed():
            # Have a look, if there is a repo in the given directory.
            if not self.create_repo():
                raise RMTException(40, "Based on the config '%s' a "
                                   "repository is needed - but there is "
                                   "none" % self.config.reqs_spec[1])

        if start_vers!="FILES":
            # When there is FILES given as last parameter - get
            # everything from start_vers upto HEAD
            end_repo = end_vers
            if end_vers=="FILES":
                end_repo = "HEAD"
            self.create_continuum_from_git(start_vers, end_repo)
        # Maybe add also the FILES:
        if end_vers=="FILES":
            self.create_continuum_from_file()

    # This method sets up the repository and splits out the repository
    # dir from the requirements dir.
    def create_repo(self):
        directory = self.config.reqs_spec[0]
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

    # Build up the requirements tree
    # ??? NEEDED?
    def get_reqs_tree(self, tree):
        for d in self.reqs_subdir_parts:
            tree = tree[d]
        return tree

    # ???? THIS NEEDS MAJOR REWORK!!!!
    def create_base_reqset_from_git(self, start_vers, end_vers):
        assert(False)
        rs = RequirementSet(self.mods, self.opts, self.config)
        try:
            reqs_tree = self.get_reqs_tree(self.base_commit.tree)
            self.base_requirement_set.read_from_git_tree(reqs_tree)
            self.base_git_requirement_set = self.base_requirement_set
        except KeyError, ke:
            # This is thrown if the requirements are not git based.
            self.base_git_requirement_set = None

    def create_continuum_from_file(self):
        rs = RequirementSet(self.mods, self.opts, self.config)
        rs.read_from_filesystem(self.config.reqs_spec[0])
        self.continuum_add("FILES", rs)

    # CMAD write REQS list
    # ??? SHOULD NOT USED ANY MORE.
    def cmad_write_reqs_list_777(self, ofile):
        # Write out the list
        ofile.write("REQS=")
        for r in self.base_requirement_set.reqs:
            ofile.write("%s.req " % os.path.join(self.opts.directory, r))
        ofile.write("\n")

