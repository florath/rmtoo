#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Requirement Tag Priority
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

# A priority is a number between 0 and 1.
# The stakeholders can name a number between 0 and 10 (only full
# numbers) which are scaled down to the interval [0..1].
# If a priority is not given, a priority of 0 is assumed - which in
# turn means, that the whole subtree has priority 0.
# The computed priority is the average of all stakeholders numbers.

class ReqPriority(ReqTagGeneric):
    tag = "Priority"
    ltype = set(["reqtag", ])

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config)

    def rewrite(self, rid, req):
        # This tag is mandatory - but might be empty
        if self.tag not in req:
            return "Factor", 0.0
        # Compute the priority.  This is done by adding the simple
        # priorities and afterwars build the average from this.
        t = req[self.tag]
        lop = t.get_content().split()
        # The (computed) priority
        priority_sum = 0.0
        num_stakeholders = 0
        # A list to check if each stakeholder votes maximal one time.
        priority_done = []
        for l in lop:
            p = l.split(":", 1)
            if len(p) != 2 or len(p[1]) == 0:
                raise RMTException(12, "%s: faulty priority declaration '%s'"
                                   % (rid, l))
            # p[0] is the stakeholder
            # p[1] is the given priority
            if p[0] not in self.config.get_value('requirements.stakeholders'):
                raise RMTException(13, "%s: stakeholder '%s' not known"
                                   % (rid, p[0]))
            if p[0] in priority_done:
                raise RMTException(14, "%s: stakeholder '%s' voted more "
                                   "than once" % (rid, p[0]))
            # Convert it to a float - so it's easier to compare.
            f = float(p[1])
            # Check if in valid range [0..10]
            if f < 0 or f > 10:
                raise RMTException(15, "%s: invalid priority '%f' - must "
                                   "be between 0 and 10" % (rid, f))
            # Compute new sum...
            priority_sum += f / 10
            # ... and increase the stakeholders count.
            num_stakeholders += 1
            # Flag stakeholder that he voted already
            priority_done.append(p[0])

        del req[self.tag]
        return "Factor", priority_sum / float(num_stakeholders)
