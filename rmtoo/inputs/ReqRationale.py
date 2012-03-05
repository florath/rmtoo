'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Rationale attribute
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqRationale(ReqTagGeneric):
    tag = "Rationale"
    ltype = set(["reqtag", "ctstag"])

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config)

    def rewrite(self, _, req):
        return self.handle_optional_tag(req)

