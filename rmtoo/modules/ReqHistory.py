#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class ReqHistory:
    tag = "History"

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config
        
    def type(self):
        return "reqtag"

    def rewrite(self, req):
    	# This is optional
        if self.tag in req.req:
            req.t_History = req.req[self.tag]
            del req.req[self.tag]
