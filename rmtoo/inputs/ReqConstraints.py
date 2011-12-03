#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Requirement Tag Constraints
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqConstraints(ReqTagGeneric):
    tag = "Constraints"
    ltype = set(["reqtag", ])

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config)

    def rewrite(self, rid, req):
    	# This is optional
        return self.handle_optional_tag(req)

