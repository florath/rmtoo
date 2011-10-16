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
    def main_setup(args, mstdout, mstderr, parse_cmd_line_opts):
        opts = parse_cmd_line_opts(args)
        config = MainHelper.load_config(opts)
        mods = Modules(opts.modules_directory, opts, config)
        return opts, config, mods
