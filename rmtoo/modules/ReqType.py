#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Requirement import Requirement

# Note:
# The type of the requirement is used in the 'Depends on' checker.
# So if something changes here - possible also there must be changed
# something.

class ReqType:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

        # Note: this can someday move to the class 
        self.types = [
            [ "master requirement", Requirement.rt_master_requirement ],
            [ "initial requirement", Requirement.rt_initial_requirement ],
            [ "design decision", Requirement.rt_design_decision ],
            [ "requirement", Requirement.rt_requirement ],
            ]

        # Precompute once for all the rewrites
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
