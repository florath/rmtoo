'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Main Helper. 
   
 (c) 2011 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.InputModules import InputModules
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.configuration.DefaultValues import DefaultValues
from rmtoo.lib.logging.MemLogStore import MemLogStore

class MainHelper:
    '''Utility class for different aspects of the different mains.'''

    @staticmethod
    def main_setup_config(args, log_store):
        config = Cfg()
        DefaultValues.set_default_values(config)
        config.merge_cmd_line_params(args)
        config.evaluate(log_store)
        return config

    @staticmethod
    def main_setup(args, mstdout, mstderr):
        log_store = MemLogStore()
        config = MainHelper.main_setup_config(args, log_store)

        moddirs = config.get_value("global.modules.directories")
        if len(moddirs) != 1:
            # TODO Handle multiple module directories.
            assert(False)

        mods = InputModules(moddirs[0], config)
        log_store.write_log(mstderr)
        return config, mods
