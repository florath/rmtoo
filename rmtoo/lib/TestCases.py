'''
 rmtoo
   Free and Open Source Requirements Management Tool

  TestCases handling

 (c) 2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from six import iteritems

from rmtoo.lib.logging import tracer


class TestCases(object):
    '''Helper functions for testcases handling.'''

    @staticmethod
    def collect(topic_set):
        '''Collect all the testcases which are used in the given topic.'''
        tracer.debug("Called for topic set.")
        testcases = {}

        if topic_set is None:
            assert False

        for testcase, tcval in iteritems(topic_set.get_requirement_set().
                                         get_testcases()):
            tracer.debug("Add constraint [%s]" % testcase)
            testcases[testcase] = tcval
        tracer.debug("Finished; size [%d]" % len(testcases))
        return testcases
