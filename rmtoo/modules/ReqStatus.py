#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Requirement import Requirement

class ReqStatus:
    tag = "Status"

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config
        
    def type(self):
        return "reqtag"

    def rewrite(self, req):
        # This tag (Status) is mandatory
        if self.tag not in req.req:
            print("+++ ERROR %s: does not contain the "
                  "tag 'Status'" % req.id)
            req.mark_syntax_error()
            return
        t = req.req[self.tag]

        if t=="open":
            req.t_Status = Requirement.st_open
        elif t=="completed":
            req.t_Status = Requirement.st_completed
        else:
            print("+++ ERROR %s: Status tag invalid '%s'" 
                  % (req.id, t))
            req.mark_syntax_error()
            return

        del req.req[self.tag]
