'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 LaTeX output class version 2.
  
 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


from rmtoo.lib.Statistics import Statistics
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum

class stats_burndown1(StdOutputParams, ExecutorTopicContinuum):

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)

# TODO: Adapt to new executor strcuture.
    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because stats can only one topic continuum,
           the latest (newest) is used.'''
        return [ topic_sets[vcs_commit_ids[-1].get_commit()] ]

    def requirement_set_pre(self, requirement_set):
        '''Compute stats for each requirements set.'''
        rv = Statistics.get_units(requirement_set,
                                  self._start_date, self._end_date)
        Statistics.output_stat_files(self._output_filename, self._start_date, rv)

