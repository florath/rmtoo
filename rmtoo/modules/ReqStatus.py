#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqStatus(ReqTagGeneric):
    tag = "Status"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        if not self.check_mandatory_tag(rid, req):
            return False, None, None

        # Handle Status semantics
        t = req[self.tag]
        if t=="open":
            v = Requirement.st_open
        elif t=="completed":
            v = Requirement.st_completed
        else:
            print("+++ ERROR %s: Status tag invalid '%s'" 
                  % (rid, t))
            return

        del req[self.tag]
        return True, self.tag, v
