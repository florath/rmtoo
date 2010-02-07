#
# Requirement Management Toolset
#  class ReqName
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class ReqName:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

    def type(self):
        return "reqtag"

    def rewrite(self, req):
        # This tag (Name) is mandatory
        if "Name" not in req.req:
            print("+++ ERROR: requirement '%s' does not contain the "
                  + "tag 'Name'" % req.id)
            req.mark_syntax_error()
            return
        req.t_Name = req.req['Name']
        del req.req['Name']
