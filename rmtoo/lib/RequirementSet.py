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

from Requirement import Requirement

# This class handles a whole set of requirments.
# These set must be enclosed, i.e. all references must be resolvable.

class RequirementSet:

    def __init__(self, directory, mods, opts, config):
        self.reqs = {}
        self.mods = mods
        self.opts = opts
        self.config = config
        self.read(directory)

        # Dependencies can be done, if all requirements are successfully
        # read in.
        self.handle_modules_reqdeps()

        # The must no be left
        if not self.check_left_tags():
            print("+++ ERROR there were errors encountered during parsing "
                  "and checking - can't continue")
            sys.exit(1)

    def read(self, directory):
        files = os.listdir(directory)
        for f in files:
            m = re.match("^.*\.txt$", f)
            if m==None:
                continue
            rid = f[:-4]
            fd = file(os.path.join(directory, f))
            req = Requirement(fd, rid, self.mods, self.opts, self.config)
            self.reqs[req.id] = req

    def handle_modules_reqdeps(self):
        for module in self.mods.reqdeps:
            self.mods.reqdeps[module].rewrite(self)

    def check_left_tags(self):
        alls_fine = True
        for r in self.reqs:
            rr = self.reqs[r]
            if len(rr.req)>0:
                print("+++ ERROR %s: req not empty. Missing tag handers "
                      "for '%s'" % (rr.id, rr.req)) 
                alls_fine = False
        return alls_fine

    # This is a major heuristic
    # ToDo: have a very, very close look, because it might work (or
    # not) 
    def output_latex_check_master(self, directory):
        f = file(os.path.join(directory, "requirements.tex"), "r")

        included = set()
        for line in f:
            if len(line)>0 and line[-1]=='\n':
                line = line[:-1]
            m=re.match("^\\\input\{reqs/(.*)\.tex\}$", line)
            if m!=None:
                included.add(m.group(1))

        ks = set(self.reqs.keys())

        # Some very basic checks which are there and which are too
        # much... 
        if ks < included:
            print("+++ ERROR: additional reqs in document: '%s'" 
                  % (included - ks))
            return False

        if included < ks:
            print("+++ ERROR: missing reqs in document: '%s'" 
                  % (ks - included))
            return False

        if ks!=included:
            print("+++ OH NO");
            print("Set is:        %s" % included)
            print("Set should be: %s" % ks)
            return False

        return True
                
    def output_latex(self, directory):
        if not self.output_latex_check_master(directory):
            print("+++ ERROR: please fix errors first")
            return
        reqs_dir = os.path.join(directory, "reqs")
        try:
            os.makedirs(reqs_dir)
        except OSError:
            # This is not a problem: the directory already exists.
            pass
        # Initialize the graph output
        reqdepgraph = os.path.join(reqs_dir, "dependsgraph.dot")
        g = file(reqdepgraph, "w")
        g.write("digraph reqdeps {\nrankdir=BT\n")
        g.close()
        for r in self.reqs:
            self.reqs[r].output_latex(reqs_dir)
        g = file(reqdepgraph, "a")
        g.write("}")
        g.close()
