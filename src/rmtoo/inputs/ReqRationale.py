'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Rationale attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqRationale(ReqTagGeneric):
    """Rationale attribute"""

    def __init__(self, config):
        ReqTagGeneric.__init__(
            self, config, "Rationale",
            set([InputModuleTypes.ctstag, InputModuleTypes.reqtag,
                 InputModuleTypes.testcase]))

    def rewrite(self, _, req):
        """Rewrite: standard optional"""
        return self.handle_optional_tag(req)
