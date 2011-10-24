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
                cfg.append_list(['topics', topic, 'output', 'html'],
                                {'output_directory': output_spec[1][1],
                                 'header': output_spec[1][2],
                                 'footer': output_spec[1][3]})
                continue
            if output_spec[0] in ['prios', 'stats_sprint_burndown1']:
                print("PRIOS OUTPUTSPEC [%s]" % output_spec)
                pval = {'output_filename': output_spec[1][1] }
                if len(output_spec[1]) > 2:
                    pval['start_date'] = output_spec[1][2]['start_date']
                    if 'end_date' in output_spec[1][2]:
                        pval['end_date'] = output_spec[1][2]['end_date']
                print("INTERNAL CONVERT PRIO [%s]" % pval)
                cfg.append_list(['topics', topic, 'output', output_spec[0]], pval)
                continue
            if output_spec[0] in ['stats_burndown1']:
                print("SBD OUTPUTSPEC [%s]" % output_spec)
                pval = {'output_filename': output_spec[1][1] }
                if len(output_spec[1]) > 2:
                    # The third element of this is just the date...
                    pval['start_date'] = output_spec[1][2]
                print("INTERNAL CONVERT PRIO [%s]" % pval)
                cfg.append_list(['topics', topic, 'output', output_spec[0]], pval)
                continue
            if output_spec[0] in ['graph', 'graph2', 'stats_reqs_cnt',
                                  'latex2', 'xml_ganttproject_2',
                                  'oopricing1', 'version1', 'tlp1']:
                cfg.append_list(['topics', topic, 'output', output_spec[0]],
                                {'output_filename': output_spec[1][1]})
                continue
            print("OS [%s]" % output_spec)
            assert(False)

    @staticmethod
    def internal_convert_reqs(cfg, reqs_spec):
        '''Converts the old reqs_spec to the new requirements specification.'''
        cfg.set_value('requirements.input.directory',
                      reqs_spec['directory'])
        cfg.set_value('requirements.input.commit_interval.begin',
                      reqs_spec['commit_interval'][0])
        cfg.set_value('requirements.input.commit_interval.end',
                      reqs_spec['commit_interval'][1])
        cfg.set_value('requirements.input.default_language',
                      reqs_spec['default_language'])
        if 'dependency_notation' in reqs_spec:
            cfg.set_value('requirements.input.dependency_notation',
                          set(reqs_spec['dependency_notation']))
        else:
            # The default is only 'Solved by'.
            print("Using default Depends on relationship.")
            cfg.set_value('requirements.input.dependency_notation',
                          set(['Depends on', ]))
            print("DEP ON 22 [%s]" % cfg.get_value('requirements.input.dependency_notation'))

    @staticmethod
    def internal_convert_analytics(cfg, analytics_specs):
        '''Converts the old analytics spec to the new requirements
           specification.'''
        if 'stop_on_errors' in analytics_specs:
            cfg.set_value('processing.analytics.stop_on_errors',
                          analytics_specs['stop_on_errors'])
            print("interncvl_convert_analytics [%s]" %
                  cfg.get_value('processing.analytics.stop_on_errors'))

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
        if hasattr(old_config, 'inventors'):
            cfg.set_value('requirements.inventors', old_config.inventors)
            old_config_dir.remove('inventors')
        # Topic specs must be done before the output_spec, because the
        # output specs will be inserted into the  topic specs.
        if hasattr(old_config, 'topic_specs'):
            Old.internal_convert_topics(cfg, old_config.topic_specs)
            old_config_dir.remove('topic_specs')
        if hasattr(old_config, 'output_specs'):
            Old.internal_convert_output(cfg, old_config.output_specs)
            old_config_dir.remove('output_specs')
        if hasattr(old_config, 'reqs_spec'):
            Old.internal_convert_reqs(cfg, old_config.reqs_spec)
            old_config_dir.remove('reqs_spec')
        if hasattr(old_config, 'analytics_specs'):
            Old.internal_convert_analytics(cfg, old_config.analytics_specs)
            old_config_dir.remove('analytics_specs')
        print("Old Config: Not converted attributes: [%s]" % old_config_dir)

    @staticmethod
    def convert_to_new(cfg, old_config_file):
        '''Reads in the old configuration file and converts it to 
           a dictionary which can be used in the new configuration.'''
        old_config = Old.load_config(old_config_file)
        return Old.internal_convert_to_new(cfg, old_config)
