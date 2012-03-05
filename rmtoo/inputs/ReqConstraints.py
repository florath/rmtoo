'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Requirement Tag Constraints
   
 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqConstraints(ReqTagGeneric):
    tag = "Constraints"
    ltype = set(["reqtag", ])

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config)

    def rewrite(self, _, req):
        '''This tag is optional.'''
        return self.handle_optional_tag(req)
