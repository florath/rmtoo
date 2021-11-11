'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Status attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.RequirementStatus import create_requirement_status
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqStatus(ReqTagGeneric):
    """Status attribute"""

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Status",
                               set([InputModuleTypes.reqtag, ]))

    def rewrite(self, rid, req):
        """Mandatory status attribute"""
        self.check_mandatory_tag(rid, req, 16)

        # Handle Status semantics
        tag = req[self.get_tag()].get_content()
        val = create_requirement_status(self.get_config(), rid, tag)
        del req[self.get_tag()]
        return self.get_tag(), val
