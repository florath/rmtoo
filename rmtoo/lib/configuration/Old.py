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
        # ('execfile' does not work here.)
        old_config_fd = file(old_config_file, "r")
        conf_file = old_config_fd.read()
        exec(conf_file)
        config = Config()
#        ConfigUtils.set_defaults(config)
#        ConfigUtils.check(config)
        old_config_fd.close()
        return config

    @staticmethod
    def internal_convert_to_new(config):
        '''Converts the old given config object to the new configuration
           using a dictionary.'''
        ldict = {'requirements': {} }
        # This is done only for housekeeping
        old_config_dir = dir(config)
        # Remove the system specific from the list
        old_config_dir.remove('__doc__')
        old_config_dir.remove('__module__')
        if hasattr(config, 'stakeholders'):
            ldict['requirements']['stakeholders'] = config.stakeholders
            old_config_dir.remove('stakeholders')
        print("Old Config: Not converted attributes: [%s]" % old_config_dir)
        return ldict

    @staticmethod
    def convert_to_new(old_config_file):
        '''Reads in the old configuration file and converts it to 
           a dictionary which can be used in the new configuration.'''
        config = Old.load_config(old_config_file)
        return Old.internal_convert_to_new(config)
