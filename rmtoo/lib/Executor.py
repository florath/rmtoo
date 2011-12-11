'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Base class for handling different executions on different levels
  of the rmtoo data.
  This can be used for the analyse module, as well as for the different
  output modules.
   
 (c) 2011 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum

class Executor(ExecutorTopicContinuum):
    '''Base class for the different executors.
       All methods are implemented: they are doing nothing.'''

    def topics_continuum_set_pre(self, topics_continuum_set):
        '''This is call in the TopicsContinuumSet pre-phase.'''
        return

    def topics_continuum_set_post(self, topics_continuum_set):
        '''This is call in the TopicsContinuumSet post-phase.'''
        return

