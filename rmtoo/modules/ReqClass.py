#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Requirement import Requirement

# Note:
# The class of the requirement is used in the 'Depends on' checker.
# So if something changes here - possible also there must be changed
# something.

class ReqClass:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

    def type(self):
        return "reqtag"

    def find_class(self, tag):
        for t in self.classs:
            if tag==t[0]:
                return t
        return None

    def rewrite(self, req):
        # This tag (Class) is mandatory optional
        # (which means: if it's not there, there is a default - but
        # every requirment do own one class.
        if "Class" not in req.req:
            req.t_Class = Requirement.ct_detailable
        else:
            t = req.req['Class']
            if t=="implementable":
                req.t_Class = Requirement.ct_implementable
            elif t=="detailable":
                req.t_Class = Requirement.ct_detailable
            else:
                print("+++ ERROR %s: invalid class field '%s': " 
                      "must be one of 'implementable' or 'detailable'"
                      % (req.id, t))
                return
            del req.req['Class']
