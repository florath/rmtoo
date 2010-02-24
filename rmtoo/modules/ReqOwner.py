#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqOwner(ReqTagGeneric):
    tag = "Owner"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        # This tag (Owner) is mandatory
        if not self.check_mandatory_tag(rid, req):
            return False, None, None

        # Also the owner must be in the list of stakeholders
        t = req[self.tag]
        if t not in self.config.stakeholders:
            print("+++ ERROR %s: invalid owner '%s'. Must be one "
                  "of the stakeholder '%s'" %
                  (rid, t, self.config.stakeholders))
            return
        # Copy and delete the original
        del req['Owner']
        return True, self.tag, t
