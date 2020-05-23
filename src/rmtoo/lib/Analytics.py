'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Heuristics to check the quality of the requirements.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.analytics.HotSpot import HotSpot
from rmtoo.lib.analytics.DescWords import DescWords
from rmtoo.lib.analytics.ReqTopicCohe import ReqTopicCohe
from rmtoo.lib.analytics.TopicCohe import TopicCohe
from rmtoo.lib.logging import tracer


# pylint: disable=too-few-public-methods
class Analytics(object):
    '''Collection class which calls the other analytics modules.'''

    @staticmethod
    def execute(config, topic_continuum_set, mstderr):
        '''Executes all the available analytics modules.'''
        tracer.debug("Called.")
        success = True
        for analytic_type in [DescWords, HotSpot, ReqTopicCohe, TopicCohe]:
            tracer.debug("Calling [%s]", analytic_type)
            analytics = analytic_type(config)
            topic_continuum_set.execute(analytics, "")
            analytics.write_result(mstderr)
            if not analytics.get_success():
                success = False
        tracer.debug("Finished with success [%s]", success)
        return success
