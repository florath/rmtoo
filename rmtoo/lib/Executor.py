'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Base class for handling different executions on different levels
  of the rmtoo data.
  This can be used for the analyze module, as well as for the different
  output modules.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum


# This is a non-abstract base class coming with some
# NOP default implementations of methods.
# pylint: disable=no-self-use
class Executor(ExecutorTopicContinuum):
    '''Base class for the different executors.
       All methods are implemented: they are doing nothing.'''

    def topic_continuum_set_pre(self, _topics_continuum_set):
        '''This is call in the TopicsContinuumSet pre-phase.'''
        return

    def topic_continuum_set_sort(self, list_to_sort):
        '''Sorts the list of topic continuums.'''
        return list_to_sort

    def topic_continuum_set_post(self, _topics_continuum_set):
        '''This is call in the TopicsContinuumSet post-phase.'''
        return
