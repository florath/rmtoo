'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Requirement class itself

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from builtins import str
import operator
import hashlib
from enum import Enum

from rmtoo.lib.Encoding import Encoding
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.BaseRMObject import BaseRMObject
from rmtoo.lib.logging import tracer
from rmtoo.lib.FuncCall import FuncCall
from rmtoo.lib.InputModuleTypes import InputModuleTypes


# pylint: disable=too-few-public-methods
class RequirementType(Enum):
    """Each requirement has exactly one type.

    The class ReqType sets this from the contents of the file.
    Note: There can only be one (master requirement)
    """
    master_requirement = 1
    # Initial requirement is deprecated
    initial_requirement = 2
    design_decision = 3
    requirement = 4

    def as_string(self):
        """Return RequirementType as string"""
        # The number are used because some old python 3.4 bail out with
        # 'RequirementType' object has no attribute 'master_requirement'
        if self.value == 1:  # self.master_requirement:
            return "requirement"
        if self.value == 2:  # self.initial_requirement:
            return "requirement"
        if self.value == 3:  # self.design_decision:
            return "design decision"
        if self.value == 4:  # self.requirement:
            return "requirement"
        assert False


class Requirement(Digraph.Node, BaseRMObject):
    """Class representing a requirement"""

    def execute(self, executor, func_prefix):
        '''Execute the parts which are needed for Requirement.'''
        tracer.debug("Called: name [%s]", self.name)
        FuncCall.pcall(executor, func_prefix + "requirement", self)
        tracer.debug("Finished: name [%s]", self.name)

    # pylint: disable=too-many-arguments
    def __init__(self, content, rid, file_path, mods, config):
        self._hash = None
        Encoding.check_unicode(content)
        Encoding.check_unicode(rid)
        Digraph.Node.__init__(self, rid)
        BaseRMObject.__init__(self, InputModuleTypes.reqtag,
                              content, rid, mods,
                              config, u"requirements", file_path)

    def get_hash(self):
        """Return sha256 hash of description and name"""
        if self._hash is None:
            s = str(self.get_value("Name"))
            s += str(self.get_value("Description"))
            try:
                s += self.get_value("VerifMethod")
            except KeyError:
                pass
            us = s.encode('utf-8')
            self._hash = hashlib.sha256(us).hexdigest()
        return self._hash[0:8]

    def get_prio(self):
        """Get priority of requirement"""
        return self.values["Priority"]

    def __str__(self):
        '''Return the name/id of the requirement.'''
        return "Requirement [%s]" % self.get_id()

    def __repr__(self):
        return self.__str__()

    def get_status(self):
        """Get the requirement's status"""
        status = self.values["Status"]
        if status.rid_hash is None:
            status.rid_hash = self.get_hash()
        return status

    def get_topic(self):
        """Get the requirement's topic"""
        return self.values["Topic"]

    def get_efe_or_0(self):
        '''Returns the EfE units or 0 if not available.'''
        efe = self.get_value("Effort estimation")
        if efe is None:
            return 0
        return efe

    def is_implementable(self):
        """Get if the requirement is implementable"""
        return self.values["Class"].is_implementable()

    def write_analytics_result(self, mstderr):
        '''Write out the analytics results.'''
        for k, val in sorted(self.analytics.items(),
                             key=operator.itemgetter(0)):
            if val[0] < 0:
                mstderr.write("+++ Error:Analytics:%s:%s:result is '%+3d'\n"
                              % (k, self.get_id(), val[0]))
                for line in val[1]:
                    mstderr.write("+++ Error:Analytics:%s:%s:%s\n" %
                                  (k, self.get_id(), line))
