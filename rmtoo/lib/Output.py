'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Output class.
   
 (c) 2011 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.Executor import Executor

class Output(Executor):
    '''Handles the different outputs.'''

    def __init__(self, config):
        '''Creates the output module handler.'''
        pass

    def topics_continuum_pre(self, topic_continuum):
        '''This is call in the TopicsContinuum pre-phase.'''
        assert False

    @staticmethod
    def execute(config, topic_continuum_set, mstderr):
        output = Output(config)
        return topic_continuum_set.execute(output)
