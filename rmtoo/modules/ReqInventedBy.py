#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqInventedBy(ReqTagGeneric):
    tag = "Invented by"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        # This tag (Invented by) is mandatory
        if not self.check_mandatory_tag(rid, req):
            return False, None, None

        t = req[self.tag]
        # This must be one of the inventors
        if t not in self.config.inventors:
            print("+++ ERROR %s: invalid invented by '%s'. Must be one "
                  "of the inventors '%s'" %
                  (rid, t, self.config.inventors))
            return False, None, None

        del req[self.tag]
        return True, self.tag, t
