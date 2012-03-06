'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Rationale attribute
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes

class ReqRationale(ReqTagGeneric):
    tag = "Rationale"
    ltype = set([InputModuleTypes.ctstag, InputModuleTypes.reqtag])

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config)

    def rewrite(self, _, req):
        return self.handle_optional_tag(req)

