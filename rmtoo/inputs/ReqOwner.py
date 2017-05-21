'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Owner attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqOwner(ReqTagGeneric):
    """Owner Tag"""

    def __init__(self, config):
        ReqTagGeneric.__init__(
            self, config, "Owner",
            set([InputModuleTypes.ctstag, InputModuleTypes.reqtag,
                 InputModuleTypes.testcase]))

    def rewrite(self, rid, req):
        """This tag (Owner) is mandatory"""
        self.check_mandatory_tag(rid, req, 10)

        # Also the owner must be in the list of stakeholders
        tcontent = req[self.get_tag()].get_content()
        # flonatel is always a valid stakeholder - because the
        # standard constraints are introduced by them.
        stakeholders = self.get_config().get_value('requirements.stakeholders')
        if tcontent != 'flonatel' and tcontent not in stakeholders:
            raise RMTException(11, "%s: invalid owner '%s'. Must be one "
                               "of the stakeholder '%s'" %
                               (rid, tcontent, stakeholders))
        # Copy and delete the original
        del req[self.get_tag()]
        return self.get_tag(), tcontent
