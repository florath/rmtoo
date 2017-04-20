'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Main Helper.

 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.InputModules import InputModules
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.configuration.DefaultValues import DefaultValues


class MainHelper:
    '''Utility class for different aspects of the different mains.'''

    def __init__(self):
        '''Private constructor only - do not use.'''
        assert False

    @staticmethod
    def main_setup_config(args):
        config = Cfg()
        DefaultValues.set_default_values(config)
        config.merge_cmd_line_params(args)
        config.evaluate()
        return config

    @staticmethod
    def main_setup(args, mstdout, mstderr):
        config = MainHelper.main_setup_config(args)

        moddirs = config.get_value("global.modules.directories")
        if len(moddirs) != 1:
            # TODO Handle multiple module directories.
            assert(False)

        mods = InputModules(moddirs[0], config)
        return config, mods
