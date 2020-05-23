'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Burndown diagram

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.Statistics import Statistics
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.logging import tracer
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies


class stats_sprint_burndown1(StdOutputParams, ExecutorTopicContinuum,
                             CreateMakeDependencies):

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.info("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because stats can only one topic continuum,
           the latest (newest) is used.'''
        return [topic_sets[vcs_commit_ids[-1].get_commit()]]

    def requirement_set_pre(self, requirement_set):
        '''Compute stats for each requirements set.'''
        rval = Statistics.get_units_sprint(requirement_set,
                                           self._start_date, self._end_date)
        Statistics.output_stat_files(self._output_filename,
                                     self._start_date, rval)
