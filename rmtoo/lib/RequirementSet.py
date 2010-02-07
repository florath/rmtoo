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

from Requirement import Requirement

class RequirementSet:

    def __init__(self, directory):
        self.reqs = {}
        self.read(directory)

    def read(self, directory):
        files = os.listdir(directory)
        for f in files:
            m = re.match("^[IRD]\-.*\.txt$", f)
            if m==None:
                continue
            rid = f[:-4]
            fd = file(os.path.join(directory, f))
            req = Requirement(fd, rid)
            self.reqs[req.id] = req

