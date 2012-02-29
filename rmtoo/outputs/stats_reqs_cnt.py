'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Requirement statistics.
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import time
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies

class stats_reqs_cnt(StdOutputParams, ExecutorTopicContinuum,
                     CreateMakeDependencies):

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)
        tracer.debug("Finished.")

    def topics_continuum_pre(self, topics_continuum):
        '''Prepare file.'''
        self.__ofile = file(self._output_filename, "w")
        
    def topics_continuum_post(self, topics_continuum):
        '''Cleanup file.'''
        self.__ofile.close()

    def topics_set_pre(self, tset):
        '''Output the data for this topics set.'''
        self.__ofile.write("%s %d\n" %
            (time.strftime("%Y-%m-%d_%H:%M:%S",
             time.localtime(tset.get_commit_info().get_timestamp())),
             tset.get_topic_set().get_complete_requirement_set_count()))

    def cmad_topics_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file, 
                                              self._output_filename)

# deprecated

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def output(self, reqscont):
        # Depending on the number of elements in the continuum, this
        # might be a list or, if only FILES should be used, exactly
        # one value (the current time).
        ofile = file(self.output_filename, "w")

        for cid in reqscont.continuum_order:
            rs = reqscont.continuum[cid]
            ofile.write("%s %d\n" %
                        (time.strftime("%Y-%m-%d_%H:%M:%S",
                                       time.localtime(rs.timestamp())),
                         rs.reqs_count()))

        # Clean up the file.
        ofile.close()

