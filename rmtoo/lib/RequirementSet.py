#
# Requirement Management Toolset
#  class RequirementSet
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import re
import sys

from Requirement import Requirement

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
            m = re.match("^[IRD]\-.*\.txt$", f)
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


