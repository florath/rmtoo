#
# Completed on Tag Class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import time
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqCompletedOn(ReqTagGeneric):
    tag = "Completed on"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        status, k, v = self.handle_optional_tag(req)
        if v == None:
            return status, k, None

        try:
            # It's better to check, if the date is ok
            pt = time.strptime(v, "%Y-%m-%d")
            return True, self.tag, pt
        except ValueError, ve:
            print("+++ ERROR %s: invalid date specified (must be YYYY-MM-DD) "
                  "was '%s'" % (rid, t)) 
            return False, None, None
