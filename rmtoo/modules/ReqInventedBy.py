#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class ReqInventedBy:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config
        self.tag = "Invented by"

    def type(self):
        return "reqtag"

    def rewrite(self, req):
        # This tag (Invented by) is mandatory
        if self.tag not in req.req:
            print("+++ ERROR %s does not contain the " \
                  "tag '%s'" % (req.id, self.tag))
            req.mark_syntax_error()
            return
        t = req.req[self.tag]
        # This must be one of the inventors
        if t not in self.config.inventors:
            print("+++ ERROR %s: invalid invented by '%s'. Must be one "
                  "of the inventors '%s'" %
                  (req.id, t, self.config.inventors))
            req.mark_sematic_error()
            return
        req.t_InventedBy = t
        del req.req[self.tag]

