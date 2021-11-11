'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Type attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.Requirement import RequirementType
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes

# Note:
# The type of the requirement is used in the 'Depends on' checker.
# So if something changes here - possible also there must be changed
# something.


class ReqType(ReqTagGeneric):
    """Type attribute"""
    types = [
        ["master requirement", RequirementType.master_requirement],
        ["initial requirement", RequirementType.initial_requirement],
        ["design decision", RequirementType.design_decision],
        ["requirement", RequirementType.requirement],
    ]

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Type",
                               set([InputModuleTypes.reqtag, ]))

        # Precompute once for all the rewrites
        self.type_keys = []
        for ltype in self.types:
            self.type_keys.append(ltype[0])

    def find_type(self, tag):
        """Find a type fromt the above list."""
        for ltype in self.types:
            if tag == ltype[0]:
                return ltype
        return None

    def rewrite(self, rid, req):
        """This tag (Type) is mandatory"""
        self.check_mandatory_tag(rid, req, 18)

        tag = req[self.get_tag()].get_content()
        req_tag = self.find_type(tag)
        if req_tag is None:
            raise RMTException(19, "%s: invalid type field '%s': "
                               "must be one of '%s'" %
                               (rid, tag, self.type_keys))

        del req[self.get_tag()]
        return self.get_tag(), req_tag[1]
