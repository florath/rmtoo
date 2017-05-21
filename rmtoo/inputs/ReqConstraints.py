'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Requirement Tag Constraints

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqConstraints(ReqTagGeneric):
    """Constraints Tag"""

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Constraints",
                               set([InputModuleTypes.reqtag, ]))

    def rewrite(self, _, req):
        '''This tag is optional.'''
        return self.handle_optional_tag(req)
