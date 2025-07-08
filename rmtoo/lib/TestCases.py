'''
 rmtoo
   Free and Open Source Requirements Management Tool

  TestCases handling

 (c) 2012,2017,2025 by flonatel GmbH & Co. KG / Andreas Florath

 For licensing details see COPYING
'''

from rmtoo.lib.logging import tracer


def collect(topic_set):
    '''Collect all the testcases which are used in the given topic.'''
    if topic_set is None:
        assert False

    tracer.debug("Called for topic set.")
    testcases = {}
    for testcase, tcval in \
            topic_set.get_requirement_set().get_testcases().items():
        tracer.debug("Add constraint [%s]", testcase)
        testcases[testcase] = tcval
    tracer.debug("Finished; size [%d]", len(testcases))
    return testcases
