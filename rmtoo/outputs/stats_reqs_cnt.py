'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Requirement statistics.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import time

from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies


class stats_reqs_cnt(StdOutputParams, ExecutorTopicContinuum,
                     CreateMakeDependencies):

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.__ofile = None
        tracer.debug("Finished.")

    def topic_continuum_pre(self, _topics_continuum):
        '''Prepare file.'''
        self.__ofile = open(self._output_filename, "w")
        self.__data_written = False

    def topic_continuum_post(self, _topics_continuum):
        '''Cleanup file.'''
        if not self.__data_written:
            # Write minimal fallback data for empty topic continuum
            self.__ofile.write("# No data available for requirement count statistics\n")
            self.__ofile.write("%s 0\n" % time.strftime("%Y-%m-%d_%H:%M:%S"))
        self.__ofile.close()

    def topic_set_pre(self, tset):
        '''Output the data for this topics set.'''
        self.__ofile.write(
            "%s %d\n" %
            (time.strftime("%Y-%m-%d_%H:%M:%S",
                           time.localtime(
                               tset.get_commit_info().get_timestamp())),
             tset.get_topic_set().get_complete_requirement_set_count()))
        self.__data_written = True

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)
