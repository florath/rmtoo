'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Normalize dependencies to 'Solved by'.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import sys
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.main.MainHelper import MainHelper
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.logging import tracer
from rmtoo.lib.vcs.FileSystem import FileSystem
from rmtoo.lib.vcs.ObjectCache import ObjectCache


def main_func(args, mstdout, mstderr):
    """The 'real' main function.

    Sets up everything, reads in the requirements and
    writes out everything.
    """
    tracer.debug("Called.")
    config, mods = MainHelper.main_setup(args, mstdout, mstderr)

    file_system_if = FileSystem(config)
    object_cache = ObjectCache()

    req_set = RequirementSet(config)
    command_line_args = config.get_rvalue('general.command_line_arguments')

    req_set.read_requirements(file_system_if, None, mods, object_cache)
    return req_set.normalize_dependencies() \
        and req_set.write_to_filesystem(command_line_args[0])


def main_impl(args, mstdout, mstderr, local_main_func=main_func,
              exitfun=sys.exit):
    """Call the main_func and handle possible exceptions"""
    try:
        exitfun(not local_main_func(args, mstdout, mstderr))
    except RMTException as rmte:
        mstderr.write("+++ ERROR: Exception occurred: %s\n" % rmte)
        exitfun(1)


def main():
    """Call the main_imp with the approprite parameters.

    This is needed to be able to write test cases for the 'main_impl'
    function.
    """
    main_impl(sys.argv[1:], sys.stdout, sys.stderr)
