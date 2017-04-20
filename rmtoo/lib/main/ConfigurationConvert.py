'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Configuration Convert Utilities.

 (c) 2011,2017 by flonatel

 For licensing details see COPYING
'''
import json
import sys

from rmtoo.lib.main.MainHelper import MainHelper
from rmtoo.lib.logging.MemLogStore import MemLogStore


def main_impl(args, mstdout, mstderr):
    '''Converts the configuration.
       Reads in the given and (pretty) prints the configuration
       to mstdout.'''
    log_store = MemLogStore()
    config = MainHelper.main_setup_config(args, log_store)
    log_store.write_log(mstderr)
    mstdout.write(json.dumps(config.config, sort_keys=True, indent=4))
    mstdout.write("\n")


def main():
    main(sys.argv[1:], sys.stdout, sys.stderr)
