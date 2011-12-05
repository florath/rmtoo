'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Base class for handling different executions on different levels
  of the rmtoo data.
  This can be used for the analyse module, as well as for the different
  output modules.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

class Executor:
    '''Base class for the different executors.
       All methods are implemented: they are doing nothing.'''
       
    def topics_continuum_set_pre(self, topics_continuum_set):
        '''This is call in the TopicsContinuumSet pre-phase.'''
        return
    
    def topics_continuum_set_post(self, topics_continuum_set):
        '''This is call in the TopicsContinuumSet post-phase.'''
        return

    def topics_continuum_pre(self, topics_continuum):
        '''This is call in the TopicsContinuum pre-phase.'''
        return
    
    def topics_continuum_post(self, topics_continuum):
        '''This is call in the TopicsContinuum post-phase.'''
        return

    def topics_set_pre(self, topics_continuum):
        '''This is call in the TopicsSet pre-phase.'''
        return
    
    def topics_set_post(self, topics_continuum):
        '''This is call in the TopicsSet post-phase.'''
        return

    def topic_pre(self, topic):
        '''This is call in the Topic pre-phase.'''
        return
    
    def topic_post(self, topic):
        '''This is call in the Topic post-phase.'''
        return
