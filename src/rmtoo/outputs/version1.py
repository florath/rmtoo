'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Version output class.

 (c) 2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum


class version1(StdOutputParams, ExecutorTopicContinuum,
               CreateMakeDependencies):
    '''Outputs the version number of the version control system to a given
       file.'''

    def __init__(self, oconfig):
        '''Create a version1 output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.__used_vcs_id = None

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because graph2 can only one topic continuum,
           the latest (newest) is used.'''
        self.__used_vcs_id = vcs_commit_ids[-1]
        return [topic_sets[vcs_commit_ids[-1].get_commit()]]

    def topic_set_pre(self, _requirement_set):
        '''This is call in the RequirementSet pre-phase.'''
        tracer.debug("Called")
        with open(self._output_filename, "w") as versfd:
            versfd.write("%s\n" % self.__used_vcs_id)
