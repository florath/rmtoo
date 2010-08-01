#
# Requirement Management Toolset: Analytics
#
#  Some parts of the requirements management can be automatically
#  checked.  This class handles the analytics to the different
#  analytics modules.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.analytics.HotSpot import HotSpot
from rmtoo.lib.analytics.DescWords import DescWords

class Analytics:

    # The argument to the analytics modules is the (latest) set of
    # requirments.  (It makes sense only to check them.)
    @staticmethod
    def run(reqs):
        ok = True
        if not HotSpot.run(reqs):
            ok = False
        if not DescWords.run(reqs):
            ok = False
        return ok
