'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Expected Result attribute

 (c) 2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqExpectedResult(ReqTagGeneric):
    """Expected Result tag implementation"""

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Expected Result",
                               set([InputModuleTypes.testcase]))

    def rewrite(self, rid, req):
        """This tag (Expected Result) is mandatory"""
        self.check_mandatory_tag(rid, req, 116)
        return self.get_and_remove(req)
