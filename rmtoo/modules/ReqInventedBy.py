#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.RMTException import RMTException

class ReqInventedBy(ReqTagGeneric):
    tag = "Invented by"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        # This tag (Invented by) is mandatory
        self.check_mandatory_tag(rid, req, 5)

        t = req[self.tag].get_content()
        # This must be one of the inventors
        if t not in self.config.inventors:
            raise RMTException(6, "Invalid invented by '%s'. Must be one "
                               "of the inventors '%s'" %
                               (t, self.config.inventors), rid)

        del req[self.tag]
        return self.tag, t
