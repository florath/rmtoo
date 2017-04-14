'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Requirement class itself
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import operator

from rmtoo.lib.BaseRMObject import BaseRMObject
from rmtoo.lib.logging import tracer
from rmtoo.lib.FuncCall import FuncCall
from rmtoo.lib.InputModuleTypes import InputModuleTypes

import sys
reload(sys)
# pylint: disable=E1101
sys.setdefaultencoding('utf-8')

class Requirement(BaseRMObject):
    '''Class which holds one requirement.'''

    # Requirement Type
    # Each requirement has exactly one type.
    # The class ReqType sets this from the contents of the file.
    # Note: There can only be one (master requirement)
    rt_master_requirement = 1
    # Initial requirement is deprecated
    rt_initial_requirement = 2
    rt_design_decision = 3
    rt_requirement = 4

    @staticmethod
    def get_type_as_str(rtype):
        if rtype == Requirement.rt_master_requirement:
            return "requirement"
        if rtype == Requirement.rt_initial_requirement:
            return "requirement"
        if rtype == Requirement.rt_design_decision:
            return "design decision"
        if rtype == Requirement.rt_requirement:
            return "requirement"
        assert False

    def __init__(self, content, rid, file_path, mods, config):
        BaseRMObject.__init__(self, InputModuleTypes.reqtag,
                              content, rid, mods,
                              config, "requirements", file_path)

    def get_prio(self):
        return self.values["Priority"]

    def __str__(self):
        '''Return the name/id of the requirement.'''
        return "Requirement [%s]" % self.get_id()

    def __repr__(self):
        return self.__str__()

    def get_status(self):
        return self.values["Status"]

    def get_topic(self):
        return self.values["Topic"]

    def get_efe_or_0(self):
        '''Returns the EfE units or 0 if not available.'''
        efe = self.get_value("Effort estimation")
        if efe == None:
            return 0
        return efe

    def is_implementable(self):
        return self.values["Class"].is_implementable()
