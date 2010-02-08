#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class ReqType:
    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

        self.rt_initial_requirement = 1
        self.rt_design_decision = 2
        self.rt_requirement = 3

        self.types = [
            [ "initial requirement", self.rt_initial_requirement ],
            [ "design decision", self.rt_design_decision ],
            [ "requirement", self.rt_requirement ],
            ]

        self.type_keys = []
        for t in self.types:
            self.type_keys.append(t[0])

    def type(self):
        return "reqtag"

    def find_type(self, tag):
        for t in self.types:
            if tag==t[0]:
                return t
        return None

    def rewrite(self, req):
        # This tag (Type) is mandatory
        if "Type" not in req.req:
            print("+++ ERROR %s: does not contain the "
                  + "tag 'Type'" % req.id)
            req.mark_syntax_error()
            return
        t = req.req['Type']
        rt = self.find_type(t)
        if rt==None:
            print("+++ ERROR %s: invalid type field '%s': " \
                      "must be one of '%s'" % (req.id, t, self.type_keys))
            req.mark_syntax_error()
            return
        req.t_Type = rt[1]
        del req.req['Type']
