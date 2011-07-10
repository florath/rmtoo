#
# Requirement Management Toolset
#
#  This is the main function - it is called from the 'rmtoo'
#  executable directly. 
#  It is stored here (in a seperate file) for (blackbox) testing
#  proposes. 
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import sys

from optparse import OptionParser
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.ReqsContinuum import ReqsContinuum
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.TopicHandler import TopicHandler
from rmtoo.lib.OutputHandler import OutputHandler
from rmtoo.lib.Analytics import Analytics
from rmtoo.lib.main.MainHelper import MainHelper

def parse_cmd_line_opts(args):
    parser = OptionParser()
    parser.add_option("-f", "--file-config", dest="config_file",
                  help="Config file")
    parser.add_option("-m", "--modules-directory", dest="modules_directory",
                  help="Directory with modules")
    parser.add_option("-c", "--create-makefile-dependencies",
                      dest="create_makefile_dependencies",
                      help="Create makefile dependencies")

    (options, args) = parser.parse_args(args=args)

    if options.modules_directory==None:
        # If there is no modules directory given, use the pycentral one.
        options.modules_directory = "/usr/share/pyshared"

    if options.config_file==None:
        raise RMTException(60, "no config_file option is specified")

    if len(args)>0:
        raise RMTException(61, "too many args")

    return options

def execute_cmds(opts, config, mods, mstdout, mstderr):
    # Checks are allways done - to be sure that e.g. the dependencies
    # are correct.
    try:
        rc = ReqsContinuum(mods, opts, config)
        reqs = rc.continuum_latest()
    except RMTException, rmte:
        mstderr.write("+++ ERROR: Problem reading in the continuum: '%s'"
                      % rmte)
        return False

    # Setup the OutputHandler
    # Note: this can be more than one!
    # For the topic based output also all the Topics are needed -
    # before the OutputHandler itself - because different output
    # handler may reference the same Topic.
    topics = TopicHandler(config, reqs)
    ohandler = OutputHandler(config, topics)

    # When only the dependencies are needed, output them to the given
    # file. 
    if opts.create_makefile_dependencies!=None:
        ofile = file(opts.create_makefile_dependencies, "w")
        # Write out the REQS=
        rc.cmad_write_reqs_list(ofile)
        # Write out the rest
        ohandler.create_makefile_dependencies(ofile, rc)
        ofile.close()
        return True

    # Print out all logs (from all kinds of objects)
    reqs.write_log(mstderr)
    topics.write_log(mstderr)
    # If there is a problem with the last requirement set included in
    # the requirements continuum and stop processing. (Note the logs
    # were already written out).
    if not reqs.is_usable():
        return False

    # The requirments are syntatically correct now: therefore it is
    # possible to do some analytics on them
    if not Analytics.run(config, reqs, topics):
        reqs.write_log(mstderr)
        reqs.write_analytics_result(mstderr)

        if hasattr(config, 'analytics_specs') \
                and 'stop_on_errors' in config.analytics_specs \
                and config.analytics_specs['stop_on_errors']:
            return False

    # Output everything
    ohandler.output(rc)
   
    return True

def main_impl(args, mstdout, mstderr):
    opts, config, mods = MainHelper.main_setup(args, mstdout, mstderr,
                                               parse_cmd_line_opts)
    return execute_cmds(opts, config, mods, mstdout, mstderr)

def main(args, mstdout, mstderr, main_impl=main_impl, exitfun=sys.exit):
#    try:
        exitfun(not main_impl(args, mstdout, mstderr))
#    except RMTException, rmte:
#        mstderr.write("+++ ERROR: Exception occured: %s\n" % rmte)
#        exitfun(1)
