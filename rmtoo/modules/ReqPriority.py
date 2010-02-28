#
# Requirement Tag Priority
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqPriority(ReqTagGeneric):
    tag = "Priority"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        # This tag is mandatory - but might be empty
        if self.tag not in req:
            return True, self.tag, None
        # Compute the priority.  This is done by adding the simple
        # priorities. 
        t = req[self.tag]
        lop = t.split()
        # The (computed) priority
        priority = 0.0
        # A list to check if each stakeholder votes maximal one time.
        priority_done = []
        for l in lop:
            p = l.split(":", 1)
            if len(p)!=2:
                print("+++ ERROR %s: faulty priority declaration '%s'"
                      % (rid, l))
                return False, None, None
            # p[0] is the stakeholder
            # p[1] is the given priority
            if p[0] not in self.config.stakeholders:
                print("+++ ERROR %s: stakeholder '%s' not known"
                      % (rid, p[0]))
                return False, None, None
            if p[0] in priority_done:
                print("+++ ERROR %s: stakeholder '%s' voted more than once"
                      % (rid, p[0]))
                return
            # ToDo: Check if the priority is in some interval [0, 10]
            # (and if not: reject it)
            priority += float(p[1])
            priority_done.append(p[1])

        del req[self.tag]
        return True, self.tag, priority
