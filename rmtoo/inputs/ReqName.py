'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Name attribute
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqName(ReqTagGeneric):
    tag = "Name"
    ltype = set(["reqtag", "ctstag"])

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config)

    def rewrite(self, rid, req):
        # This tag (Name) is mandatory
        self.check_mandatory_tag(rid, req, 37)

        t = req[self.tag]
        del req[self.tag]
        return self.tag, t
