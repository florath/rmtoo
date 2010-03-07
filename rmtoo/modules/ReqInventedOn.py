#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import time
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.RMTException import RMTException

class ReqInventedOn(ReqTagGeneric):
    tag = "Invented on"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        # This tag (Invented on) is mandatory
        self.check_mandatory_tag(rid, req, 7)

        t = req[self.tag]
        try:
            # It's better to check, if the date is ok
            pt = time.strptime(t, "%Y-%m-%d")
            del req[self.tag]
            return self.tag, pt
        except ValueError, ve:
            raise RMTException(8, "%s: invalid date specified (must be "
                               "YYYY-MM-DD) was '%s'" % (rid, t))

            
