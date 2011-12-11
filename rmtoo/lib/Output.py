'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Output class.
   
 (c) 2011 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.Executor import Executor
from rmtoo.lib.logging.EventLogging import tracer

class Output(Executor):
    '''Handles the different outputs.'''

    def __init__(self, config):
        '''Creates the output module handler.'''
        pass

    @staticmethod
    def __load_output_module(output_name):
        '''Loads the module with the given name.'''
        tracer.debug("Loading output module [%s]" % output_name)
        # Concatenate the needed names
        output_path_parts = ["rmtoo", "outputs", output_name]
        output_path = ".".join(output_path_parts)

        # Load the module
        return __import__(output_path, globals(), locals(), output_path)

    def __create_output_module(self, output_name):
        '''Creates the module object.'''
        output_module = self.__load_output_module(output_name)
        # Create the constructor object
        cstrt = eval("output_module.%s" % output_name)
        # Call the constructor to get an object.
        return cstrt()

    def topics_continuum_pre(self, topic_continuum):
        '''This is call in the TopicsContinuum pre-phase.'''
        tracer.info("Called.")
        output_config = topic_continuum.get_output_config()
        print("OUTPUT CONFIG %s" % output_config)

        for oconfig_name, oconfig in output_config.iteritems():
            print("NAME %s  Inhalt %s " % (oconfig_name, oconfig))
            output_module = self.__create_output_module(oconfig_name)
        assert False

    @staticmethod
    def execute(config, topic_continuum_set, mstderr):
        output = Output(config)
        return topic_continuum_set.execute(output)
