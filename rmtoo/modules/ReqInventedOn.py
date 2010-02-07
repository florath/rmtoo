#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import time

class ReqInventedOn:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config
        self.tag = "Invented on"
    
    def type(self):
        return "reqtag"

    def rewrite(self, req):
        # This tag (Invented on) is mandatory
        if self.tag not in req.req:
            print("+++ ERROR: requirement '%s' does not contain the " \
                  "tag '%s'" % (req.id, self.tag))
            req.mark_syntax_error()
            return
        t = req.req[self.tag]
        try:
            # It's better to check, if the date is ok
            pt = time.strptime(t, "%Y-%m-%d")
            req.t_InventedOn = pt
            del req.req[self.tag]
        except ValueError, ve:
            print("+++ ERROR %s: invalid date specified (must be YYYY-MM-DD) "
                  "was '%s'" % (req.id, t)) 
            req.mark_syntax_error()
            
