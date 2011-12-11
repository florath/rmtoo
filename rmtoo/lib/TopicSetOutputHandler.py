'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Output handler for one TopicSet.
  
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

class TopicSetOutputHandler:
    '''Contains one handler to output a TopicSet in a specific
       way and format.'''

    def __init__(self, cfg, name, param_cfg, topic_set):
        '''Create an object with the given parameters.'''
        self.cfg = cfg
        self.name = name
        self.param_cfg = param_cfg
        self.output_module = self.internal_create_output_module(topic_set)



    def output(self, rc):
        '''Calls the output.'''
        return self.output_module.output(rc)

    def cmad(self, reqscont, ofile):
        '''Calls the creation of makefile dependency.'''
        return self.output_module.cmad(reqscont, ofile)
