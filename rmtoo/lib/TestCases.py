'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  TestCases handling
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.logging.EventLogging import tracer

# pylint: disable=W0232
class TestCases:
    '''Helper functions for testcases handling.'''

#    @staticmethod
#    def set_default_values(cfg):
#        '''Set the default values to the given configuration.'''
#        cfg.set_value('constraints.search_dirs',
#                      ['/usr/share/pyshared/rmtoo/collection/constraints'])

    @staticmethod
    def collect(topic_set):
        '''Collect all the testcases which are used in the given topic.'''
        tracer.debug("Called for topic set.")
        testcases = {}

        if topic_set == None:
            assert False

        for testcase, tcval in topic_set.get_requirement_set().\
                    get_testcases().iteritems():
            tracer.debug("Add constraint [%s]" % testcase)
            testcases[testcase] = tcval
        tracer.debug("Finished; size [%d]" % len(testcases))
        return testcases
