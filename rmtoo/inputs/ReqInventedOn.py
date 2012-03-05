'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Invented on attribute
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.DateUtils import parse_date

class ReqInventedOn(ReqTagGeneric):
    tag = "Invented on"
    ltype = set(["reqtag", "ctstag"])

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config)

    def rewrite(self, rid, req):
        # This tag (Invented on) is mandatory
        self.check_mandatory_tag(rid, req, 7)

        t = req[self.tag]
        pt = parse_date(rid, t.get_content())
        del req[self.tag]
        return self.tag, pt
