#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Normalize dependdencies to 'Solved by'
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

import sys
from optparse import OptionParser
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.main.MainHelper import MainHelper
from rmtoo.lib.RequirementSet import RequirementSet

def parse_cmd_line_opts(args):
    parser = OptionParser()
    parser.add_option("-f", "--file-config", dest="config_file",
                  help="Config file")
    parser.add_option("-m", "--modules-directory", dest="modules_directory",
                  help="Directory with modules")

    (options, args) = parser.parse_args(args=args)

    if options.modules_directory==None:
        # If there is no modules directory given, use the pycentral one.
        options.modules_directory = "/usr/share/pyshared"

    if options.config_file==None:
        raise RMTException(82, "no config_file option is specified")

    if len(args)!=1:
        raise RMTException(83, "args must be set to the requirements directory")
    options.args = args

    return options

def main_impl(args, mstdout, mstderr):
    opts, config, mods = MainHelper.main_setup(args, mstdout, mstderr,
                                               parse_cmd_line_opts)
    rs = RequirementSet(mods, opts, config)
    return rs.read_from_filesystem(opts.args[0]) \
        and rs.normalize_dependencies() \
        and rs.write_to_filesystem(opts.args[0])

def main(args, mstdout, mstderr, main_impl=main_impl, exitfun=sys.exit):
    try:
        exitfun(not main_impl(args, mstdout, mstderr))
    except RMTException, rmte:
        mstderr.write("+++ ERROR: Exception occured: %s\n" % rmte)
        exitfun(1)
