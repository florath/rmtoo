#
# Requirement Management Toolset
#
#   RequirementSet
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import re
import sys
import time
import operator
import StringIO

from Requirement import Requirement
from PyGitCompat import PyGitCompat
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.MemLogStore import MemLogStore

# This class handles a whole set of requirments.
# These set must be enclosed, i.e. all references must be resolvable.

class RequirementSet(Digraph):

    er_fine = 0
    er_error = 1

    def __init__(self, mods, opts, config):
        Digraph.__init__(self)
        self.reqs = {}
        self.mods = mods
        self.opts = opts
        # The requirement set is only (fully) usable, when everything
        # is fine.
        self.state = self.er_fine
        self.config = config
        self.logger = MemLogStore()

    def handle_modules(self):
        # Dependencies can be done, if all requirements are successfully
        # read in.
        self.handle_modules_reqdeps()
        # If there was an error, the state flag is set:
        if self.state != self.er_fine:
            print("+++ ERROR: there was a problem handling the "
                  "requirement set modules")
            return False

        # The must no be left
        if not self.check_left_tags():
            print("+++ ERROR there were errors encountered during parsing "
                  "and checking - can't continue")
            return False

        return True

    # Read the whole requirement set from files stored in the
    # filesystem (which is typically the latest version when a repo is
    # available). 
    def read_from_filesystem(self, directory):
        everythings_fine = self.read(directory)
        if not everythings_fine:
            print("+++ ERROR: There were errors in the requirments")
            return False

        return self.handle_modules()

    def read(self, directory):
        everythings_fine = True
        files = os.listdir(directory)
        for f in files:
            m = re.match("^.*\.req$", f)
            if m==None:
                continue
            rid = f[:-4]
            fd = file(os.path.join(directory, f))
            req = Requirement(fd, rid, self.mods, self.opts, self.config)
            if req.ok():
                # Store in the map, so that it is easy to access the
                # node by id.
                self.reqs[req.id] = req
                # Also store it in the digraph's node list for simple
                # access to the digraph algorithms.
                self.nodes.append(req)
            else:
                print("+++ ERROR %s: could not be parsed" % req.id)
                everythings_fine = False
        self.ts = time.time()
        return everythings_fine

    def read_from_git_tree(self, tree):
        assert(False)

        # Rework needed:
        # Read in everything from the repo
        # All (error / log) output should go to a local log-buffer.

        everythings_fine = True
        files = PyGitCompat.Tree.items(tree)
        for f in files:
            m = re.match("^.*\.req$", PyGitCompat.Tree.iter_name(f))
            if m==None:
                continue
            rid = PyGitCompat.Tree.iter_name(f)[:-4]
            req = Requirement(StringIO.StringIO(PyGitCompat.Tree.iter_data(f)), 
                              rid, self.mods, self.opts, self.config)
            if req.ok():
                # Store in the map, so that it is easy to access the
                # node by id.
                self.reqs[req.id] = req
                # Also store it in the digraph's node list for simple
                # access to the digraph algorithms.
                self.nodes.append(req)
            else:
                print("+++ ERROR %s: could not be parsed" % req.id)
                everythings_fine = False

        if not everythings_fine:
            return False
        return self.handle_modules()


    # This is mostly the same functionallaty of similar method of the
    # class Requirement.
    # ToDo: Unify this!
    def handle_modules_reqdeps(self):
        for module in self.mods.reqdeps_sorted:
            state = module.rewrite(self)
            if state==False:
                # Some sematic error occured.
                self.state = self.er_error
                # Do not continue - return immediately, because some
                # algorithms rely on the correct run from others.
                return

    def check_left_tags(self):
        alls_fine = True
        for r in self.reqs:
            rr = self.reqs[r]
            if len(rr.req)>0:
                print("+++ ERROR %s: req not empty. Missing tag handers "
                      "for '%s'" % (rr.id, rr.req)) 
                alls_fine = False
        return alls_fine

    # Return the timestamp of the whole Requirment Set.
    # This is the current time for FILES and the checkin point of time
    # for files from the repo.
    def timestamp(self):
        return self.ts

    # Return the number of requirments in this RequirementSet.  This
    # is e.g. needed for statistics.
    def reqs_count(self):
        return len(self.reqs)
