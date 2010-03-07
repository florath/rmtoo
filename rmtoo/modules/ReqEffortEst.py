#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

#
# The 'Effort estimation' must be one of
#   0, 1, 2, 3, 5, 8, 13, 21
#

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqEffortEst(ReqTagGeneric):
    tag = "Effort estimation"
    valid_values = [0, 1, 2, 3, 5, 8, 13, 21]

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
    	# This is optional
        state, tag, value = self.handle_optional_tag(req)
        if value==None:
            return state, tag, value

        v = int(value)

        if v not in self.valid_values:
            print("+++ ERROR %s: effort estimation must be one of %s"
                  % self.valid_values)
            return False, None, None

        return True, tag, v

            
