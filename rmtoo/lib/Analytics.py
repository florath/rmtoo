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
from rmtoo.lib.analytics.ReqTopicCohe import ReqTopicCohe
from rmtoo.lib.analytics.TopicCohe import TopicCohe

class Analytics:

    # The argument to the analytics modules is the (latest) set of
    # requirments.  (It makes sense only to check them.)
    @staticmethod
    def run(config, reqs, topics):
        ok = True
        
        for ana in HotSpot, DescWords, ReqTopicCohe, TopicCohe:
            if not ana.run(config, reqs, topics):
                ok = False

        return ok
