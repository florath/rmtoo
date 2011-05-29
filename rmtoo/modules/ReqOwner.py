#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Requirement Management Toolset
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqOwner(ReqTagGeneric):
    tag = "Owner"
    ltype = set(["reqtag", "ctstag"])

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        # This tag (Owner) is mandatory
        self.check_mandatory_tag(rid, req, 10)

        # Also the owner must be in the list of stakeholders
        t = req[self.tag].get_content()
        # flonatel is always a valid stakeholder - because the
        # standard constraints are introduced by them.
        if t!='flonatel' and t not in self.config.stakeholders:
            raise RMTException(11, "%s: invalid owner '%s'. Must be one "
                               "of the stakeholder '%s'" %
                               (rid, t, self.config.stakeholders))
        # Copy and delete the original
        del req[self.tag]
        return self.tag, t
