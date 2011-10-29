'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Configuration Convert Utilities.
 
 (c) 2011 by flonatel

 For licensing details see COPYING
'''

import json
from rmtoo.lib.main.MainHelper import MainHelper

def main(args, mstdout, mstderr):
    config = MainHelper.main_setup_config(args)

    print(json.dumps(config.config, sort_keys=True, indent=4))
