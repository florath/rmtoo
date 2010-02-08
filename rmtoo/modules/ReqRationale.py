#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class ReqRationale:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

    def type(self):
        return "reqtag"

    def rewrite(self, req):
        # This tag (Rationale) is mandatory
        if "Rationale" not in req.req:
            req.t_Rationale = None
            return
        
        req.t_Rationale = req.req['Rationale']
        del req.req['Rationale']
