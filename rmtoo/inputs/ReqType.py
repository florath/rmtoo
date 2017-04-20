'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Type attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes

# Note:
# The type of the requirement is used in the 'Depends on' checker.
# So if something changes here - possible also there must be changed
# something.


class ReqType(ReqTagGeneric):
    types = [
        ["master requirement", Requirement.rt_master_requirement],
        ["initial requirement", Requirement.rt_initial_requirement],
        ["design decision", Requirement.rt_design_decision],
        ["requirement", Requirement.rt_requirement],
        ]

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Type",
                               set([InputModuleTypes.reqtag, ]))

        # Precompute once for all the rewrites
        self.type_keys = []
        for t in self.types:
            self.type_keys.append(t[0])

    # Find a type fromt the above list.
    def find_type(self, tag):
        for t in self.types:
            if tag == t[0]:
                return t
        return None

    def rewrite(self, rid, req):
        # This tag (Type) is mandatory
        self.check_mandatory_tag(rid, req, 18)

        t = req[self.get_tag()].get_content()
        rt = self.find_type(t)
        if rt is None:
            raise RMTException(19, "%s: invalid type field '%s': "
                               "must be one of '%s'" %
                               (rid, t, self.type_keys))

        del req[self.get_tag()]
        return self.get_tag(), rt[1]
