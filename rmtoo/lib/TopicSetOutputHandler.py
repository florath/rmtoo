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

    def __init__(self, cfg, name, param_cfg):
        '''Create an object with the given parameters.'''
        self.cfg = cfg
        self.name = name
        self.param_cfg = param_cfg
        self.output_module = self.internal_create_output_module()

    def internal_load_output_module(self):
        '''Loads the module with the given name.'''
        # Concatenate the needed names
        output_path_parts = ["rmtoo", "outputs", self.name]
        output_path = ".".join(output_path_parts)

        # Load the module
        return __import__(output_path, globals(), locals(), output_path)

    def internal_create_output_module(self):
        '''Creates the module object.'''
        output_module = self.internal_load_output_module()
        # Call the constructor
        obj = eval("output_module.%s(%s)" % (self.name, self.param_cfg))
        return obj
