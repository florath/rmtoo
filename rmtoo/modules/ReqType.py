#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

# Note:
# The type of the requirement is used in the 'Depends on' checker.
# So if something changes here - possible also there must be changed
# something.

class ReqType(ReqTagGeneric):
    tag = "Type"

    types = [
        [ "master requirement", Requirement.rt_master_requirement ],
        [ "initial requirement", Requirement.rt_initial_requirement ],
        [ "design decision", Requirement.rt_design_decision ],
        [ "requirement", Requirement.rt_requirement ],
        ]

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

        # Precompute once for all the rewrites
        self.type_keys = []
        for t in self.types:
            self.type_keys.append(t[0])

    # Find a type fromt the above list.
    def find_type(self, tag):
        for t in self.types:
            if tag==t[0]:
                return t
        return None

    def rewrite(self, rid, req):
        # This tag (Type) is mandatory
        if not self.check_mandatory_tag(rid, req):
            return False, None, None

        t = req[self.tag]
        rt = self.find_type(t)
        if rt==None:
            print("+++ ERROR %s: invalid type field '%s': " \
                      "must be one of '%s'" % (rid, t, self.type_keys))
            return False, None, None

        del req[self.tag]
        return True, self.tag, rt[1]
