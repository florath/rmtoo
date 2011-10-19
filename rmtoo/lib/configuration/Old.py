'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Old way of configuration handling.
  
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import os

class Old:
    '''Deprecated.
       Class to handle the old configuration in a new configuration
       environment.'''

    def __init__(self):
        '''Hide the constructor for the Utility class'''
        assert(False)

    @staticmethod
    def load_config(old_config_file):
        '''Load old config file'''
        # 'execfile' does not work here.
        print("OLD CONFIG FILE [%s]" % old_config_file)
        old_config_fd = file(old_config_file, "r")
        conf_file = old_config_fd.read()
        exec(conf_file)
        config = Config()
#        ConfigUtils.set_defaults(config)
#        ConfigUtils.check(config)
        old_config_fd.close()
        return config

    @staticmethod
    def internal_convert_topics(cfg, topic_specs):
        '''Converts the old topic_spec to the new topic configuration.'''
        for key, value in topic_specs.iteritems():
            cfg.set_value(['topics', key],
                    {'directory': value[0],
                     'name': value[1]})

    @staticmethod
    def internal_convert_output(cfg, output_specs):
        '''Converts the old output_spec to the new output configuration.'''
        for output_spec in output_specs:
            topic = output_spec[1][0]
            if output_spec[0] == 'html':
                cfg.append_list([topic, 'output', 'html'],
                                {'output_directory': output_spec[1][1],
                                 'header': output_spec[1][2],
                                 'footer': output_spec[1][3]})
                continue
            if output_spec[0] == 'prios':
                pval = {'output_filename': output_spec[1][1] }
                if len(output_spec[1]) > 2:
                    pval['start_date'] = output_spec[1][2]
                cfg.append_list([topic, 'output', 'prios'], pval)
                continue
            if output_spec[0] in ['graph', 'graph2', 'stats_reqs_cnt',
                                  'latex2', 'xml_ganttproject_2',
                                  'oopricing1']:
                cfg.append_list([topic, 'output', output_spec[0]],
                                {'output_filename': output_spec[1][1]})
                continue
            print("OS [%s]" % output_spec)
            assert(False)

    @staticmethod
    def internal_convert_to_new(cfg, old_config):
        '''Converts the old given old_config object to the new configuration
           using a dictionary.'''
        cfg.set_value('requirements', {})
        # This is done only for housekeeping
        old_config_dir = dir(old_config)
        # Remove the system specific from the list
        old_config_dir.remove('__doc__')
        old_config_dir.remove('__module__')
        if hasattr(old_config, 'stakeholders'):
            cfg.set_value('requirements.stakeholders', old_config.stakeholders)
            old_config_dir.remove('stakeholders')
        # Topic specs must be done before the output_spec, because the
        # output specs will be inserted into the  topic specs.
        if hasattr(old_config, 'topic_spec'):
            Old.internal_convert_topics(cfg, old_config.topic_spec)
            old_config_dir.remove('topic_spec')
        if hasattr(old_config, 'output_specs'):
            Old.internal_convert_output(cfg, old_config.output_specs)
            old_config_dir.remove('output_specs')
        print("Old Config: Not converted attributes: [%s]" % old_config_dir)

    @staticmethod
    def convert_to_new(cfg, old_config_file):
        '''Reads in the old configuration file and converts it to 
           a dictionary which can be used in the new configuration.'''
        old_config = Old.load_config(old_config_file)
        return Old.internal_convert_to_new(cfg, old_config)
