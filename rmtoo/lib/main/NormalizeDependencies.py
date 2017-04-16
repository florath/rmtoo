'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Normalize dependencies to 'Solved by'.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import sys
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.main.MainHelper import MainHelper
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.logging import tracer
from rmtoo.lib.vcs.FileSystem import FileSystem
from rmtoo.lib.vcs.ObjectCache import ObjectCache


def main_func(args, mstdout, mstderr):
    tracer.debug("Called.")
    config, mods = MainHelper.main_setup(args, mstdout, mstderr)

    file_system_if = FileSystem(config)
    object_cache = ObjectCache()

    rs = RequirementSet(config)
    command_line_args = config.get_rvalue('general.command_line_arguments')

    rs.read_requirements(file_system_if, None, mods, object_cache)
    return rs.normalize_dependencies() \
        and rs.write_to_filesystem(command_line_args[0])


def main_impl(args, mstdout, mstderr, main_func=main_func, exitfun=sys.exit):
    try:
        exitfun(not main_func(args, mstdout, mstderr))
    except RMTException as rmte:
        mstderr.write("+++ ERROR: Exception occurred: %s\n" % rmte)
        exitfun(1)


def main():
    main_impl(sys.argv[1:], sys.stdout, sys.stderr)
