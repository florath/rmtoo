'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Output class.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from stevedore import extension
from six import iteritems

from rmtoo.lib.Executor import Executor
from rmtoo.lib.logging import tracer
from rmtoo.lib.FuncCall import FuncCall


class Output(Executor):
    '''Handle different outputs.'''

    def __init__(self, config):
        '''Creates the output module handler.'''
        tracer.debug("Called.")
        self.__config = config
        self.__cmad_file = None
        self.__plugin_manager = extension.ExtensionManager(
            namespace='rmtoo.output.plugin',
            invoke_on_load=False)

    def __common_topic_continuum_pre(self, topic_continuum, special):
        '''Common method used by cmad_ and normal callback.'''
        tracer.info("Called.")
        output_config = topic_continuum.get_output_config()

        for oconfig_name, oconfig in iteritems(output_config):
            for cfg in oconfig:
                output_obj = self.__plugin_manager[oconfig_name].plugin(cfg)
                if special != "":
                    FuncCall.pcall(output_obj, "init_" + special,
                                   self.__cmad_file)
                topic_continuum.execute(output_obj, special)
        tracer.info("Finished.")

    def topic_continuum_pre(self, topic_continuum):
        '''This is called in the TopicsContinuum pre-phase.'''
        tracer.debug("Called.")
        return self.__common_topic_continuum_pre(topic_continuum, "")

    def cmad_topic_continuum_set_pre(self, _topic_continuum_set):
        '''Initialized the global cmad.'''
        cmad_filename = self.__config.get_rvalue(
            'actions.create_makefile_dependencies')
        tracer.debug("Opening cmad file [%s]", cmad_filename)
        self.__cmad_file = open(cmad_filename, "w")

    def cmad_topic_continuum_set_post(self, _topic_continuum_set):
        '''Cleans up the global cmad.'''
        tracer.debug("Closing cmad file.")
        self.__cmad_file.close()

    def cmad_topic_continuum_pre(self, topic_continuum):
        '''Main entry point for creating make dependencies.'''
        # This is a link to the topics_continuum pre
        return self.__common_topic_continuum_pre(topic_continuum, "cmad_")

    @staticmethod
    def execute(config, topic_continuum_set, _mstderr, func_prefix):
        """Run this output module"""
        output = Output(config)
        return topic_continuum_set.execute(output, func_prefix)
