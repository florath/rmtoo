#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class ReqOwner:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

    def type(self):
        return "reqtag"

    def rewrite(self, req):
        # This tag (Owner) is mandatory
        if "Owner" not in req.req:
            print("+++ ERROR %s: does not contain the "
                  "tag 'Owner'" % req.id)
            req.mark_syntax_error()
            return
        # Also the owner must be in the list of stakeholders
        t = req.req['Owner']
        if t not in self.config.stakeholders:
            print("+++ ERROR %s: invalid owner '%s'. Must be one "
                  "of the stakeholder '%s'" %
                  (req.id, t, self.config.stakeholders))
            req.mark_sematic_error()
            return
        # Copy and delete the original
        req.t_Owner = t
        del req.req['Owner']
