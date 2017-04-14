'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Configuration Convert Utilities.
 
 (c) 2011 by flonatel

 For licensing details see COPYING
'''

import json
from rmtoo.lib.main.MainHelper import MainHelper
from rmtoo.lib.logging import configure_logging

def main(args, mstdout, mstderr):
    '''Converts the configuration.
       Reads in the given and (pretty) prints the configuration
       to mstdout.'''
    config = MainHelper.main_setup_config(args)
    configure_logging(config, mstderr)
    mstdout.write(json.dumps(config.config, sort_keys=True, indent=4))
    mstdout.write("\n")
