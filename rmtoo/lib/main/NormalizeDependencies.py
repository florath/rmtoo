'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Normalize dependencies to 'Solved by'.
   
 (c) 2011 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import sys
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.main.MainHelper import MainHelper
from rmtoo.lib.RequirementSet import RequirementSet


def main_impl(args, mstdout, mstderr):
    config, mods = MainHelper.main_setup(args, mstdout, mstderr)
    rs = RequirementSet(mods, config)
    command_line_args = config.get_value('general.command_line_arguments')
    return rs.read_from_filesystem(command_line_args[0]) \
        and rs.normalize_dependencies() \
        and rs.write_to_filesystem(command_line_args[0])

def main(args, mstdout, mstderr, main_func=main_impl, exitfun=sys.exit):
    try:
        exitfun(not main_func(args, mstdout, mstderr))
    except RMTException, rmte:
        mstderr.write("+++ ERROR: Exception occurred: %s\n" % rmte)
        exitfun(1)
