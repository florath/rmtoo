'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  This is the main function - it is called from the 'rmtoo'
  executable directly. 
  It is stored here (in a separate file) for (black-box) testing
  proposes. 
   
 (c) 2010-2011 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import sys

from optparse import OptionParser
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.TopicContinuumSet import TopicContinuumSet
from rmtoo.lib.TopicContinuum import TopicContinuum
from rmtoo.lib.OutputHandler import OutputHandler
from rmtoo.lib.Analytics import Analytics
from rmtoo.lib.Output import Output
from rmtoo.lib.main.MainHelper import MainHelper

def execute_cmds(config, input_mods, mstdout, mstderr):
    # Checks are always done - to be sure that e.g. the dependencies
    # are correct.
    # Please note: there is no 'ONE' latest continuum any more
    #  - but a list.
    try:
        topic_continuum_set = TopicContinuumSet(input_mods, config)
    except RMTException, rmte:
        mstderr.write("+++ ERROR: Problem reading in the continuum [%s]\n"
                      % rmte)
        return False

    # Print out all logs (from all kinds of objects)
    topic_continuum_set.write_log(mstderr)
    # If there is a problem with the last requirement set included in
    # the requirements continuum and stop processing. (Note the logs
    # were already written out).
    if not topic_continuum_set.is_usable():
        mstderr.write("+++ ERROR: topic continuum set is not usable.\n")
        return False

    # When only the dependencies are needed, output them to the given
    # file.

    cmad_filename = config.get_value_wo_throw(
                       'actions.create_makefile_dependencies')
    if cmad_filename != None:
        cmad_rfilename = config.dollar_replace(cmad_filename)
        Output.execute(config, topic_continuum_set, mstderr, "cmad_")
        return True

    # The requirements are syntactically correct now: therefore it is
    # possible to do some analytics on them.
    # Note that analytics are only run on the latest version.
    if not Analytics.execute(config, topic_continuum_set, mstderr):
        if config.get_bool('processing.analytics.stop_on_errors', True):
            return False

    # Output everything
    Output.execute(config, topic_continuum_set, mstderr, "")
    return True

def main_impl(args, mstdout, mstderr):
    config, input_mods = MainHelper.main_setup(args, mstdout, mstderr)
    return execute_cmds(config, input_mods, mstdout, mstderr)

def main(args, mstdout, mstderr, main_func=main_impl, exitfun=sys.exit):
    '''The main entry function
    This calls the main_func function and does the exception handling.'''
    try:
        exitfun(not main_func(args, mstdout, mstderr))
    except RMTException, rmte:
        mstderr.write("+++ ERROR: Exception occurred: %s\n" % rmte)
        exitfun(1)
