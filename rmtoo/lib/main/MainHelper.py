#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Main Helper
#
# (c) 2011 by flonatel
#
# For licensing details see COPYING
#

import os

from rmtoo.lib.ConfigUtils import ConfigUtils
from rmtoo.lib.Modules import Modules
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.configuration.DefaultValues import DefaultValues

class MainHelper:

    @staticmethod
    def load_config(opts):
        # Load config file
        # ('execfile' does not work here.)
        f = file(opts.config_file, "r")
        conf_file = f.read()
        exec(conf_file)
        config = Config()
        ConfigUtils.set_defaults(config)
        ConfigUtils.check(config)
        f.close()
        return config

    @staticmethod
    def main_setup(args, mstdout, mstderr):
        config = Cfg()
        DefaultValues.set_default_values(config)
        config.merge_cmd_line_params(args)
        config.evaluate()

        moddirs = config.get_value("global.modules.directories")
        if len(moddirs) != 1:
            # TODO Handle multiple module directories.
            assert(False)

        mods = Modules(moddirs[0], config)
        return config, mods
