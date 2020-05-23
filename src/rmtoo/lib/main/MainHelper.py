'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Main Helper.

 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.InputModules import InputModules
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.configuration.DefaultValues import DefaultValues


class MainHelper(object):
    '''Utility class for different aspects of the different mains.'''

    def __init__(self):
        '''Private constructor only - do not use.'''
        assert False

    @staticmethod
    def main_setup_config(args):
        """Setup the config for main()"""
        config = Cfg()
        DefaultValues.set_default_values(config)
        config.merge_cmd_line_params(args)
        config.evaluate()
        return config

    @staticmethod
    def main_setup(args, _mstdout, _mstderr):
        """Create the config and input modules for the main()"""
        config = MainHelper.main_setup_config(args)
        mods = InputModules(config)
        return config, mods
