'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Base class for handling different executions in and
  beneath the TopicContinuum.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

class ExecutorTopicContinuum:

    def topics_continuum_pre(self, topics_continuum):
        '''This is call in the TopicsContinuum pre-phase.
           This is typically the phase where all the output modules
           will be used.'''
        return

    def topics_continuum_post(self, topics_continuum):
        '''This is call in the TopicsContinuum post-phase.'''
        return

    def topics_set_pre(self, topics_set):
        '''This is call in the TopicsSet pre-phase.'''
        return

    def topics_set_post(self, topics_set):
        '''This is call in the TopicsSet post-phase.'''
        return

    def topic_pre(self, topic):
        '''This is call in the Topic pre-phase.'''
        return

    def topic_post(self, topic):
        '''This is call in the Topic post-phase.'''
        return

    def requirement_set_pre(self, requirements_set):
        '''This is call in the RequirementSet pre-phase.'''
        return

    def requirement_set_post(self, requirements_set):
        '''This is call in the RequirementSet post-phase.'''
        return

    def requirement(self, requirement):
        '''This is call in the Requirement phase.'''
        return
