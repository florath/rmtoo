#
# Version Control System
#
#  This will be (in future) the interface for possible multiple
#  different version control systems.
#
#  Currently this defines the generic interface and the implementation
#  for git.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import sys

# To find the correct version of git-python (and friends) [the rmtoo
# local version must be used], the sys.path is scanned and when a
# sp/rmtoo/contrib is found, this is included (prepended) to sys.path.
# This can be removed once the git-pyhton is removed.
# (Calling this durint the main does not help - because this might
# already been loaded.) 
for sp in sys.path:
    rc = os.path.join(sp, 'rmtoo/contrib')
    if os.path.exists(rc):
        sys.path.insert(0, rc)
        break
import git

import re
import StringIO

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.MemLogStore import MemLog
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.Requirement import Requirement

class VCSException(Exception):
    pass

class VCSGit:

    def __init__(self, directory):
        self.repo = git.Repo(directory)
        self.set_directories(directory)

    # Some variables are needed to access the files themself.
    # Especially the different subdirs where the requirements can be
    # found. 
    def set_directories(self, directory):
        self.repo_base_dir = self.repo.git_dir[:-4]
        
        if not directory.startswith(self.repo_base_dir):
            raise RMTException(28, "Cannot split up the given "
                                   "directory name")

        self.reqs_subdir = directory[len(self.repo_base_dir):]
        # NEEDED?
        #self.reqs_subdir_parts = self.reqs_subdir.split("/")

    # This reads in the history of all sequirments sets including
    # start_vers end end_vers.
    # Each new requirement set is added to the given object
    def read_history(self, continuum_storage, start_vers, end_vers):
        # Do the whole history.
        for ci in self.repo.iter_commits(start_vers + ".." + end_vers):
            self.rh_one_commit(continuum_storage, ci)
        # Do the start seperatly
        self.rh_one_commit(continuum_storage, self.repo.commit(start_vers))

    def rh_one_commit(self, cs, ci):
        rs = RequirementSet(cs.mods, cs.opts, cs.config)
        rs.set_version_id(ci.hexsha)
        try:
            files = ci.tree[self.reqs_subdir].blobs
        except KeyError, ke:
            # This means, that at this point of time the directory was
            # not available.
            rs.log(46, MemLog.error, "Path '%s' not available" %
                   self.reqs_subdir)
            rs.not_usable()
            return

        # Read in all the requirments for this requirements set. 
        self.rh_one_rs(cs, rs, files)
        # Adapt the timestamp to the authored_date
        rs.ts = ci.authored_date
        # Add this requirements set to the requirements continuum.
        cs.continuum_add(ci.hexsha, rs)

    def rh_one_rs(self, cs, rs, files):
        for f in files:
            # Only files which end in .req are taken
            m = re.match("^.*\.req$", f.name)
            if m==None:
                continue

            rid = f.name[:-4]
            req = Requirement(f.data_stream, rid, rs,
                              cs.mods, cs.opts, cs.config)
            if req.ok():
                rs.add_req(req)
            else:
                rs.not_usable()
        rs.handle_modules()
        # XXX IS here some return value needed?
                   
class VersionControlSystem:
    
    # This is the the 'virtual' constructor:
    # It will check all available VCS systems and returns the correct
    # one. 
    # Note: At the moment only the VCSGit is available.
    @staticmethod
    def create(directory):
        return VCSGit(directory)
