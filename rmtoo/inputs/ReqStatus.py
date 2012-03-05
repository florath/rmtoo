'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Status attribute
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.RequirementStatus import create_requirement_status

class ReqStatus(ReqTagGeneric):
    tag = "Status"
    ltype = set(["reqtag", ])

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config)

    def rewrite(self, rid, req):
        self.check_mandatory_tag(rid, req, 16)

        # Handle Status semantics
        t = req[self.tag].get_content()
        v = create_requirement_status(self.config, rid, t)
        del req[self.tag]
        return self.tag, v
