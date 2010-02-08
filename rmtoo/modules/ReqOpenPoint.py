#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class ReqOpenPoint:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

    def type(self):
        return "reqtag"

    def rewrite(self, req):
        # This tag (Open Point) is optional
        if "Open Point" in req.req:
            req.t_OpenPoint = req.req['Open Point']
            del req.req['Open Point']
        
