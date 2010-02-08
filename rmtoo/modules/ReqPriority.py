#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class ReqPriority:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config
        self.tag = "Priority"

    def type(self):
        return "reqtag"

    def rewrite(self, req):
        # This tag is mandatory - but might be empty
        if self.tag not in req.req:
            req.t_Priority = 0.0
            return
        # Compute the priority.  This is done by adding the simple
        # priorities. 
        t = req.req[self.tag]
        lop = t.split()
        # The (computed) priority
        priority = 0.0
        # A list to check if each stakeholder votes maximal one time.
        priority_done = []
        for l in lop:
            p = l.split(":", 1)
            if len(p)!=2:
                print("+++ ERROR %s: faulty priority declaration '%s'"
                      % (req.rid, l))
                req.mark_syntax_error()
                return
            # p[0] is the stakeholder
            # p[1] is the given priority
            if p[0] in priority_done:
                print("+++ ERROR %s: stakeholder '%s' voted more than once"
                      % (req.rid, p[0]))
                req.mark_syntax_error()
                return
            priority += float(p[1])
        req.t_Priority = priority
        del req.req[self.tag]
