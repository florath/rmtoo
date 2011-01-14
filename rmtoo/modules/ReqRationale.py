#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqRationale(ReqTagGeneric):
    tag = "Rationale"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        OT, O2 = self.handle_optional_tag(req)

        print("===== RAT %s ====" % OT)
        if O2!=None:
            print("===== RAT2 %s ====" % O2.get_content())

        return self.handle_optional_tag(req)
    
