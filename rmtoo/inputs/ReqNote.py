'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Note attribute
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqNote(ReqTagGeneric):
    tag = "Note"
    ltype = set(["reqtag", "ctstag"])

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config)

    def rewrite(self, _, req):
        '''This attribute is optional.'''
        return self.handle_optional_tag(req)

