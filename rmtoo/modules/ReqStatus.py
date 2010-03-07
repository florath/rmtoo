#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.RMTException import RMTException

class ReqStatus(ReqTagGeneric):
    tag = "Status"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        self.check_mandatory_tag(rid, req, 16)

        # Handle Status semantics
        t = req[self.tag]
        if t=="not done":
            v = Requirement.st_not_done
        elif t=="finished":
            v = Requirement.st_finished
        else:
            raise RMTException(17, "%s: Status tag invalid '%s'" 
                               % (rid, t))

        del req[self.tag]
        return self.tag, v
